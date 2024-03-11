import pyodbc

# Establishing connection to MS Access database
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\Dell Inspiron 3000\Downloads\Not laugh\acak.mdb;'  # Lokasi file database yang Anda berikan
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Function to check the number of prizes
def check_prize(prize_name):
    cursor.execute("SELECT COUNT(*) FROM Pesertaundian WHERE Hadiah = ?", (prize_name,))
    return cursor.fetchone()[0]

# Function to check the number of "DoorPrize" prizes
def check_doorprize():
    cursor.execute("SELECT COUNT(*) FROM Pesertaundian WHERE [Jenis Hadiah] LIKE '%DoorPrize%'")
    return cursor.fetchone()[0]

# Function to count total prizes
def count_total_prizes():
    cursor.execute("SELECT COUNT(Hadiah) FROM Pesertaundian")
    return cursor.fetchone()[0]


# Dictionary of prizes and their counts
prizes = {
    "Teflon": 5,
    "Kotak Makan": 50,
    "Botol Minum": 50,
    "Kipas Portable": 20,
    "Handuk": 20,
    "Payung": 20,
    "Tas Kotak Bekal": 50,
    "Pisau Set": 10,
    "Voucher Belanja": 63,
    "Selimut": 20,
    "Magicom Mini 2": 5,
    "Setrika": 5,
    "Headset Bluethooth": 5,
    "Panci Hotpot": 5,
    "Bantal leher": 10,
    "1 Set sendok garpu": 50,
    "Keset": 50,
    "Tumbler": 50,
    "Juicer": 10,
    "Mini Chooper": 10,
    "Panci Ramen": 10,
    "1 Set spatula": 50,
    "Jam Dinding": 50,
    "Jas Hujan": 20,
    "Mouse": 20,
    "Set Mangkok": 50,
    "Set Gelas": 50,
    "Emergency Lamp": 10,
    "Teko Plastik": 50,
    "Smart Watch": 10,
    "Set Piring": 50,
    "Kotak Tisu": 50,
    "Mug": 50
}

# Checking the prizes
for prize, count in prizes.items():
    actual_count = check_prize(prize)
    if actual_count == count:
        print(f"Jumlah {prize} sesuai: {count}")
    else:
        print(f"Jumlah {prize} tidak sesuai: seharusnya {count}, sebenarnya {actual_count}")

# Checking the number of "DoorPrize" prizes
doorprize_count = check_doorprize()
print(f"Jumlah hadiah dengan teks 'DoorPrize': {doorprize_count}")

# Counting total prizes
total_prizes = count_total_prizes()
print(f"Total hadiah di kolom 'Hadiah': {total_prizes}")

# Closing connection
cursor.close()
conn.close()
