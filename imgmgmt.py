import numpy as np
from polarform import complex2polar

def flatten(ls):
    flat = []
    for r in ls:
        for x in r:
            flat.append(x)
    return flat

def padding(img, pad):
    pad = int(pad /2)
    w = len(img[0])
    h = len(img)
    paddingzero = [0 for _ in range(pad)]
    for row in img:
        for zero in paddingzero:
            row.insert(0, zero)
        row.extend(paddingzero)
    paddingzero = [[0 for _ in range(w + 2 * pad)] for _ in range(pad)]
    
    for row in paddingzero:
        img.insert(0, row)
    img.extend(paddingzero)

def inverse(img):
    return [[255 - pixel for pixel in row] for row in img]

def shift(fourier, x, y):
    w = len(fourier[0])
    h = len(fourier)
    return [[fourier[i][j] * np.exp(-2j*np.pi*((x*j/w)+(y*i/h))) for j in range(w)] for i in range(h)]

def rotate(fourier, deg):
    rad = np.deg2rad(deg)
    return [[pixel['r'] * np.exp(1j*(rad+pixel['angle'])) for pixel in row] for row in fourier]

def toPolarform(z):
    return [[complex2polar(pixel) for pixel in row] for row in z]

def downScale(img, w, h):
    ratio = [len(img[0])/w, len(img)/h]
    return [[img[int(i*ratio[0])][int(j*ratio[1])] for j in range(w)] for i in range(h)]