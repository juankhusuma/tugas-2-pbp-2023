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