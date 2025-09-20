def is_balanced(expression):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()

    return len(stack) == 0
test_cases = [
    "({[]))"]  # Balanced

for expr in test_cases:
    result = "Balanced" if is_balanced(expr) else "Not Balanced"
    print(f"{expr:10} → {result}")

