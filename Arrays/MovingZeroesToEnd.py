arr=[1,2,3,0,4,0,5,0,6]
non_zero=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[non_zero]=arr[i]
        non_zero+=1
for i in range(non_zero,len(arr)):
    arr[i]=0
print(arr)