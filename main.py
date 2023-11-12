import datetime
import time

from parsezim import parse
from Helper import *
from build import *
from extras import *

'''
def find_repeated_nodes(nodles):
    node_count = {}
    repeated_nodes = []

    for node in nodles:
        if node.node_id in node_count:
            repeated_nodes.append(node)
        else:
            node_count[node.node_id] = 1

    return repeated_nodes
'''
#-----------------------------//menu novo\\---------------------------------


def menu_info(morada, caminho):
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

    menu_principal()


#-----------------------------//menu novo\\---------------------------------


def menu_ninfo(morada, caminho):
    print ("---------------------------Proura não informada--------------------------")
    print ("|1 -> Procura em Profundidade                                           |")
    print ("|2 -> Proura em Largura                                                 |")
    print ("|3 -> Sair                                                              |")
    print("--------------------------------------------------------------------------")

    input1 = int (input())

    if input1 == 1:
        
        builder = Build(caminho)
        builder.expand_graph()
        destination_id = morada
        bfs_path = builder.bfs(destination_id)
        print(f"Caminho BFS para o destino {destination_id}: {bfs_path}")
        
    elif input1 == 2:
        builder = Build(menu_principal)
        builder.expand_graph()
        destination_id = morada
        dfs_path = builder.dfs(destination_id)
        print(f"Caminho DFS para o destino {destination_id}: {dfs_path}")

    else:
        menu_procura()

    menu_principal
#-----------------------------//menu novo\\---------------------------------


def menu_procura(morada, caminho):
    print ("--------------------------Proura do melhor Path--------------------------")
    print ("|1 -> Procura não informada                                             |")
    print ("|2 -> Procura informada                                                 |")
    print ("|3 -> Sair                                                              |")
    print("--------------------------------------------------------------------------")

    
    input1 = int(input())

    if input1 == 1:
        menu_ninfo(morada, caminho)
    elif input1 == 2:
        menu_info(morada, caminho)
    else:
        menu_principal()

#-----------------------------//menu novo\\---------------------------------



def menu_preco(peso, tempo, morada, caminho):
    print("--------------------------------------------------------------------------")
    print("|     Aguarde, estamos a calcular quanto ficará a sua encomenda. . .     |")
    encomenda_price = str(calcular_preco_encomenda(peso, tempo))
    time.sleep(2)
    print("|        A sua encomenda ficará a " + encomenda_price + "€ .                                  |")
    print("---------------------------------------------------------------------------")
 
    menu_procura(morada, caminho)


#-----------------------------//menu novo\\---------------------------------


def menu_encomendas (caminho):
    print("------------------------Encomendas e especificações-----------------------")
    print("|Em quanto tempo quer que a sua encomenda seja entregue (horas)          |") 
    print("|Qual o peso da encomenda em KG?                                         |")
    print("|Qual o volume da encomenda em cm3                                       |")
    print("|Qual a sua morada (número do nodo)                                      |")
    print("--------------------------------------------------------------------------")
        
    print ("tempo : ")
    tempo = float (input())
    
    print ("peso: ")
    peso = float (input())

    print ("volume: ")
    volume = float (input())

    print ("morada: ")
    morada = int (input())

    menu_preco(peso, tempo, morada, caminho)


#-----------------------------//menu novo\\---------------------------------


def menu_principal (caminho):

    print("------------------------------Menu Principal------------------------------")
    print("|1 -> Ver Nodos e Conexões                                               |")
    print("|2 -> Ver o mapa em forma de grafo                                       |")
    print("|3 -> Fazer uma encomenda                                                |")
    print("|4 -> Ver o que acontece quando há concorrência e choques                |") #implementar em último, comecemos pelo básico
    print("|5 - > Sair                                                              |")
    print("--------------------------------------------------------------------------")
    opcao = int(input())


    if opcao == 1:

        builder = Build(caminho)
        builder.expand_graph()

        nodles = builder.nodes
        graph = builder.graph

        for node in nodles:
            print(f"Node {node.node_id} - Coordenadas: ({node.x}, {node.y})")
            print(f"Conexões: {list(graph[node.node_id])}")
            '''
        repeated_nodes = builder.find_repeated_nodes(nodles)
        if repeated_nodes:
            print("Nós repetidos:")
            for node in repeated_nodes:
                print(f"Node {node.node_id} - Coordenadas: ({node.x}, {node.y})")
            '''
        menu_principal(caminho)

    elif opcao == 2:

        builder = Build(caminho)
        builder.expand_graph()
        builder.visualize_graph()
        menu_principal(caminho)

    elif opcao == 3:

        menu_encomendas(caminho)

    elif opcao == 4:
        print("ainda não está implementado")

    elif opcao ==5:
        menu()


#-----------------------------//menu novo\\---------------------------------


def menu():

    print("-----------------------------------Menu-----------------------------------")
    print("|1 -> Indique o caminho para o ficheiro no qual deseja trabalhar         |")
    print("|2 -> Sair                                                               |")
    print("--------------------------------------------------------------------------")
    opcao = int(input())

    if opcao == 1:
        print("caminho: ")
        caminho = input()
        menu_principal(caminho)

    elif opcao == 2:
        return

menu()
