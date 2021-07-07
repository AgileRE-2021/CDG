<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/AgileRE-2021/CDG">
    <img src="https://user-images.githubusercontent.com/67138576/121291339-52c26d00-c912-11eb-9cff-a7ebc79ab5e0.png" alt="Logo" width="500" height="500">
  </a>

  
  <p align="center">
    BPMN & Database to Class Diagram Model Generator
    <br />
    <a href=https://youtu.be/gOxOLRDUUz4><strong>Demo Project »</strong></a>
    <br />
</p>

## Daftar Isi
* [Tentang Proyek](#tentang-proyek)
  * [Definisi](#definisi)
  * [Sistem Pembangun](#sistem-pembangun)
* [Petunjuk Instalasi](#petunjuk-instalasi)
* [Petunjuk Penggunaan](#petunjuk-penggunaan)
* [Informasi Lainnya](informasi-lainnya)
  * [Anggota Proyek](#anggota-proyek)
  * [Tanggal Rilis](#tanggal-rilis)
  * [Versi](#versi)
  * [Kontak](#kontak)



<!-- TENTANG PROYEK -->
## Tentang Proyek
### Definisi
CDG (*Class Diagram Generator*) merupakan aplikasi yang bertujuan untuk mengubah BPMN (*Business Process Modeling Notation*) dan Database menjadi Class Diagram. Berikut adalah penjelasan dari masing-masing artefak yang dilibatkan dalam aplikasi ini. 
>- **BPMN** merupakan standar notasi grafis yang mendeskripsikan langkah logis dari proses bisnis.
>- **Database** merupakan kumpulan informasi yang disimpan di dalam komputer secara sistematik sehingga informasi tersebut dapat dikelola dengan mudah dan baik.
>- **Class Diagram** merupakan  diagram UML yang menggambarkan kelas-kelas dalam sebuah sistem dan hubungannya antar satu kelas dengan yang lainnya

Secara garis besar, komponen pembentuk dari Class Diagram sebagai *output* yang dihasilkan terbentuk melalui komponen input, yaitu :
1. Nama Class : Nama *data object* BPMN
2. Atribut Class : Kolom tabel *Database*
3. Method Class : State *data object* BPMN
4. Relasi Antar Class : Foreign Key *Database*
### Sistem Pembangun
Aplikasi CDG dibangun dengan memanfaatkan *software*, *framework*, dan beberapa bahasa pemrograman, diantaranya adalah sebagai berikut :
- [VsCode Editor](https://code.visualstudio.com/)
- [SQLite Database](https://www.sqlite.org/index.html)
- [GitHub](https://github.com/)
- [Django Framework](https://www.djangoproject.com/) 
- [Bootstrap Framework](https://getbootstrap.com/)
- [Python](https://www.python.org/)
- [Javascript](javascript.com)

## Petunjuk Instalasi 
Petunjuk mengenai prosedur instalasi untuk aplikasi CDG dilakukan pada sesi terminal, berikut prosedur yang dapat dilakukan :
1. Lakukan *clone* pada repositori
   ```sh
   git clone https://github.com/AgileRE-2021/CDG.git
   ```
2. Membuat *virtual environment* pada *python*
   ```sh
   py -m venv env
   ```
3. Masuk ke dalam *virtual environment* 
   ```sh
   env\Scripts\activate.bat
   ```
4. Lakukan instalasi *Django Framework*
   ```sh
   py -m pip install Django
   ```
5. Masuk ke dalam folder aplikasi CDG
   ```sh
   cd CDG
   ```
6. Lakukan instalasi *Bootstrap Framework* 
   ```sh
   pip install django-bootstrap-v5
   ```
7. Lakukan instalasi plantUML
   ```sh
   pip install plantuml
   ```
8. Lakukan instalasi library Six
   ```sh
   pip install six
   ```
9. Jalankan aplikasi pada *localhost*
   ```sh
   py manage.py runserver
   ```
## Petunjuk Penggunaan
Petunjuk mengenai prosedur penggunaan aplikasi CDG dapat dilihat pada bagian di bawah ini :
1. Jalankan aplikasi dengan klik "START!"
2. Buatlah data proyek dengan klik "+ Tambah" pada tab "Inisiasi Proyek"
3. Masukkan nama proyek yang diinginkan dan klik "Save"
4. Buatlah data proses dengan klik "+ Tambah" 
5. Unggahlah file BPMN yang berekstensi .xpdl dengan klik "Unggah"
6. File BPMN yang berhasil terunggah akan menampilkan "File telah terunggah"
7. Klik "Database" untuk melakukan pengunggahan file database
8. Unggahlah file database yang berekstensi .xml dengan *drop* file atau klik "Unggah"
9. File *database* yang berhasil terunggah akan ditampilan pada bagian *database*
10. Klik "Ok, Lanjut!" untuk dapat melakukan pengunduhan hasil translasi 
11. Pilih proyek yang diinginkan untuk diunduh hasil translasinya dengan klik jenis ekstensi file yang diinginkan "JPG", "PNG", atau "SVG"
12. File *class diagram* hasil translasi akan otomatis tesimpan pada penyimpanan lokal perangkat anda
13. Apabila merasa kesulitan dalam menggunakan aplikasi ini, lihat panduan penggunaan dengan klik tab "User Manual" dan jalankan video panduan

> [Video Panduan Penggunaan](https://youtu.be/gOxOLRDUUz4)

## Informasi Lainnya
### Anggota Proyek
Anggota pada proyek pengerjaan aplikasi *Class Diagram Generator* terdiri dari 7 orang, meliputi :

<a href="https://www.linkedin.com/in/muhammad-fadlul-kabir-b050a61b7" target="_blank"><img src="https://user-images.githubusercontent.com/67138576/121288576-c9a93700-c90d-11eb-9fee-77a74b65b65f.png" width="90" height="90"></a>
<a href="https://www.linkedin.com/in/farida-utami-23338117a/" target="_blank"><img src="https://user-images.githubusercontent.com/67138576/121289485-3244e380-c90f-11eb-9e11-4b13bb04df89.png" width="90" height="90"></a>
<a href="https://www.linkedin.com/in/bilal-hidayaturrohman-95a058214/" target="_blank"><img src="https://user-images.githubusercontent.com/67138576/121288571-c910a080-c90d-11eb-98db-b0ce464a303b.png" width="90" height="90"></a>
<a href="https://www.linkedin.com/in/nadirelc/" target="_blank"><img src="https://user-images.githubusercontent.com/67138576/121289494-34a73d80-c90f-11eb-8811-7904e7b88606.png" width="90" height="90"></a>
<a href="https://www.linkedin.com/in/syafira-nurilhaq-940621214/" target="_blank"><img src="https://user-images.githubusercontent.com/67138576/121288587-cd3cbe00-c90d-11eb-9162-53d8efae4ce9.png" width="90" height="90"></a>
<a href="https://www.linkedin.com/in/muhammadzegezain/" target="_blank"><img src="https://user-images.githubusercontent.com/67138576/121288589-ce6deb00-c90d-11eb-99f4-339fc5f713e0.png" width="90" height="90"></a>
<a href="http://www.linkedin.com/in/arva-firjatullah/" target="_blank"><img src="https://user-images.githubusercontent.com/67138576/121289472-2fe28980-c90f-11eb-8ae1-5441398114ff.png" width="90" height="90"></a>

### Tanggal Rilis 
Tanggal 15 Juni 2021
### Versi 
Version 1.0 
### Kontak 
Informasi kontak setiap anggota lebih detail dapat dilihat di bawah ini. 
1.  Muhammad Fadlul Kabir : fadil2701@gmail.com
2.  Farida Utami : utamifarida15@gmail.com
3.  Bilal Hidayaturrohman : bilalhidayaturrohman25@gmail.com
4.  Nadlir Mubarak : nadir.mubarak11@gmail.com
5.  Syafira Nurilhaq Maulidya : syafiranurilhaq@gmail.com
6.  Muhammad Zege Zain : zege_muhammad@yahoo.com
7. Arva Firjatullah Gyonanda : arvafg07@gmail.com

<h2 align="center"> -------S1 Sistem Informasi - Universitas Airlangga - 2021------- </h2>
<br/>
