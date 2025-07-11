a="The quick brown fox jumps over the lazy dog"
longest=""
current=""
for char in a:
    if char!=" ":
        current+=char
    else:
        if len(current)>=len(longest):
            longest=current
        current=""
if len(current)>len(longest):
    longest=current
print(longest)

# Approach2: # Using split() method to break the string into words and then finding the longest word.

    # a="The quick brown fox jumps over the lazy dog".split()
    # big=a[0]
    # for i in range(1,len(a)):
    #     if len(big)<=len(a[i]):
    #         big=a[i]
    # print(big)
        
    

        


        