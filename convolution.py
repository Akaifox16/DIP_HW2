import numpy as np
from dft import fft

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

def cutOff(i, j, n):
    return np.sqrt((j -n/2)**2 + (i- n/2)**2)

def idealLPfilter(fourier, cutFreq):
    n = len(fourier)
    kernel = [[1.0 if cutOff(i,j,n) <= float(cutFreq) else 0.0 for j in range(n)] for i in range(n)]
    return filterFreqDomain(fourier, np.array(kernel))

def gaussianLPfilter(fourier, cutFreq):
    n =len(fourier)
    kernel = [[ np.exp(-0.5 * (cutOff(i, j, n)/ cutFreq) ** 2) for j in range(n)] for i in range(n)]
    return filterFreqDomain(fourier, np.array(kernel))

def medianfilter(fourier):
    kernel= np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) * (1/9)
    return convolution(np.pad(fourier,1), kernel)

def rms(img, img2):
    summation = (img.flatten() - img2.flatten()) ** 2
    return np.sqrt(summation.flatten().mean())