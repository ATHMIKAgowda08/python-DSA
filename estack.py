stack = []

def push():
    element = input("Enter element to push: ")
    stack.append(element)
    print(f"{element} pushed to stack")

def pop():
    if not stack:
        print("Stack Underflow! Nothing to pop.")
    else:
        popped = stack.pop()
        print(f"Popped element: {popped}")

def display():
    if not stack:
        print("Stack is empty")
    else:
        print("Stack elements from top to bottom:")
        for i in reversed(stack):
            print(i)

# Menu-driven program
while True:
    print("\nOptions: 1.Push  2.Pop  3.Display  4.Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1-4.")
