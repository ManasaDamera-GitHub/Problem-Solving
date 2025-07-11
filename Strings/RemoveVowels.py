# a="hello world"
# def remove_vowels(a):
#     res=""
#     for char in a:
#         if char not in "aeiouAEIOU":
#             res+=char
#     return res
# print(remove_vowels(a))

# method 2:using replace method
# This method replaces each vowel with an empty string, effectively removing it from the original string.

def Remove_vowels(a):
    for i in a:
        if i.lower() in "aeiou":
            a = a.replace(i, "")
            return a
print(Remove_vowels("manasa"))


# method3:# This method iterates through each character in the string and constructs a new string without vowels.

a="hello world"
for i in a:
    if i not in "aeiouAEIOU":
        print(i,end="")
