def dicing_ele(arr):
    dic={}
    for i in arr:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for k in dic:
        if dic[k]!=1:
            print (k)
arr=[10, 20, 40, 30, 50, 20, 10, 20]
dicing_ele(arr)
# print(dicing_ele(arr))