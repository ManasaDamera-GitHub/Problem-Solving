arr=[-6,-4,0,1,3,7]
# arr=[10, 3, 5, 6, 20]
def find_max(arr):
    arr.sort()
    max_pro=arr[-1]*arr[-2]*arr[-3]   
    temp=arr[0]*arr[1]*arr[-1]
    if temp>max_pro:
        return temp
    return max_pro
print(find_max(arr))  