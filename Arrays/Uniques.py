def Uniques(arr):
    uni=[]
    for i in arr:
        if i not in uni:
            uni.append(i)
    # Sorting
    for i in range(len(uni)):
        for j in range(i+1,len(uni)):
            if uni[i]>uni[j]:
                uni[i],uni[j]=uni[j],uni[i]
    return len(uni)
arr=[10,50,20,30,20,40,20,10]
print(Uniques(arr))

