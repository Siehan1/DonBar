import module as md

while True:
    md.clear()
    print("============= D O N B A R =============")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Pilih opsi: ")
    if choice == '1':
        md.clear()
        print("========== HALAMAN REGISTRASI =========")
        namaLengkap = input("Masukkan Nama Lengkap: ")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        noHp = input("Masukkan Nomor HP: ")
        role = input("Pendonasi/Penerima?: ")
        md.register(namaLengkap,username,password,noHp,role)
    elif choice == '2':
        for i in range(1,4):
            login_status, role = md.login()
            if login_status:
                print(f"Login berhasil! sebagai {role}")
                if role == "Pendonasi":
                    while True:
                        md.clear()
                        print("============ HALAMAN PENDONASI ============")
                        print("1. Tampil Barang")
                        print("2. Tambah Barang")
                        print("3. Refund Barang")
                        print("4. Cari Barang")
                        print("5. Tampil Keranjang")
                        print("6. Tampil Profil")
                        choice1 = input("Pilih Opsi: ")
                        if choice1 == "1":
                            while True:
                                md.clear()
                                print("============ TAMPIL BARANG ============")
                                md.tampil_barang()
                                kembali = input("Kembali? (Y/N)")
                                if kembali == "Y":
                                    break
                        elif choice1 == "2":
                            md.clear()
                            print("============ TAMBAH BARANG ============")
                            nama = input("Masukkan Nama barang: ")
                            detail = input("Detail Produk: ")
                            kategori = input("Kategori Barang: ")
                            harga = input("Harga Barang: ")
                            md.tambah_barang(nama,kategori,harga,detail)
                        elif choice1 == "3":
                            md.clear()
                            print("============ REFUND BARANG ============")
                            md.tampil_barang()
                            idBarang = int(input("ID Barang yang Akan di Refund: "))
                            md.pengembalian_barang(idBarang)
                        elif choice1 == '4':
                            md.clear()
                            print("============= CARI BARANG =============")
                            nama = input("Nama Barang: ")
                            if md.cari_barang(nama):
                                print("1. Masukkan Keranjang")
                                print("2. Kembali")
                                choice2 = input(">>")
                                if choice2 == '1':
                                    idBarang = int(input("ID Barang: "))
                                    md.add_keranjang(idBarang)
                        elif choice1 == '5':
                            md.clear()
                            print("============== KERANJANG ==============")
                            md.tampil_keranjang()
                        elif choice1 == "6":
                            logoutStat = md.profile()
                            if logoutStat:
                                break
                elif role == "Penerima":
                    while True:
                        md.clear()
                        print("============ HALAMAN PENERIMA ============")
                        print("1. Cari Barang")
                        print("2. Tampil Keranjang")
                        print("3. Tampil Profil")
                        choice1 = input("pilih Opsi: ")
                        if choice1 == '1':
                            md.clear()
                            print("============= CARI BARANG =============")
                            nama = input("Nama Barang: ")
                            if md.cari_barang(nama):
                                print("1. Masukkan Keranjang")
                                print("2. Kembali")
                                choice2 = input(">>")
                                if choice2 == '1':
                                    idBarang = int(input("ID Barang: "))
                                    md.add_keranjang(idBarang)
                        elif choice1 == '2':
                            md.clear()
                            print("============== KERANJANG ==============")
                            md.tampil_keranjang()
                        elif choice1 == '3':
                            logoutStat = md.profile()
                            if logoutStat:
                                break
            else:
                print("Login gagal. Periksa kembali username dan password Anda.")
    elif choice == '3':
        print("Anda Keluar Dari Aplikasi! Selamat Tinggal!")
        break
    else:
        print("Opsi tidak valid. Silakan pilih opsi yang benar.")