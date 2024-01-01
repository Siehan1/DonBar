import pandas as pd
from datetime import datetime
import os
import time

date = datetime.now()

def clear():
    time.sleep(1.5)
    os.system("cls")

def login():
    clear()
    print("============ HALAMAN LOGIN ============")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    data = pd.read_csv("database/user_data.csv")
    global user
    user = data[data['Username'] == username]

    if len(user) == 1 and user['Password'].values[0] == password:
        return True,user['Role'].values[0]
    return False,None

def register(namaLengkap,username,password,noHp,role):
    new_data = {
        'Nama Lengkap': [namaLengkap],
        'Username': [username],
        'Password': [password],
        'No Hp': [noHp],
        # role adalah pendonasi dan penerima
        'Role': [role]
    }

    try:
        data = pd.read_csv('database/user_data.csv')
        new_data['id User'] = data['id User'].max() + 1
        new_data['Poin'] = 50
        while username in data['Username'].values:
            print("Username sudah digunakan. Mohon coba lagi.")
            username = input("Masukkan Username: ")
            new_data['Username']=username

        new_df = pd.DataFrame(new_data)

        # untuk menggabungkan data frame yang baru
        data = pd.concat([data,new_df], ignore_index=True)

        # datanya masuk ke folder user_data
        data.to_csv('database/user_data.csv', index=False)
        print("Registrasi berhasil!")
    except FileNotFoundError:
        new_data['Alamat'] = ['']
        new_df = pd.DataFrame(new_data)
        new_df.to_csv('database/user_data.csv', index=False)
        print("File user_data.csv dibuat. Registrasi berhasil!")

def profile():
    while True:
        clear()
        print("=========== HALAMAN PROFILE ===========")
        print(f"Nama Lengkap: {user['Nama Lengkap'].values[0]}")
        print(f"Username    : {user['Username'].values[0]}")
        if pd.isnull(user['Alamat'].values[0]) or user['Alamat'].values[0] == '':
            print("Alamat      : Belum di set")
        else:
            print(f"Alamat      : {user['Alamat'].values[0]}")
        print(f"No Hp       : {user['No Hp'].values[0]}")
        print("1. Ubah Alamat")
        print("2. Logout")
        choice2 = input(">")
        if choice2 == "1":
            alamat = input("Masukkan alamat baru: ")
            add_alamat(alamat)
        if choice2 == '2':
            print(f"Berhasil Logout! Selamat Tinggal {user['Username'].values[0]}")
            return True

def add_alamat(alamat):
    clear()
    data = pd.read_csv('database/user_data.csv')
    # untuk mengakses dan mengubah data
    data.loc[data['Username'] == user['Username'].values[0], 'Alamat'] = alamat

    data.to_csv('database/user_data.csv', index=False)
    print("Alamat diubah!")

def tambah_barang(nama,kategori,harga,detail):
    new_data = {
        'Nama Produk': [nama],
        'Kategori': [kategori],
        'Harga': [harga],
        'Detail Produk': [detail]
    }

    try:
        data = pd.read_csv('database/barang.csv')

        new_data['Username'] = user['Username'].values
        new_data['id Barang'] = data['id Barang'].max() + 1

        new_df = pd.DataFrame(new_data)

        data = pd.concat([data,new_df], ignore_index=True)

        data.to_csv('database/barang.csv', index=False)
        print("Berhasil Tambah Barang!")
    except FileNotFoundError:
        new_data['Username'] = user['Username'].values
        new_df = pd.DataFrame(new_data)
        new_df.to_csv('database/barang.csv', index=False)
        print("File barang.csv dibuat. Barang Berhasil Ditambah!")

def pengembalian_barang(idBarang=None):
    try:
        data = pd.read_csv('database/barang.csv')

        if idBarang is not None:
            data = data[~((data['id Barang'] == idBarang) & (data['Username'] == user['Username'].values[0]))]
            data.to_csv('database/barang.csv', index=False)
            print(f"Barang dengan ID {idBarang} berhasil dikembalikan.")
        else:
            print("Tidak ada barang yang dikembalikan.")

    except FileNotFoundError:
        print("File barang.csv tidak ditemukan.")

def tampil_barang():
    try:
        data = pd.read_csv('database/barang.csv')

        barang_user = data[data['Username'] == user['Username'].values[0]]
        
        if not barang_user.empty:
            print(f"Barang milik pengguna '{user['Username'].values[0]}':")
            filtered_barang = barang_user.filter(items=['id Barang','Nama Produk','Harga','Detail Produk'])
            print(filtered_barang.to_string(index=False))
            print("===========================================")
            return True
        else:
            print(f"Tidak ada barang yang dimiliki oleh pengguna '{user['Username'].values[0]}'.")
            return False

    except FileNotFoundError:
        print("File barang.csv tidak ditemukan.")

def cari_barang(nama):
    try:
        data = pd.read_csv('database/barang.csv')

        hasil_pencarian = data[data['Nama Produk'].str.contains(nama, case=False)]

        if not hasil_pencarian.empty:
            hasil_pencarian = hasil_pencarian.filter(items=["id Barang","Nama Produk","Kategori","Harga"])
            print(f"Hasil pencarian untuk '{nama}':")
            print(hasil_pencarian.to_string(index=False))
            return True
        else:
            print(f"Tidak ditemukan barang dengan nama '{nama}'.")
            return False

    except FileNotFoundError:
        print("File barang.csv tidak ditemukan.")

def add_keranjang(idBarang):
    try:
        data_barang = pd.read_csv('database/barang.csv')
        
        # Melakukan filtering untuk mendapatkan data barang berdasarkan idBarang
        filtered_barang = data_barang[data_barang['id Barang'] == idBarang]
        
        if not filtered_barang.empty:
            data_keranjang = pd.read_csv('database/keranjang.csv')
            
            if data_keranjang.empty:
                id_terakhir = 1
            else:
                id_terakhir = data_keranjang['id Keranjang'].max() + 1
            
            # Mengambil nilai dari baris pertama setelah filtering
            barang = filtered_barang.iloc[0]
            
            new_data = {
                'id Keranjang': [id_terakhir],
                'Penerima': [user['Username'].values[0]],  # Pastikan user sudah didefinisikan sebelumnya
                'id Barang': [barang['id Barang']],
                'Nama Produk': [barang['Nama Produk']],
                'Harga': [barang['Harga']],
                'Pendonasi': [barang['Username']]
            }
            
            new_df = pd.DataFrame(new_data)
            
            # Menggabungkan DataFrame data_keranjang dengan new_df
            data_keranjang = pd.concat([data_keranjang, new_df], ignore_index=True)
            
            data_keranjang.to_csv('database/keranjang.csv', index=False)
            print("Berhasil Tambah ke Keranjang!")
        else:
            print(f"Tidak ditemukan barang dengan ID {idBarang}.")

    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def tampil_keranjang():
    try:
        data = pd.read_csv('database/keranjang.csv')

        barang_user = data[data['Penerima'] == user['Username'].values[0]]
        
        if not barang_user.empty:
            print(f"Keranjang milik pengguna '{user['Username'].values[0]}':")
            print(barang_user.filter(items=['Nama Produk','Harga']))
            print(f"Total Harga: {barang_user['Harga'].sum()}")
            print("===========================================")
            print("1. Checkout")
            print("2. Kembali")
            choice = input(">>")
            if choice == '1':
                add_pesanan()
        else:
            print(f"Keranjang Kosong!.")

    except FileNotFoundError:
        print("File keranjang.csv tidak ditemukan.")

def add_pesanan():
    try:
        data_keranjang = pd.read_csv('database/keranjang.csv')
        barang_user = data_keranjang[data_keranjang['Penerima'] == user['Username'].values[0]]

        if not barang_user.empty: # Pastikan tipe data Harga adalah numerik
            if barang_user['Harga'].sum() <= user['Poin'].values[0]:
                data_pesanan = pd.read_csv('database/pesanan.csv')

                if data_pesanan.empty:
                    id_pesanan = 1
                else:
                    id_pesanan = data_pesanan['id Pesanan'].max() + 1

                tanggal = datetime.now().strftime('%d-%m-%Y')

                new_pesanan = {
                    'id Pesanan': [id_pesanan],
                    'Tanggal': [tanggal],
                    'Total Harga': [barang_user['Harga'].sum()],
                    'Penerima': [user['Username'].values[0]]  # Ambil nilai username
                }

                df_pesanan = pd.DataFrame(new_pesanan)
                df_pesanan.to_csv('database/pesanan.csv', mode='a', header=not os.path.exists('database/pesanan.csv'), index=False)
                print("Pesanan berhasil diproses.")
                add_detail()
            else:
                print("Poin Tidak Mencukupi")
        else:
            print("Tidak ada barang dalam keranjang untuk pengguna ini.")

    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def add_detail():
    data_pesanan = pd.read_csv('database/pesanan.csv')
    data_keranjang = pd.read_csv('database/keranjang.csv')
    data_detail = pd.read_csv('database/detailPesanan.csv')

    data_pesanan = data_pesanan[data_pesanan['Penerima'] == user['Username'].values[0]]
    data_keranjang = data_keranjang[data_keranjang['Penerima'] == user['Username'].values[0]]

    if not data_keranjang.empty:
        # untuk mengetahui data detail kosong atau tidak
        id_detail = 1 if data_detail.empty else data_detail['id detail'].max() + 1

        detail = []
        # untuk mengakses setiap baris dari data frame
        for idx, row in data_keranjang.iterrows():
            detail.append({
                'id detail': id_detail,
                'id Pesanan': data_pesanan.iloc[0]['id Pesanan'],
                'id Barang': row['id Barang'],
                'Nama Produk': row['Nama Produk'],
                'Harga': row['Harga'],
                'Pendonasi': row['Pendonasi'],
                'Penerima': user['Username'].values[0]
            })
            id_detail += 1
        
        # Buat DataFrame dari list detail
        df_detail = pd.DataFrame(detail)
        
        # Append data ke file CSV menggunakan mode='a' (append)
        # os.path.exists untuk mengembalikan nilai true jika filenya ada, jika tidak ada maka nilainya akan 'false'
        df_detail.to_csv('database/detailPesanan.csv', mode='a', header=not os.path.exists('database/detailPesanan.csv'), index=False)

        data_keranjang = data_keranjang.iloc[len(detail):]
        data_keranjang.to_csv('database/keranjang.csv', index=False)
    else:
        print("Tidak ada data keranjang untuk pengguna ini.")
