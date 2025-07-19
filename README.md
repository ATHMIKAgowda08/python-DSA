number = [1,2,3,4,5]
print("The first number is", number[0])
print("The last number is", number[-1])
print("all elements using loop",number)
for num in (number):
    print(num, end=' ')
print("reversed list using slice")
print(number[::-1])
