Bir veriseti oluşturma adımlarının **[veri kazıma](https://github.com/Teknofest-Nane-Limon/twitter-scraper)** aşamasından sonraki bütün adımlarının kolay, hızlı ve ulaşılabilir şekilde yapılması için tasarlanmış bir otomasyondur.
Ekip üyelerinin verisetini oluşturmak için herhangi bir zamanda herhangi bir yerden işbirliği yapabilmelerini sağlamaktadır. 
Aynı zamanda etiketlenen verilerin istatistiklerini içermektedir. 
Bu sayede hangi sınıftan ne kadar etiketli veriye sahip olunduğu ve kaç adet verinin veri setine dahil edilip kaçının dahil edilmeyeceği gibi bilgilerin 
veri etiketleme adımındayken monitörize edilmesi sağlanmıştır. 
Etiketlemenin sonunda etiketli verilerin incelenebilmesi ve veri setinin excel formatında çıktısının alınması gibi özellikleri de bulunmaktadır. 
Bu özellikleri sayesinde etiketli bir veri seti oluşturulması için gerekli bütün adımlar tek bir otomasyon ile yapılabilir hale gelmiştir.
[Heroku bulut tabanlı platform servisi](https://www.heroku.com/about#:~:text=Heroku%20is%20a%20container%2Dbased,getting%20their%20apps%20to%20market.) kullanılarak ücretsiz bir şekilde verileri paylaşma ve etiketli verilerin database e aktarılıp veri setinin oluşturulması sağlanmıştır.


#### Aracın kullanımını anlatan video için <youtube-link>

# Ortam Oluşturma

Lütfen Python sürümünüzü '3.10' olarak ayarlayın.

Python versiyonunuzdan emin olmak için:

```bash
python3 --version
```

## Geliştirme Ortamını Ayarlamak
- Virtual environment oluşturunuz.
```bash
    $ python -m venv <venv-name>
```
- Virtual environmentınızı aktive ediniz.
```bash
    $ source <venv-name>/bin/activate
```
- Kütüphaneleri Yükleyiniz.
```bash
    $ pip install -r requirements.txt
```
## data.csv nin Uygulamaya Dahil Edilmesi
  
  Etiketlemesini yapmak istediğiniz verileri [static/datas](https://github.com/Teknofest-Nane-Limon/easy-data-labeling-engine/tree/main/static/datas) altına taşıyınız. 
  ```bash
    $ mv data.csv static/datas
  ```
## Veritabanının Düzenlenmesi
  Etiketlenecek olan metadata ve etiketlenen verinin oluşturulması için kurgulanmış database modellerinin bir veritabanı motorunda tutulması gerekmektedir.
  
  Bu veritabanı motoru app.py ve ctor.py içinde ayarlanmalıdır.
  ### app.py
  SQLite için;
  ```bash
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
  ```
  
  Postgresql için;  
  ```bash
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:password@localhost/database'
  ```

  ### ctor.py
  SQLite için;
  ```bash
    engine = create_engine('sqlite:///' + os.path.join(basedir, 'database.db'), echo=True)
  ```
  
  Postgresql için;  
  ```bash
    create_engine('postgresql://root:password@localhost/database', echo=True)
  ```

  ### Veritabanı Tabloları
  
  Constructor File(ctor.py) çalıştırılması ile eklenen data.csv Scraped tablosuna kaydedilmektedir. 
  Uygulama üzerinden etiketlenen her veri için Tagging tablosuna kayıt atılmaktadır. 
  Bu sayede aralarında ilişki kurulmakta ve etiketli veriler etiketli veriseti haline getirilmektedir.
  
  ![plot](./static/img/table_models.png)
  
## Metadatanın Veritabanına Eklenmesi
constructor file çalıştırılarak data.csv içindeki verilerin veritabanına kaydedilmesi sağlanmıştır.
```bash
    $ python3 ctor.py
```

# Çalıştırma

Uygulamanın çalışması için gerekli adımlar tamamlanmıştır.

```bash
    $ python3 wsgi.py
```

App 8000 portunda çalışmaktadır.
> http://localhost:8000/ 



[araç linki](https://easy-data-labeling-engine.herokuapp.com/)
