import pyodbc
from faker import Faker
import random
import string

def generate_random_data():
    fake = Faker()
    # Generate data secara acak menggunakan modul faker
    # NIP (Number&Alphabet) - menggunakan kombinasi angka dan huruf sepanjang 8 karakter
    nip = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    # Nama (Text) - menggunakan nama palsu yang di-generate oleh Faker
    nama = fake.name()
    # Divisi (Text) - menggunakan divisi acak dari list yang telah diberikan
    divisi_list = ['IT', 'Keuangan', 'SDM', 'Pemasaran']
    unit = random.choice(divisi_list)
    # Email (Text) - menggunakan kombinasi huruf acak sepanjang 5 karakter ditambah '@example.com'
    email = ''.join(random.choices(string.ascii_lowercase, k=5)) + '@example.com'
    return [nip, nama, unit, email]

def main():
    # Inisialisasi koneksi ke database MS Access
    database_path = 'C:/Users/Dell Inspiron 3000/Downloads/Not laugh/acak.mdb'
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + database_path)
    cursor = conn.cursor()

    # Mengisi tabel dengan 1000 data
    for i in range(1, 3001):
        # Parsing data yang di-scan (dalam kasus ini, digenerate secara acak)
        qr_code_fields = generate_random_data()

        # Memasukkan data ke dalam database
        nip, nama, unit, email = qr_code_fields
        cursor.execute("INSERT INTO pesertaundian (No, Nip, Nama, Divisi, Email, Status) VALUES (?, ?, ?, ?, ?, ?)", (i, nip, nama, unit, email, 'Scanned'))
        conn.commit()
        print(f"Data {i} berhasil dimasukkan ke database.")

if __name__ == "__main__":
    main()
