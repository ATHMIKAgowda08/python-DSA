def divide_and_conquer(lst):
    if len(lst) <= 1:
        print("Base case:", lst)
        return
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    print("Dividing:", lst)
    divide_and_conquer(left)
    divide_and_conquer(right)

numbers = list(range(1, 17))
divide_and_conquer(numbers)
