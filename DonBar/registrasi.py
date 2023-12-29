import pandas as pd

def register(df):
    while True:
        nama_lengkap = input("Masukkan Nama Lengkap: ")
        username = input("Masukkan Username: ")
        while username in df['Username'].values:
            print("Username sudah digunakan. Mohon coba lagi.")
            username = input("Masukkan Username: ")
        
        password = input("Masukkan Password: ")
        nomor_hp = input("Masukkan Nomor HP: ")
        kategori = input("Masukkan Kategori (Pendonasi/Penerima): ")

        # untuk menambahkan baris baru ke DataFrame. 
        df.loc[len(df)] = [nama_lengkap, username, password, nomor_hp, kategori]

        print(f"Selamat datang, {username}! Anda telah berhasil registrasi.")
        
        # Menyimpan data ke file CSV
        df.to_csv('data_registrasi.csv', index=False) 
        break

if __name__ == "__main__":
    try:
        # untuk membaca DataFrame dari file CSV yang sudah ada (jika ada). Jika file CSV tidak ditemukan, maka kita membuat DataFrame kosong.
        df = pd.read_csv('data_registrasi.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Nama Lengkap', 'Username', 'Password', 'Nomor HP', 'Kategori'])

    print("Halo, selamat datang di aplikasi DonBar!")
    register(df)

    # Tampilan setelah registrasi berhasil
    username_login = input("Masukkan Username: ")
    password_login = input("Masukkan Password: ")

    if username_login in df['Username'].values and password_login == df.loc[df['Username'] == username_login, 'Password'].values[0]:
        print(f"Selamat datang, {username_login}! Anda telah berhasil login.")
    else:
        print("Username atau password salah. Silakan coba lagi.")
