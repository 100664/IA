# função responsável por transformar o nosso map de simbolos em forma de matriz para o nosso mapa de simbolos em 
#forma de lista de strings onde cada string é uma linha
 
#ESTÁ A FUNCIONAR, ESTA CLASSE JÁ NÃO MEXE MAIS

def parse (path): 
    file = open(path, 'r')
    lines = file.readlines()

    aux = []

    for sub in lines:
        aux.append(sub.rstrip("\n"))

    file.close()

    return aux
