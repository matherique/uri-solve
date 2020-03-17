#!/usr/bin/env python3 
size = len(open('in', 'r').readlines())

for _ in range(size):
    entrada = list(map(float, input().split(" ")))
    entrada.sort()
    entrada.reverse()
    a, b, c = entrada

    if a >= (b + c):
        print("NAO FORMA TRIANGULO")
    if (a**2) == (b**2) + (c**2):
        print("TRIANGULO RETANGULO")
    if (a**2) > (b**2) + (c**2):
        print("TRIANGULO OBTUSANGULO")
    if (a**2) < (b**2) + (c**2):
        print("TRIANGULO ACUTANGULO")
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    if a == b or b == c:
        print("TRIANGULO ISOSCELES")
    
