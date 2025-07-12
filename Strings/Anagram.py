word1,word2="listen", "silent"
if len(word1)!=len(word2):
    print("not an anagram")
else:
    word1=sorted(word1)
    word2=sorted(word2)
    if word1==word2:
        print("anagram")


# Approach2: using dictionary

# word1,word2="listen", "silent"
# if len(word1)!=len(word2):
#     print("not an anagram")
# count1,count2={},{}
# for i in range(len(word1)):
#     count1[word1[i]]=1+count1.get(word1[i],0)
#     count2[word2[i]]=1+count2.get(word2[i],0)
# for c in count1:
#     if count1[c]!=count2.get(c,0):
#         print(False)
#         break
#     print(True)
#     break
    

