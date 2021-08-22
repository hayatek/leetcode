#s = "(]"
#s = "()[]{}" True
#s = "(]" False
#s = "([)]" False
s = "({[]})"

def isValid(s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        print('values=',dict.values())
        for char in s:
            print('stack=',stack)
            print('char=',char)
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

print(isValid(s))