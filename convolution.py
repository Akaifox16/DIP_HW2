import numpy as np

def convolution(img, kernel):
    n = len(img)
    m =len(kernel) - 1
    convo = np.array([[0]*(n-m) for _ in range(n-m)])
    kernel_flat = kernel.flatten()
    for i in range(2, n-2):
        for j in range(2, n-2):
            a = img[i-2:i+3, j-2:j+3]
            convo[i-2][j-2] = convolute(a.flatten(), kernel_flat)
    return convo

def convolute(arr_flat, kernel_flat):
    sum_flat = arr_flat * kernel_flat
    return sum_flat.sum()