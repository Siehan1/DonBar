list_barang = []

def tambah_barang (nama_barang):
    list_barang.append(nama_barang)
    print(f"{nama_barang} berhasil ditambahkan!")

def lihat_barang():
    if list_barang:
        print("List barang:")
        for barang in list_barang:
            print(f"-{barang}")
    else:
        print("Barang belum ditambahkan")