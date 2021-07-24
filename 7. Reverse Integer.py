x = 123
ans = 0
while x:
    temp = ans * 10 + x % 10
    if temp // 10 != ans:
        rev = 0
        break
    ans = temp
    x //= 10
print(f'ans is {ans}')