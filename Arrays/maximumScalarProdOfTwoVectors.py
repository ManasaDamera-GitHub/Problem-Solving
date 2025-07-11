# find sort of first array and second array in ascending order then multiply them

arr1=[10, 30, 40, 20]
arr2=[2, 4, 5, 1]
n=len(arr1)
for i in range(n):
    for j in range(i+1,n):
        if arr1[i]>arr1[j]:
            arr1[i],arr1[j]=arr1[j],arr1[i]
for i in range(n):
    for j in range(i+1,n):
        if arr2[i]>arr2[j]:
            arr2[i],arr2[j]=arr2[j],arr2[i]
product=0
for i in range(n):
    product+=arr1[i]*arr2[i]
print(product)