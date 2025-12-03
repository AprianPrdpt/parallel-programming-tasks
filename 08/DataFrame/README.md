# Dask DataFrames — Pertemuan 08

File ini berisi rangkuman hasil pengerjaan bagian **DataFrames** dari Dask Examples ([https://examples.dask.org/](https://examples.dask.org/)), mencakup:

* Read & Write Data
* Groupby
* Gotchas (perbedaan Dask vs Pandas)
* Reading Messy Data

Semua contoh dijalankan menggunakan Python dan Dask pada folder **08/**.

---

## ✅ 1. Read & Write Data

Program membuat file `people.csv`, kemudian membacanya menggunakan Dask.

**Output:**

```
=== READ & WRITE DATA ===
      name  age
0    Alice   25
1      Bob   30
2  Charlie   35
3    Diana   40
      name  age
0    Alice   25
1      Bob   30
2  Charlie   35
3    Diana   40
```

Selanjutnya data ditulis ke format **Parquet** dan dibaca kembali menggunakan Dask.

---

## ✅ 2. Groupby

Contoh sederhana melakukan operasi pengelompokan berdasarkan kolom `category`.

**Output:**

```
=== GROUPBY EXAMPLE ===
category
A    30
B    20
C     7
Name: value, dtype: int64
```

---

## ✅ 3. Gotchas (Pandas → Dask)

Menunjukkan bahwa Dask **tidak langsung menghitung** sebelum `.compute()` dipanggil.

**Output:**

```
=== GOTCHAS (Pandas → Dask) ===
Dask tidak langsung menghitung sampai .compute() dipanggil
      name  age  age_plus_5
0    Alice   25          30
1      Bob   30          35
2  Charlie   35          40
3    Diana   40          45
      name  age  age_plus_5
0    Alice   25          30
1      Bob   30          35
2  Charlie   35          40
3    Diana   40          45
```

---

## ✅ 4. Reading Messy Data

Membaca file CSV yang berisi data tidak rapi (misal kolom angka bercampur teks).

**Output:**

```
=== MESSY DATA READING ===
      name     age
0    Alice      25
1      Bob  thirty
2  Charlie      35
```

---

## 🏁 Selesai

Semua contoh dari bagian **DataFrames** berhasil dijalankan.

Script lengkap dapat dilihat pada file:

```
08/dask_dataframe_examples.py
```
