# output: "world hello"
# This code reverses the order of words in a given string.
# It handles leading and trailing spaces, as well as multiple spaces between words.
# Example input: " hello world"
# Example output: "world hello"
# Note: The input string is stripped of leading and trailing spaces before processing

s=" hello world"
s=s.strip()
words=[]
word=""
for char in s:
    if char!=" ":
        word+=char
    elif word:
        words.append(word)
        word=""
if word:
    words.append(word)
print(" ".join(words[::-1]))