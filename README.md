# pbp-tugas5

[Link Deployment](http://muhammad-azzam31-pbpstore.pbp.cs.ui.ac.id)

Agar README tidak terlalu panjang, jawaban tiap tugas saya taruh di branch `tugas<i>` dengan i nomor tugas

#### Jawaban Pertanyaan:

# Panduan CSS dan Konsep Responsive Design

## Urutan Prioritas Pengambilan CSS Selector

Jika sebuah elemen memiliki lebih dari satu selector CSS, maka _style_ yang di-_apply_ mengikuti urutan berikut:

1. **Inline Style**: Style yang langsung didefinisikan pada elemen HTML dengan atribut `style`.
2. **ID Selector**: Selektor dengan `#id` memiliki prioritas lebih tinggi daripada class atau tag selector.
3. **Class, Attribute, dan Pseudo-Class Selectors**: Selektor seperti `.class`, `[attribute]`, dan `:hover` memiliki prioritas di bawah ID.
4. **Tag Selector**: Selektor yang memilih elemen berdasarkan nama tag HTML seperti `div`, `p`, dll.
5. **Universal Selector & Inherited Styles**: Selektor `*` dan style yang dihasilkan dari elemen parent.

Prioritas CSS juga dapat dipengaruhi oleh **specificity** (spesifisitas) dan **!important**, di mana `!important` mengesampingkan semua prioritas lainnya.

[Sumber W3C](https://www.w3schools.com/css/css_specificity.asp)

## Mengapa Responsive Design Penting?

**Responsive design** penting karena dapat memungkinkan sebuah aplikasi dapat digunakan dengan nyaman di berbagai ukuran device. Responsive design dapat menyesuaikan isi konten sesuai device, seperti: hp, tablet, hingga desktop. Konsep responsive design memastikan konten tetap mudah digunakan terlepas dari perangkat yang digunakan pengguna.

- **Contoh aplikasi yang sudah menerapkan responsive design**: Facebook, Scele, Youtube. layout aplikasi berubah seusai ukuran device yang digunakan
- **Contoh aplikasi yang belum menerapkan responsive design**: PWS, Siaren. Sudah tidak responsive, tidak secure lagi

[Sumber MDN Responsive Web Design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design)

## Perbedaan Margin, Border, dan Padding

- **Margin**: Area di bagian **luar** elemen, memberikan jarak antara elemen dengan elemen lain di sekitarnya.
- **Border**: Garis yang **mengelilingi** elemen, menjadi pembatas padding dan margin atau bagian dalam dan luar elemen.
- **Padding**: Area di bagian **dalam** elemen, memberikan jarak antara konten elemen dan batas elemen (border).

Dapat diimplementasi dengan tailwind dengan menambahkan class dibawah ke sebuah elemen:
`class="w-20 h-10 m-6 p-4 border-4 border-orange-500"`

Hasl yang dihaslikan kurang lebih seperti ini (padding tdk ada warnanya):
[Sumber MDN Box Model](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*M1rrBjfUxoPNsda6s-V5MA.png)

## Konsep Flexbox dan Grid Layout

- **Flexbox**: Layout **satu dimensi** yang digunakan untuk menyusun elemen dalam satu arah (horizontal atau vertikal).
  - **Pemakaian**: Flexbox lebih baik digunakan jika kita ingin ukuran container menyesuaikan isi.
- **Grid Layout**: Layout **dua dimensional** yang memungkinkan penempatan elemen secara horizontal dan vertikal.
  - **Pemakaian**: Grid lebih baik digunakan jika kita ingin ukuran konten menyesuaikan ukuran container.

[Sumber simplilearn flex vs grid](https://www.simplilearn.com/tutorials/css-tutorial/css-grid-vs-flexbox#:~:text=Flexbox%20is%20made%20for%20one,Grids%20can%20work%20on%20both.)
