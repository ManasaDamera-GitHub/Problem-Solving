def duplicate_ele(arr):
    dupli=[]
    for i in arr:
        if i not in dupli:
            dupli.append(i)
    print(dupli)
arr=[10, 20, 20, 30, 40, 40, 40, 50, 50]
duplicate_ele(arr)

        