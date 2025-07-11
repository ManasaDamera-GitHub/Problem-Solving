# sort the first array in ascending order
# sort the second array in descending order
# find product of two arrays



arr1=[10, 30, 40, 20]
arr2=[2, 4, 5, 1]
for i in range(len(arr1)):
    for j in range(i+1,len(arr1)):
        if arr1[i]>arr1[j]:
            arr1[i],arr1[j]=arr1[j],arr1[i]
for i in range(len(arr2)):
    for j in range(i+1,len(arr2)):
        if arr2[i]<arr2[j]:
            arr2[i],arr2[j]=arr2[j],arr2[i]
product=0
for i in range(len(arr1)):
    product+=arr1[i]*arr2[i]
print(product)
    