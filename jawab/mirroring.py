import numpy as np
import imageio as img
import matplotlib.pyplot as plt

path = 'C:\\Users\\User\\Documents\\SEMESTER 5\\Pengolahan Citra Digital\\TUGAS_PRAKTIKUM\\img\\jaguar.jpg'
image = img.imread(path)

height, width = image.shape[:2]

horizontal = np.zeros_like(image)
vertical = np.zeros_like(image)
both_mirrored = np.zeros_like(image)

for y in range(height):
    for x in range(width): 
        horizontal[y, x] = image[y, width - 1 - x]

for y in range(height): 
    for x in range(width):
        vertical[y, x] = image[height - 1 - y, x]

for y in range(height): 
    for x in range(width):
        both_mirrored[y, x] = image[height - 1 - y, width - 1 - x]

plt.figure(figsize=(15, 5))

plt.subplot(1, 4, 1)
plt.title("Original")
plt.imshow(image)

plt.subplot(1, 4, 2)
plt.title("Horizontal Mirroring")
plt.imshow(horizontal)

plt.subplot(1, 4, 3)
plt.title("Vertical Mirroring")
plt.imshow(vertical)

plt.subplot(1, 4, 4)
plt.title("Both Mirrored")
plt.imshow(both_mirrored)

plt.show()