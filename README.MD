# ***Follower Controller***

---
<br>

## ![a.png](images/a.png) **Table of Contents**
- ### [Decription](#bpng-description) 
- ### [Key Features](#cpng-key-features) 
- ### [Setup](#fpng-setup) 
- ### [Usage](#epng-usage) 
- ### [Third Party License](#fpng-third-party-licenses) 

---
<br>

## ![b.png](images/b.png) **Description**
- Projenin yapılış amacı; takipçi ve takip edilenleri kontrol eden bir bot olması. Eğerki sürekli takipçilerinizi ve takip edilenleri kontrol ediyorusanız bunu sizin yerinize yapıyor.

---
<br>

## ![c.png](images/c.png) **Key Features**
- Projenin iki ana fonksiyonu vardır:
    <br>
    - Birinci olarak, takipçi bildirim sistemidir. Bu sistemde sizi yeni takip edenler bir mail içerisinde isimleri ve bilgileri gönderilir.
    <br>

    - İkinci olarak, sizin takip ettiğiniz ama sizi takip etmeyen kişilerin filtrelenmesi. Ve filtreler sonucunda istenmeyen kişilerin takipten çıkılması. Bu profiller 

---
<br>

## ![f.png](images/d.png) **Setup**
- ### *Modüllerin Kurulması*
    - Uygulamanın kullandığı 4 built in olmayan modül var. Eğerki bunlar veya bunlardan biri bilgisayarınızda yoksa aşağıda gözüken pip kodları ile indirebilirsiniz
    ```
    pip install pyinstaller
    pip install pandas
    pip install selenium
    pip install yagmail
    ```
    
    >***Not***: Yukarıdaki kodların çalışabilmesi için PİP(Python Package Installer) yüklü olması lazım

<br>

- ### *Kaynak dosyaların indirilmesi*
    - Uygulumanın çalışabilmesi için 3 ana ihtiyaç var
        - <ins>Kaynak kodları</ins>: Kaynak kodlarının hepsi src klasörünün içerisinde bulunmaktadır.
        > src/
        - <ins>Driver</ins>: Uygulamanın chrome ile bağlantı kurması için bir driver ihtiyacımız var. Bu driver'ı kendiniz interntten bulabilirsiniz ama direk aşağıdaki klasör içinden alabilirsinizde
        > driver/

        - <ins>Gerekli Veriler</ins>:  Uygulumanın çalışabilmesi için gerekli verileri bulunduran klasörü indirmelisiniz. Bu klasörde takipçi-takip edilen listesi ve uygulumanın çalışabilmesi için gerekli olan verilerinizn olduğu json dosyaları var
        >Datas/
    
    - Bunların hepsine clone ile direk bilgisayarınıza yükleyebilirsiniz


    ```
    git clone https://github.com/AlgorithmXplorer/Follower_Controller 
    ```
    

---
<br>

## ![e.png](images/e.png) **Usage**

---
<br>

## ![f.png](images/f.png) **Third Party Licenses**

### ![g.png](images/g.png) Yagmail
- **License**: <ins>MIT License</ins> → Bu lisans oldukça serbest bir lisans türüdür; kodu kısıtlama olmaksızın kullanabilir, değiştirip dağıtabilirsiniz; lisans bildirimi ve telif hakkı bildiriminin muhafazası gerekir
- **Link**: https://pypi.org/project/yagmail
<br>

### ![g.png](images/g.png) Selenium
- **License**: <ins>Apache License 2.0</ins> → Bu lisans koşullarıyla, yazılımı ticari veya açık kaynak kullanımlarında serbestçe kullanabilirsiniz; tek şart telif hakkı bildirimi ve lisans bildirimini korumanızdır
- **Link**: https://pypi.org/project/selenium
<br>

### ![g.png](images/g.png) Pandas
- **License**: <ins>BSD 3-Clause License</ins> → Bu lisans, yazılımı geniş şekilde kullanmanıza ve dağıtmanıza izin verir; kaynak kod bildirimlerini korumanız gerekir.
- **Link**: https://pypi.org/project/pandas
<br>

### ![g.png](images/g.png) Pyinstaller
- **License**: <ins>GNU General Public License v2 (GPLv2) […with an exception that allows you to build commercial applications with it]</ins> → Bu lisansla, PyInstaller’ı kullanarak oluşturduğunuz yürütülebilir paketleri kendi lisansınızla dağıtabilirsiniz; ancak PyInstaller’ın kaynak kodunda yaptığınız değişiklikleri dağıtırsanız bu değişiklikler GPL v2 şartlarına tabi olur.
- **Link**: https://pypi.org/project/pyinstaller




