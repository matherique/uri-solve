#!/usr/bin/env python3 
a, b, c = list(map(float, input().split(" ")))

delta = b ** 2 - 4*a*c

if delta > 0 and a > 0:
    r1 = (b * (-1) + (delta ** 0.5)) / (2 * a)
    r2 = (b * (-1) - (delta ** 0.5)) / (2 * a)
    print("R1 = {:.05f}".format(r1))
    print("R2 = {:.05f}".format(r2))
else:
    print("Impossivel calcular")
