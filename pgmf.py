from pointop import normalizeLog, contrastStretching
from imgmgmt import flatten

def readPGM(file):
    _ = file.readline()
    wh = file.readline()
    if str(wh).find('#') != -1:
        wh = file.readline()
    (width, height) = [int(i) for i in wh.split()]
    depth = int(file.readline())
    image = []
    for y in range(height):
        row = []
        for y in range(width):
            row.append(ord(file.read(1)))
        image.append(row)
    file.close()
    return depth, image

def openImg(name):
    file = open(name, 'rb')
    return readPGM(file)

def writePGM(file, w, h, depth, flatImg):
    file.write('P5\n'.encode())
    file.write('{} {}\n'.format(w, h).encode())
    file.write('{}\n'.format(depth).encode())
    file.write(bytearray(flatImg))
    file.close()

def saveImg(name, img, depth, w, h):
    file = open(name, 'wb')
    writePGM(file, w, h, depth, flatten(img))

def saveNormImg(name, img, depth):
    w, h, norm = normalizeLog(img)
    saveImg(name, norm, depth, w, h)

def saveContrastImg(name, img, depth):
    w, h, contrast = contrastStretching(img)
    saveImg(name, contrast, depth, w, h)