word = list(input())

def my_count_word(new_wordx):
    if len(new_wordx) == len(word):
        print("".join(new_wordx))
        return
    for i in word:
        new_wordx = new_wordx.copy()
        if i not in new_wordx:
            new_wordx.append(i)
            my_count_word(new_wordx.copy())
    

# new_word = []
# for o in range(len(word)):
#     new_word.append(word[o])
#     count_word(new_word.copy())

my_count_word([])