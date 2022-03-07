import numpy as np
from math import exp

def complex2polar(z):
    return { 'r': abs(z) , 'angle': np.angle(z)} 

def polar2complex(r, angle):
    return r * exp(1j*angle)

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

def fuseAmplitudeAndPhase(amp, phase):
    img = []
    for i in range(len(amp)):
        row = []
        for j in range(len(amp[i])):
            row.append(polar2complex(amp[i][j], phase[i][j]))
        img.append(row)
    return img