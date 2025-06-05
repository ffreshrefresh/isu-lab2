# 🔬 Araştırma-Geliştirme Promptu: "Nmap ile Aktif ve Pasif Ağ Haritalaması: Çok Katmanlı Bir Yaklaşım"

## 🎯 Genel Amaç
Bu projede, Nmap kullanılarak farklı ağ segmentlerinin çok katmanlı olarak haritalanması hedeflenmektedir. Sadece basit port taramaları değil, aynı zamanda OS fingerprinting, versiyon analizi, zamanlama davranışları, firewall atlatma teknikleri ve Nmap Scripting Engine (NSE) ile zafiyet keşfi dahil olmak üzere kapsamlı bir bilgi toplama süreci tasarlanacaktır.

---

## 🧠 Araştırma Soruları

### 1. Ağ Haritalama Stratejileri
- Nmap ile hangi durumlarda aktif, hangi durumlarda pasif yöntemler tercih edilmelidir?
- Büyük ölçekli bir ağda segment bazlı keşif nasıl planlanır?

### 2. Tarama Teknikleri ve Zamanlama
- `-T0` ila `-T5` zamanlama seviyelerinin tespit edilebilirlik ve performans açısından etkileri nedir?
- IDS/IPS sistemlerinden kaçınmak için en uygun zamanlama ayarları nelerdir?

### 3. Firewall/IPS Atlatma ve Şifrelenmiş Trafik Analizi
- `--data-length`, `--source-port`, `--badsum`, `-f` gibi bayraklarla yapılan taramaların etkileri nelerdir?
- TLS/SSL üzerinden çalışan servislerde portların arkasına saklanan bilgileri tespit etmek mümkün müdür?

### 4. Gerçek Senaryoda Uygulama
- Sanal bir test laboratuvarı (örneğin: Metasploitable2, DVWA, custom pfSense FW) üzerinde örnek keşif ve analiz süreci
- Elde edilen verilerin log analiziyle eşleştirilmesi

### 5. Etik, Yasal ve Operasyonel Boyut
- Nmap taramalarının yasal sınırları nelerdir?
- Red Team ve Blue Team bakış açılarıyla bu taramaların kullanımı nasıl farklılaşır?

---

## 🔨 Pratik Uygulama Alanları

- Kurumsal bir ağda güvenlik denetimi
- Kendi ağınızda Red Team simülasyonu
- Penetrasyon testi öncesi bilgi toplama fazı
- Honeypot sistemlerinin tespiti ve analizi

---

## 📦 Teslim Edilmesi Beklenen Çıktılar

1. **Detaylı bir teknik rapor:**
   - Kullanılan Nmap komutları ve açıklamaları
   - Elde edilen bulgular (OS, servis, port, zafiyet vb.)
   - Zamanlama analizi sonuçları ve IDS/IPS tespiti üzerine yorumlar

2. **NSE Script kullanımı içeren mini kütüphane veya öneri listesi**

3. **Geliştirilmiş özel bir Nmap komut seti veya bash wrapper script’i (opsiyonel)**

4. **Varsa:** Wireshark logları veya ekran görüntüleriyle desteklenmiş vaka çalışmaları

---

## 🧰 Kullanılabilecek Araçlar

- **Nmap** (en güncel sürüm)
- **Wireshark** (trafik gözlemi için)
- **Metasploitable2**, **DVWA**, **pfSense**, **Kali Linux** (test ortamı için)
- **Python veya Bash** (otomasyon için)

---

## 🌐 Ekstra Derinlik için Kaynaklar

- [Nmap Book (Gordon Lyon)](https://nmap.org/book/)
- Nmap NSE Script Library: [https://nmap.org/nsedoc/](https://nmap.org/nsedoc/)
- Offensive Security Exploit DB
- BlackHat & DefCon sunumları (özellikle ağ keşfi ve firewall bypass üzerine)
