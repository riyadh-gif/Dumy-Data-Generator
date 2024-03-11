import pyodbc

def get_input_from_user():
    # Mengambil input dari pengguna melalui command line
    return input("Masukkan teks yang di-scan dari alas scan QR: ")

def main():
    # Inisialisasi koneksi ke database MS Access
    database_path = 'C:/Users/Dell Inspiron 3000/Downloads/Not laugh/acak.mdb'
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + database_path)
    cursor = conn.cursor()

    # Mendapatkan nomor terakhir
    last_no = get_last_no(cursor)

    while True:
        # Ambil teks dari pengguna
        scanned_data = get_input_from_user()

        # Parsing data yang di-scan
        qr_code_fields = scanned_data.split(',')

        # Memasukkan data ke dalam database
        nip = qr_code_fields[0].strip()
        nama = qr_code_fields[1].strip()
        unit = qr_code_fields[2].strip()
        email = qr_code_fields[3].strip()

        # Memeriksa apakah NIP sudah ada dalam database
        if not is_nip_exists(cursor, nip):
            # Menambahkan 1 ke nomor terakhir
            last_no += 1

            cursor.execute("INSERT INTO pesertaundian (No, Nip, Nama, Divisi, Email, Status) VALUES (?, ?, ?, ?, ?, ?)", (last_no, nip, nama, unit, email, 'Scanned'))
            conn.commit()
            print("Data berhasil dimasukkan ke database.")
        else:
            print("NIP sudah ada dalam database. Data tidak dimasukkan.")

def is_nip_exists(cursor, nip):
    # Memeriksa apakah NIP sudah ada dalam database
    cursor.execute("SELECT COUNT(*) FROM pesertaundian WHERE Nip = ?", (nip,))
    count = cursor.fetchone()[0]
    return count > 0

def get_last_no(cursor):
    # Mendapatkan nomor terakhir
    cursor.execute("SELECT MAX(No) FROM pesertaundian")
    last_no = cursor.fetchone()[0]
    return last_no if last_no else 0

if __name__ == "__main__":
    main()
