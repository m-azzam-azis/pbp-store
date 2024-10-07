# pbp-tugas6

[Link Deployment](http://muhammad-azzam31-pbpstore.pbp.cs.ui.ac.id)

Agar README tidak terlalu panjang, jawaban tiap tugas saya taruh di branch `tugas<i>` dengan i nomor tugas

#### Jawaban Pertanyaan:

# Javascript dan AJAX

## Penggunaan JavaScript dalam Pengembangan Aplikasi Web

Bersama dengan WebAssebly, Javascript merupakan bahasa native pada web browser moderen. Berikut adalah beberapa manfaat utamanya:

1. **Interaktif**: JavaScript memungkinkan aplikasi web menjadi lebih interaktif dan dinamis, yang meningkatkan pengalaman pengguna dengan memberikan tanggapan seketika terhadap aksi pengguna tanpa perlu me-refresh halaman.
2. **Asinkron**: JavaScript mendukung pemrograman asinkron menggunakan teknologi seperti `AJAX`, sehingga memungkinkan komunikasi dengan server di latar belakang untuk memperbarui konten halaman secara real-time.
3. **Integrasi dengan HTML dan CSS**: JavaScript dapat dengan mudah berintegrasi dengan HTML dan CSS untuk memberikan animasi, validasi formulir, dan efek UI yang menarik.
4. **Eksekusi di Sisi Klien**: Karena berjalan di browser, JavaScript memungkinkan pemrosesan data langsung di sisi klien, yang dapat mengurangi beban server dan meningkatkan performa aplikasi.

[Referensi: MDN Web Docs - JavaScript Overview](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

## Fungsi `await` dalam `fetch()` dan Konsekuensi Tidak Menggunakannya

`await` digunakan untuk menunggu penyelesaian dari suatu promise sebelum melanjutkan eksekusi kode berikutnya. Ketika kita menggunakan `fetch()`, ia akan mengembalikan objek `Promise` karena proses pengambilan data adalah operasi asinkron.

Contoh penggunaan `await` pada `fetch()`:

```javascript
const response = await fetch('https://api.example.com/data');
const data = await response.json();
console.log(data);
```

Fungsi dari await adalah menghentikan eksekusi sampai fetch() selesai mendapatkan data, sehingga kita bisa langsung mengakses hasilnya. Jika kita tidak menggunakan await:

```javascript
const response = fetch('https://api.example.com/data');
console.log(response); // Akan mencetak Promise, bukan data yang diinginkan
```

Tanpa await, response masih berupa Promise, bukan hasil dari pengambilan data. Hal ini mengharuskan kita menggunakan metode seperti `.then()` untuk menangani hasilnya, sehingga menambah kompleksitas.

[Referensi: MDN Web Docs - await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)


## Penggunaan `@csrf_exempt` dalam View untuk AJAX POST

Dalam Django, decorator @csrf_exempt digunakan untuk menonaktifkan perlindungan CSRF (Cross-Site Request Forgery) pada view tertentu. Pada umumnya, setiap POST request di Django harus dilengkapi dengan CSRF token untuk mencegah serangan CSRF. Namun, ketika menggunakan AJAX POST, terutama jika tidak mudah untuk menyertakan CSRF token, kita bisa menggunakan `@csrf_exempt` untuk view tersebut.

Penggunaan `@csrf_exempt` harus dilakukan dengan hati-hati karena menonaktifkan mekanisme perlindungan keamanan penting, sehingga hanya direkomendasikan pada view yang memiliki tingkat risiko rendah atau pada saat kita bisa memastikan bahwa request tersebut aman.

[Referensi: Django Documentation - Cross Site Request Forgery protection](https://docs.djangoproject.com/en/stable/ref/csrf/)

## Pembersihan Data Input Pengguna di Backend

Pembersihan data input pengguna tidak cukup jika hanya dilakukan di sisi frontend karena beberapa alasan:

1. **Keamanan**: Validasi di frontend dapat dilewati oleh pengguna yang berpengalaman atau oleh malicious actors menggunakan tool seperti Postman untuk memodifikasi request. Backend menjadi lapisan terakhir yang memastikan bahwa data yang diterima aman dan sesuai dengan spesifikasi.
2. **Konsistensi**: Validasi di backend memastikan standar yang sama untuk setiap input, meskipun frontend mengalami perubahan atau jika aplikasi memiliki beberapa platform client (web, mobile, dll.).
3. **Integritas Data**: Backend bertanggung jawab untuk menyimpan data yang valid. Jika hanya validasi di frontend, data yang masuk ke database bisa rusak atau salah.

Karena itulah validasi di backend adalah keharusan dalam menjaga keamanan dan integritas data.

[Referensi: OWASP - Input Validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)

## Langkah Pengerjaan

Berikut ini adalah langkah-langkah implementasi AJAX GET dan POST dalam aplikasi PBP Store yang saya kembangkan .

### AJAX GET untuk Mengambil Data Toko

1. **Mengubah Kode Cards Data Shop ke Bentuk Embedded HTML**: Ubah file bagian yang menampilkan cards pada `main.html` dengan menambahkan script javascript dengan manipulasi DOM
2. **Fetch Data dari Backend**gunakan fitur fetch dan `XMLHttpRequest` untuk mendapatkan list cards dari database
3. **Buat Fungsi untuk me-refresh Cards**tampilkan data dalam cards yang sudah dinamis

### AJAX POST untuk Menambahkan Shop Entry Baru

1. **Membuat Tombol dan Modal Form untuk Menambahkan Shop Entry**
- Buat tombol pada `main.html` yang akan membuka modal dengan form untuk menambahkan sjop entry.
- Modal ini akan menampilkan form input yang sesuai.
2. **Membuat Fungsi View untuk Menambahkan Shop Entry**: Buat view Django yang menangani penambahan Shop Entry dan menyimpan Shop Entry baru ke dalam basis data
3. **Membuat Path `/create-ajax/`**: Tambahkan path ke dalam urls.py untuk menghubungkan dengan view yang baru dibuat
4. **Menghubungkan Form di Modal ke Path /create-ajax/ dengan AJAX POST**: Implementasikan JavaScript untuk menangani pengiriman form melalui AJAX
5. **Refresh Halaman Secara Asinkronus**: Setelah penambahan Shop Entry berhasil, fungsi `refreshShopEntry()` yang telah dibuat sebelumnya dapat dipanggil untuk memperbarui daftar Shop Entry secara asinkronus tanpa perlu melakukan reload keseluruhan halaman.


