from random import *


def getColor():  # 产生一个颜色
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0, 15))
    return color


def toHexChar(value):  # 产生十六进制字符
    if 0 <= value <= 9:
        return chr(value + ord("0"))
    else:
        return chr(value - 10 + ord("A"))
