inst = list(input())
words = []

def test(word):
    if len(word) == len(inst):
        if word not in words:
            words.append(word)
            print("".join(word))
        return
    for i in range(len(inst)):
        x = word.copy()
        if inst[i] not in word:
            x.append(inst[i])
            test(x)

test([])