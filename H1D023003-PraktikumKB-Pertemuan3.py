import random
import datetime

# Struktur Data 
menu_minuman = {
    "Matcha (Jepang)": 15000,
    "Thai Tea (Thailand)": 12000,
    "Bubble Tea (Taiwan)": 18000,
    "Morrocan Mint Tea (Maroko)": 10000,
    "Turkish Coffee (Turki)": 20000
}

# Fungsi buat nampilin menunya
def tampilkan_menu():
    print("\n🌍 Menu Minuman Internasional 🌍")
    for idx, (minuman, harga) in enumerate(menu_minuman.items(), start=1):
        print(f"{idx}. {minuman} - Rp {harga}")

# Fungsi buat pesan minumny
def pesan_minuman():
    tampilkan_menu()
    pilihan = int(input("\nPilih minuman (1-5): "))
    jumlah = int(input("Masukkan jumlah yang ingin dipesan: "))

    minuman_terpilih = list(menu_minuman.keys())[pilihan - 1]
    total_harga = menu_minuman[minuman_terpilih] * jumlah

    print(f"\n✅ Anda memesan {jumlah} {minuman_terpilih}. Total harga: Rp {total_harga}")

# Fungsi untuk menampilkan waktu transaksi
def tampilkan_waktu():
    sekarang = datetime.datetime.now()
    print(f"\n⏰ Waktu Transaksi: {sekarang.strftime('%Y-%m-%d %H:%M:%S')}")

# Program utamaa
while True:
    print("\n✨ Selamat Datang di Kedai Minuman Internasional ✨")
    print("1. Pesan Minuman")
    print("2. Keluar")
    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "1":
        pesan_minuman()
        tampilkan_waktu()
    elif pilihan == "2":
        print("🙏 Terima kasih telah berkunjung!")
        break
    else:
        print("⚠️ Pilihan tidak valid, coba lagi.")
