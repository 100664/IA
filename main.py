import datetime
import time

from extras import *
from build import *

def menu_mapa():
    print()

def menu_info():
    print ("-----------------------------Proura informada----------------------------")
    print ("|1 -> Procura A*                                                        |")
    print ("|2 -> Proura Gulosa                                                     |")
    print ("|3 -> Sair                                                              |")
    print("--------------------------------------------------------------------------")

    input1 = int (input())

    if input1 == 1:
        #procura A*
        print("a*")
        
    elif input1 == 2:
        #procura gulosa
        print("greedy")
    else:
        menu_procura()

        menu()

def menu_ninfo():
    print ("---------------------------Proura não informada--------------------------")
    print ("|1 -> Procura em Profundidade                                           |")
    print ("|2 -> Proura em Largura                                                 |")
    print ("|3 -> Sair                                                              |")
    print("--------------------------------------------------------------------------")

    input1 = int (input())

    if input1 == 1:
        #procura em profundidade
        print("prof")
        
    elif input1 == 2:
        #procura em largura
        print("larg")
    else:
        menu_procura()


def menu_procura():
    print ("--------------------------Proura do melhor Path--------------------------")
    print ("|1 -> Procura não informada                                             |")
    print ("|2 -> Procura informada                                                 |")
    print ("|3 -> Sair                                                              |")
    print("--------------------------------------------------------------------------")

    
    input1 = int(input())

    if input1 == 1:
        menu_ninfo()
    elif input1 == 2:
        menu_info()
    else:
        menu()



def menu_preco(peso, tempo):
    print("|     Aguarde, estamos a calcular quanto ficará a sua encomenda. . .     |")
    encomenda_price = str(calcular_preco_encomenda(peso, tempo))
    time.sleep(2)
    print("|        A sua encomenda ficará a " + encomenda_price + "€ .                                  |")
 
    menu_procura()


def menu_encomendas ():
    print("------------------------Encomendas e especificações-----------------------")
    print("|Em quanto tempo quer que a sua encomenda seja entregue (horas)          |") 
    print("|Qual o peso da encomenda em KG?                                         |")
    print("|Qual o volume da encomenda em cm3                                       |")
    print("--------------------------------------------------------------------------")
        
    print ("tempo : ")
    tempo = float (input())
    
    print ("peso: ")
    peso = float (input())

    print ("volume: ")
    volume = float (input())

    menu_preco(peso, tempo)



def menu():

#pode ser que o mapa tenha que ser criado pelo utilizador não sei bem como funciona a geração do mapa, por enquanto é um mapa pre-feito

    print("------------------------------Menu Principal------------------------------")
    print("|1 -> Ver os Mapas                                                       |")
    print("|2 -> Ver o mapa em forma de grafo                                       |")
    print("|3 -> Fazer uma encomenda                                                |")
    print("|4 -> Ver o que acontee quando há concorrência e choques                 |") #implementar em último, comecemos pelo básico
    print("|4 - >Sair                                                               |")
    print("--------------------------------------------------------------------------")
    opcao = int(input())

    if opcao == 1:
        menu_mapa()

    elif opcao == 2:
        print ("2")
        #g = Grafo
        #g.desenha()

    elif opcao == 3:
        menu_encomendas()

    elif opcao ==4:

        return

menu()
