print("w x y z | F")
s = [0, 1]
for w in s:
    for x in s:
        for y in s:
            for z in s:
                st = (not (y <= (x == w))) * (z <= x)
                print(f"{w} {x} {y} {z} | {st}")