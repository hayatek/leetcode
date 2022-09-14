def romanToInt(s: str) -> int:
    list_s = list(s)
    output = 0

    for char in s[:-1]:
        print(char)

    # for i in range(len(list_s)):
    #     if list_s[i] == 'I':
    #         if list_s[i+1] == 'V':
    #             output = output + 4
    #             i += 1
    #         output += 1
    #     if list_s[i] == 'V':
    #         output = output + 5
    #     if list_s[i] == 'L':
    #         output = output + 10
    #     if list_s[i] == 'C':
    #         output = output + 100
    #     if list_s[i] == 'D':
    #         output = output + 500
    #     if list_s[i] == 'M':
    #         output = output + 1000

    # print(output)


romanToInt('IVXXVV')
