# NmapEducator – Proje Yol Haritası

Bu belge, NmapEducator projesinin geliştirme sürecinde izlenecek adımları ve hedefleri açıklar.

---

## 🎯 Proje Hedefi

Terminal tabanlı etkileşimli bir Python uygulaması geliştirerek, kullanıcılara Nmap'in temel tarama komutlarını deneyimleme ve anlamlandırma imkânı sunmak.

---

## 🧩 Geliştirme Aşamaları

### 1. Proje Başlangıcı ve Yapı Kurulumu
- GitHub reposunun oluşturulması
- Ana Python dosyasının (`nmapeducator.py`) açılması
- Temel terminal karşılama ekranı hazırlanması

### 2. Kullanıcı Etkileşimi ve Menü Yapısı
- Kullanıcıdan tarama tipi seçimi alma
- Seçilen tarama tipine göre komutların eşleştirilmesi
- Hedef IP adresi girişinin alınması

### 3. Nmap Komutlarının Uygulanması
- Seçime göre Nmap taramasının çalıştırılması:
  - Ping Taraması (`-sn`)
  - TCP Tarama (`-sT`)
  - SYN Tarama (`-sS`)
  - OS Tespiti (`-O`)
  - Servis Versiyon Tespiti (`-sV`)
  - Script Taraması (`--script vuln`)
  - Hepsi Bir Arada

### 4. Açıklama ve Eğitim İçeriği Entegrasyonu
- Her tarama komutu sonrası açıklayıcı metnin gösterilmesi
- Açıklamaların ayrı bir yapıdan (örneğin `.json` veya `.txt`) alınması

### 5. Loglama ve Raporlama
- Tüm tarama çıktılarının `scan_log.txt` gibi bir dosyaya yazdırılması
- Hedef IP ve tarama tipi bilgisiyle birlikte zaman damgası eklenmesi

### 6. Test ve Değerlendirme
- Bilinen örnek hedefler ile test yapılması (örn. `scanme.nmap.org`)
- Yanlış IP girilmesi gibi hataların kullanıcı dostu şekilde ele alınması

### 7. Dokümantasyon ve Teslim Hazırlığı
- `README.md`, `ROADMAP.md`, kullanım açıklamaları
- Geliştirici notları ve görev dağılımı dosyası
- Son demo ve çıktılarla birlikte proje sunumunun hazırlanması

---

## 🔚 Hedef

Kullanıcıların ağ tarama araçlarını etik ve güvenli bir biçimde öğrenmesini sağlayan, sade, terminal tabanlı bir uygulama geliştirmek ve dokümantasyonu tamamlanmış şekilde teslim etmektir.