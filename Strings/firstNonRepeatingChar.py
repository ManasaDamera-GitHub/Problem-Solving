# word="swiss"
# freq={}
# for i in word:
#     freq[i]=freq.get(i,0)+1
# for x in range(len(word)):
#     if freq[word[x]]==1:
#         print(x)
#         break
# print(freq)

# Approach2: normal method

word="swiss"
for i in word:
    count=0
    for j in word:
        if i==j:
            count+=1
    if count==1:
        print(word.index(i))
        break