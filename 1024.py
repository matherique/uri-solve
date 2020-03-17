#!/usr/bin/env python3
casos = int(input())
dados = []

def p1(n):
    return n if not n.isalpha() else chr(ord(n) + 3)

def p3(n):
    return chr(ord(n) - 1)

for _ in range(casos):
   d = input()
   dados.append(d)


for d in dados:
    res1 = list(map(p1, list(d)))
    res1.reverse()
    i = len(res1)//2
    m = res1[i:]
    res = list(map(p3, m))
    print("".join(res1[:i] + res))


