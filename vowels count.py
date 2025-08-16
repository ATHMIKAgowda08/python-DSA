text = input("enter a string")
vowels = 0
consonents = 0
for char in text:
    if char.lower() in 'aeiou':
        vowels+=1
    elif char.isalpha():
        consonents+= 1
print("vowels:", vowels)
print("consonents:", consonents)
