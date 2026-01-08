Untuk instalasi paket:

  Jika menggunakan dask:
    uv pip install dask[complete]
  Jika menggunakan fastapi:
    uv pip install fastapi[standard]

Menjalankan FastAPI:

  fastapi dev api.py 

    => definisi RESTful API ada di api.py

Semua source code di pertemuan 11 ini menggunakan data yang bisa diperoleh di URL sesuai file url.txt.
Untuk menjalankan:
  Setiap direktori mempunyai versi Python tertentu (tidak perlu 'uv python pin <versi>' lagi). 
  Atur dengan menggunakan uv untuk paket-paketnya.
    Buat venv lebih dahulu:
      uv venv
      source .venv/bin/activate
    Install paket:
      uv pip install -r requirements.txt

Jika ingin berpindah workspace:
  jangan lupa deactivate venv lebih dulu dengan perintah 'deactivate'.
  Aktifkan dengan source .venv/bin/activate di setiap direktori/workspace
