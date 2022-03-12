import numpy as np
from math import exp

def complex2polar(z):
    return { 'r': abs(z) , 'angle': np.angle(z)} 

def extractAmplitudeAndPhase(imgFT):
    amplitude = []
    phase = []
    for row in imgFT:
        a_row = []
        p_row = []
        for pixel in row:
            polar = complex2polar(pixel)
            a_row.append(polar['r'])
            p_row.append(polar['angle'])
        amplitude.append(a_row)
        phase.append(p_row)
    return amplitude, phase

def toComplex(amp):
    return [[complex(amp[i][j]) for j in range(len(amp[0]))] for i in range(len(amp))]