import numpy as np

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
    h = len(amp)
    w = len(amp[0])
    return [[complex(amp[i][j]) for j in range(w)] for i in range(h)]