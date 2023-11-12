import datetime
import time

from parsezim import parse
from Helper import *
from build import *
from extras import *

def find_repeated_nodes(nodes):
    node_count = {}
    repeated_nodes = []

    for node in nodes:
        if node.node_id in node_count:
            repeated_nodes.append(node)
        else:
            node_count[node.node_id] = 1

    return repeated_nodes

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

def menu_ninfo(morada):
    print ("---------------------------Proura não informada--------------------------")
    print ("|1 -> Procura em Profundidade                                           |")
    print ("|2 -> Proura em Largura                                                 |")
    print ("|3 -> Sair                                                              |")
    print("--------------------------------------------------------------------------")

    input1 = int (input())

    if input1 == 1:
        
        builder = Build("freg.txt")
        builder.expand_graph()
        print("0")
        destination_id = morada  # Substitua pelo ID de destino desejado
        print(morada)
        bfs_path = builder.bfs(destination_id)
        print ("1")
        print(f"Caminho BFS para o destino {destination_id}: {bfs_path}")
        print("2")
        
    elif input1 == 2:
        builder = Build("freg.txt")
        builder.expand_graph()
        destination_id = morada  # Substitua pelo ID de destino desejado
        dfs_path = builder.dfs(destination_id)
        print(f"Caminho DFS para o destino {destination_id}: {dfs_path}")

    else:
        menu_procura()


def menu_procura(morada):
    print ("--------------------------Proura do melhor Path--------------------------")
    print ("|1 -> Procura não informada                                             |")
    print ("|2 -> Procura informada                                                 |")
    print ("|3 -> Sair                                                              |")
    print("--------------------------------------------------------------------------")

    
    input1 = int(input())

    if input1 == 1:
        menu_ninfo(morada)
    elif input1 == 2:
        menu_info()
    else:
        menu()



def menu_preco(peso, tempo, morada):
    print("--------------------------------------------------------------------------")
    print("|     Aguarde, estamos a calcular quanto ficará a sua encomenda. . .     |")
    encomenda_price = str(calcular_preco_encomenda(peso, tempo))
    time.sleep(2)
    print("|        A sua encomenda ficará a " + encomenda_price + "€ .                                  |")
    print("---------------------------------------------------------------------------")
 
    menu_procura(morada)


def menu_encomendas ():
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

    menu_preco(peso, tempo, morada)



def menu():

#pode ser que o mapa tenha que ser criado pelo utilizador não sei bem como funciona a geração do mapa, por enquanto é um mapa pre-feito

    print("------------------------------Menu Principal------------------------------")
    print("|1 -> Ver Nodos e Conexões                                               |")
    print("|2 -> Ver o mapa em forma de grafo                                       |")
    print("|3 -> Fazer uma encomenda                                                |")
    print("|4 -> Ver o que acontece quando há concorrência e choques                |") #implementar em último, comecemos pelo básico
    print("|4 - > Sair                                                              |")
    print("--------------------------------------------------------------------------")
    opcao = int(input())

    if opcao == 1:
                
        builder = Build("/Users/martimr/Desktop/3ano1sem/IA/IA_projeto/Projeto_4/freguesia.txt")
        builder.expand_graph()
        nodes = builder.nodes
        graph = builder.graph
        for node in nodes:
            print(f"Node {node.node_id} - Coordenadas: ({node.x}, {node.y})")
            print(f"Conexões: {list(graph[node.node_id])}")  # Converta o conjunto para lista para impressão
        repeated_nodes = find_repeated_nodes(nodes)
        if repeated_nodes:
            print("Nós repetidos:")
            for node in repeated_nodes:
                print(f"Node {node.node_id} - Coordenadas: ({node.x}, {node.y})")
        menu()

    elif opcao == 2:
        builder = Build("/Users/martimr/Desktop/3ano1sem/IA/IA_projeto/Projeto_4/freguesia.txt")
        builder.expand_graph()
        builder.visualize_graph()
        menu()

    elif opcao == 3:
        menu_encomendas()

    elif opcao ==4:

        return

menu() 