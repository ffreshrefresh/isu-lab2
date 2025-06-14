# ✨ NmapEducator – Terminal Tabanlı Nmap Eğitim Aracı

**NmapEducator**, ağ güvenliği ve port tarama tekniklerini interaktif bir şekilde öğrenmenizi sağlayan, zengin özelliklere sahip bir CLI aracıdır.

---

## 📋 İçindekiler
1. [Özellikler](#-özellikler)  
2. [Demo](#-demo)  
3. [Kurulum](#-kurulum)  
4. [Kullanım](#-kullanım)  
5. [Ekip](#-ekip)  
6. [Lisans](#-lisans)  

---

## 🌟 Özellikler

- 🚀 **Hızlı Başlangıç:** Tek komutla menü tabanlı tarama  
- 🖥️ **Çeşitli Modüller:** Ping, TCP/SYN, OS tespiti, servis versiyonu  
- 🔍 **Script Taraması:** Vuln, Web Enum, WAF fingerprint  
- 🌐 **IPv6 & IoT:** IPv6 ping, UPnP & CoAP taramaları  
- 🕒 **Zamanlama Şablonları:** Paranoid’den Insane’e 6 mod  
- 📂 **OpenVAS Export:** Nmap çıktısını direkt XML formatına aktar  
- 🛡️ **WAF & OSINT:** Web uygulama duvarı tespiti, hedef okuma  
- 🔔 **Anomali Tespiti:** Önceki ve sonraki taramaları karşılaştır  
- 🧠 **Tehdit İstihbaratı:** Açık portlara MITRE ATT&CK TTP eşlemesi  
- 📝 **Loglama:** `scan_log.txt` ile tüm tarama geçmişi saklanır  

---

## 🖥️ Demo

```bash
$ python3 nmapeducator.py

=== NmapEducator ===
Ağ tarama tekniklerini öğrenmek için bir seçim yapın.

1) Ping Taraması (-sn)
2) TCP Taraması (-sT)
...
```

<p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/placeholder/demo.gif" alt="Demo GIF">
</p>

---

## ⚙️ Kurulum

1. Repoyu klonlayın:
    ```bash
    git clone https://github.com/ffreshrefresh/isu-lab2.git
    cd isu-lab2
    ```
2. Gerekli modülleri yükleyin (isteğe bağlı):
    ```bash
    pip3 install -r requirements.txt
    ```
3. Uygulamayı çalıştırın:
    ```bash
    chmod +x nmapeducator.py
    ./nmapeducator.py
    ```

---

## 🎯 Kullanım

- Menüyü görüntüleyip seçim yapın.  
- Hedef IP/domain girin.  
- Çıktıyı görün ve `scan_log.txt` dosyasına kaydedin.

```bash
Seçiminiz: 9
Zamanlama Modları:
0) Paranoid
...
Seçiminiz: 3
Hedef IP/domain girin: 192.168.1.1
...
```

---

## 👥 Ekip

| İsim                | Öğrenci No   |
|---------------------|--------------|
| Engin Can ÜNLÜER    | 2320191039   |
| Ömer Berk ERİŞ      | 2320191017   |
| Doğukan KUMBASAR    | 2320191026   |
| Ferhat CİVELEK      | 2320191053   |
| Mert ÇAKMAK         | 2320191029   |

---

## 📄 Lisans

Bu proje tamamen **eğitim amaçlı**dır. İzinsiz tarama veya kötü niyetli kullanım yasaktır.
