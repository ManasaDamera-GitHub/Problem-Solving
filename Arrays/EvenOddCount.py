arr=[11, 20, 35, 40, 53]
evenC=0
oddC=0
for i in arr:
    if i%2==0:
        evenC+=1
    else:
        oddC+=1
print("Even element count:",evenC)
print("odd element count:",oddC)