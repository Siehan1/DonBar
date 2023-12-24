keranjang_belanja = []

def lihat_keranjang():
    if keranjang_belanja:
        print("Daftar Keranjang Belanja:")
        for barang in keranjang_belanja:
            print(f"- {barang}")
    else:
        print("Keranjang masih kosong")

def tambah_keranjang(barang):
    keranjang_belanja.append(barang)
    print(f"{barang} berhasil ditambahkan ke keranjang!")

def kosongkan_keranjang():
    keranjang_belanja.clear()
    print("Keranjang berhasil dikosongkan!")

tambah_keranjang("Mie Instan")
tambah_keranjang("Sampo")  
tambah_keranjang("Sikat Gigi")

lihat_keranjang() 

kosongkan_keranjang()

lihat_keranjang()