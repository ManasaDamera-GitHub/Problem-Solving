def String_to_number(s):
    num=0
    for i in s:
        # converts character to digit
        digit=ord(i)-ord("0")
        if digit< 0 or digit>9:
            return -1
        num=num*10+digit
    return type(num)
print(String_to_number("12"))

        