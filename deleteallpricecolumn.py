import pyodbc

def hapus_isi_kolom(access_file_path):
    # Menghubungkan ke database MS Access
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=' + access_file_path + ';'
    )
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    try:
        # Menghapus isi kolom "Jenis Hadiah"
        cursor.execute("UPDATE Pesertaundian SET [Jenis Hadiah] = NULL")
        
        # Menghapus isi kolom "Hadiah"
        cursor.execute("UPDATE Pesertaundian SET Hadiah = NULL")

        # Commit perubahan
        conn.commit()
        print("Isi kolom 'Jenis Hadiah' dan 'Hadiah' berhasil dihapus.")

    except Exception as e:
        print("Terjadi kesalahan:", e)
        conn.rollback()

    finally:
        # Menutup koneksi
        cursor.close()
        conn.close()

# Panggil fungsi hapus_isi_kolom dengan menyertakan path file database MS Access
hapus_isi_kolom(r"C:\Users\Dell Inspiron 3000\Downloads\Not laugh\acak.mdb")
