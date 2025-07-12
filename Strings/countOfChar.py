s="aabcccccaaa"
freq={}
for i in s:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
for key ,value in freq.items():
    print(f"{key}{value}",end="")

#  output="a5b1c5"      