import math
while True:
    #menu
    print("0. KELUAR")
    print("1. HITUNG VOLUME BALOK")
    print("2. HITUNG VOLUME BOLA")
    print("3. HITUNG VOLUME KERUCUT")
    print("4. HITUNG VOLUME SILINDER")
    print("5. HITUNG VOLUME LIMAS SEGITIGTA")

    #inputan untuk memilih menu
    key = int(input("MASUKAN PILIHAN ANDA : "))

    #menu ke-1 menerima inputan panjang, lebar, dan tinggi dan akan menampilkan volume balok
    if (key == 1):
      panjang = int(input("Masukan panjang balok: "))
      lebar  = int(input("Masukan lebar balok: "))
      tinggi = int(input("Masukan tinggi balok: "))
      volume = panjang*lebar*tinggi
      print("Volume balok adalah ", volume)

    # menu ke-2 menerima inputan jari-jari bola dan akan menampilkan volume dari bola
    elif (key == 2):
        jari_jari = int(input("Masukan jari-jari bola: "))
        volume = 4/3*math.pi*jari_jari*jari_jari*jari_jari
        print("volume bola adalah ", volume)

        # menu ke-3 menerima inputan jari-jari dan tinggi lalu akan menampilkan volume kerucut
    elif (key == 3):
        jari_jari = int(input("Masukan jari-jari kerucut: "))
        tinggi = int(input("Masukan tinggi kerucut: "))
        luas_alas = math.pi * jari_jari*jari_jari
        volume = 1/3 *luas_alas*tinggi
        print("Volume kerucut adalah ", volume)

        # menu ke-4 menerima inputan jari-jari dan tinggi lalu akan menampilkan volume silinder
    elif (key == 4):
        jari_jari = int(input("Masukan jari-jari silinder: "))
        tinggi = int(input("Masukan tinggi silinder: "))
        volume = math.pi*jari_jari*jari_jari*tinggi
        print("Volume silinder adalah ", volume)

        # menu ke-5 menerima inputan alas segitiga, tinggi segitiga dan tinggi limas
        #lalu akan menampilkan volume limas segitiga dengan menghitung menghitung luas alas terlebih dahulu
    elif (key == 5):
        alas_segitiga = int(input("Masukan panjang alas segitiga: "))
        tinggi_segitiga = int(input("Masukan tinggi alas segitiga: "))
        tinggi_limas = int(input("Masukan tinggi limas: "))
        luas_alas = 1 / 2 * alas_segitiga * tinggi_segitiga
        volume = 1/3 *luas_alas*tinggi_limas
        print("Volume limas segitiga adalah ", volume)

        # menu ke-0 akan menampilkam kata terima kasih dan menghentikan loop while dengan break
    elif (key == 0):
        print("TERIMA KASIH")
        break
    # untuk menangani inputan angka diluar nomer menu
    else:
        print("INPUTAN YANG DIMASUKAN TIDAK TEPAT")