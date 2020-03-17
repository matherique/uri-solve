#!/usr/bin/env python

valor = float(input())


if valor >= 0.00000 and valor <= 25.00000:
    print("Intervalo [0,25]")
elif valor > 25.00001 and valor <= 50.00000:
    print("Intervalo (25,50]")
elif valor > 50.00001 and valor <= 75.00000:
    print("Intervalo (50,75]")
elif valor > 75.00001 and valor <= 100.00000:
    print("Intervalo (75,100]")
else: 
    print("Fora de intervalo")
