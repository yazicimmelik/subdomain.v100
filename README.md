<h1>🌐 Subdomain Keşif Aracı v2.0</h1>

<h2>📝 Proje Açıklaması</h2>
<p>Gelişmiş Python tabanlı subdomain keşif aracı. Hedef domain üzerindeki alt alan adlarını (subdomain) tespit eder, IP adreslerini çözümler ve çeşitli DNS kayıtlarını kontrol eder.</p>

<h2>✨ Özellikler</h2>
<ul>
    <li>🔍 Kapsamlı subdomain taraması (24 yaygın subdomain)</li>
    <li>🚀 Paralel tarama ile hızlı sonuç</li>
    <li>🌐 IP adresi çözümleme</li>
    <li>📊 DNS kayıt analizi (A, MX, TXT, CNAME)</li>
    <li>🌍 HTTP durum kontrolü</li>
    <li>📋 JSON ve CSV formatında raporlama</li>
    <li>⚡ Çoklu thread desteği</li>
    <li>🛡️ Gelişmiş hata yönetimi</li>
</ul>

<h2>🛠 Gereksinimler</h2>
<ul>
    <li>Python 3.7+</li>
    <li>dns.resolver</li>
    <li>requests</li>
    <li>concurrent.futures</li>
    <li>csv</li>
    <li>json</li>
    <li>datetime</li>
    <li>os</li>
    <li>typing</li>
</ul>

<h2>🚀 Kurulum</h2>
<pre>
Projeyi klonlayın:
<code>
git clone https://github.com/kullaniciadi/subdomain-scanner.git
cd subdomain-scanner
</code>

Gerekli paketleri yükleyin:
<code>
pip install -r requirements.txt
</code>
</pre>

<h2>💻 Kullanım</h2>
<pre>
Programı çalıştırın:
<code>
python main.py
</code>

İstenildiğinde domain adını girin:
<code>
Domain adını girin (örn: example.com): example.com
</code>
</pre>

<h2>📋 Çıktı Formatları</h2>
<h3>JSON Çıktı Örneği:</h3>
<pre>
<code>
{
    "scan_info": {
        "domain": "example.com",
        "scan_date": "2025-01-28T14:30:00",
        "total_subdomains_checked": 24,
        "found_subdomains": 3
    },
    "findings": [
        {
            "subdomain": "www.example.com",
            "ip_addresses": ["93.184.216.34"],
            "http_status": 200,
            "dns_records": {
                "MX": ["10 mail.example.com"],
                "TXT": ["v=spf1 include:_spf.example.com ~all"]
            }
        }
    ]
}
</code>
</pre>

<h3>CSV Çıktı Örneği:</h3>
<pre>
<code>
Subdomain,IP Addresses,HTTP Status,DNS Records
www.example.com,93.184.216.34,200,{"MX":["10 mail.example.com"]}
</code>
</pre>

<h2>🔧 Konfigürasyon</h2>
<p><code>config.json</code> dosyasını düzenleyerek ayarları özelleştirebilirsiniz:</p>
<pre>
<code>
{
    "default_domain": "example.com",
    "timeout": 10,
    "max_threads": 10,
    "output_dir": "results"
}
</code>
</pre>

<h2>🚧 Geliştirilecek Özellikler</h2>
<ul>
    <li>🔒 SSL sertifika kontrolü</li>
    <li>🌐 Web arayüzü</li>
    <li>🔌 API desteği</li>
    <li>🚪 Port tarama özelliği</li>
    <li>📸 Screenshot alma özelliği</li>
    <li>📧 E-posta bildirim sistemi</li>
</ul>

<h2>🤝 Katkıda Bulunma</h2>
<ol>
    <li>Projeyi fork edin</li>
    <li>Yeni bir branch oluşturun (<code>git checkout -b yeni-ozellik</code>)</li>
    <li>Değişikliklerinizi commit edin (<code>git commit -am 'Yeni özellik: X'</code>)</li>
    <li>Branch'inizi push edin (<code>git push origin yeni-ozellik</code>)</li>
    <li>Pull Request oluşturun</li>
</ol>

<h2>📄 Lisans</h2>
<p>Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için <code>LICENSE</code> dosyasını inceleyebilirsiniz.</p>

<h2>📬 İletişim</h2>
<ul>
    <li>GitHub: @yazicimmelik</li>
    <li>E-posta: yedekmelik80@gmail.com</li>
</ul>

<h2>⚠️ Yasal Uyarı</h2>
<p>Bu araç, yalnızca yasal ve etik kullanım için tasarlanmıştır. Yetkisiz sistem taraması yasal değildir.</p>
