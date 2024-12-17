n = int(input())
dc = {}
for i in range(n):
    word, number = input().split()
    dc[word] = int(number)

text = ""
unique_symbols = []
for word in dc.keys():
    text += word*dc[word]
    for letter in word:
        if letter not in unique_symbols:
            unique_symbols.append(letter)

mx = 0
for s in unique_symbols:
    x = text.count(s)
    if x > mx:
        mx = x

print(mx)