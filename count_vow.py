# counting vowel in a string
vowel=["a","e","i","o","u"]
x=input("enter a string")
count=0
for char in vowel:
    if char in x:
        count+=1

print("total vowel in string = ",count)