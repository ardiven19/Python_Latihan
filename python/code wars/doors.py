n = 9
a = [True] * n
for i in range(2, n+1):
    for j in range(n):
        if (j+1) % i == 0:
            a[j] = False if a[j]  else True
print(a.count(True))