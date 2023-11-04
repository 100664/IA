import datetime

def calcular_preco_encomenda(peso, tempo):

    preco_base = 5

    if peso <= 1:
        preco_final = preco_base
    elif peso <= 5:
        preco_final = preco_base + 3
    else:
        preco_final = preco_base + 5

    if tempo < 1:
        preco_final += 10
    elif tempo < 2:
        preco_final +=5

    return preco_final

