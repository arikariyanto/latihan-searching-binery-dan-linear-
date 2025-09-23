# main.py
import modul_search

print("="*50)
print("   📚 SISTEM PENCARIAN NAMA MAHASISWA   ")
print("="*50)

# Data awal mahasiswa
mahasiswa = ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fajar"]

while True:
    print("\nMenu:")
    print("1. Tampilkan daftar mahasiswa")
    print("2. Cari mahasiswa (Linear Search)")
    print("3. Cari mahasiswa (Binary Search)")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        print("\nDaftar Mahasiswa:")
        for m in mahasiswa:
            print("-", m)

    elif pilihan == "2":
        target = input("Masukkan nama mahasiswa yang dicari: ")
        hasil = modul_search.linear_search(mahasiswa, target)   # isian kosong 6
        if hasil != -1:
            print(f"✅ {target} ditemukan pada index {hasil}")
        else:
            print("❌ Data tidak ditemukan!")

    elif pilihan == "3":
        target = input("Masukkan nama mahasiswa yang dicari: ")
        hasil = modul_search.binary_search(mahasiswa, target)   # isian kosong 7
        if hasil != -1:
            print(f"✅ {target} ditemukan (binary search)")
        else:
            print("❌ Data tidak ditemukan!")

    elif pilihan == "4":
        print("Terima kasih, program selesai.")
        break

    else:
        print("⚠️ Pilihan tidak valid!")
