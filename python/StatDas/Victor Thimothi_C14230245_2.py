# tujuannya adalah memindahkan semua cakram ke tiang tujuan
def TowerOfHanoi(n, tiang_asal, tiang_tujuan, tiang_pembantu):
    # base case dimana jika cakram yang mau dipindahkan cakram 1 atau yang paling kecil
    # maka langsung akan dipindahkan ke tujuannya tanpa ke tiang pembantu dulu
    if n == 1:
        print("Move disk 1 from source", tiang_asal, "to destination", tiang_tujuan)
        return
    # akan memindahkan cakram diatas cakram ke n contohnya n = 4 makan cakram ke 1-3 akan dipindahkan ke tiang pembantu lalu cakram ke 4 dipindahkan ke tujuan
    # lalu cakram 1-3 dipindahkan lagi ke tujuan cakram kee 4
    # tapi cara mindahin cakram 1 - 3 sama juga seperti caranya cakram ke 4
    # mindahin cakram diatasnya dulu 1-2 lalu mindahin cakram 3 ke tujuan lalu mindahin lagi ke tujuannya cakram ke 3
    # sampai jika cakram yang pindah itu cakram 1 maka akan langsung dipindahkan.
    TowerOfHanoi(n - 1, tiang_asal, tiang_pembantu, tiang_tujuan) # ini untuk pemindahan cakram diatas cakram ke n ke tiang bantuan
    print("Move disk", n, "from source", tiang_asal, "to destination", tiang_tujuan) # ini pemindahan cakram ke n ke tujuan
    TowerOfHanoi(n - 1, tiang_pembantu, tiang_tujuan, tiang_asal) # ini pemindahan cakran diatas ke n ke tujuan



# Driver code
n = int(input("masukan jumlah cakram: "))
TowerOfHanoi(n, 'A', 'C', 'B')

