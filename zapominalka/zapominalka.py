import random

contents = []

with open("wordlist.txt", "r", encoding="utf-8") as f:
    c = f.read()
    c = c.replace("\xad", "") # google docs wtf?
    contents = c.split(";")
    random.shuffle(contents)

for c in contents:
    c = c.split(":")
    print(c[0])
    input("Ответ:")
    print(c[-1])
    input("\nСледующий:")