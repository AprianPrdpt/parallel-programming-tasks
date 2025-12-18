from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Koneksi ke database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",      
    database="db_flask"
)

@app.route("/")
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM mahasiswa")
    data = cursor.fetchall()
    cursor.close()
    return render_template("index.html", mahasiswa=data)

if __name__ == "__main__":
    app.run(debug=True)
