# pbp-tugas2

This repository contains the source code for the PWS application. You can access the deployed application at the following link:

[Link Deployment](http://muhammad-azzam31-tugas2.pbp.cs.ui.ac.id)

##### Jawaban Pertanyaan:

## Urutan Setup Aplikasi Django?

### 1. Setup Django Project

#### 1.1. Buat Project Directory Baru
```bash
mkdir tugas2
cd tugas2
```

#### 1.2. Set Up Virtual Environment
```bash
python3 -m venv env
source env/bin/activate
```

#### 1.3. Buat File `requirements.txt` 
```bash
echo "django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3" >> requirements.txt
```

#### 1.4. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 1.5. Buat Folder untuk Projek
```bash
django-admin startproject my_project .
```

#### 1.6. Tambahkan File `.gitignore` 
isi dengan seperti di [Tutoial 1](https://pbp-fasilkom-ui.github.io/ganjil-2025/docs/tutorial-0#tutorial-unggah-proyek-ke-repositori-github)


#### 1.7. Set Up Repo Git dan Github 
```bash
echo "tugas2" >> README.MD
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:your-username/pbp-tugas2.git
git push -u origin main
```

### 2. Buat Main App

#### 2.1. Init Folder Main
```bash
python manage.py startapp main
```

#### 2.2. Tambahkan Main ke Settings
Edit `settings.py` and add `'main'` to the `INSTALLED_APPS` list.

#### 2.3. Buat Template
- Buat folder dengan nama `templates` di dalam app `main` .
- Buat file dengan nama `main.html` di dalam `templates` folder, lalu isi HTML-nya.

### 3. Buat Model Django

#### 3.1. Init Model dan Atribut dalam `models.py`
```python
from django.db import models

class ShopEntry(models.Model):
    # buat attributes disini
```

#### 3.2. Migrasi Model Baru ke Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Buat Fungsi dalam Views

#### 4.1. Buat File `views.py` dan Masukkan Fungsi
```python
from django.shortcuts import render

def show_main(request):
    context = {
        # add your context dictionary here
    }
    return render(request, "main.html", context)
```

### 5. Setup Routing URL 

#### 5.1. Definisikan URL dalam `urls.py` of `main` App
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

#### 5.2. Masukan Main ke dalam `urls.py` dalam Parent Folder
```python
...

from django.urls import path, include
...
...

urlpatterns = [
    path('', include('main.urls')),
]
...

```

### 6. Deployment ke PWS

#### 6.1. Set Up PWS Repository
buat projek baru, simpan credentials dan jalankan:
```bash
git remote add pws http://pbp.cs.ui.ac.id/your-username/tugas2
git branch -M master
git push pws master
```

#### 6.2. Update `ALLOWED_HOSTS` dalam `settings.py`
```python
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "http://pbp.cs.ui.ac.id/muhammad-azzam31-tugas2"]
```

## Request-Response dalam Aplikasi Berbasis Django 

![Django Request-Response Flow](https://example.com/diagram.png)

**Explanation**:

- **Client Request**: The client sends a request to the Django web application.
- **urls.py**: The request is routed through `urls.py`, where it matches a defined URL pattern.
- **views.py**: The matching pattern triggers a specific view in `views.py`, which contains the logic to process the request.
- **models.py**: If the view requires database interaction, it communicates with `models.py`, which defines the data structure using Django's ORM.
- **Response**: The view then returns a response, either rendering an HTML template or sending JSON data, which is sent back to the client.

## Fungsi Git dalam pengembagan aplikasi 

Git dapat mempermudah developer dalam melakukan version control dalam _code base_ aplikasi mereka. Selain itu, ada :

- **Version control**: Git merekam semua perubahan, komen, dan branch dalam kode kita. Kita dapat menggunakan fitur tersebut untuk kembali ke versi sebelumnya walaupun sudah mematikan komputer kita.
- **Kolaborasi**: Kita dapat berkolaborasi dalam pengembangan _software_ dengan menggunakan platform berbasis git seperti Github atau Gitlab.
- **Fitur Branch**: Developer dapat membuat banyak branch/cabang kode. Selain untuk kolaborasi, branch berguna untuk melakukan eksperimen tanpa mengubah kode produksi.

## Kenapa Django diajarkan sebagai pengantar framework?

Beberapa alasa utama mengapa Django baik untuk diajarkan ke-pemula adalah:

- **Kemudahan sintaks**: Django menggunakan syntax python yang cenderung mudah, Selain itu, banyak _built-in_ fitur yang sudah di implementasi oleh Django demi kemudahan pengguna.
- **Framework fullstack**: Seorang developer dapat membuat aplikasi full-stack hanya dengan framework django saja. Hal ini mempersingkat _learning curve_ mahasiswa dalam PBP.
- **Well established**: Django sudah ada sejak 2005. Selain itu, Django merupakan program _open-source_, artinya Django bersifat gratis, dan memiliki supoort dari komunitas developer. Dokumentasi dan tutorial django juga tersedia lengkap di internet.

## Mengapa model pada Django disebut sebagai ORM?

Django menggunakan ORM atau _Object relational management_ agar developer dapat dengan mudah mengakses database menggunakan kode python. ORM juga memudahkan developer untuk membuat I/O data dengan bentuk OOP.
