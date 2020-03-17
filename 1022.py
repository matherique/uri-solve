#!/usr/bin/env python3
casos = int(input())
frac = []

for _ in range(casos):
   f = input()
   frac.append(f)


def mdc(a,b):
    return a if b == 0 else mdc(b, a % b)
 
def simplificar(n, d):
    m = mdc(n, d)
    
    nn = n // m
    nd = d // m
    
    return nn, nd

def res(fracao):
    n1, _, d1, op, n2, _, d2 = fracao.split(" ")
    n1, d1, n2, d2 = list(map(int, [n1, d1, n2, d2]))
    
    if op == "+":
        return ((n1*d2) + (n2*d1)) , (d1*d2)
    elif op == "-":
        return ((n1*d2) - (n2*d1)) , (d1*d2)
    elif op == "*":
        return (n1*n2), (d1*d2)
    elif op == "/":
        return (n1*d2), (n2*d1)

for f in frac:
    n, d = res(f)
    nn, nd = simplificar(n, d)
    print("{}/{} = {}/{}".format(n, d, nn, nd))
