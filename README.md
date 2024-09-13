# pbp-tugas3

[Link Deployment](http://muhammad-azzam31-pbpstore.pbp.cs.ui.ac.id)

 Agar README tidak terlalu panjang, jawaban tiap tugas saya taruh di branch `tugas<i>` dengan i nomor tugas

#### Jawaban Pertanyaan:


## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery dibutuhkan agar aplikasi kita dapat digunakan ulang di banyak tempat. Seminimal mungkin, data yang ada di server kita harus bisa ditampilkan dalam aplikasi local kita. Selanjutnya, saat kita ingin mempublish site kita untuk digunakan banyak orang, data kita juga butuh di deliver ke client host masing-masing pengguna.


## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Untuk preferensi pribadi, saya lebih suka ke JSON. beberapa poin utama yang saya pikirkan yang menjadi alasan JSON lebih di gunakan adalah:
- **Fleksibilitas Formatting**: JSON dikirim dalam bentuk Objek yang dapat dengan mudah dimodifikasi, baik secara struktur maupun cara menampilkannya dalam page kita. Di lain sisi XML memaksa kita untuk menampilkan data sesuai bentuk data yang dikirm dari server.
- **Ukuran Data**: JSON hanya mengirim data berbentuk objek biasa, sedangkan XML memuat data dalam bentuk struktur `tag`, hal tersebut membuat data lebih besar dan lama untuk di proses
- **Readability**: Membaca data dalam JSON jauh lebih mudah dan intuitif dibandingkan dengan data dalam bentuk XML


## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method `is_valid()` pada form Django digunakan validasi data yang ada dikirm lewat form. `is_valid()` akan mengecek validitas form sesuai batasan yang sudah kita buat, seperti: minimal karakter, jenis input, hingga boleh/tidaknya sebuah field untuk kosong (tidak diisi)


## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf adalah singkatan dari: Cross-Site Request Forgery, sebuah jenis serangan siber dimana penyerang dapat mengakses sebuah aplikasi tanpa persetujuan pengguna asli dengan cara mencuri token milik pengguna. 

Kita membutuhkan csrf_token dalam form Django agar token diperbarui setiap kali user masuk ke dalam aplikasi (disebut juga session). Kode token di-generate secara random setiap session agar peretas tidak bisa mencuri token pengguna dan digunakan saat user sudah keluar dari aplikasi.

Tanpa csrf_token, penyerang dapat mengakses akun user dan mensubmit form yang ada dalam aplikasi. Contohnya membuat pembelian, mengganti password, dan sebagainya.


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- **Buat Base**: Buat folder `template` di `root` folder dan isi dengan `base.html`. Setelah itu setup url agar base menjadi template aplikasi kedepannya.
- **Buat Page Forms dan Hasil**: dengan meng-extend `base.html` file, kita bisa membuat form dan menampilkan hasilnya di pages utama dibawah npm dan nama
- **Update File `Views`**: Buat fungsi baru di views yang mengambil response request atas masing-masing hasil form yang kta buat. Setelah itu fungsi akan me-retur http request sesuai page yang kita inginkan.
- **Update URL**: Buat `url_pattern` baru dengan meng-import nama page dari views.
  

## Screenshot Postman:
### JSON:

<img width="618" alt="SCR-20240912-keex" src="https://github.com/user-attachments/assets/882758ce-3521-4603-bc2b-9cb23e1afc6f">

### XML:

<img width="623" alt="SCR-20240912-kegl" src="https://github.com/user-attachments/assets/ba5446b0-8f8c-4185-8adf-4bf987851d4c">


### JSON by ID:

<img width="626" alt="SCR-20240912-kelh" src="https://github.com/user-attachments/assets/1f4d660e-eac2-4326-b02a-44789c09d8a4">

### XML by ID:

<img width="624" alt="SCR-20240912-keii" src="https://github.com/user-attachments/assets/2f3f8a6e-b5c9-4625-815e-d053ac1f7cf1">




