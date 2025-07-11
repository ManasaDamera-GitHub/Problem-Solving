# Approach 1: Using Slicing
        # a="hello"
        # res=a[::-1]
        # print(res)

# Approach 2: Using a loop

        # a="Hello"
        # for i in range(len(a)-1,-1,-1):
        #     print(a[i],end="")

#Approach 3: Using 2pointers
        # a="hello"
        # left,right=0,len(a)-1
        # while left<right:
        #     a[left],a[right]=a[right],a[left]
        #     left+=1
        #     right-=1
        # print(a)

# Approach 4: Using reverse() and join() method

a="hello"
print("".join(reversed(a)))


