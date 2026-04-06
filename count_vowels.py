set_vowel= {'a','e','i','o','u'}
count = 0
string = input()
for i in string:
    if i in set_vowel:
        count+=1
print(count)
