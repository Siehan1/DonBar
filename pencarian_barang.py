daftar_barang = ["Buku", "Pensil", "Bolpoin", "Penghapus"]

def cari_barang(nama_barang_dicari):
    ditemukan = False
    
    for barang in daftar_barang:
        if barang.lower() == nama_barang_dicari.lower():
            ditemukan = True
            break

    if ditemukan:
        print(f"Barang {nama_barang_dicari} ditemukan di daftar barang!") 
    else:
        print(f"Barang {nama_barang_dicari} tidak ditemukan di daftar barang.")

barang_yang_dicari = input("Search: ")
cari_barang(barang_yang_dicari)