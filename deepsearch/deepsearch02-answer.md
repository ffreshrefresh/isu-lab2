🔬 Nmap ile Aktif ve Pasif Ağ Haritalaması: Çok Katmanlı Bir Yaklaşım - Proje Raporu Taslağı
🎯 Giriş ve Proje Özeti
Bu rapor, "Nmap ile Aktif ve Pasif Ağ Haritalaması: Çok Katmanlı Bir Yaklaşım" başlıklı araştırma ve geliştirme projesi kapsamında yürütülen çalışmaları ve elde edilen bulguları detaylandırmaktadır. Projenin temel amacı, Nmap'i kullanarak farklı ağ segmentlerinin sadece port taramalarıyla sınırlı kalmayıp, OS fingerprinting, versiyon analizi, zamanlama davranışları, firewall atlatma teknikleri ve Nmap Scripting Engine (NSE) ile zafiyet keşfi dahil olmak üzere kapsamlı bir bilgi toplama sürecini tasarlamak ve uygulamaktır.

Bu çalışma, kurumsal ağlarda güvenlik denetimleri, Red Team simülasyonları, penetrasyon testi öncesi bilgi toplama ve Honeypot sistemlerinin tespiti gibi pratik uygulama alanlarına odaklanmaktadır.

🧠 Araştırma Soruları ve Cevapları
1. Ağ Haritalama Stratejileri

Nmap ile hangi durumlarda aktif, hangi durumlarda pasif yöntemler tercih edilmelidir?
Aktif Tarama (Nmap): Hedef sistemle doğrudan etkileşim kurularak bilgi toplama yöntemidir. Yüksek doğruluk ve detaylı bilgi sağlama potansiyeli vardır. Genellikle penetrasyon testi öncesi bilgi toplama, kendi ağınızda güvenlik denetimi veya bilinen sistemlerde hızlı keşif gerektiğinde tercih edilir. Ancak, IDS/IPS sistemleri tarafından kolayca tespit edilebilir ve loglarda iz bırakır.
Pasif Tarama (Wireshark, tcpdump): Ağ trafiğini dinleyerek bilgi toplama yöntemidir. Hedef sistemle doğrudan etkileşim kurulmadığı için daha az tespit edilebilir ve daha gizlidir. Özellikle gizliliğin öncelikli olduğu senaryolarda, hedef sistemde anormal aktivite yaratmak istemediğinizde veya ağdaki mevcut trafik desenlerini analiz etmek istediğinizde tercih edilir. Pasif taramalar genellikle açık portlar, kullanılan protokoller ve belirli servislerin varlığı hakkında ipuçları sağlayabilir ancak aktif tarama kadar detaylı bilgi (örneğin spesifik versiyon numaraları, işletim sistemi detayları) vermeyebilir.
Büyük ölçekli bir ağda segment bazlı keşif nasıl planlanır?
Ağ Segmentasyon Haritalaması: İlk adım, ağın mantıksal ve fiziksel segmentasyonunu çıkarmaktır (VLAN'lar, alt ağlar, güvenlik bölgeleri vb.).
Hedef Belirleme ve Prioritizasyon: Kritik sunucular, DMZ'ler, kullanıcı ağları gibi öncelikli hedefler belirlenir.
Aşamalı Tarama: Tüm ağı aynı anda taramak yerine, her bir segment için ayrı ayrı planlama yapılır. Küçük segmentlerden başlanarak genişlemeli bir yaklaşım izlenebilir.
Zamanlama ve Kaynak Yönetimi: Büyük ağlarda tarama süreleri uzun olabileceğinden, taramalar mesai saatleri dışında veya düşük yük zamanlarında planlanmalıdır. Ağ bant genişliği ve sistem kaynaklarının etkilenmemesi için dikkatli olunmalıdır.
Tespit Edilebilirlik Yönetimi: Her bir segment için farklı zamanlama ayarları ve firewall atlatma teknikleri uygulanabilir.
Otomasyon: Python veya Bash scriptleri kullanılarak tarama süreçleri otomatize edilebilir, sonuçlar düzenli olarak raporlanabilir.
2. Tarama Teknikleri ve Zamanlama

-T0 ila -T5 zamanlama seviyelerinin tespit edilebilirlik ve performans açısından etkileri nedir?
-T0 (Paranoid): En yavaş tarama modudur. Pakeler arasında uzun bekleme süreleri vardır. IDS/IPS sistemleri tarafından tespiti en zor olanıdır ancak performansı çok düşüktür ve uzun sürer. Çok gizli operasyonlarda kullanılır.
-T1 (Sneaky): -T0'dan biraz daha hızlıdır ancak hala yavaştır. Daha az tespit edilebilirliği hedefler.
-T2 (Polite): Tarama hızını kontrol eder, bant genişliğini daha az tüketir. Hedef sistemde düşük etki bırakır.
-T3 (Normal) (Varsayılan): Varsayılan tarama hızıdır. Performans ve tespit edilebilirlik arasında iyi bir denge sunar. Çoğu durumda yeterlidir.
-T4 (Aggressive): Daha hızlı tarar, daha agresif zamanlama kullanır. Daha kolay tespit edilebilir ancak sonuçları daha çabuk verir.
-T5 (Insane): En hızlı tarama modudur. Çok yüksek hızda paket gönderimi yapar. IDS/IPS sistemleri tarafından tespiti en kolay olanıdır ve hedef sistem üzerinde yüksek yük oluşturabilir. Hızlı ve gürültülü bilgi toplama gerektiğinde kullanılır.
IDS/IPS sistemlerinden kaçınmak için en uygun zamanlama ayarları nelerdir?
-T0 veya -T1: Maksimum gizlilik için tercih edilir. Ancak çok yavaş oldukları unutulmamalıdır.
Paket Boyutunu Ayarlama (--data-length): Anormal paket boyutları IDS'leri tetikleyebilir.
Fragmentasyon (-f veya --mtu): Paketleri küçük parçalara bölerek imzaların eşleşmesini zorlaştırabilir.
Decoy Tarama (-D): Tarama trafiğini gerçek tarayıcılar ve sahte IP'ler arasında dağıtarak tespiti zorlaştırır.
Kaynak IP Değiştirme (-S): Sahte kaynak IP adresleri kullanarak tespiti zorlaştırır.
Rastgele Host Sıralaması (--randomize-hosts): Hedefleri rastgele sırada taramak, belirli bir tarama desenini kırmayı sağlar.
Rastgele Gecikmeler (--scan-delay): Her tarama arasında rastgele gecikmeler ekleyerek düzenli tarama paternlerini bozar.
3. Firewall/IPS Atlatma ve Şifrelenmiş Trafik Analizi

--data-length, --source-port, --badsum, -f gibi bayraklarla yapılan taramaların etkileri nelerdir?
--data-length <num>: Gönderilen paketlere rastgele veri ekler. Bu, paketlerin boyutunu değiştirerek IDS/IPS imzalarını atlatmaya veya normal trafik gibi görünmelerini sağlamaya yardımcı olabilir. Ancak, bazı güvenlik cihazları anormal boyutlu paketleri de tespit edebilir.
--source-port <portnumber>: Kaynak portunu belirli bir port numarası olarak ayarlar (örneğin, 80 veya 53). Bu, bazı güvenlik duvarı kurallarını atlatmak için kullanılabilir. Güvenlik duvarları genellikle bilinen servis portlarından gelen trafiğe daha az şüpheyle yaklaşır.
--badsum: Geçersiz bir TCP/UDP/IP sağlama toplamı gönderir. Güvenlik duvarları ve işletim sistemleri genellikle bu tür paketleri düşürür. Amacı, bazı firewall veya IDS/IPS sistemlerinin paketleri yanlış işlemesini tetikleyerek bilgi toplamaktır. Genellikle pasif bir tarama tekniğidir, doğrudan yanıt beklenmez.
-f (fragment): Tarama paketlerini küçük IP parçalarına böler. Bu, paket filtreleme kurallarını atlatmak için etkilidir, çünkü bazı güvenlik duvarları sadece paketin ilk parçasını inceler veya yeniden birleştirme mantığı hatalıdır. IDS/IPS imzalarını da atlatabilir.
TLS/SSL üzerinden çalışan servislerde portların arkasına saklanan bilgileri tespit etmek mümkün müdür?
Evet, kısmen mümkündür. Doğrudan şifreli içeriği okuyamazsınız ancak bazı bilgiler şifreleme öncesi veya şifreleme el sıkışması (handshake) sırasında ortaya çıkabilir:
SSL/TLS Sertifika Bilgileri: Sertifikadaki Ortak Ad (Common Name - CN), kuruluş, geçerlilik tarihleri gibi bilgiler, web sunucusunun veya uygulamanın kimliği hakkında ipucu verir. Nmap'in ssl-cert veya ssl-enum-ciphers NSE scriptleri bu bilgileri çekebilir.
Server Name Indication (SNI): Birçok web sunucusu, aynı IP adresinde birden fazla alan adını barındırır. TLS handshake sırasında istemci, hangi alan adına bağlanmak istediğini SNI uzantısıyla belirtir. Bu bilgi şifresizdir ve sunucunun barındırdığı diğer domainler hakkında bilgi verebilir.
Desteklenen Şifreleme Süitleri: Nmap, sunucunun desteklediği şifreleme algoritmalarını ve protokol versiyonlarını (TLS 1.0, 1.1, 1.2, 1.3) listeleyebilir. Bu, zayıf şifreleme kullanımı gibi potansiyel zafiyetleri ortaya çıkarabilir.
Hata Mesajları/Davranışlar: Şifreli bir servisle etkileşime girildiğinde dönen hata mesajları veya anormal davranışlar, arkadaki uygulamanın türü veya versiyonu hakkında ipuçları verebilir. Örneğin, belirli bir HTTP kodu veya hata metni.
NSE Scriptleri: Nmap'in çeşitli NSE scriptleri (http-enum, http-headers, dns-brute gibi) şifreli trafik üzerinden doğrudan içerik okumasa da, uygulamanın davranışlarına veya sertifika bilgilerine dayanarak ek bilgiler (örneğin, sanal hostlar, dizin listelemeleri) bulmaya çalışabilir.
4. Gerçek Senaryoda Uygulama

Sanal bir test laboratuvarı (örneğin: Metasploitable2, DVWA, custom pfSense FW) üzerinde örnek keşif ve analiz süreci
Laboratuvar Kurulumu: VirtualBox/VMware üzerinde Kali Linux (Nmap yüklü), Metasploitable2, DVWA (LAMP stack üzerinde), ve pfSense güvenlik duvarı kurulu bir ağ topolojisi oluşturulacaktır.
Metasploitable2 Keşfi:
Pasif Keşif (Wireshark): Metasploitable2'ye ping atarak veya bilinen portlarına (21, 22, 80) bağlantı girişiminde bulunarak Wireshark ile trafik yakalanacak. Hedef IP, MAC adresi, açılan TCP bağlantıları gözlemlenecek.
Aktif Keşif (Nmap):
Basit port taraması: nmap -sV -sC <Metasploitable2_IP>
OS fingerprinting: nmap -O <Metasploitable2_IP>
Gizli tarama (SYN scan): nmap -sS -T4 <Metasploitable2_IP>
NSE ile zafiyet tespiti: nmap --script vuln <Metasploitable2_IP> (Örnek: smb-vuln-ms17-010, ftp-anon)
Firewall atlatma denemeleri: -f, --source-port 80, --data-length 25 gibi bayraklarla taramalar yapılacak ve Wireshark ile gözlemlenecek.
DVWA Keşfi:
Nmap ile web sunucusunun (Apache) ve veritabanının (MySQL) portları tespit edilecek.
http-enum, http-headers gibi NSE scriptleri ile DVWA'nın web yapısı hakkında bilgi toplanacak.
pfSense Firewall Etkisinin Analizi:
pfSense arkasındaki bir hosta (örneğin Metasploitable2) hem pfSense üzerinden izin verilen hem de engellenen portlar için Nmap taramaları yapılacak.
Farklı zamanlama ayarları (-T0 vs. -T4) ve firewall atlatma bayrakları kullanılarak pfSense'in tepkisi gözlemlenecek. Wireshark ile pfSense üzerindeki ve hedefteki trafik karşılaştırılacak.
Elde edilen verilerin log analiziyle eşleştirilmesi
Nmap taramaları sırasında Metasploitable2'nin syslog/audit logları veya pfSense'in firewall logları incelenecek.
Hangi Nmap taramalarının hangi log girdilerini tetiklediği, IDS/IPS uyarılarını nasıl tetiklediği veya atlandığı tespit edilecek.
Log analiz araçları (örneğin, ELK Stack, Splunk Lite) kullanılarak tarama desenlerinin loglardaki karşılıkları görselleştirilebilir.
5. Etik, Yasal ve Operasyonel Boyut

Nmap taramalarının yasal sınırları nelerdir?
Yasal Yetki: Nmap taramaları, yalnızca yasal izne sahip olduğunuz ağlarda yapılmalıdır. İzinsiz tarama yapmak, çoğu ülkede siber suç olarak kabul edilir ve yasal sonuçları olabilir (örneğin, yasa dışı erişim girişimi, ağa zarar verme).
Sözleşmeler ve Politikalar: Bir şirket ağı üzerinde çalışırken, ilgili tüm sözleşmeler, gizlilik anlaşmaları ve şirket politikalarına uyulmalıdır.
Veri Gizliliği ve Güvenliği: Toplanan verilerin nasıl saklandığı, işlendiği ve raporlandığı, GDPR, KVKK gibi veri gizliliği düzenlemelerine uygun olmalıdır.
Zarar Verme: Tarama faaliyetleri, ağın veya sistemlerin performansını olumsuz etkilememeli, hizmet kesintisine neden olmamalıdır. Özellikle agresif tarama yöntemleri bu riski taşır.
Red Team ve Blue Team bakış açılarıyla bu taramaların kullanımı nasıl farklılaşır?
Red Team Bakış Açısı:
Amaç: Sistemlerin zafiyetlerini ve zayıf noktalarını tespit ederek güvenlik açıklarını istismar etmek.
Kullanım: Nmap'i gizli, tespit edilemez veya düşük ayak izli yöntemlerle kullanarak hedef ağ hakkında mümkün olduğunca fazla bilgi toplamak. Firewall atlatma teknikleri, IDS/IPS'i bypass etme ve zafiyet odaklı NSE scriptleri önceliklidir. Gerçek bir saldırgan gibi davranarak savunma mekanizmalarını test ederler.
Odak: Bilgi toplama, saldırı yüzeyini belirleme, potansiyel istismar vektörlerini bulma.
Blue Team Bakış Açısı:
Amaç: Kendi ağlarını ve sistemlerini siber saldırılara karşı savunmak, tespit etmek ve yanıt vermek.
Kullanım: Nmap'i kendi ağlarının zafiyetlerini belirlemek için proaktif olarak kullanırlar. Kendi ağlarında düzenli güvenlik denetimleri yaparlar, güvenlik politikalarının etkinliğini test ederler. Ayrıca, saldırı sonrası adli analizlerde (post-mortem forensics) şüpheli aktivitelerin kaynağını ve etki alanını belirlemek için de kullanabilirler. IDS/IPS loglarını Nmap taramalarıyla ilişkilendirerek kendi savunma sistemlerinin ne kadar etkili olduğunu anlarlar.
Odak: Savunma pozisyonunu güçlendirme, tespit ve yanıt kapasitesini artırma, güvenlik kontrollerinin doğrulanması.
🔨 Pratik Uygulama Alanları
Bu projenin çıktıları ve öğrenimleri, aşağıdaki pratik uygulama alanlarında değerli katkılar sağlayacaktır:

Kurumsal Bir Ağda Güvenlik Denetimi: Ağ segmentlerinin detaylı haritalandırılması, açıkta kalan servislerin tespiti ve zafiyet analizi ile güvenlik duruşunun güçlendirilmesi.
Kendi Ağınızda Red Team Simülasyonu: Saldırgan perspektifinden ağın zayıf noktalarını keşfederek proaktif savunma stratejileri geliştirmek.
Penetrasyon Testi Öncesi Bilgi Toplama Fazı: Hedef hakkında kapsamlı ve gizli bilgi toplayarak daha etkili bir saldırı planı oluşturmak.
Honeypot Sistemlerinin Tespiti ve Analizi: Ağdaki potansiyel Honeypot'ları Nmap ile tespit ederek, onların davranışlarını ve yakalama yeteneklerini analiz etmek.
📦 Teslim Edilmesi Beklenen Çıktılar
Bu projenin sonunda aşağıdaki çıktılar detaylı bir şekilde sunulacaktır:

1. Detaylı Bir Teknik Rapor

Kullanılan Nmap Komutları ve Açıklamaları: Sanal laboratuvarda kullanılan her bir Nmap komutu, amacı, parametreleri ve neden tercih edildiği detaylı bir şekilde açıklanacaktır.
Elde Edilen Bulgular (OS, Servis, Port, Zafiyet vb.): Her bir hedef sistem (Metasploitable2, DVWA, pfSense arkasındaki host) için tespit edilen işletim sistemi, açık portlar, çalışan servisler (versiyon bilgileriyle), ve tespit edilen zafiyetler (CVE ID'leri ile mümkünse) tablolar ve ekran görüntüleriyle sunulacaktır.
Zamanlama Analizi Sonuçları ve IDS/IPS Tespiti Üzerine Yorumlar: Farklı zamanlama seviyelerinin ve firewall atlatma tekniklerinin (data-length, source-port, fragmentasyon vb.) IDS/IPS sistemleri (pfSense firewall logları üzerinden) üzerindeki etkileri analiz edilecek ve elde edilen loglarla birlikte yorumlanacaktır. Hangi yöntemlerin daha gizli olduğu, hangilerinin tespiti tetiklediği belirtilecektir.
2. NSE Script Kullanımı İçeren Mini Kütüphane veya Öneri Listesi

Proje boyunca kullanılan ve faydalı bulunan NSE scriptlerinin bir listesi, her bir script'in amacı, kullanım senaryosu, örnek komutları ve elde ettiği bilgi türü hakkında kısa açıklamalarla birlikte sunulacaktır. Özellikle bilgi toplama, zafiyet tespiti, kimlik doğrulama zafiyetleri ve web zafiyetleri kategorilerinden scriptler içerecektir.

3. Geliştirilmiş Özel Bir Nmap Komut Seti veya Bash Wrapper Script’i (Opsiyonel)

(Bu bölüm, proje ilerledikçe geliştirilirse eklenecektir.)
Tekrarlayan tarama görevlerini otomatize etmek veya belirli bir test senaryosuna özel olarak hazırlanmış, optimize edilmiş Nmap komutlarını içeren bir Bash wrapper script'i veya Python script'i geliştirilecektir. Bu script, kullanıcı dostu parametreler alarak karmaşık Nmap komutlarını otomatik olarak oluşturabilecektir.

4. Wireshark Logları veya Ekran Görüntüleriyle Desteklenmiş Vaka Çalışmaları

Özellikle firewall atlatma denemeleri ve pasif ağ keşfi bölümleri için Wireshark'tan alınmış trafik yakalama logları veya ekran görüntüleri rapora eklenecektir. Bu görseller, Nmap paketlerinin ağda nasıl göründüğünü, fragmentation'ın etkilerini, kaynak port değişikliğinin nasıl yansıdığını ve IDS/IPS tarafından nasıl algılandığını somut bir şekilde gösterecektir.

🧰 Kullanılacak Araçlar
Proje kapsamında kullanılacak başlıca araçlar:

Nmap (en güncel sürüm): Temel ağ keşif ve tarama aracı.
Wireshark (trafik gözlemi için): Ağ trafiğini analiz etmek ve Nmap paketlerinin davranışını gözlemlemek için.
Metasploitable2, DVWA, pfSense, Kali Linux (test ortamı için): Sanal test laboratuvarı ortamını oluşturmak için.
Python veya Bash (otomasyon için): Tarama süreçlerini otomatize etmek ve raporlama için.
🌐 Ekstra Derinlik için Kaynaklar
Araştırma sürecinde faydalanılacak başlıca kaynaklar:

Nmap Book (Gordon Lyon)
Nmap NSE Script Library: https://nmap.org/nsedoc/
Offensive Security Exploit DB
BlackHat & DefCon sunumları (özellikle ağ keşfi ve firewall bypass üzerine)
İlgili RFC'ler ve akademik yayınlar.
