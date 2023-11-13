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

def menu_avaliacao():
    print("--------------------------------------------------------------------------")
    print("|      Avalie a nossa entrega de 1 a 5 (1-> horrível e 5->perfeita)      |")
    print("--------------------------------------------------------------------------")
    avalia = int(input())
    print("--------------------------------------------------------------------------")
    print("|          A nossa entrega foi avaliada com 5 estrelas                   |")
    print("|    Opinião não passa de opinião. Esperamos por si numa próxima <3      |")
    print("--------------------------------------------------------------------------")
    menu()

#-----------------------------//menu novo\\---------------------------------

def menu_entrega(dist, tempo, peso):
    transporte = escolher_meio_transporte(dist, tempo, peso)
    emissao, atraso = calcular_co2_atraso(transporte,dist, tempo, peso)
    print ("----------------------------------Menu Entrega--------------------------------")
    print ("|                          Dados da sua encomenda:                           |")
    print ("| Meio de transporte usado na entrega: " +str(transporte)+ "                               |")
    print ("| CO2 gasto para a entrega: " +str(emissao)+ "Kg de CO2                                        |")
    print ("| Atras da encomenda (HH.MM): " +str(atraso)+ "                                         |")
    print("--------------------------------------------------------------------------")

    menu_avaliacao()

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


def menu_ninfo( morada,caminho,peso, tempo):
    print ("---------------------------Proura não informada--------------------------")
    print ("|1 -> Procura em Profundidade                                           |")
    print ("|2 -> Proura em Largura                                                 |")
    print ("|3 -> Sair                                                              |")
    print("--------------------------------------------------------------------------")

    input1 = int (input())

    if input1 == 1:
        
        builder = Build(caminho)
        builder.expand_graph()
        start_node = builder.get_node_by_id(0)
        end_node = builder.get_node_by_id(morada)
        if start_node and end_node:
            dfs_path = builder.dfs(0, morada)
            print("Caminho DFS:", dfs_path)
            menu_entrega(len(dfs_path),tempo, peso)
        else:
            print("Nó inicial ou nó objetivo não encontrado.")
            menu()

    elif input1 == 2:
        builder = Build(caminho)
        builder.expand_graph()
        #procura
        menu_entrega(50, tempo, peso)

    else:
        menu_procura(morada, caminho, peso, tempo)
#-----------------------------//menu novo\\---------------------------------


def menu_procura(morada, caminho, peso, tempo):
    print ("--------------------------Proura do melhor Path--------------------------")
    print ("|1 -> Procura não informada                                             |")
    print ("|2 -> Procura informada                                                 |")
    print ("|3 -> Sair                                                              |")
    print("--------------------------------------------------------------------------")

    
    input1 = int(input())

    if input1 == 1:
        menu_ninfo(morada, caminho, peso, tempo)
    elif input1 == 2:
        menu_info(morada, caminho, peso, tempo)
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
 
    menu_procura(morada, caminho, peso, tempo)


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
    print("|5 -> Sair                                                               |")
    print("--------------------------------------------------------------------------")
    opcao = int(input())


    if opcao == 1:

        builder = Build(caminho)
        builder.expand_graph()
        builder.print_graph()

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