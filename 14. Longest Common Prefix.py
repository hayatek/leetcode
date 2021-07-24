strs = ["flower","flow","flight"]
o = ''

str_min = min(strs, key=len)
min_i = strs.index(str_min)
f = strs.pop(min_i)
strs_len = len(strs)
counter = 0
for i in reversed(range(len(str_min) + 1)):
    for s in strs:
        if s.startswith(str_min[:i]):
            counter += 1
        else:
            print('o=',o)
            break
    if counter == strs_len:
        o = str_min[:i]
        print('o=',str_min[:i])
        break
    counter = 0