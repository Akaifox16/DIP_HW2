import numpy as np

def convolution(img, kernel):
    n = len(img)
    m =len(kernel) - 1
    x = m - 1
    convo = np.array([[0]*(n-m) for _ in range(n-m)])
    kernel_flat = kernel.flatten()
    for i in range(x, n-x):
        for j in range(x, n-x):
            a = img[i-x:i+m, j-x:j+m]
            convo[i-x][j-x] = convolute(a.flatten(), kernel_flat)
    return convo

def filterFreqDomain(fourier, kernelFourier):
    return fourier * kernelFourier


def convolute(arr_flat, kernel_flat):
    sum_flat = arr_flat * kernel_flat
    return sum_flat.sum()