import datetime
import time

from extras import *


def menu_preco(peso, tempo):
    print("|     Aguarde, estamos a calcular quanto ficará a sua encomenda. . .     |")
    encomenda_price = str(calcular_preco_encomenda(peso, tempo))
    time.sleep(2)
    print("|        A sua encomenda ficará a " + encomenda_price + "€ .                                  |")
 


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

    print("------------------------------Menu Principal------------------------------")
    print("|1->Fazer uma encomenda                                                  |")
    print("|2->Sair                                                                 |")
    print("--------------------------------------------------------------------------")
    opcao = int(input())


    if opcao == 1:
        menu_encomendas()

    elif opcao == 2:

        return

menu()