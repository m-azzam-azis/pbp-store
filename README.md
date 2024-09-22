# pbp-tugas4

[Link Deployment](http://muhammad-azzam31-pbpstore.pbp.cs.ui.ac.id)

Agar README tidak terlalu panjang, jawaban tiap tugas saya taruh di branch `tugas<i>` dengan i nomor tugas

#### Jawaban Pertanyaan:

## Perbedaan HttpResponseRedirect() dan redirect()?

**HttpResponseRedirect()**: Merupakan class yang mengembalikan respons redirect ke URL tertentu. Argumen hanya dapat berupa url saja.
**redirect()**: Merupakan fungsi shortcut yang lebih fleksibel. Dapat menerima URL, nama view, atau objek sebagai argumen. Argumen selain url akan diproses dibalik layar, dan hasil return-nya akan berupa sebuah HttpResponseRedirect() dengan argumen url yang sesuai.

[Sumber Stack Overflow Forum](https://stackoverflow.com/questions/13304149/what-the-difference-between-using-django-redirect-and-httpresponseredirect)

## Perbedaan Authentication dan Authorization?

- **Autentikasi**: Proses untuk memverifikasi identitas pengguna.
- **Otorisasi**: Proses untuk memberikan hak akses ke bagian tertentu dari aplikasi, biasanya setelah pengguna berhasil diautentikasi.

### Autentikasi saat Login:

Dalam fitur login, yang digunakan adalah authentikasi, yaitu memverifikasi identitas pengguna dengan menggunakan username dan password.

### Implementasi Auth dalam Django

Dalam Django, otorisasi dan autentikasi dapat dilakukan dengan menggunakan import modul bernama `django.contrib.auth`. Modul tersebut sudah memiliki fitur yang lengkap, mulai dari form register, login, permission (otorisasi), dan sebagainya.

[Sumber Django Documentation](https://docs.djangoproject.com/en/stable/topics/auth/default/#authentication-and-authorization)

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login menggunakan **session cookies**. Setelah pengguna berhasil login, Django menyimpan sesi pengguna di server dan mengirimkan _session ID_ melalui cookie ke browser pengguna. Cookie ini dikirim dikrim setiap kali ada `request` dari client pengguna. Hal tersebut memungkinkan Django untuk mengingat user tanpa haru melakukan autentikasi berulang kali.

### Kegunaan lain dari cookies:

- **Menyimpan preferensi pengguna**: Seperti tema situs (gelap/terang) atau pilihan bahasa.
- **Melacak aktivitas pengguna**: Digunakan dalam aplikasi e-commerce untuk menyimpan keranjang belanja atau riwayat pencarian.
- **Menyimpan kredensial device**: Memungkinkan pengguna tetap login dalam jangka waktu yang dapat ditentukan tanpa harus melakukan login berulang kali.

### Apakah semua cookies aman digunakan?

Tidak, penggunaan cookies akan selalu memiliki risiko keamanan, terutama jika cookies tidak diatur dengan benar. Beberapa risiko dan solusi untuk meningkatkan keamanan cookies di Django adalah:

- **Cross-Site Scripting (XSS)**: Penyerang dapat mencuri cookies jika mereka dapat meg-_inject_ skrip berbahaya ke halaman web. Django dapat mengatasi ini dengan menggunakan flag `HttpOnly` yang dapat mencegah injeksi javascript.
- **Man-in-the-middle (MITM) attacks**: Jika cookie dikirim melalui koneksi tidak terenkripsi (HTTP), maka bisa disadap oleh pihak ketiga. Untuk menghindari ini, gunakan flag `Secure` yang memastikan cookie hanya dikirim melalui koneksi HTTP**S**.
- **Cross-Site Request Forgery (CSRF)**: Sebuah serangan yang mengeksploitasi sesi pengguna untuk mengakses akun pengguna tanpa sepengetahuan mereka. Django memiliki fitur form CSRF untuk mencegah hal ini.

### Untuk keamanan tambahan:

- Pastikan validasi dan perlindungan CSRF selalu diaktifkan.
- Gunakan `HttpOnly` untuk melindungi cookies dari skrip berbahaya.
- Gunakan `Secure` untuk mengirim cookies hanya melalui HTTPS.

[Sumber Django Documentation](https://docs.djangoproject.com/en/stable/topics/http/sessions/)

## Bagaimana cara implementasi checklist secara step-by-step?

1. **Register, Login, dan Logout**:
   - membuat ketiga fungsi tersebut dalam file `views.py`
   - menambahkan url masing-masing fitur tersebut ke dalam `urls.py` sesuai url masing-masing
   - menambahkan fitur otorisasi dengan decorator method pada fungsi `main`
2. **Menyambung Model dengan User**:
   - menambahkan foreign key ke dalam objek user dalam `models.py`
   - melakukan `python manage.py makemigrations` setelah menambahkan foreign key
   - membuat satu dummy account saat di prompt
   - membuat dummy account dan melakukan `python manage.py migrate`
3. **Membuat Dummy Account**:
   - menyalakan server dan membuat satu akun baru
   - login dengan akun baru, setelah itu isi form dengan dummy data sebanyak tiga kali
4. **Menampilkan Detail Login**
   - menambahkan sebuah text yang berisi informasi terakhir login dalan `main.html`
