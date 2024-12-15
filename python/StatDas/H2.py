arr = [1,2,5,3,8,5,7,3,7,10]

import  statistics

def jumlah(arr):
    print(sum(arr))
jumlah(arr)
print(sum(arr)/len(arr))
print(statistics.stdev(arr))