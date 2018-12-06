import numpy as np
import math

# opens the image and reads the contents into a list
with open('lena256_PGM.pgm', 'r') as lena:
    header = next(lena)
    comment = next(lena)
    dimensions = next(lena)
    max_value = next(lena)
    data = []
    for val in lena:
        data.append(int(val))
    lena.close()

# dimensions of the input image
rows = int(dimensions[0:3])
cols = int(dimensions[3:len(dimensions)])
data = np.reshape(data, (rows, cols))

# scale factor for output image size
scale_factor = 3
out_rows = int(rows * scale_factor)
out_cols = int(cols * scale_factor)

# functions for inverse mapping
def inverse_map_a(u):
        return u/scale_factor

def inverse_map_b(v):
        return v/scale_factor

# interpolation function that calculates the pixel value based on four locations
# uses the backwards mapping nearest neighbor approach
def interpolate(u, v):
    x = 0
    y = 0

    x = round(u)
    y = round(v)

    if u > len(data) - 1:
        x = len(data) - 1
    if v >= len(data[x]) - 1:
        y = len(data[x]) - 1

    return data[x][y]

# loops though the output image and maps a pixel to spcific pixels in the input image
output = np.zeros((out_rows, out_cols))
for i in range(0, out_rows):
    for j in range(0, out_cols):
        a = inverse_map_a(i)
        b = inverse_map_b(j)
        output[i][j] = interpolate(a, b)

# wtiting the output data to a file
lena_out = open('lena768_PGM.pgm', 'w')

lena_out.write(header + comment + str(out_rows) + ' ' + str(out_cols) + '\n' + max_value)

for i in output:
    for j in i:
        lena_out.write(str(int(j)) + '\n')

lena_out.close()
