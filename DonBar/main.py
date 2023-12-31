import module as md

while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Pilih opsi: ")
    if choice == '1':
        namaLengkap = input("Masukkan Nama Lengkap: ")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        NoHp = input("Masukkan Nomor HP: ")
        role = input("Pendonasi/Penerima?: ")

        md.register(namaLengkap, username, password, NoHp, role)
    elif choice == '2':
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        login_status, role = md.login(username,password)
        if login_status:
            print(f"Login berhasil! sebagai {role}")
            if role == "Pendonasi":
                while True:
                    print("1. Tampil Barang")
                    print("2. Tambah Barang")
                    print("3. Refund Barang")
                    print("4. Tampil Profil")
                    choice1 = input("Pilih Opsi: ")
                    if choice1 == "1":
                        md.tampil_barang()
                    elif choice1 == "2":
                        nama = input("Masukkan Nama barang: ")
                        kategori = input("Kategori Barang: ")
                        harga = input("Harga Barang: ")
                        md.tambah_barang(nama,kategori,harga)
                    elif choice1 == "3":
                        nama = input("Nama Barang yang Akan di Refund: ")
                        md.pengembalian_barang(nama)
                    elif choice1 == "4":
                        logoutStat = md.profile()
                        if logoutStat:
                            break
            elif role == "Penerima":
                print("1. Tampil Profil")
                choice1 = input("pilih Opsi: ")
                if choice1 == '1':
                    md.profile()
        else:
            print("Login gagal. Periksa kembali username dan password Anda.")
    elif choice == '3':
        print("Anda Keluar Dari Aplikasi! Selamat Tinggal!")
        break
    else:
        print("Opsi tidak valid. Silakan pilih opsi yang benar.")