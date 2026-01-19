Menjalankan:

$ fastapi dev api.py 

   FastAPI   Starting development server 🚀
 
             Searching for package file structure from directories with __init__.py files
             Importing from /home/bpdp/kerjaan/utdi/kuliah/ganjil-2025-2026/komp-paralel-cloud/10/regular/src-10
 
    module   🐍 api.py
 
      code   Importing the FastAPI app object from the module with the following code:
 
             from api import app
 
       app   Using import string: api:app
 
    server   Server started at http://127.0.0.1:8000
    server   Documentation at http://127.0.0.1:8000/docs
 
       tip   Running in development mode, for production use: fastapi run
 
             Logs:
 
      INFO   Will watch for changes in these directories: ['/home/bpdp/kerjaan/utdi/kuliah/ganjil-2025-2026/komp-paralel-cloud/10/regular/src-10']
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      INFO   Started reloader process [13251] using WatchFiles
      INFO   Started server process [13254]
      INFO   Waiting for application startup.
      INFO   Application startup complete.

Setelah itu akses menggunakan browser (atau curl):

  http://localhost:8000
  http://localhost:8000/mahasiswa/23415
