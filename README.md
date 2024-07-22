# Website Klasifikasi Berita

Website ini adalah aplikasi untuk klasifikasi berita dalam bahasa Inggris. API backend dibangun menggunakan Django dengan bahasa Python, sementara frontend dibangun menggunakan ReactJS. Saat ini, frontend masih dalam tahap pengembangan.

## Daftar Isi

- [Instalasi Backend](#instalasi-backend)
- [Instalasi Frontend](#instalasi-frontend)
- [Penggunaan](#penggunaan)

## Instalasi Backend

### Prasyarat

- [Python](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [Django](https://www.djangoproject.com/)

### Setup Backend (Django)

1. Clone repository:

    ```bash
    git clone https://github.com/username/news-classification-website.git
    cd news-classification-website
    ```

2. Instal dependensi Python:

    ```bash
    pip install -r requirements.txt
    ```

3. Salin file `.env.example` ke `.env` dan perbarui kredensial database serta pengaturan lainnya:

    ```bash
    cp .env.example .env
    ```

4. Jalankan migrasi database:

    ```bash
    python manage.py migrate
    ```

5. Jalankan server development Django:

    ```bash
    python manage.py runserver
    ```

## Instalasi Frontend

### Prasyarat

- [Node.js](https://nodejs.org/)
- [npm](https://www.npmjs.com/)

### Setup Frontend (ReactJS)

1. Navigasikan ke folder frontend:

    ```bash
    cd frontend
    ```

2. Instal dependensi Node.js:

    ```bash
    npm install
    ```

3. Mulai server development React:

    ```bash
    npm start
    ```

   **Catatan:** Frontend masih dalam tahap pengembangan dan mungkin tidak sepenuhnya berfungsi.

## Penggunaan

- **Backend:** Buka browser Anda dan navigasikan ke `http://localhost:8000` untuk mengakses API.
- **Frontend:** Buka browser Anda dan navigasikan ke `http://localhost:3000` untuk mengakses aplikasi frontend.
