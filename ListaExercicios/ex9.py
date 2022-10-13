def contaVogaiseConsoantes(s):
    nVogais = 0
    nConsoantes = 0
    for c in s:
        if str(c).lower() in "aeiou":
            nVogais += 1
        elif str(c).lower() in "bcdfghjklmnpqrstvwxyz":
            nConsoantes +=1

    return (nVogais, nConsoantes)

print(contaVogaiseConsoantes("aeioub"))