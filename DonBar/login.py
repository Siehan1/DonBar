def login():
    namauser = "donbar"
    passcode = "123"
    
    kesempatan = 3
    
    while 0 < kesempatan:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        if username == namauser and password == passcode:
            print("Login berhasil!")
            break
        else:
            kesempatan == 1
            print(f"Login gagal! Kesempatan Anda {kesempatan}x lagi")
    
    if kesempatan == 0:
        print("Anda telah mencapai batar percobaan. Keluar dari login.")

login()