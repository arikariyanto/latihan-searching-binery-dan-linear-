
import modul_search

print("="*50)
print("   📚 SISTEM PENCARIAN NAMA MAHASISWA   ")
print("="*50)

mahasiswa = ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fajar"]

while True:
    print("\nMenu:")
    print("1. Tampilkan daftar mahasiswa")
    print("2. Cari mahasiswa (Linear Search)")
    print("3. Cari mahasiswa (Binary Search)")
    print("4. Tambah mahasiswa baru")
    print("5. Hapus mahasiswa")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        print("\nDaftar Mahasiswa:")
        if len(mahasiswa) == 0:
            print("⚠️ Belum ada data mahasiswa.")
        else:
            for i, m in enumerate(mahasiswa):
                print(f"{i+1}. {m}")

    elif pilihan == "2":
        target = input("Masukkan nama mahasiswa yang dicari: ")
        hasil = modul_search.linear_search(mahasiswa, target)
        if hasil != -1:
            print(f"✅ {target} ditemukan pada index {hasil}")
        else:
            print("❌ Data tidak ditemukan!")

    elif pilihan == "3":
        target = input("Masukkan nama mahasiswa yang dicari: ")
        hasil = modul_search.binary_search(mahasiswa, target)
        if hasil != -1:
            print(f"✅ {target} ditemukan (binary search)")
        else:
            print("❌ Data tidak ditemukan!")

    elif pilihan == "4":
        nama_baru = input("Masukkan nama mahasiswa baru: ")
        if nama_baru not in mahasiswa:
            mahasiswa.append(nama_baru)
            print(f"✅ {nama_baru} berhasil ditambahkan!")
        else:
            print("⚠️ Nama sudah ada dalam daftar!")

    elif pilihan == "5":
        nama_hapus = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        if nama_hapus in mahasiswa:
            mahasiswa.remove(nama_hapus)
            print(f"🗑️ {nama_hapus} berhasil dihapus!")
        else:
            print("⚠️ Nama tidak ditemukan!")

    elif pilihan == "6":
        print("Terima kasih, program selesai.")
        break

    else:
        print("⚠️ Pilihan tidak valid!")
