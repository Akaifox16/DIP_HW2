import numpy as np
from polarform import toComplex

def fft(img):
    return np.fft.fftshift(np.fft.fft2(img))

def ifft(transform):
    return np.fft.ifft2(np.fft.ifftshift(transform))

def fuseAmpPhase(inverse):
    return np.abs(inverse)

def oneDomainIFFT(img):
    return fuseAmpPhase(ifft(img))

def phaseIFFT(phase):
    return oneDomainIFFT(phase)

def ampIFFT(amp):
    return phaseIFFT(toComplex(amp))

