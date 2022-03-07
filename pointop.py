import numpy as np
import math

def contrastStretching(img):
    imgCopy = np.array(img.copy())
    flatImg = imgCopy.flatten()
    min_gray = min(flatImg)
    diff_gray = max(flatImg) - min_gray
    w, h = imgCopy.shape
    for r in range(h):
        for c in range(w):
            img[r][c] = int((img[r][c] - min_gray) / diff_gray * 255)
    return w, h

def normalizeLog(img):
    imgCopy = np.array(img.copy())
    img_max = (np.max(imgCopy))
    log = (255.0/ math.log10(255))
    w, h = imgCopy.shape
    for r in range(h):
        for c in range(w):
            img[r][c] = int(log * np.log10(1 + (255.0/img_max* img[r][c])))
    return w, h