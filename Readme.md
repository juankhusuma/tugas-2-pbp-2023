# Link Web Tugas
[Link Deploymennt](http://juan-dharmananda-tutorial.pbp.cs.ui.ac.id)
http://juan-dharmananda-tutorial.pbp.cs.ui.ac.id

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

# Tugas 5
## 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya. 
Element selector berfungsi untuk memberikan styling secara umum kepada semua element atau tag yang dipilih, umumnya digunakan untuk memberikan styling yang bersifat global kepada semua kemunculan tag atau element tersebut, misal untuk memberikan warna text pada element p atau membuang default styling pada suatu element, misal membuang underline pada link atau tag a, dan sebagainya

## 2. Jelaskan HTML5 Tag yang kamu ketahui.
- h1 - h6: untuk menampilkan heading, dengan urutan kepentingan yang berbeda-beda, h1 paling besar dan penting, h6 paling kecil dan paling kecil tingkatanya
- p: untuk menampilkan paragraf
- a: untuk menampilkan link
- img: untuk menampilkan gambar
- form: untuk membuat form
- input: untuk menerima form input dari user
- button: untuk menampilkan tombol
- ul: menampilkan list yang tidak berurut
- ol: menampilkan list yang terurut
- li: menampilkan masing-masing item list
- table: menampilkan tabel
- thead: menampilkan header tabel
- tbody: menampilkan body tabel
- tr: menampilkan baris dari tabel
- td: menampilkan masing-masing item dari tabel

## 3. Jelaskan perbedaan antara margin dan padding.
Padding adalah whitespace didalam border suatu element sedangkan margin merupakan whitespace diluar border dan berada di sekeliling element

## 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Tailwind didesain sebagai utility framework untuk memudahkan developer untuk menambahkan styling dengan hanya menambahkan class pada suatu element tanpa ada prebuilt component sedangkan Bootstrap merupakan framework css yang didesain untuk mempermudah pembuatan component dengan berbagai prebuilt component yang sudah responsive dan siap digunakan

Tailwind memberikan fleksibilitas dan styling yang lebih kompleks sehingga lebih cocok untuk proyek yang membutuhkan kostumisasi yang lebih tinggi sedangkan Bootstrap lebih baik untuk sebuah proyek yang tidak memerlukan styling dengan kostumisasi yang tinggi dan memerlukan waktu pengembangan yang cepat

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
- Menambahkan konfigurasi static file pada settings.py
- Membuat folder static untuk menampung file static css
- Membuat file css index.css untuk memberikan styling reset yang membuang styling default css dan menambahkan styling general
- Menbamhakan file css untuk semua page, yaitu ada index.css untuk memberikan styling pada page home dan table
- Menambahkan styling untuk form dari django pada file create_form.css
- Memberikan link pada html ke file css yang tepat

# Tugas 6
## 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
asynchronous programming memungkinkan eksekusi beberapa proses secara bersamaan, dimana apabila suatu proses async belum selesai, maka program tidak akan menunggu program selesai, melainkan lanjut melakukan proses selanjutnya, dengan demikian proses async tidak akan menghambat proses lainya, sedangkan pada synchronous programming semua proses dilakukan beruntun satu per-satu dan program akan menunggu setiap proses untuk selesai sebelum pindah ke proses selanjutnya.

## 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
event driven programming adalah suatu paradigma pemrograman dimana suatu program disusun dalam bentuk event dan event handler, event adalah semacam notifikasi dari program untuk menandakan terjadinya suatu peristiwa pada proses berjalanya program, lalu masing-masing event tersebut dapat diberikan event handler yang merupakan sekumpulan kode yang dieksekusi apabila suatu event dikeluarkan oleh komponen tertentu.

## 3. Jelaskan penerapan asynchronous programming pada AJAX.
Pada ajax asynchronous programming diimplementasikan agar proses rendering browser tidak terhenti ketika menunggu response dari server, selain itu, dengan AJAX, kita dapat mengganti tampilan browser tanpa merusak interaktivitas dari browser

## 4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
jQuery dikembangkan pada masa awal pemrograman web, dimana API modern pada browser serperti fetch dan query selector masih belum ada atau belum sempurna, namun seiiring berkembangnya teknologi web, fitur-fitur yang ditawarkan oleh jQuery sudah menjadi standar yang didukung di semua browser modern, namun tetap jQuery menawarkan kemudahan melakukan manipulasi dom dan fitur-fitur tambahan lainya, sehingga untuk proyek yang sederhana lebih cocok menggunakan fetch api, namun untuk proyek yang lebih kompleks jquery dapat memberikan kemudahan dan membantu proses pengembangan sehingga lebih baik digunakan.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- menambahkan create_ajax pada views.py untuk membuat product dengan AJAX
- memodifikasi index.html dan index.css sehingga menggunakan cards
- menambahkan boostrap dan modal boostrap pada index.html
- menambahkan index.js pada static
- menambahkan kode js untuk menambahkan card secara ajax ketika file html pertama kali di render
- menambahkan event handler untuk create product by ajax dan melakukan manipulasi dom untuk menambah item
- melakukan perintah ```./manage.py collectstatic```
