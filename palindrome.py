s = input("enter a string")
s= s.replace(" ", "").lower()
if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("the string is not a palindrome")
