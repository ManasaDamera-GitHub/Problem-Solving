# Approach - 1:
        # a="madam"
        # res=""
        # for i in a:
        #     res=i+res
        # if a==res:
        #     print("Palindrome")
        # else:
        #     print("Not a palindrome")


# Approach - 2:
    # a="madam"
    # for i in range(0,len(a)//2):
    #     if a[i]!=a[len(a)-1-i]:
    #         print("not a palindrome")
    #         break
    # else:
    #     print("Palindrome")


# Approach - 3:
# a="madam"
# # len(a) = 5
# for i in range(len(a)):
#     # i = 0 - a[0] = m
#     # 5-0-1=4 - a[4] = m
#     if a[i] != a[len(a)-1-i]:
#         print("Not a palindrome")
#         break


# Approach - 4: Two pointers method
        # a="madam"
        # left,right=0,len(a)-1
        # while left<right:
        #     if a[left]!=a[right]:
        #         print("Not a palindrome")
        #         break
        #     left+=1
        #     right-=1
        # else:
        #     print("Palindrome")


# Approach - 5: Using slicing
        # a="madam"
        # res=a[::-1]
        # if res==a:
        #     print("Palindrome")
        # else:
        #     print("Not a palindrome")


# Approach - 6: Using reversed function

s="racecar"
def palind(s):
    temp="".join(reversed(s))
    print(temp)
    if s==temp:
        return "true"
    else:
        return "false"
print(palind(s))


        