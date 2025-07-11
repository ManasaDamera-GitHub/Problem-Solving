# course="Fullstack developer"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())
# print(course[0:5])
# print(course[-1:3])

import math
print(ord("A"))
print(abs(-2.5))
print(round(2.5))
print(math.ceil(2.1))
res="big" > "apple" 

#In Python, strings are compared lexicographically, meaning character by character using their Unicode (ASCII) values.
#Let's analyze:
#"bag" > "apple"
#Compare character by character:
#First letters:
#'b' → Unicode value is 98
#'a' → Unicode value is 97
#Since 98 > 97, "bag" > "apple" is True.
#Python stops comparing as soon as it finds the first pair of characters that are not equal. So even though "apple" has more characters, it doesn't matter here.
#Summary:
#python
#print("bag" > "apple")  # True
#✅ Because 'b' > 'a' → 98 > 97
#Let me know if you want to see this for other examples or with sort() behavior.

print(res)