# NmapEducator Proje Raporu

## Özet
NmapEducator, Nmap aracını kullanarak ağ güvenliği ve port tarama tekniklerini öğretmek amacıyla tasarlanmış etkileşimli bir komut satırı (CLI) uygulamasıdır. Menü tabanlı arayüzü sayesinde kullanıcılar çeşitli tarama türlerini çalıştırabilir, sonuçları görebilir ve her komutun amacı ile çıktısının nasıl yorumlanacağına dair bilgi edinebilirler.

## Giriş
Ağ keşfi ve port tarama, siber güvenliğin temel becerilerindendir. Nmap, bu alanda yaygın olarak kullanılan güçlü bir araçtır, ancak farklı parametrelerin anlaşılması yeni başlayanlar için karmaşık olabilir. NmapEducator, her tarama komutunu bağlamsal açıklamalarla sunarak öğrenme sürecini kolaylaştırmayı hedefler.

## Proje Hedefleri
- Nmap komutlarının öğrenilmesini basitleştirmek için interaktif bir menü sağlamak.
- Her tarama için açıklayıcı geri bildirim ve loglama sunmak.
- IPv6 tarama, zamanlama şablonları, WAF tespiti gibi ileri teknikleri entegre etmek.
- Kullanıcıların pratik yaparak öğrenmesini teşvik etmek.

## Yöntem
Proje Python ile geliştirilmiş olup, subprocess ile Nmap komutlarını çalıştırmak, JSON ile açıklamaları okumak ve dosya I/O ile loglama yapmak üzerine kuruludur. `descriptions.json` dosyası, her tarama türü için açıklamaları içerir. Ana script, kullanıcı girişini alır, uygun Nmap komutunu çalıştırır ve sonuçları hem ekrana hem de `scan_log.txt` dosyasına kaydeder.

## Uygulama Detayları
- **Menü Sistemi:** Ping, TCP, SYN, OS tespiti, servis versiyonu gibi 20'den fazla tarama seçeneği.
- **Açıklamalar:** `descriptions.json` üzerinden bağlamsal bilgi sunar.
- **Loglama:** `scan_log.txt` dosyasına zaman damgalı tarama geçmişi ekler.
- **İleri Modüller:** IPv6 tarama, zamanlama şablonları, XML çıktı, WAF tespiti, anomali ve tehdit istihbaratı özellikleri.

## Özelliklerin Özeti
1. Temel taramalar: Ping, TCP, SYN, OS, sürüm tespiti, script zafiyet taraması.
2. IPv6 Ping desteği.
3. Zamanlama şablonları: Paranoid’den Insane’e 6 mod.
4. OpenVAS için XML çıktı.
5. WAF tespiti, IoT port taraması, web enum.
6. OSINT hedef otomasyonu, idle/stealth scan.
7. Anomali tespiti ve MITRE ATT&CK eşleme.

## Test ve Sonuçlar
- **Localhost (127.0.0.1)** üzerinde temel taramalar başarıyla test edildi.
- **scanme.nmap.org** ile OS, sürüm ve script taramaları doğrulandı.
- **IPv6 loopback (::1)** ile IPv6 ping testi gerçekleştirildi.
- Anomali tespiti, iki tarama arasındaki değişiklikleri doğru şekilde işaretledi.

## Sonuç
NmapEducator, ağ tarama tekniklerini öğretmek için başarılı bir platform sunar. Modüler yapısı, yeni tarama türleri ve eğitim modülleri eklemeyi kolaylaştırır. Gelecekte GUI entegrasyonu veya Python Nmap kütüphanesi ile daha zengin kontrol imkânı sağlanabilir.

## Kaynaklar
- Nmap Resmi Dokümantasyonu: https://nmap.org/book/man.html
- Fyodor, “Nmap Network Scanning”, Nmap.org.
- Python 3 Standart Kütüphane Dokümantasyonu.
- 2025 Ağ Keşfi Araştırma Prompt'ları.
