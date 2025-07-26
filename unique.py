text = input("enter a character")
unique_char = []

for ch in text:
    if text.count(ch) == 1:
        print("unique characters is:",ch)
