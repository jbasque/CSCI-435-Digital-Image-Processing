# basic program that opens an image,
# reads its contents and outputs them to a new file

# opens the image file in read mode
with open('lena256_PGM.pgm', 'r') as lena:
    header = next(lena)
    comment = next(lena)
    dimensions = next(lena)
    data = []
    for line in lena:
        data.append([int(x) for x in line.split()])


lenaCOPY = open('lenaCOPY.pgm', 'w')
lenaCOPY.write(header + comment + dimensions)

for sub in data[0:]:
    lenaCOPY.write(str(sub[0]) + '\n')

lena.close()
lenaCOPY.close()
