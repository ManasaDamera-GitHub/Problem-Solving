a=list("Icecream")
vowels="aeiouAEIOU"
left,right=0,len(a)-1
while left<right:
    if a[left] not in vowels:
        left+=1
    if a[right] not in vowels:
        right-=1
    else:
        a[left],a[right]=a[right],a[left]
        left+=1
        right-=1
print("".join(a))