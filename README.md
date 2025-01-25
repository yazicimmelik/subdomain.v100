Proje Adı: Melik YAZICI

Öğrenci Adı ve Numarası: Melik Yazıcı - 2320191071

Teslim Tarihi: 31.01.2025

<h1>Projenin Tanımı</h1>

Subdomain Keşif Aracı, bir alan adına ait tüm alt alan adlarının (subdomain) tespit edilmesini sağlayan bir yazılım aracıdır. Araç, hem aktif hem de pasif tarama yöntemleri kullanarak DNS kayıtlarını analiz eder, wildcard DNS gibi yaygın çözümlemeleri tespit eder ve sonucu JSON formatında sunar.

Kapsam

Bu proje, bir siber güvenlik sızma testi aşamasında hedef alan adı hakkında derinlemesine bilgi toplamak için tasarlanmıştır.

Keşfedilen Alanlar:

Subdomain brute-force ve permütasyon türevleri

DNS Sunucu türü ve kayıtlarının analizi (A, AAAA, CNAME, MX)

Sertifika Transparency Log'ları ile subdomain keşifleri

Erişim kontrolü ve çözümleme doğrulama

Çözülen Güvenlik Problemi

Bir kurumun subdomain bilgilerini gizli tutması, potansiyel siber sızma tehditlerini engellemek adına kritiktir. Yanlış konfigüre edilmiş veya unutulmuş subdomainler ciddi güvenlik açıklarına neden olabilir. Bu araç, subdomainlerin tespit edilmesini kolaylaştırarak görünmeyen bu riskleri ortaya çıkarır ve daha güvenli bir altyapı sağlar.

Hedef Kitle ve Kullanım Alanları

Hedef Kitle:

Siber güvenlik uzmanları ve sızma testi ekipleri

DevOps ve altyapı güvenliği yöneticileri

Üniversite öğrencileri (siber güvenlik alanında çalışanlar)

Kullanım Alanları:

Kurumsal altyapı güvenlik taramaları

Red-Team/Pentest operasyonlarında reconnaissance aşaması

DNS yapılarının çözümleme ve konfigürasyon denetimleri

Teknik Gereksinimler

Programlama Dili: Python 3.11

Gerekli Kütüphaneler:

dnspython (v2.3.0): DNS sorguları için kullanılacak.

requests (v2.31.0): Sertifika log verilerinin çekilmesi.

argparse (standart Python kütüphanesi): Komut satırı parametreleri için.

json (standart Python kütüphanesi): Sonuçların JSON formatında çıktısı.

concurrent.futures (standart Python kütüphanesi): Paralel DNS sorguları için.

Değerlendirme Kriterleri

Araç, minimum şu özellikleri desteklemelidir:

DNS sorguları ile subdomain doğrulama.

Wildcard DNS algılama.

Erişim kontrolü ve aktif subdomain raporlaması.

JSON formatında çıktı doğruluğu ve okunabilirliği.

Kodun temizliği, yorumlar ve okunabilirlik.

Dokümantasyonun tam ve anlaşılır olması.

Performans: 1000 subdomain içeren bir listede ortalama tarama sürelerinin optimize edilmiş olması.

