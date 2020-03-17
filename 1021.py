#!/usr/bin/env python3 
valor = 22.01
while 0 > valor < 10000000:
  valor = float(input())

valor += 0.001

todasNotas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
p = False
t = valor
for d in todasNotas:
  q = t // d
  t -= (t//d) * d

  if d < 2:
    if not p:
        print("MOEDAS:")
        p = True
  
    print("{} moeda(s) de R$ {:.02f}".format(int(q), d))
  else:
    print("{} nota(s) de R$ {:.02f}".format(int(q), d))



