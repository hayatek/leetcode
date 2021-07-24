x = 101
r = False

if x < 0 or (x % 10 == 0 and x != 0):
    ans = False
else:
    r = 0
    while(x>r):
        r = r * 10 + x % 10
        x = x // 10

print('r is ',True if (x==r or x == r // 10) else False)