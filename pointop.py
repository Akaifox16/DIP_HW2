import numpy as np
import math

def contrastStretching(img):
    imgCopy = np.array(img.copy())
    flatImg = imgCopy.flatten()
    min_gray = flatImg.min()
    diff_gray = flatImg.max() - min_gray
    w, h = imgCopy.shape
    contrast = [[ int((img[r][c] - min_gray) / diff_gray * 255)  for c in range(w)] for r in range(h)]
    return w, h, contrast

def normalizeLog(img):
    imgCopy = np.array(img.copy())
    img_max = (np.max(imgCopy.flatten()))
    log = (255.0/ math.log(255))
    w, h = imgCopy.shape
    norm = [[ int(log * np.log(1 + (255.0/img_max* img[r][c]))) for c in range(w)] for r in range(h)]
    return w, h, norm