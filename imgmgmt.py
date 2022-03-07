def flatten(ls):
    flat = []
    for r in ls:
        for x in r:
            flat.append(x)
    return flat

def padding(img, pad):
    pad = int(pad /2)
    w = len(img[0])
    h = len(img)
    paddingzero = [0 for _ in range(pad)]
    for row in img:
        for zero in paddingzero:
            row.insert(0, zero)
        row.extend(paddingzero)
    paddingzero = [[0 for _ in range(w + 2 * pad)] for _ in range(pad)]
    
    for row in paddingzero:
        img.insert(0, row)
    img.extend(paddingzero)

def inverse(img):
    return [[255 - pixel for pixel in row] for row in img] 