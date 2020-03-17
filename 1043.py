#!/usr/bin/env python3
a, b, c = list(map(float, input().split(" ")))

if abs(b - c) < a < (b + c) or abs(a - c) < b < (a + c) or abs(a - b) < c < (a + b):
    res = a+b+c
    print("Perimetro = {:.01f}".format(res))
else:
    res = (a+b)*c
    print("Area = {:.01f}".format(res/2))
