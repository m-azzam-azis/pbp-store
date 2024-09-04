# pbp-tugas2

This repository contains the source code for the PWS application. You can access the deployed application at the following link:

[View Deployed Application](http://muhammad-azzam31-tugas2.pbp.cs.ui.ac.id)

## Implementation Details

### Step-by-Step Implementation

1. **Project Setup**:

   - Initialized a Django project using `django-admin startproject`.
   - Set up a virtual environment and installed necessary dependencies.
   - Configured the project settings, including the database setup (PostgreSQL).

2. **App Creation**:

   - Created the core application with `python manage.py startapp core`.
   - Defined models in `models.py` corresponding to the required database schema.
   - Ran migrations to apply the models to the database using `python manage.py migrate`.

3. **Views and URLs**:

   - Created views in `views.py` to handle the business logic.
   - Mapped views to URLs in `urls.py` to define accessible routes.
   - Created templates in the `templates` directory and linked them with views.

4. **Static and Media Files**:

   - Configured static and media file settings in `settings.py`.
   - Added necessary CSS, JS, and image files to the `static` directory.

5. **Testing**:

   - Wrote unit tests for views and models to ensure the correctness of the application.
   - Used Django’s test client to simulate requests and validate responses.

6. **Deployment**:
   - Configured the application for deployment using Gunicorn and Nginx.
   - Deployed the application on a cloud service provider like AWS or Heroku.
   - Set up environment variables and security configurations for the production environment.

### Request-Response Flow in Django

![Django Request-Response Flow](https://example.com/diagram.png)

**Explanation**:

- **Client Request**: The client sends a request to the Django web application.
- **urls.py**: The request is routed through `urls.py`, where it matches a defined URL pattern.
- **views.py**: The matching pattern triggers a specific view in `views.py`, which contains the logic to process the request.
- **models.py**: If the view requires database interaction, it communicates with `models.py`, which defines the data structure using Django's ORM.
- **Response**: The view then returns a response, either rendering an HTML template or sending JSON data, which is sent back to the client.

### Fungsi Git dalam pengembagan aplikasi

Git dapat mempermudah developer dalam melakukan version control dalam _code base_ aplikasi mereka. Selain itu, ada :

- **Version control**: Git merekam semua perubahan, komen, dan branch dalam kode kita. Kita dapat menggunakan fitur tersebut untuk kembali ke versi sebelumnya walaupun sudah mematikan komputer kita.
- **Kolaborasi**: Kita dapat berkolaborasi dalam pengembangan _software_ dengan menggunakan platform berbasis git seperti Github atau Gitlab.
- **Fitur Branch**: Developer dapat membuat banyak branch/cabang kode. Selain untuk kolaborasi, branch berguna untuk melakukan eksperimen tanpa mengubah kode produksi.

### Kenapa Django diajarkan sebagai pengantar framework?

Beberapa alasa utama mengapa Django baik untuk diajarkan ke-pemula adalah:

- **Kemudahan Syntax**: Django menggunakan syntax python yang cenderung mudah, Selain itu, banyak _built-in_ fitur yang sudah di implementasi oleh Django demi kemudahan pengguna.
- **Full-stack Framework**: Seorang developer dapat membuat aplikasi full-stack hanya dengan framework django saja. Hal ini mempersingkat _learning curve_ mahasiswa dalam PBP.
- **Well Established**: Django sudah ada sejak 2005. Selain itu, Django merupakan program _open-source_, artinya Django bersifat gratis, dan memiliki supoort dari komunitas developer. Dokumentasi dan tutorial django juga tersedia lengkap di internet.

### Mengapa model pada Django disebut sebagai ORM?

Django menggunakan ORM atau _Object relational management_ agar developer dapat dengan mudah mengakses database menggunakan kode python. ORM juga memudahkan developer untuk membuat I/O data dengan bentuk OOP.
