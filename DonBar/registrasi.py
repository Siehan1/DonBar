class Pengguna:
    def isi_pengguna(self, nama_lengkap, username, password, no_telp, kategori):
        self.nama_lengkap = nama_lengkap
        self.username = username
        self.password = password
        self.no_telp = no_telp
        self.kategori = kategori

def registrasi_pengguna():
    print("Selamat datang di halaman registrasi!")
    nama_lengkap = input("Nama Lengkap: ")
    username = input("Username: ")
    password = input("Password: ")
    no_telp = input("Nomor HP: ")
    kategori = input("Kategori (pendonasi atau penerima): ")

    user = Pengguna()
    user.isi_pengguna(nama_lengkap, username, password, no_telp, kategori)
    return user

def pendonasi(username):
    print(f"Selamat datang, {username}! Anda sekarang berada di halaman pendonasi.")

def penerima(username):
    print(f"Selamat datang, {username}! Anda sekarang berada di halaman penerima.")

user = registrasi_pengguna()

if user.kategori == 'pendonasi':
    pendonasi(user.username)
elif user.kategori == 'penerima':
    penerima(user.username)
