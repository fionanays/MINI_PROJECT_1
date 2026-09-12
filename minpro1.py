daftar_tanaman = [
    ["Anggrek", "Indoor", "Sudah disiram"],
    ["Mawar", "Outdoor", "Belum disiram"],
    ["Melati", "Outdoor", "Sudah disiram"],
    ["Lavender", "Outdoor", "Sudah disiram"],
    ["Peace Lily", "Indoor", "Belum disiram"],
    ["Lidah Mertua", "Indoor", "Belum disiram"]
]

while True:
    print("\nSISTEM SIRAM TANAMAN")
    print("1. Lihat daftar tanaman")
    print("2. Tambah data tanaman baru")
    print("3. Hapus tanaman")
    print("4. Update status siram tanaman")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan Anda (1-5): ")

    if pilihan == "1":
        print("\nDAFTAR TANAMAN")
        no = 1
        for tanaman in daftar_tanaman:
            print(f"{no}. {tanaman[0]} - {tanaman[1]} - {tanaman[2]}")
            no = no + 1

    elif pilihan == "2":
        nama_baru = input("Masukkan nama tanaman baru: ")
        jenis_baru = input("Masukkan jenis tanaman baru (Indoor/Outdoor): ")
        status_baru = input("Masukkan status siram (Sudah disiram/Belum disiram): ")

        tanaman_baru = [nama_baru, jenis_baru, status_baru]
        
        daftar_tanaman.append(tanaman_baru)

        print(f"Tanaman '{nama_baru}' berhasil ditambahkan!")

    elif pilihan == "3":
        print("\n--- DAFTAR TANAMAN ---")
        no = 1
        for tanaman in daftar_tanaman:
            print(f"{no}. {tanaman[0]}")
            no = no + 1

        nomor = int(input("Masukkan nomor tanaman yang ingin dihapus: "))
        indeks_hapus = nomor - 1

        tanaman_dihapus = daftar_tanaman.pop(indeks_hapus)

        print(f"Tanaman '{tanaman_dihapus[0]}' berhasil dihapus dari daftar!")

    elif pilihan == "4":
        print("\n--- DAFTAR TANAMAN ---")
        no = 1
        for tanaman in daftar_tanaman:
            print(f"{no}. {tanaman[0]} - {tanaman[2]}")
            no = no + 1

        nomor = int(input("Masukkan nomor tanaman yang ingin diupdate statusnya: "))
        indeks_update = nomor - 1

        status_saat_ini = daftar_tanaman[indeks_update][2]
        
        if status_saat_ini == "Sudah disiram":
            daftar_tanaman[indeks_update][2] = "Belum disiram"
            print(f"Status '{daftar_tanaman[indeks_update][0]}' diubah menjadi 'Belum disiram'.")
        else:
            daftar_tanaman[indeks_update][2] = "Sudah disiram"
            print(f"Status '{daftar_tanaman[indeks_update][0]}' diubah menjadi 'Sudah disiram'.")

    elif pilihan == "5":
        print("Terima kasih telah menggunakan Sistem Siram Tanaman. Semoga harimu menyenangkan:D")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-5.")