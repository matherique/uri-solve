#!/usr/bin/env python3 
n1, n2, n3, n4 = list(map(float, input().split(" ")))
pesos = [2, 3, 4, 1]

media = ((n1 * 2)  + (n2 * 3) + (n3 * 4) + (n4 * 1)) / sum(pesos)

if media >= 7.0:
    print("Media: {:.01f}".format(media))
    print("Aluno aprovado.")
else:
    if media < 5.0:
        print("Media: {:.01f}".format(media))
        print("Aluno reprovado.")
    else:
        exame = float(input())
        print("Media: {:.01f}".format(media))
        print("Aluno em exame.")
        print("Nota do exame: {:.01f}".format(exame))
        novamedia = (media + exame) / 2 
        if novamedia >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print("Media final: {:.01f}".format(novamedia))
