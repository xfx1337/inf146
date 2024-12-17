x1, y1, x2, y2 = map(int, input("x1 y1 x2 y2: ").split())

def get_func(x1, y1, x2, y2):
    b = y1
    x2 = x2 - x1
    x1 = 0
    y2 = y2 - y1
    y1 = 0
    return {"k": y2/x2, "b": b}

step_x = 1
if x2 < x1:
    step_x = -1

step_y = 1
if y2 < y1:
    step_y = -1

func = get_func(x1, y1, x2, y2)
print(func)
points = []
for x_c in range(x1, x2+1, step_x):
    for y_c in range(y1, y2+1, step_y):
        if func["k"] * x_c + func["b"] == y_c:
            points.append([x_c, y_c])

print(points)