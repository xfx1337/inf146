d = [0,1]

print("w x y z | F")

for w in d:
    for x in d:
        for y in d:
            for z in d:
                st = int(( (w) or (y <= z) and x ))
                print(f"{w} {x} {y} {z} | {st}")