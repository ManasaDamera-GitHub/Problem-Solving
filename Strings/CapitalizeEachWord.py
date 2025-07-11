# Approach1 : using split and join

# a="hello world".split(" ")
# res=[]
# for word in a:
#     if word:
#         res.append(word[0].upper()+word[1:].lower())
# print(" ".join(res))
        
# Approach2 : using title() method

a="hello world"
print(a.title())

# Approach3 : normal approach
a="The quick brown fox jumps over the lazy dog"
result=""
is_new_word=True
for char in a:
    if char.isalpha() and is_new_word:
        result+=char.upper()
        is_new_word=False
    elif char==" ":
        result+=char
        is_new_word=True
    else:
        result+=char
print(result)
        


        
