# simple program that subtracts one image from another
data = []
data_block = []

with open('lena256_PGM.pgm','r') as lena, open('lena256_block.pgm','r') as lena_block:
    header = next(lena)
    comment = next(lena)
    dimensions = next(lena)
    max_value = next(lena)
    header_block = next(lena_block)
    comment_block = next(lena_block)
    dimensions_block = next(lena_block)
    max_value_block = next(lena_block)
    for val in lena:
        data.append(int(val))
    for val in lena_block:
        data_block.append(int(val))

lena.close()
lena_block.close()


data_output = []

for i, j in zip(data, data_block):
    if i - j <= 0:
        data_output.append(0)
    else:
        data_output.append(i-j)


lena_output = open('lena_output.pgm', 'w')
lena_output.write(header + comment + dimensions + max_value)

for i in data_output:
    lena_output.write(str(i) + '\n')

lena_output.close()
