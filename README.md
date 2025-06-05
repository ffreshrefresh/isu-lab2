# NmapEducator – Terminal Tabanlı Nmap Eğitim Aracı

## 📌 Proje Tanımı

NmapEducator, Nmap'in temel tarama komutlarını öğretmek amacıyla geliştirilen etkileşimli bir terminal uygulamasıdır. Kullanıcıdan alınan seçimler doğrultusunda Nmap komutları çalıştırılır, çıktılar gösterilir ve ardından açıklayıcı bilgiler sunularak öğrenme desteklenir.

---

## 🎯 Amaç

Ağ güvenliğine giriş yapan kullanıcıların:
- Nmap komutlarını doğrudan deneyimlemesi,
- Her komutun işlevini ve çıktısını öğrenmesi,
- Gerçek örneklerle ağ tarama becerilerini geliştirmesi amaçlanmıştır.

---

## ⚙️ Özellikler

- Etkileşimli terminal menüsü
- Kullanıcıdan hedef IP alma
- 7 farklı tarama türü:
  - Ping Taraması (`-sn`)
  - TCP Taraması (`-sT`)
  - SYN Taraması (`-sS`)
  - OS Tespiti (`-O`)
  - Servis Versiyon Tespiti (`-sV`)
  - Script Taraması (`--script vuln`)
  - Hepsi Bir Arada
- Tarama sonrası açıklayıcı bilgi sunumu
- Tüm çıktılar `scan_log.txt` dosyasına kaydedilir

---

## 🚀 Kurulum ve Kullanım

### Gereksinimler:
- Python 3
- Nmap yüklü olmalıdır (`sudo apt install nmap`)

### Kurulum:
```bash
git clone https://github.com/kullaniciadi/nmapeducator.git
cd nmapeducator
```

### Çalıştırmak için:
```bash
python3 nmapeducator.py
```

---

## 💡 Örnek Kullanım

```
NmapEducator'a hoş geldiniz.

Lütfen gerçekleştirmek istediğiniz taramayı seçin:
1) Ping Taraması
2) TCP Taraması
...
Seçiminiz: 2

Lütfen hedef IP adresini girin: scanme.nmap.org
[Tarama Başlatıldı: nmap -sT scanme.nmap.org]

-- Çıktı görüntülenir --

Açıklama:
TCP Connect taraması, açık portlara tam bağlantı kurarak tarama yapar. Firewall’lar tarafından kolayca tespit edilebilir.
```

---

## 📂 Çıktılar

- Tüm tarama sonuçları `scan_log.txt` dosyasında saklanır.
- Her kayıtta tarih, hedef IP ve tarama tipi bilgisi bulunur.

---

## 👥 Geliştirici Ekip

- Engin Can ÜNLÜER – 2320191039  
- Ömer Berk ERİŞ – 2320191017  
- Doğukan KUMBASAR – 2320191026  
- Ferhat Civelek – 2320191053  
- Mert Çakmak – 2320191029

---

## 📄 Lisans

Bu proje yalnızca eğitim amaçlıdır. Gerçek sistemlere izinsiz tarama yapılmamalıdır.
