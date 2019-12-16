
try:
    xrange
except NameError:
    xrange = range
    
def pixelCollision(rect1, rect2, hitmask1, hitmask2):

    rect = rect1.clip(rect2)

    if rect.width == 0 or rect.height == 0:
        return False

    x1, y1 = rect.x - rect1.x, rect.y - rect1.y
    x2, y2 = rect.x - rect2.x, rect.y - rect2.y

    for x in xrange(rect.width):
        for y in xrange(rect.height):
            if hitmask1[x1+x][y1+y] and hitmask2[x2+x][y2+y]:
                return True
    return False

def salinim(salinim):
    # salınım hareketi
    if abs(salinim['val']) == 10:
        salinim['dir'] *= -1

    if salinim['dir'] == 1:
         salinim['val'] += 1
    else:
        salinim['val'] -= 1