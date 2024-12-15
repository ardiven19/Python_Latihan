import math

n = 1000
def is_palindrome(number):
    s = str(number)
    return s == s[::-1]



a = set()
for i in range(1, int(math.sqrt(n))):
    count = 0
    for j in range(i + 1, int(math.sqrt(n))):
        count = (((j * (j + 1) * (2 * j + 1)) // 6) - (((i - 1) * i * (2 * i - 1)) // 6))
        if count > n:
            break
        if is_palindrome(count):
            a.add(count)

print(len(set(a)))
