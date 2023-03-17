#Nama : Najww Caesa Putri Ramadhania Suharizman Poerwo
#Kelas: Sistem Informasi A 2022
#NIM: 2209116048

from prettytable import PrettyTable
import os

print("=============================================================")
print("=========== Selamat datang di Kedai Seblak Cesa =============")
print("=============================================================\n")

admin = {"username" : ["admin"],
      "password" : ["cesaa12"]}
pelanggan ={"username" : ["jeno"],
      "password" : ["nctdr"]}

daftar= {"Varian" : ["Seblak Komplit", "Seblak Pentol", "Seblak Sosis", "Seblak Mie", "Seblak Ceker", "Seblak Telur"],      
          "Harga Seblak" : [18000, 16000, 16000, 15000, 17000, 15000],
          "Stok Seblak" : [10, 15, 12, 17, 8, 12]}
         
tabel_varian = PrettyTable() 
tabel_admin = PrettyTable()
tabel_varian.field_names = ["Varian", "Harga Seblak", "Stok Seblak"]

def Varian_seblak(vr, hs, ss): 
    daftar.get("Varian").append(vr)
    daftar.get("Harga Seblak").append(hs)
    daftar.get("Stok Seblak").append(ss)

def UbahVarian_seblak(cariin, hs, ss): 
    daftar.get("Harga Seblak")[cariin]= hs
    daftar.get("Stok Seblak")[cariin]= ss

def btable():
    tabel_varian.clear_rows()
    for i in range(len(daftar["Varian"])):
        tabel_varian.add_row([daftar["Varian"][i],daftar["Harga Seblak"][i],daftar["Stok Seblak"][i]])
    print(tabel_varian)

def hapusVarian():
    btable()
    hapus = input("masukkan nama seblak yang ingin di hapus : ")
    hapusvarian = daftar.get("Varian").index(hapus)
    daftar.get("Varian").pop(hapusvarian)
    daftar.get("Harga Seblak").pop(hapusvarian)
    daftar.get("Stok Seblak").pop(hapusvarian)
    btable()

def Menu_admin():
    print("""
    ====================================
    |              Menu                |
    ====================================
    |      1. Tampilkan Varian         |
    |      2. Tambahkan Varian         |
    |      3. Mengubah Varian          |
    |      4. Menghapus Varian         |
    |      5. keluar                   |
    ====================================
    """)
    
def Varian_seblak():
    vr = (input("Masukkan Varian seblak: "))
    hs = int(input("Masukkan harga seblak: "))
    ss = int(input ("Masukkan stok seblak: "))
    daftar.get("Varian").append(vr)
    daftar.get("Harga Seblak").append(hs)
    daftar.get("Stok Seblak").append(ss)
    tabel_admin.add_row([vr,hs,ss])
    btable()

def ubahVarian_seblak():
    ubh = input("Masukkan varian seblak yang akan anda ubah : ")
    cariin = daftar.get("Varian").index(ubh)
    hs = input("Masukkan harga seblak terbaru : ")
    ss = input("Masukkan stok seblak Terbaru : ")
    UbahVarian_seblak (cariin, hs, ss)
    btable()

def login_admin():
    while True :
        username = input("Masukkan username :")
        password = input("Masukkan password :")
        try:
            cariin= admin.get("username").index(username)
            if admin.get("username")[cariin] == username and admin.get("password")[cariin] == password : 
                print("\n======Selamat anda berhasil login=====\n")
                aplikasi_berjalan = True
                while aplikasi_berjalan:
                    Menu_admin()
                    pilih=int(input("Silahkan pilih:  "))
                    if pilih == 1:
                        os.system('cls')
                        btable()
                    elif pilih == 2: 
                        os.system('cls')
                        Varian_seblak()
                    elif pilih == 3: 
                        os.system('cls')
                        ubahVarian_seblak()
                    elif pilih == 4:
                        os.system('cls') 
                        hapusVarian()
                    elif pilih == 5 : 
                        os.system('cls')
                        menu_login()
                else :
                    print("\n===== Maaf password anda salah, coba lagi =====\n")
                    salah = username["Kesempatan"] - 1
                    username["Kesempatan"] = salah
                    print("Kesempatan anda login sisa :", username["Kesempatan"])
        except ValueError:
            print("Error")

def login_pelanggan():
    while True:
        username = input("Masukkan username anda: ")
        password = input("Masukkan password anda: ")
        try:
            login = pelanggan.get("username").index(username)
            if username == pelanggan.get("username")[login] and password == pelanggan.get("password")[login]:
                break
            else:
                print("\n===== Maaf password anda salah, coba lagi =====\n")
        except ValueError:
            print("\n===== Maaf username anda salah, coba lagi =====\n")


def bayar():
    btable()
    vrn = input("masukan varian seblak yang ingin dibeli : ")
    if vrn in daftar["Varian"]:
        cari_menu = daftar["Varian"].index(vrn)
        if vrn == daftar["Varian"][cari_menu]:
            cari_harga = daftar["Varian"].index(vrn)
            total_harga = daftar["Harga Seblak"][cari_harga]
            nama = input("Masukkan nama anda: ")
            hp = int(input("Masukkan no hp anda: 628"))
            emoney = int(input("Masukkan nominal pembelian dengan e-money: "))
            kembali = emoney - total_harga
            os.system("cls")
            print("\n============ STRUK PEMBELIAN ===========")
            print ("Nama         :",nama)
            print ("no hp        : 628",hp)
            print ("Total        : Rp.",total_harga)
            print ("uang         : Rp.",emoney)
            print ("kembalian    : Rp.",kembali)
            print("========================================")

        else:
            print("menu tak tersedia, harap masukan menu yang tersedia")

def menu_login():
    print("""
    ====================================
    |              Menu                |
    ====================================
    |      1. login pelanggan          |
    |      2. login admin              |
    |      3. keluar                   |
    ====================================
        """)

    pilih = input("pilih menu yang tersedia (1/2/3): ")
    if pilih == "1":
        os.system('cls')
        login_pelanggan()
        bayar()
            
    if pilih == "2":
        os.system('cls')
        login_admin()
        Menu_admin()
    
    elif pilih =="3":
        os.system('cls')
        print("\n\n========== terimakasi telah berkunjung:) ==========\n\n")
        exit()

    else:
        print("menu invalid")

menu_login()