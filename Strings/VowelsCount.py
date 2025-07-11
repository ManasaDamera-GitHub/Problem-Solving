# a="Hello World"   
# def count_vowels(a):
#     vowels="aeiouAEIOU"
#     count=0
#     for char in a:
#         if char in vowels:
#             count+=1
#     return count
# print(count_vowels(a))

# Approach : using 2 pointers method
def count_vowels_two_pointers(a):
    vowels = "aeiouAEIOU"
    left, right = 0, len(a) - 1
    count = 0
    
    while left <= right:
        if a[left] in vowels:
            count += 1
        if left != right and a[right] in vowels:
            count += 1
        left += 1
        right -= 1
    
    return count

print(count_vowels_two_pointers("manasa"))