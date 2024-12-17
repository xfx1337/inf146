for a in range(1, 1000): # a = min 1000
    flag = 1
    for x in range(1,10000): # x=10a or 100a
        f = (a % 9==0) and ((280%x==0)<=((a%x!=0)<=(730%x!=0)))    # not ВСЕГДА В СКОБКАХ! или ставить !=
        if f == 0:
            flag = 0
            break
    if flag:
        print(a)