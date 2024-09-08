Tautan menuju aplikasi PWS: http://erland-hafizh-pacilshop.pbp.cs.ui.ac.id/

[] Cara mengimplementasikan checlist yang ditugaskan secara step-by-step
1) Langkah pertama untuk membuat sebuah proyek Django baru adalah dengan membuat direktori utama lokal baru. Setelah itu, kita harus membuat virtual environment dan mengaktifkannya. Setelah virtual environment berhasil terbuat dan menyala, kita perlu membuat berkas requirements.txt di dalam direktori yang sama yang berisi beberapa dependencies. Setelah itu, kita harus melakukan instalasi terhadap dependencies yang berada pada file .txt sebelumnya. Setelah selesai, baru kita dapat membuat proyek Django dengan menjalankan perintah 'django-admin startproject (nama project) .'.
2) Untuk membuat aplikasi dengan nama main, kita perlu menjalan perintah 'python manage.py startapp main' pada terminal direktori lokal kita. Setelah perintah tersebut dijalankan, direktori baru dengan nama 'main' akan terbentuk pada direktori utama. Setelah terbuat, kita harus mendaftarkan aplikasi main tersebut ke dalam proyek kita dengan membuka berkas settings.py. 
3) Langkah awal agar dapat melakukan routing pada proyek sehingga dapat menjalankan aplikasi main adalah membuat berkas 'urls.py' di dalam direktori main yang telah dibuat. Lalu, perlu mengisi berkas tersebut dengan beberapa baris kode yang terdiri atas beberapa komponen. Komponen pertama ialah baris kode impor parth dan juga show_main. Fungsi path digunakan untuk mendefinisikan pola URL dalam aplikasi Django dan dengan ini kita dapat menentukan URL mana yang harus diproses oleh view tertentu, sedangkan fungsi show_main adalah sebuah view (fungsi atau kelas yang menangani permintaan HTTP dan mengembalikan respons HTTP) yang berada di file views.py dalam aplikasi main. Setelah itu, kita juga perlu menambahkan baris kode untuk mengimpor fungsi include dari django.urls pada berkas urls.py yang berada di dalam direktori proyek, digunakna untuk mengimpor rute URL dari aplikasi lain ke dalam berkas urls.py proyek. Lalu, penambahan rute URL juga diperlukan untuk mengarahkan ke tampilan main di dalam variabel urlpatterns. Terakhir, kita hanya tinggal menjalankan proyek Django dengan perintah 'python manage.py runserver'. 
4) 
5) 
6) 
7) 

[x] Bagan request client ke web aplikasi berbasis Django beserta responnya dan kaitan antara urls.py, views.py, models.py, dan berkas html

Client Request => Django Server => urls.py (URL Routing) => views.py (View) => (models.py jika diperlukan untuk interaksi dengan database) => views.py (View, setelah mendapatkan data dari models.py) => Templates (HTML Rendering) => Response dikirim kembali ke Client

Penjelasan bagan di atas terhadap keterkaitan antara urls.py, views.py, models.py, dan berkas html: 
1) urls.py bertanggung jawab untuk menentukan pola URL dan mengarahkan permintaan klien ke view yang sesuai di views.py. Ketika klien mengirim permintaan HTTP (seperti GET atau POST), Django pertama-tama memeriksa urls.py untuk menemukan pola URL yang cocok. Jika ditemukan kecocokan, Django akan mengirimkan permintaan tersebut ke fungsi atau kelas view yang ditentukan di views.py.
2) views.py adalah tempat di mana logika pemrosesan permintaan dijalankan. View bertindak sebagai pengendali (controller) yang memproses permintaan dan menentukan respons apa yang akan dikirim kembali ke klien. Setelah urls.py mengarahkan permintaan ke views.py, view tersebut akan memutuskan apakah perlu berinteraksi dengan model (models.py) untuk mengambil atau memodifikasi data dari basis data.
3) models.py berisi definisi model yang menggunakan Object-Relational Mapping (ORM) untuk mengelola interaksi dengan basis data. Ketika views.py membutuhkan data, misalnya untuk menampilkan daftar produk atau menyimpan data pengguna baru, views.py akan memanggil metode di models.py untuk berinteraksi dengan basis data. Model inilah yang mengabstraksikan kompleksitas SQL dan memungkinkan pengembang menggunakan objek Python untuk bekerja dengan data.
4) Setelah views.py memproses permintaan dan mendapatkan data yang diperlukan (baik langsung dari views.py atau melalui interaksi dengan models.py), langkah berikutnya adalah menyiapkan respons yang akan dikirim kembali ke klien. Untuk ini, Django menggunakan berkas HTML (template) untuk merender data menjadi halaman web. views.py akan mengambil data yang telah diproses dan menggabungkannya dengan template HTML untuk membuat konten HTML yang lengkap.
5) Setelah template HTML dirender, Django server mengirimkan HTML tersebut sebagai respons HTTP kembali ke klien. Browser klien menerima respons ini dan menampilkan halaman web kepada pengguna.


[x] Fungsi git dalam pengembangan perangkat lunak

Git memiliki beberapa fungsi dalam pengembangan perangkat lunak, antara lain:
1) Git memungkinkan developer untuk menyimpan riwayat perubahan, memulihkan versi sebelumnya, dan melihat siapa yang mengubah apa dan kapan
2) Git memungkinkan beberapa developer untuk bekerja bersama di proyek yang sama secara efisien tanpa saling menganggu.
3) Git menyediakan cadangan kode secara otomatis melalui repositori yang terdistribusi, yang berarti setiap developer memiliki salinan lengkap dari 'history' suatu proyek. Hal ini membantu dalam pemulihan jika ada kegagalan sistem atau kehilangan data

[x] Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak

Django sering dijadikan framework permulaan dalam pembelajaran pengembangan perangkat lunak dikarenakan sifatnya yang 'full-stack', hal ini berarti mencakup semua yang diperlukan untuk membangun aplikasi web, dimulai dari pengelolaan basis data hingga routing URL dan template HTML. Hal ini memungkinkan pemula untuk memahami konsep pengembangan web secara menyeluruh. 
Selain itu, Django juga menawarkan kemudahan penggunaan dengan sintaks yang jelas dan konvensi yang masuk akal, ditambah dengan dokumentasi yang sangat lengkap dan tutorial yang membantu pemula memahami konsep-konsep penting. 
Lebih jauh lagi, Django memungkinkan pengembangan aplikasi yang scalable dan aman, sehingga bukan hanya pilihan baik untuk belajar, tetapi juga untuk pengembangan aplikasi yang nyata. 

[x] Mengapa model pada Django disebut sebagai ORM

Model pada Django disebut sebagai ORM atau Object-Relational-Mapping karena menggunakan pendekatan tersebut untuk berinteraksi dengan basis data. ORM adalah teknik pemrograman yang menghubungkan antara objek dalam kode program, seperti kelas Python, dengan tabel dalam basis data relasional. Hal ini memungkinkan developer untuk bekerja dengan basis data menggunakan objek Python dibanding menulis perintah SQL secara langsung, membuat developer lebih intuitif bagi mereka yang terbiasa dengan pemrograman berorientasi objek. ORM Django mendukung pembuatan pembuatan query yang kompleks dengan metode Python yang mudah dibaca dan dikelola, serta menawarkan fitur-fitur seperti validasi, hubungan antar tabel, dan lain-lain. Hal ini membuatnya menjadi alat yang kuat untuk manipulasi data yang efisien dan aman dalam aplikasi Django.