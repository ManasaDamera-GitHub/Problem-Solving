# Input : arr[5][2] = {{10,20}, {30,40}, {50,60}, {20,10}, {40,30}, {90, 100}, {1, 9}, {100, 90}}
# Output : (10,20) (30,40) (90, 100)
# print the pairs(x,y) that have present in the array as (y,x)

arr = ((10,20), (30,40),(50,60), (20,10), (40,30),(90, 100), (1, 9), (100, 90))
s=set()
for (x,y) in arr:
    s.add((x,y))
    if (y,x) in s:
        print((y,x))

