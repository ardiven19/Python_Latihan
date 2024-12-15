def cek_duplikat(x):
    tes = []
    for i in range(len(x)):
        tes.append(x[i])
    tes_akhir = list(set(tes))
    if (len(tes_akhir) == len(tes)):
        return True


angka = int(input())
awal1 = 1234
awal2 = 1234
for i in range(awal1, 100000):
    for j in range(awal2, 100000):
        cek = str(j)+str(i)
        if (j<i or j/i >62 or j/i<62):
            continue

        if (cek_duplikat(str(cek))):
            if (int(j/i) == 62 and j%i == 0):
                print(f"{j}/{i}={angka}")
