x1, y1, x2, y2 = map(int, input("x1 y1 x2 y2: ").split())

tga = (y2-y1)/(x2-x1)

step_x = 1
if x2 < x1:
    step_x = -1

step_y = 1
if y2 < y1:
    step_y = -1

points = []
for x_c in range(x1+1, x2+1, step_x):
    for y_c in range(y1+1, y2+1, step_y):
        if (y_c-y1)/(x_c-x1) == tga:
            points.append([x_c, y_c])

print(points)