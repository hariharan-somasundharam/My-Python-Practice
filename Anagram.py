def isAnagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
str1 = input("String 1 : ")
str2 = input("String 2 : ")
print("Is Anagram : ", isAnagram(str1,str2))

# String 1 : HariHaranS
# String 2 : HaranHariS
# Is Anagram :  True
