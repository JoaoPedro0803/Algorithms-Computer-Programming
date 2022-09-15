sigla = ""
qtd = {}
while sigla != "final":
    sigla = str(input())
    if sigla == "final":
        break
    if sigla in qtd:
        qtd[sigla] = qtd[sigla] + 1
    else:
        qtd[sigla] = 1
maior = 0
lista = []
for s in qtd:
    if qtd[s]>maior:
        maior = qtd[s]
        lista = []
        lista.append(s)
    elif qtd[s] == maior:
        lista.append(s)
lista.sort()
for s in lista:
    print(s)