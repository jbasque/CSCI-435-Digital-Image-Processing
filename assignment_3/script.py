import numpy as np

data = []
with open('lena256_PGM.pgm','r') as lena:
    header = next(lena)
    comment = next(lena)
    dimensions = next(lena)
    max_value = next(lena)
    for val in lena:
        data.append(int(val))

lena.close()

x_dim = int(dimensions[0:3])
y_dim = int(dimensions[3:len(dimensions)])

data = np.reshape(data, (y_dim, x_dim))

# edge detecting convolution mask (sobel)
mask = [[0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]

output = np.empty((y_dim, x_dim))
output.fill(0)


def calculatePixel(input, x, y):
    sum = 0
    for i in range(-1,2):
        for j in range(-1,2):
            sum += input[y+i][x+j] * mask[i+1][j+1]
    if sum < 0:
        return 0
    elif sum > 255:
        return 255
    else:
        return sum


for y_coord, i in enumerate(data):
    for x_coord, j in enumerate(i):
        if((x_coord > 0 and x_coord < x_dim-1) and (y_coord > 0 and y_coord < y_dim-1)):
            output[y_coord][x_coord] = calculatePixel(data, x_coord, y_coord)
        else:
            output[y_coord][x_coord] = data[y_coord][x_coord]

lena_out = open('lena_out.pgm', 'w')

lena_out.write(header + comment + dimensions + max_value)

for i in output:
    for j in i:
        lena_out.write(str(int(j)) + '\n' )

lena_out.close()
