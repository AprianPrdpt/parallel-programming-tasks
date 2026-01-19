Untuk menjalankan:

1. Install semua packages:
    
      uv pip install -r requirements.txt

2. Buat tabel Piccolo:

      piccolo playground run 

  Tekan Ctrl-D setelah terbentuk file piccolo.sqlite.

3.  Jalankan:

      fastapi dev api.py 

    Akses melalui curl / browser  ke 
      hhtp://localhost:8000 
      http://localhost:8000/Band/1
      http://localhost:8000/Band/2
      http://localhost:8000/Band/3
