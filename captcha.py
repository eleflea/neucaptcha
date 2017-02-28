import json
from os import path

from PIL import Image

_D = path.dirname(__file__)
# Set the positions of 2 digits and operator.
BOX_1 = (7, 2, 17, 16)
BOX_O = (19, 2, 27, 16)
BOX_2 = (33, 2, 43, 16)

# Vector dot product.
def _dot(v1, v2):
    return sum(map(lambda x, y: x * y, v1, v2))

# Calculates the cosine of the angle of the vector.
def _cos(v1, v2):
    norm = sum(v1) ** 0.5 * sum(v2) ** 0.5
    # If norm is zero, return 1 if and only if all zero.
    if not norm:
        if any(v1):
            return 0
        else:
            return 1
    return _dot(v1, v2) / norm

# Calculates the matrix by mean.
def _mcos(m1, m2):
    l = len(m1)
    return sum(map(_cos, m1, m2)) / l

# Binarization & Generate a image matrix.
def _matrix_im(image, box, threshold):
    m = []
    pixels = image.load()
    for x in range(box[0], box[2], 3):
        v = []
        for y in range(box[1], box[3], 2):
            v.append(1) if pixels[x,y] > threshold else v.append(0)
        m.append(v)
    return m

def identify(image, threshold=140, tol=0.85):
    """
    Identify a grayscale (L mode) image and return result.
    Return None if fail.
    :tol: toleration of uncertainty.
    """
    m1 = _matrix_im(image, BOX_1, threshold)
    m2 = _matrix_im(image, BOX_2, threshold)
    mc = _matrix_im(image, BOX_O, threshold)
    dic_num = json.load(open(path.join(_D, 'num.json')))
    for i in range(1, 8):
        if _mcos(m1, dic_num.get(str(i))) > tol:
            d1 = i
            break
    for i in range(1, 8):
        if _mcos(m2, dic_num.get(str(i))) > tol:
            d2 = i
            break
    try:
        if _mcos(mc, dic_num.get('+')) > tol:
            result = d1 + d2
        else:
            result = d1 * d2
        return result
    except:
        print('Can not identify.')
        return None

def scan_captcha(fp, threshold=140, tol=0.85):
    """Identify a captcha fp and return result, same as *identify*."""
    return identify(Image.open(fp).convert('L'), threshold, tol)
