n = 6

a = b = 1
for _ in range(n):
    a, b = b, a + b

print("ans=",a)