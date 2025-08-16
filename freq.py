text = input("enter a string")
freq = {}
for i in text:
   freq[i] = freq.get(i, 0) + 1
print(freq)
