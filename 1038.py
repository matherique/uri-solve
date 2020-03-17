#!/usr/bin/env python3 

t = {1: 4.0, 2: 4.5, 3:5.0, 4:2.0, 5: 1.5}

c, q = list(map(int, input().split(" ")))

res = t[c] * q

print("Total: R$ {:.02f}".format(res))
