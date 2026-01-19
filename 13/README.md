# FastAPI + Piccolo ORM Cloud Native Application

- Nama  : Aprian Pradipta E S
- NIM   : 235510008
- Prodi : Teknik Komputer S1


Project ini merupakan implementasi **RESTful API** menggunakan **FastAPI** dan **Piccolo ORM**, kemudian dikemas menjadi **aplikasi cloud native** dengan **Docker** dan dideploy menggunakan **Kubernetes**.

Aplikasi ini menyediakan endpoint sederhana untuk menampilkan data `Band` berdasarkan ID.

---

## 📌 Teknologi yang Digunakan

- Python 3
- FastAPI
- Piccolo ORM
- SQLite
- Docker
- Kubernetes (Docker Desktop)

---

## 📁 Struktur Project

```
.
├── api.py
├── piccolo_conf.py
├── tables.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── deployment.yaml
├── service.yaml
├── README.md 
```
---

## 🚀 Menjalankan Aplikasi Secara Lokal

### 1. Install dependencies

uv pip install -r requirements.txt

### 2. Membuat database Piccolo

piccolo playground run
Tekan Ctrl + D setelah file piccolo.sqlite terbentuk.

### 3. Menjalankan server FastAPI

fastapi dev api.py

### 4. Akses API

http://localhost:8000/Band/1
http://localhost:8000/Band/2
http://localhost:8000/Band/3

## 🐳 Menjalankan Aplikasi dengan Docker

### 1. Build image Docker

docker build -t fastapi-piccolo .

### 2. Jalankan container

docker run -p 8000:8000 fastapi-piccolo

### 3. Akses API

http://localhost:8000/Band/1

## ☸️ Deploy ke Kubernetes
*Pastikan Kubernetes sudah aktif di Docker Desktop.

### 1. Apply Deployment dan Service

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

### 2. Cek status

kubectl get pods
kubectl get services
*Pastikan pod berstatus Running.

### 3. Akses API melalui Kubernetes

http://localhost:30007/Band/1

### 📡 OUTPUT
```
[
  {
    "id": 1,
    "name": "Pythonistas",
    "popularity": 1000
  }
]
```
## 📝 Catatan
Endpoint root (/) tidak disediakan karena aplikasi hanya mengimplementasikan endpoint /Band/{id}.

Service Kubernetes menggunakan tipe NodePort agar dapat diakses dari browser.

## 📄 Kesimpulan
Aplikasi RESTful API berbasis FastAPI dan Piccolo ORM berhasil dikemas menggunakan Docker dan dideploy ke Kubernetes. Dengan pendekatan ini, aplikasi dapat berjalan sebagai cloud native application yang portabel, terisolasi, dan mudah dikelola.
