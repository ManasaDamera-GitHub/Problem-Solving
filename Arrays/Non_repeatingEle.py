def non_repeat_ele(arr):
    non_repeat={}
    for i in arr:
        if i in non_repeat:
            non_repeat[i]+=1
        else:
            non_repeat[i]=1
    for i in non_repeat:
        if non_repeat[i]==1:
            print(i)
arr=[10, 20, 70, 90, 80, 20, 10, 20]
non_repeat_ele(arr)