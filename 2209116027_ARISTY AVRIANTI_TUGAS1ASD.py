# Nama          : Aristy Avrianti
# NIM           : 2209116027
# Kelas         : Sistem Informasi'A (A2)
# Judul Tema    : Penjualan Tiket Pesawat

from prettytable import PrettyTable
tabel = PrettyTable()
import os
import sys

admin = {"username" : ["admin"],
        "password" : ["aristy"]}
        
Bunga = {"Nama Bunga" : ["lily", "melati", "anggrek", "mawar"],
        "Harga" : ["56000", "65000", "35000", "43000"],
        "Stok" : ["5", "2", "3", "5"]}

tabel_bunga = PrettyTable()
tabel_admin = PrettyTable()
tabel_bunga.field_names = ["Nama Bunga", "Harga", "Stok"]

def menu():
    tabel_bunga.clear_rows()
    for i in range(len(Bunga["Nama Bunga"])):
        tabel_bunga.add_row([Bunga["Nama Bunga"][i],Bunga["Harga"][i],Bunga["Stok"][i]])
    print(tabel_bunga)

def login_admin():
    while True:
        username = input("Input Username: ")
        password = input ("Input Password : ")
        try:
            login = admin.get("username").index(username)
            if username == admin.get("username")[login] and password == admin.get("password")[login]:
                os.system('cls')
                print("Login Succesfully.")
                break
            else:
                print("Passsword tidak ditemukan")
        except ValueError:
            print("Username tidak ditemukan")    

def menu_admin():
    a = "y"
    while (a =="y"): 
        print("Welcome, Aristy! Please select the option :")
        print(" Menu ".center(60, "="))
        print(""" In this section, you can select the main menu, 
        it able to add, delete, show, or update the item.
    1. Tambah Item
    2. Hapus Item
    3. Tampilkan Item
    4. Update Item
    5. Keluar.
     """)
        try :
            pilih = input("Silahkan pilih menu (1/2/3/4) : ")
            if pilih == "1":
                    os.system("cls")
                    print("Berikut menu nya : ")
                    menu()
                    bunga1()
                    a = str(input("Apakah Anda ingin kembali ke menu? (y/n):"))
            elif pilih =="2":
                    os.system("cls")
                    print("Berikut menu nya :")
                    bunga2()
                    a = str(input("Apakah Anda ingin kembali ke menu? (y/n):"))
            elif pilih =="3":
                    os.system("cls")
                    print("Berikut menu nya :")
                    menu()
                    a = str(input("Apakah Anda ingin kembali ke menu? (y/n):"))
            elif pilih == "4":
                    os.system("cls")
                    print("Berikut menu nya :")
                    bunga3()
                    a = str(input("Apakah Anda ingin kembali ke menu? (y/n):"))
            elif pilih == "5":
                    print("Terimakasih.")
                    sys.exit()
            else :
                if a == "n":
                    sys.exit()
                else :
                    print("Gagal.")
        except ValueError:
            os.system("cls")

def update(find_fc,bgmodify,bg_price):
     Bunga.get("Harga")[find_fc] = bg_price
     Bunga.get("Stok")[find_fc] = bgmodify

def bunga1():
    while True:
            bg = input("Masukkan nama bunga baru : ")
            if bg in Bunga.get("Nama Bunga"):
                print("Nama bunga sudah tersedia, silahkan coba lagi.") 
                menu()
            else:
                hr = input("Masukkan harga terbaru :")
                sk = input("Masukkan stok terbaru  : ")    
                Bunga.get("Nama Bunga").append(bg)
                Bunga.get("Harga").append(hr)
                Bunga.get("Stok").append(sk)
                tabel.add_row([bg, hr, sk])
                menu()
                break
                 

def bunga2():
    menu()
    bgdelete = input("Masukkan nama bunga yang ingin dihapus : ")
    for i in Bunga["Nama Bunga"]:
        if bgdelete == i:
            find_bg = Bunga.get("Nama Bunga").index(bgdelete)
            if bgdelete == Bunga.get("Nama Bunga")[find_bg]:
                Bunga.get("Nama Bunga").pop(find_bg)
                Bunga.get("Harga").pop(find_bg)
                Bunga.get("Stok").pop(find_bg)
                os.system('cls')
                print("Nama Bunga sudah berhasil dihapus")
                menu()
                break
        else:
            print("Nama bunga tidak dapat ditemukan.")
            menu()
            break

def bunga3():
    while True :
        try :
            menu()
            bgupdate = input("Masukkan nama bunga yang ingin anda ubah: ") 
            bgmodify = input("Masukan jumlah stok: ")

            find_fc = Bunga.get("Nama Bunga").index(bgupdate)
            if Bunga.get("Nama Bunga")[find_fc] == bgupdate:
                bg_price = input("Masukkan  Harga baru : ")
                update(find_fc, bgmodify, bg_price)
                menu()
                print("Data bunga anda telah diganti.")
        except ValueError:
             print("Nama bunga tidak ditemukan.")

print(" LOGIN ".center(60, "="))
login_admin()
os.system('cls')
menu_admin()


        
