import copy
import random
def menu():
    global nilai, game, menang, kalah
    print('menu game')
    print(f'NILAI SAYA: {nilai}',f'\nMenang {menang}', f'\nKalah: {kalah}', f'\nTotal Game: {menang+kalah}')
    print('1. tebak biner dari angka')
    print('2. tebak angka dari biner')
    print('3. tebak hexa dari biner')
    print('4. tebak biner dari hexa')
    print('0. keluar')
    x = int(input('pilih menu: '))
    if x == 1:
        gameNTB()
    elif x == 2:
        gameBTN()
    elif x == 3:
        gameBTH()
    else:
        game = False
def create(angka):
    hasil = []
    for i in range(len(default)):
        if default[i] <= angka:
            angka -= default[i]
            hasil.append(1)
        else:
            hasil.append(0)
    return hasil
def Jawaban(jawaban, kunci):
    global menang, kalah
    if jawaban == kunci:
        print('Benar')
        menang += 1
    else:
        print('Salah, jawaban yang benar adalah', kunci)
        kalah += 1
def gameBTN():
    global default, menang, kalah
    angka = angkarandom()
    kunci = copy.deepcopy(angka)
    hasil = create(angka)
    for j in hasil:
        print(j, end=" ")
    jawaban = int(input('\nMasukan jawabannya: '))
    Jawaban(jawaban, kunci)
def gameNTB():
    global default, menang, kalah
    angka = angkarandom()
    print('angkanya adalah:', angka)
    hasil = create(angka)
    kunci = ''
    for k in hasil:
        kunci += str(k)
    jawaban = input('Masukan jawabannya tanpa spasi: ')
    Jawaban(jawaban, kunci)
def gameBTH():
    global default_hex, menang, kalah, huruf_hex
    angka = angkarandom()
    hasil = create(angka)
    tes = []
    for j in range(3, len(hasil)):
        tes.append(hasil[j])
        hasil.pop(j)
    kunci = ''
    tes_angka1 = 0
    tes_angka2 = 0
    for i in range(len(default_hex)):
        if default_hex[i] <= angka:
            tes_angka1 += default_hex
        




def angkarandom():
    return random.randrange(1, 255)
game = True
default = [128, 64, 32, 16, 8, 4, 2, 1]
default_hex = [8, 4, 2, 1]
huruf_hex = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
menang = 0
kalah = 0
nilai = 0
while(game):
    if menang + kalah != 0:
        nilai = (menang / (menang + kalah) * 100)
    menu()