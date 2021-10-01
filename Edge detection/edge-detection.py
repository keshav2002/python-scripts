from PIL import Image
import numpy as np
import math

img = Image.open('./cameraman.tif')

w, h = img.size

H = 1

I = np.empty(shape=(w, h))
I.fill(0)

dx = np.empty(shape=(w, h))
dx.fill(0)

dy = np.empty(shape=(w, h))
dy.fill(0)

edge = np.empty(shape=(w, h))
edge.fill(0)

for i in range(w):
    for j in range(h):
        I[i, j] = img.getpixel((j, i))

original_img = Image.fromarray(I)
original_img.show()

for i in range(w-1):
    for j in range(h-1):
        dx[i, j] = I[i, j+H] - I[i, j]

grad_x = Image.fromarray(dx)
grad_x.show()

for i in range(w-1):
    for j in range(h-1):
        dy[i, j] = I[i+H, j] - I[i, j]

grad_y = Image.fromarray(dy)
grad_y.show()

for i in range(w-1):
    for j in range(h-1):
        edge[i, j] = math.sqrt((dx[i, j]) ** 2 + (dy[i, j]) ** 2)

detected_edges = Image.fromarray(edge)
detected_edges.show()

new_I = img.convert("L")
new_grad_x = grad_x.convert("L")
new_grad_y = grad_y.convert("L")
new_detected_edges = detected_edges.convert("L")

new_I.save('original-image.png')
new_grad_x.save('forward-diff-x.png')
new_grad_y.save('forward-diff-y.png')
new_detected_edges.save('detected-edges.png')
