# Flights API (FastAPI)

"Nama : Aprian Pradipta E S
Nim  : 235510008
Prodi: Teknik Komputer S1"

## Struktur Direktori

```
flights-api/
│── api.py
│── requirements.txt
│── README.md
│── data/
│   └── flights.csv
```

---

## Menjalankan Aplikasi

Pastikan sudah berada di direktori `flights-api` dan virtual environment aktif.

Menjalankan server FastAPI menggunakan **uvicorn**:

```bash
uvicorn api:app --reload
```

Jika berhasil, server akan berjalan pada:

```
http://127.0.0.1:8000
```

---

## Endpoint yang Tersedia

### 1. Root Endpoint

**URL:**

```
GET /
```

**Deskripsi:**
Menampilkan pesan bahwa Flights API berhasil dijalankan.

---

### 2. Flight by Tail Number

**URL:**

```
GET /flight/{tailnum}
```

**Contoh:**

```
GET /flight/N125UW
```

**Deskripsi:**
Mengembalikan data penerbangan berdasarkan *tail number* tertentu.

---

## Pengujian Menggunakan curl (Windows)

Karena eksekusi melalui browser atau Swagger Docs (`/docs`) membutuhkan waktu lebih lama, pengujian dilakukan menggunakan **curl**.

### Mengecek Versi curl

```bash
curl --version
```

### Mengakses Root Endpoint

```bash
curl http://127.0.0.1:8000/
```

### Mengakses Data Flight

```bash
curl http://127.0.0.1:8000/flight/N125UW
```

Output berupa **JSON string** yang berisi data penerbangan sesuai *tail number*.

---

## Note

* Output API berupa **JSON dalam bentuk string**, karena data dikonversi menggunakan `pandas.DataFrame.to_json()`.
* Meskipun tidak langsung terformat rapi, data yang dihasilkan **valid JSON** dan dapat diproses lebih lanjut jika diperlukan.
* Fokus utama tugas adalah memastikan API berjalan dan dapat diakses menggunakan *command-line client*.

---

## Kesimpulan

Flights API berhasil dijalankan menggunakan FastAPI dan Uvicorn. Endpoint dapat diakses dengan baik menggunakan curl, serta mampu mengembalikan data penerbangan sesuai parameter yang diberikan. Implementasi ini memenuhi tujuan praktikum dalam memahami dasar pembuatan dan pengujian REST API.
