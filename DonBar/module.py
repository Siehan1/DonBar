import pandas as pd

def login(username, password):
    data = pd.read_csv("user_data.csv")
    global user
    user = data[data['Username'] == username]

    if len(user) == 1 and user['Password'].values[0] == password:
        return True,user['Role'].values[0]
    return False,None

def register(namaLengkap, username, password, noHp, role):
    new_data = {
        'Nama Lengkap': [namaLengkap],
        'Username': [username],
        'Password': [password],
        'No Hp': [noHp],
        'Role': [role]
    }

    try:
        data = pd.read_csv('user_data.csv')
        while username in data['Username'].values:
            print("Username sudah digunakan. Mohon coba lagi.")
            username = input("Masukkan Username: ")
            new_data['Username']=username

        new_df = pd.DataFrame(new_data)

        data = pd.concat([data,new_df], ignore_index=True)

        data.to_csv('user_data.csv', index=False)
        print("Registrasi berhasil!")
    except FileNotFoundError:
        new_data['Alamat'] = ['']
        new_df = pd.DataFrame(new_data)
        new_df.to_csv('user_data.csv', index=False)
        print("File user_data.csv dibuat. Registrasi berhasil!")

def profile():
    print("Profil")
    print(f"Nama Lengkap: {user['Nama Lengkap'].values[0]}")
    print(f"Username    : {user['Username'].values[0]}")
    if pd.isnull(user['Alamat'].values[0]) or user['Alamat'].values[0] == '':
        print("Alamat      : Belum di set")
    else:
        print(f"Alamat      : {user['Alamat'].values[0]}")
    print(f"No Hp       : {user['No Hp'].values[0]}")
    while True:
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
    data = pd.read_csv('user_data.csv')

    data.loc[data['Username'] == user['Username'].values[0], 'Alamat'] = alamat

    data.to_csv('user_data.csv', index=False)
    print("Alamat diubah!")

def tambah_barang(nama,kategori,harga):
    new_data = {
        'Nama Produk': [nama],
        'Kategori': [kategori],
        'Harga': [harga]
    }

    try:
        data = pd.read_csv('barang.csv')

        new_data['Username'] = user['Username'].values

        new_df = pd.DataFrame(new_data)

        data = pd.concat([data,new_df], ignore_index=True)

        data.to_csv('barang.csv', index=False)
        print("Berhasil Tambah Barang!")
    except FileNotFoundError:
        new_data['Username'] = user['Username'].values
        new_df = pd.DataFrame(new_data)
        new_df.to_csv('barang.csv', index=False)
        print("File barang.csv dibuat. Barang Berhasil Ditambah!")

def pengembalian_barang(nama=None):
    try:
        data = pd.read_csv('barang.csv')

        if nama is not None:
            data = data[~((data['Nama Produk'] == nama) & (data['Username'] == user['Username'].values[0]))]
            data.to_csv('barang.csv', index=False)
            print(f"Barang dengan nama '{nama}' berhasil dihapus.")
        else:
            print("Tidak ada barang yang dihapus.")

    except FileNotFoundError:
        print("File barang.csv tidak ditemukan.")

def tampil_barang():
    try:
        data = pd.read_csv('barang.csv')

        barang_user = data[data['Username'] == user['Username'].values[0]]
        
        if not barang_user.empty:
            print(f"Barang milik pengguna '{user['Username'].values[0]}':")
            print(barang_user.filter(items=['Nama Produk','Harga']))
            print("===========================================")
        else:
            print(f"Tidak ada barang yang dimiliki oleh pengguna '{user['Username'].values[0]}'.")

    except FileNotFoundError:
        print("File barang.csv tidak ditemukan.")