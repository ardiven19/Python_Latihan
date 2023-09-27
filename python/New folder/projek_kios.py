import sys
import sqlite3


def menu_awal():
    print("1. belanja")
    print("2. tambah barang")
    print("3. ubah harga")
    print("4. hapus barang")
    print("5. daftar barang")
    print("6. tutup")
    print("masukan no menu")
    no_menu = int(input())
    if no_menu == 1:
        menu_belanja()
    elif no_menu == 2:
        menu_tambah()
    elif no_menu == 3:
        menu_ubah()
    elif no_menu == 4:
        menu_hapus()
    elif no_menu == 5:
        menu_daftar()
    elif no_menu == 6:
        SystemExit
    else:
        print("404 not found")

def menu_belanja():
    kon = sqlite3.Connection('data.db')
    cur = kon.cursor()
    cur.execute('SELECT * FROM my_table')
    data_harga = dict(cur.fetchall())
    a = 0
    hasil = []
    while a < 100:
        masuk = input()
        if masuk == "sudah":
            break
        hasil.append(masuk)
        a += 1
    hasil_akhir = []
    for key in hasil:
        nilai = int(data_harga.get(key))
        if nilai != None:
            hasil_akhir.append(nilai)
    total = int(sum(hasil_akhir))
    print("total pembeliannya adalah Rp." + str(total))
    print("masukan uang yang diterima")
    uang = int(input())
    kembalian = uang - total
    print("uang kembalian adalah Rp." + str(kembalian))
    cur.close()
    kon.close()
    print()
    print()
    menu_awal()

def menu_tambah():
    kon = sqlite3.Connection('data.db')
    cur = kon.cursor()
    x = input("nama barang =  ")
    y = input("harga =  ")
    tambah = {}
    tambah[x] = (y)
    for key, value in tambah.items():
        cur.execute('INSERT INTO my_table (key, value) VALUES (?, ?)', (key, value))
    kon.commit()
    cur.close()
    kon.close()
    print()
    print()
    menu_awal()
    return

def menu_ubah():
    kon = sqlite3.Connection('data.db')
    cur = kon.cursor()
    x = input("nama barang =  ")
    y = int(input("harga barang =  "))
    tambah = {}
    tambah[x] = (y)
    for key, value in tambah.items():
        cur.execute('REPLACE INTO my_table (key, value) VALUES (?, ?)', (key, value))
    kon.commit()
    cur.close()
    kon.close()
    print()
    print()
    menu_awal()

def menu_hapus():
    kon = sqlite3.Connection('data.db')
    cur = kon.cursor()
    barang = input("nama barang ")
    cur.execute('DELETE FROM my_table WHERE key = ?', (str(barang),))
    kon.commit()
    cur.close()
    kon.close()
    print()
    print()
    menu_awal()

def menu_daftar():
    kon = sqlite3.connect("data.db")
    cur = kon.cursor()
    cur.execute('SELECT key FROM my_table')
    loaded_dict = list(cur.fetchall()) 
    loaded = sorted(loaded_dict)
    print(loaded)   
    kon.commit()
    cur.close()
    kon.close()
    print()
    print()
    menu_awal()
     
if __name__ == "__main__":
    menu_awal()