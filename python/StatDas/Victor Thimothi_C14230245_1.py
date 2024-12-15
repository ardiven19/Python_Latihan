def faktorial(n, k):
    # base case jika n = 1 akan print n dan return 1 / n
    if (n == 1):
        print(n)
        return n
    #disini akan print n untuk menampilkan urutan faktorial
    print(n,end='x')
    #disini rekursinya akan memanggil dirinya dengan n-1 dan k/k lalu dikalikan dengan n
    #setelah itu akan dibagi dengan k dan karena saat memanggil method nya yang kedua menjadi k/k
    #sehingga pembagian k akan menjadi 1 terus di pemanggilan method ke 2 dan seterusnya
    #hanya saat di pemanggilan pertama k nya bernilai sama contohnya 2
    return (n * faktorial(n-1, k/k)) / k

print(faktorial(5,2))
