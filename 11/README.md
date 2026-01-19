# FastAPI Asynchronous RESTful API (Cloud Native Application)

- Nama  : Aprian Pradipta E S
- NIM   : 235510008
- Prodi : Teknik Komputer S1

## 📌 Deskripsi Proyek
Proyek ini merupakan implementasi RESTful API menggunakan **FastAPI** yang mendukung
pemrograman **asynchronous / concurrent / non-blocking**. Source code yang digunakan
bertujuan untuk memahami bagaimana FastAPI menangani request secara efisien serta
bagaimana aplikasi dapat dijalankan sebagai **cloud native application** menggunakan
**Docker**.

Aplikasi menyediakan endpoint untuk mengambil data mahasiswa dari database PostgreSQL
serta endpoint dasar untuk pengujian server.

---

## 🛠️ Teknologi yang Digunakan
- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **PostgreSQL**
- **Docker**

---

## 📂 Struktur Folder
```
src/
├── api.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```
---

## 🚀 Menjalankan Aplikasi Secara Lokal

### 1️⃣ Aktifkan Virtual Environment

python -m venv .venv
source .venv/bin/activate

2️⃣ Install Dependency

pip install -r requirements.txt

3️⃣ Jalankan Server FastAPI

uvicorn api:app --reload

4️⃣ Akses Aplikasi
API Root
http://127.0.0.1:8000/

Dokumentasi Swagger
http://127.0.0.1:8000/docs

🔗 Endpoint API
Method	Endpoint	Deskripsi
GET	/	Mengambil seluruh data mahasiswa
GET	/mahasiswa/{nim}	Mengambil data mahasiswa berdasarkan NIM

🧠 Konsep Asynchronous & Non-Blocking
FastAPI mendukung pemrograman asynchronous dengan menggunakan async dan await
yang memungkinkan server menangani banyak request secara bersamaan tanpa menunggu
proses lain selesai (non-blocking).

Pada proyek ini, pemahaman konsep asynchronous digunakan sebagai dasar dalam
pengembangan RESTful API yang efisien dan scalable.

🐳 Docker (Cloud Native)
Build Image

docker build -t fastapi-parallel .

Jalankan Container
docker run -p 8000:8000 fastapi-parallel

Aplikasi dapat diakses melalui:
http://localhost:8000


## ☁️ Cloud Native Application
Aplikasi ini dikategorikan sebagai cloud native karena:

- Dijalankan di dalam container Docker
- Mudah dipindahkan antar environment
- Mendukung skalabilitas
- Siap diintegrasikan dengan Kubernetes

## 📌 Catatan
Koneksi database PostgreSQL perlu dipastikan berjalan sebelum aplikasi dijalankan
agar endpoint yang mengakses database dapat berfungsi dengan baik.

