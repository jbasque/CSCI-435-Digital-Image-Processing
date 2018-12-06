import numpy as np
import matplotlib.pyplot as plt

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


lena.close()

# histogram calculation
pixelCount = np.zeros(256)
pixelProportions = np.zeros(256)

for x in data[0:]:
    pixelCount[x[0]] = pixelCount[x[0]] + 1

for x, val in enumerate(pixelCount):
    pixelProportions[x] = val/(len(data)-1)


# makes the graph that displays the histogram
x = np.arange(256)
plt.grid(axis='y', alpha=.75)
plt.title("Histogram of original lena image")
plt.xlabel('Grayscale Value')
plt.ylabel('Frequency')
plt.bar(x, pixelCount)
plt.show()


# extra credit part d: histogram equalization

# normalizes the image
histSum = 0
pixelProportionsEQ = np.zeros(256)
newImage = []

for x, val in enumerate(pixelProportions):
    histSum += val
    pixelProportionsEQ[x] = histSum

for x, val in enumerate(data):
    newImage.append(255 * pixelProportionsEQ[val[0]])

# outputs eq'd image to new file
lenaEQD = open('lenaEQD.pgm', 'w')
lenaEQD.write(header + comment + dimensions)

for sub in newImage:
    lenaEQD.write(str(int(sub)) + '\n')

# calculates histogram for eq'd image
pixelCount = np.zeros(256)
pixelProportions = np.zeros(256)

for x, val in enumerate(newImage[0:]):
    pixelCount[int(val)] = pixelCount[int(val)] + 1

for x, val in enumerate(pixelCount):
    pixelProportions[x] = val/(len(newImage)-1)


# makes the graph that displays the histogram
x = np.arange(256)
plt.grid(axis='y', alpha=.75)
plt.title("Histogram of equalized lena image")
plt.xlabel('Grayscale Value (eqd)')
plt.ylabel('Frequency')
plt.bar(x, pixelCount)
plt.show()

