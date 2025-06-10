arr=[3,2,56,27,43,23,77]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)  #[2, 3, 23, 27, 43, 56, 77]

