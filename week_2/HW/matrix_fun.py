values = input("Please input matrix values separated by spaces (e.g. 1 2 3 4): ").split(" ")

# input matrix
mRow1 = tuple([float(values[0]), float(values[1])])
mRow2 = tuple([float(values[2]), float(values[3])])
m = (mRow1, mRow2)
print("Input matrix:",m)

# inverse matrix
b = ((m[0][0] * m[1][1]) - (m[0][1] * m[1][0]))
if b == 0:
    print("Matrix", m, "cannot be inverted.")
else:
    a = 1/b
    iRow1 = tuple([a * m[1][1], -1 * a * m[0][1]])
    iRow2 = tuple([-1 * a * m[1][0], a * m[0][0]])
    inverse = tuple([iRow1, iRow2])
    print("Inverted matrix:", inverse)
