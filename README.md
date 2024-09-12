# pbp-tugas3

[Link Deployment](http://muhammad-azzam31-tugas2.pbp.cs.ui.ac.id)

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



## Screenshot Postman:


