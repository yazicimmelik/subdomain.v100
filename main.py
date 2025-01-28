import dns.resolver
import requests
import socket
import json
import concurrent.futures
import os
from datetime import datetime
import csv
from typing import List, Dict, Union

class SubdomainScanner:
    def __init__(self, config_path: str = "config.json"):
        self.load_config(config_path)
        self.default_subdomains = [
            "www", "mail", "blog", "ftp", "admin", "api",
            "dev", "test", "stage", "staging", "prod",
            "database", "db", "portal", "cloud", "remote",
            "vpn", "dns", "mx", "pop", "imap", "smtp",
            "webmail", "direct", "support"
        ]
        
    def load_config(self, config_path: str) -> None:
        """Konfigürasyon dosyasını yükler."""
        try:
            with open(config_path, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {
                "default_domain": "example.com",
                "timeout": 10,
                "max_threads": 10,
                "output_dir": "results"
            }

    def check_subdomain(self, subdomain: str) -> Dict[str, Union[str, List[str]]]:
        """Tek bir subdomain için DNS kayıtlarını ve IP adreslerini kontrol eder."""
        result = {
            "subdomain": subdomain,
            "ip_addresses": [],
            "dns_records": {},
            "http_status": None
        }
        
        try:
            # A kaydı kontrolü
            answers = dns.resolver.resolve(subdomain, 'A')
            result["ip_addresses"] = [str(answer) for answer in answers]
            
            # HTTP durumu kontrolü
            try:
                response = requests.head(f"http://{subdomain}", 
                                      timeout=self.config.get("timeout", 10))
                result["http_status"] = response.status_code
            except requests.RequestException:
                pass
                
            # Diğer DNS kayıtları
            for record_type in ['MX', 'TXT', 'CNAME']:
                try:
                    answers = dns.resolver.resolve(subdomain, record_type)
                    result["dns_records"][record_type] = [str(answer) for answer in answers]
                except dns.resolver.NoAnswer:
                    continue
                except dns.resolver.NXDOMAIN:
                    continue
                
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            pass
        except Exception as e:
            result["error"] = str(e)
            
        return result

    def scan_domain(self, domain: str) -> Dict:
        """Verilen domain için tüm subdomain'leri tarar."""
        results = {
            "scan_info": {
                "domain": domain,
                "scan_date": datetime.now().isoformat(),
                "total_subdomains_checked": len(self.default_subdomains)
            },
            "findings": []
        }
        
        # Thread havuzu oluştur
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.config.get("max_threads", 10)
        ) as executor:
            # Subdomain tarama işlemlerini parallel olarak başlat
            future_to_subdomain = {
                executor.submit(
                    self.check_subdomain, 
                    f"{sub}.{domain}"
                ): sub for sub in self.default_subdomains
            }
            
            for future in concurrent.futures.as_completed(future_to_subdomain):
                result = future.result()
                if result.get("ip_addresses"):  # Sadece bulunan subdomain'leri ekle
                    results["findings"].append(result)
        
        results["scan_info"]["found_subdomains"] = len(results["findings"])
        return results

    def save_results(self, results: Dict, output_format: str = "json") -> str:
        """Tarama sonuçlarını dosyaya kaydeder."""
        os.makedirs(self.config.get("output_dir", "results"), exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        domain = results["scan_info"]["domain"]
        
        if output_format == "json":
            filename = f"{self.config['output_dir']}/{domain}_{timestamp}.json"
            with open(filename, 'w') as f:
                json.dump(results, f, indent=4)
        elif output_format == "csv":
            filename = f"{self.config['output_dir']}/{domain}_{timestamp}.csv"
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Subdomain", "IP Addresses", "HTTP Status", "DNS Records"])
                for finding in results["findings"]:
                    writer.writerow([
                        finding["subdomain"],
                        ", ".join(finding["ip_addresses"]),
                        finding["http_status"],
                        json.dumps(finding["dns_records"])
                    ])
        
        return filename

def main():
    scanner = SubdomainScanner()
    
    print("Subdomain Keşif Aracı v2.0")
    print("-" * 40)
    
    domain = input("Domain adını girin (örn: example.com): ").strip()
    if not domain:
        print("Hata: Domain adı boş olamaz!")
        return
    
    print(f"\nTarama başlatılıyor: {domain}")
    print("Bu işlem birkaç dakika sürebilir...\n")
    
    results = scanner.scan_domain(domain)
    
    # Sonuçları hem JSON hem CSV formatında kaydet
    json_file = scanner.save_results(results, "json")
    csv_file = scanner.save_results(results, "csv")
    
    print(f"\nTarama tamamlandı!")
    print(f"Toplam taranan subdomain: {results['scan_info']['total_subdomains_checked']}")
    print(f"Bulunan aktif subdomain: {results['scan_info']['found_subdomains']}")
    print(f"\nSonuçlar kaydedildi:")
    print(f"JSON: {json_file}")
    print(f"CSV: {csv_file}")

if __name__ == "__main__":
    main()
