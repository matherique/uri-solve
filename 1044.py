#!/usr/bin/env python3 

size = len(open('in', 'r').readlines())


for _ in range(size):
    x, y = list(map(int, input().split(" ")))
   
    if x % y == 0 or y % x == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")

