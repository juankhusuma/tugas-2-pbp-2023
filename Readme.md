# Tugas 2

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Membuat virtual enviroment
- Install django lalu create project inventory_app dengan django-admin pada directory sekarang menggunakan `django-admin startproject inventory_app .`
- Create app main didalam project inventory_app menggunakan manage.py menggunakan `python manage.py startapp main`
- Menambahkan 'main' ke INSTALLED_APPS di settings.py
- Setup urls.py di app main
- Setup templates dan file `layout.html` dan `index.html` yang akan di render pada app main
- Setup models.py lalu membuat object Product dengan attribute name sebagai nama item dengan tipe CharField, amount sebagai jumlah item dengan tipe IntegerField, description sebagai deskripsi item dengan tipe TextField, serta price sebagai harga item dengan tipe Integer.
- Run `./manage.py makemigrations` dan `./manage.py migrate` untuk melakukan migrasi ke database
- Setup views.py dengna menambahkan function index untuk melakukan data fetching dari object Product dan juga rendering html dari templates
- Menambahkan routing ke path / dan view index pada urls.py di app main
- Melakukan include pada urls.py di root project
- Melakukan push ke GitHub dan melakukan deployment pada platform Adaptable

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![diagram](https://cdn.discordapp.com/attachments/1029736062974705746/1151197511952891955/ws1.png)
Browser pada perangkat pengguna akan mengirimkan sebuah HTTP request ke server django melalui internet, request ini kemudian akan di route oleh urls.py ke function pada views.py yang tepat, function tersebut akan melakukan pemrosesan, mengambil data dari database melalui models.py serta melakukan rendering html dari templates, setelah selesai views akan mengembalikan HTTP response yang merupakan file html yang akan ditampilkan pada browser pengguna melalui internet.

## 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Untuk mengisolasi suatu projek dengan projek lainya, dimana modul-modul yang diinstall oleh pip di suatu projek terpisah dengan projek lain, selain itu setiap projek dengan virtual enviromentnya masing-masing dapat menggunakan versi yang berbeda dari suatu modul, hal ini dimungkinkan oleh isolasi yang dilakukan oleh virtual environment.

## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC membagi kode-kode pada suatu projek menjadi:
- Model: bagian yang berhubungan dengan pemrosesan data serta interaksi dengan database
- View: bagian yang berhubungan dengan tampilan yang disajikan ke pengguna
- Controller: bagian yang menghubungkan model dan view menjadi suatu kesatuan serta melakukan routing dan request handling

MVT membagi kode-kode pada suatu projek menjadi:
- Model: bagian yang berhubungan dengan pemrosesan data serta interaksi dengan database
- View: bagian yang melakukan pemrosesan request dan memberikan response kembali terhadap request tersebut dengan melakukan rendering template
- Template: tampilan yang akan diproses dan diberikan ke pengguna

MVVM membagi kode-kode pada suatu projek menjadi:
- Model: bagian yang berhubungan dengan pemrosesan data serta interaksi dengan database
- View: bagian yang berhubungan dengan tampilan yang disajikan ke pengguna
- ViewModel: menghubungkan view dengan model dan menjembatani pemrosesan data dari model hingga siap ditampilkan pada view

# Tugas 3

## 1. Apa perbedaan antara form ```POST``` dan form ```GET``` dalam Django?
Form  ```POST``` pada umumnya digunakan untuk mengubah data pada server atau database selain itu form ```POST``` dapat mengirimkan data dari client/browser ke server, misal saat ingin mengirim input user ke server untuk disimpan pada database, sedangkan form ```GET``` umumnya digunakan untuk mengambil data dari server ke client dan tidak mengirimkan data apapun ke server melainkan untuk meminta data agar dikirimkan dari server ke client/browser

## 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- HTML: Berupa definisi kerangka dan struktur dari suatu halaman web beserta tampilan dan juga data yang ditampilkan pada halaman web tersebut, namun HTML tidak dikembangkan untuk  pengiriman data, melainkan untuk menampilkan data secara rapi kepada pengguna.
- XML: Merupakan suatu _markup language_ untuk menyimpan dan mengirimkan data, XML besifat generic dimana pengguna dapat mendefisikan _tag_ dan struktur sendiri, umumnya XML berguna untuk pengiriman data yang bersifat kompleks.
- JSON: Merupakan format pengiriman data yang ringan dan sederhana dimana formatnya mirip seperti _dictionary_ atau _object_ pada Python dan JavaScript yang berisi _key value pair_ sehingga mudah diproses oleh mesin dan manusia, selain itu ukuranya cenderung lebih kecil dibandingkan dengan HTML dan XML.

## 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern
Karena strukturnya yang sederhana dan mirip seperti tipe data map atau object yang umumnya ada pada bahasa pemrograman modern dan dapat digunakan oleh berbagai bahasa pemrograman, sehingga mudah diproses oleh mesin dan mudah untuk membuat program yang mengubah dari data ke JSON atau sebaliknya, selain itu dikarenakan strukturnya yang sederhana, data JSON umumnya lebih ringan dan kecil dibanding format lainya.

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Membuat forms.py lalu mendefinisikan ProductForm untuk handling submission form pada model Product
- Menambahkan fungsi add_product untuk handling submit form sekaligus untuk menampilkan halaman form untuk menambahkan produk
- Menambahkan tampilan pada templates beserta styling pada static/css untuk menampilkan halaman form dan juga display item pada produk
- Menambahkan fungsi-fungsi pada views.py agar dapat menampilkan produk dalam format XML dan juga JSON, beserta menampilkan produk bedasarkan ID pada format XML dan juga JSON
- Menambahkan views yang telah dibuat pada urls.py di app main
## 5. Screenshot
- HTML
![html](https://media.discordapp.net/attachments/1029736062974705746/1153749675023794249/image.png?width=832&height=468)
- JSON
![json](https://media.discordapp.net/attachments/1029736062974705746/1151738049571602452/Screenshot_788.png?width=832&height=468)
- XML
![xml](https://media.discordapp.net/attachments/1029736062974705746/1151738049869389864/Screenshot_789.png?width=832&height=468)
- JSON By ID
![json-by-id](https://media.discordapp.net/attachments/1029736062974705746/1151738050221715487/Screenshot_790.png?width=832&height=468)
- XML By ID
![xml-by-id](https://media.discordapp.net/attachments/1029736062974705746/1151738050523709460/Screenshot_791.png?width=832&height=468)

# Tugas 4

## 1. Apa itu Django ```UserCreationForm```, dan jelaskan apa kelebihan dan kekurangannya?
```UserCreationForm``` adalah sebuah _class_ yang telah disediakan oleh Django _framework_ untuk mempermudah pembuatan form pendaftaran pengguna. 
- Kelebihan: mempermudah pembuatan dan pemrosesan form untuk pembuatan atau registrasi pengguna
- Kekurangan: sulit untuk di kostumisasi jika aplikasi membutuhkan alur atau data registrasi yang berbeda dengan yang terdapat pada ```UserCreationForm```
## 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
- Autentikasi adalah proses verifikasi pengguna untuk memastikan keaslian dari pengguna tersebut dan memastikan bahwa pengguna yang sedang melakukan _request_ sesuai dengan klaim yang dibuat.
- Otorisasi adalah proses untuk memastikan pengguna tidak mengakses _resource_ atau melakukan aksi yang seharusnya tidak dapat dilakukan atau diakses oleh pengguna tersebut, singkatnya otorisasi menentukan serta membatasi hak dari suatu pengguna mengenai apa yang dapat diakses atau dilakukan.
Kedua aspek ini penting dikarenakan autentikasi dan otorisasi membatasi dan mencegah data-data agar tidak diakses oleh pihak yang tidak seharusnya memiliki akses terhadap data tersebut agar tidak disalahgunakan.
## 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
_cookies_ adalah sebuah media penyimpanan pada suatu peramban internet yang berukuran ~5KB. _Cookies_ digunakan oleh Django dalam proses autentikasinya, dimana Django menggunakan _session based authentication_ yaitu ketika pengguna berhasil di autentikasi, Django akan membuat suatu token sesi sebagai identifikasi unik dari pengguna tersebut dan disimpan oleh _server_ pada _database_ lalu Django akan juga akan menyimpan _session_ tersebut pada _cookie_ di peramban internet dimana masa kadaluwarsa dari _cookie_ tersebut dapat disesuaikan dan selama _cookie_ yang menyimpan _session id_ dari pengguna masih valid dan belum kadaluwarsa, mana pengguna akan dianggap terautentikasi. 
## 4. Apakah penggunaan _cookies_ aman secara _default_ dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Secara _default_ tanpa proteksi apapun, _cookies_ rentan terhadap serangan, salah satunya ialah CSRF (_Cross Site Request Forgery_), dimana suatu _website_ lain melakukan _request_ ke suatu _server_ sambil melampirkan _cookie_ dari pengguna tersebut untuk berpura-pura melakukan aksi atas nama pengguna tersebut.
## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Menambahkan field ```ForeignKey``` pada model ```Product``` untuk menghubungkan ```user``` ke ```Product```
- Membuat file migrasi baru menggunakan ```./manage.py makemigrations```
- Melakukan migrasi menggunakan ```./manage.py migrate```
- Menambahkan views ```login_user```, ```register```, serta ```logout_user``` untuk proses autentikasi
- Menambahkan template serta styling untuk login dan juga registrasi pengguna
- Menambahkan views ke ```urls.py```
- Menambahkan views increment, decrement, serta delete item
- Memodifikasi template index.html dan menambahkan form untuk increment, decrement, serta delete item
- Menambahkan increment, decrement, serta delete pada ```urls.py```
- Memodifikasi views ```add_product``` agar menambahkan field ```user``` setiap kali form disubmit
- Menambahkan decorator ```@login_required``` pada views ```show_main```, ```add_product```, serta```logout_user```
- Memodifikasi template dan views agar menampilkan data pada pengguna (username pada banner) serta tampilan last_login.