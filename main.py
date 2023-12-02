import datetime
import time

from parsezim import parse
from Helper import *
from Encomenda import *
from build import *
from extras import *
import warnings

#-----------------------------//menu novo 2nd player\\---------------------------------

def menu_mediador(caminho, path1, path2, colissions):
    print("-----------------------------Mediador-----------------------------")
    print("|1 -> Ver Grafo da transportadora 1                              |")
    print("|2 -> Ver Grafo da transportadora 2                              |")
    print("|3 -> Ver caminho da transportadora 1                            |")
    print("|4 -> Ver caminho da transportadora 2                            |")
    print("|5 -> Sair                                                       |")
    print("------------------------------------------------------------------")
    input1 = int (input())

    if input1 == 1:
        builder = Build(caminho)
        builder.expand_graph()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            builder.highlight_path(path1)
    
    elif input1 == 2:
        builder = Build(caminho)
        builder.expand_graph()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            builder.highlight_path(path2, colissions)
    
    elif input1 == 3:
        builder = Build(caminho)
        builder.expand_graph()
        print(path1)
    
    elif input1 == 4:
        builder = Build(caminho)
        builder.expand_graph()
        print(path2)
    
    elif input1 == 5:
        menu_principal(caminho)

    else:
        menu_mediador(caminho, path1, path2, colissions)
    
    menu_mediador(caminho, path1, path2, colissions)

        

#-----------------------------//menu novo 2nd player\\---------------------------------

def menu_transportadora2(caminho, morada1, morada2, path1):
    print("-----------------------------Transportadora 2-----------------------------")
    print("|1 -> DFS (Depth-first search)                                           |")
    print("|2 -> BFS (Breadth-first search)                                         |")
    print("|3 -> Procura A*                                                         |")
    print("|4 -> Procura Gulosa                                                     |")
    print("|5 -> Mudar a procura da transportadora 1                                |")  
    print("|6 -> Sair                                                               |")
    print("--------------------------------------------------------------------------")
    input1 = int (input())

    if input1 == 1:
        builder = Build(caminho)
        builder.expand_graph()
        path2, colissions = builder.dfs_2nd(0, morada2, path1)

    elif input1 == 2:
        builder = Build(caminho)
        builder.expand_graph()

        path2, colissions = builder.bfs_2nd(0, morada2, path1)
    elif input1 == 3:
        builder = Build(caminho)
        builder.expand_graph()
        path2, colissions = builder.a_star_2nd(0, morada2, path1)

    elif input1 == 4:
        builder = Build(caminho)
        builder.expand_graph()
        path2, colissions = builder.greedy_best_first_search_2nd(0, morada2, path1)

    elif input1 == 5:
        menu_transportadora1(caminho, morada1, morada2)

    elif input1 == 6:
        menu_principal(caminho)

    else:
        menu_transportadora2(caminho,morada1, morada2, path1)
    
    menu_mediador(caminho, path1, path2, colissions)

#-----------------------------//menu novo 2nd player\\---------------------------------

def menu_transportadora1(caminho, morada1, morada2):
    print("-----------------------------Transportadora 1-----------------------------")
    print("|1 -> DFS (Depth-first search)                                           |")
    print("|2 -> BFS (Breadth-first search)                                         |")
    print("|3 -> Procura A*                                                         |")
    print("|4 -> Procura Gulosa                                                     |")
    print("|5 -> Sair                                                               |")
    print("--------------------------------------------------------------------------")

    input1 = int (input())

    if input1 == 1:
        builder = Build(caminho)
        builder.expand_graph()
        path1 = builder.find_path_dfs(0, morada1)

    elif input1 == 2:
        builder = Build(caminho)
        builder.expand_graph()
        path1 = builder.find_path_bfs(0, morada1)

    elif input1 == 3:
        builder = Build(caminho)
        builder.expand_graph()
        path1 = builder.a_star(0, morada1)

    elif input1 == 4:
        builder = Build(caminho)
        builder.expand_graph()
        path1 = builder.greedy_best_first_search(0, morada1)

    elif input1 == 5:
        menu_principal(caminho)

    else:
        menu_transportadora1(caminho, morada1, morada2)

    menu_transportadora2(caminho, morada1, morada2, path1)

#-----------------------------//menu novo 2nd player\\---------------------------------

def menu_encomendas_2nd (caminho):
    print("-----------------------------Encomendas_Colisões---------------------------")
    print("| Como o objetivo é ver como o programa responde às colisões, vamos criar |")
    print("|  duas transportadoras, cada uma com o seu caminho. E ver como reagem à  |")
    print("|         concorrência. Para tal vamos 'ignorar' as encomendas            |")
    print("---------------------------------------------------------------------------")
    print("| Qual a morada da encomenda da primeira transportadora (número do nodo)  |")
    print("|  Qual a morada da encomenda da segunda transportadora (número do nodo)  |")    
    print("---------------------------------------------------------------------------")
        
    print("Morada 1:", end=" ")
    morada_input1 = input()
    try:
        morada1 = int(morada_input1)
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número válido.")
        menu_encomendas_2nd(caminho)

    print("Morada 2:", end=" ")
    morada_input2 = input()
    try:
        morada2 = int(morada_input2)
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número válido.")
        menu_encomendas_2nd(caminho)
    
    menu_transportadora1(caminho, morada1, morada2)

#-----------------------------//menu novo\\---------------------------------

def menu_helper2 (lista_encomendas, caminho):
    print ("---------------------------------Menu Mediador-------------------------------")
    print ("|1 -> Começar uma nova leva de encomendas                                   |")
    print ("|2 -> Continuar com as mesmas encomendas                                    |")
    print ("|3 -> Sair do programa                                                      |")
    print ("-----------------------------------------------------------------------------")

    input1 = int (input())

    if input1 == 1:
        menu_principal(caminho)
    elif input1 == 2:
        menu_procura (caminho, lista_encomendas)
    else:
        return
    
#-----------------------------//menu novo\\---------------------------------

def menu_avaliacao(lista_encomendas_copia, ordered_deliveries, caminho):
    print("--------------------------------------------------------------------------")
    print("|      Avalie a nossa entrega de 1 a 5 (1-> horrível e 5->perfeita)      |")
    print("--------------------------------------------------------------------------")

    print("Avaliação:", end=" ")
    avaliacao_input = input()
    try:
        avaliacao = int(avaliacao_input)
        if (avaliacao>5 or avaliacao<1):
            i = 1
            print("--------------------------------------------------------------------------")
            print("|   Avalie corretamente, só vai aumentar o tempo de espera. Obrigado!    |")
            print("--------------------------------------------------------------------------")
            time.sleep(2*i)
            i+=1
            menu_avaliacao(lista_encomendas_copia, ordered_deliveries, caminho)

    except ValueError:
        print("ERROR: Entrada inválida. Certifique-se de inserir um número válido.")
        menu_avaliacao(lista_encomendas_copia, ordered_deliveries, caminho)
    
    menu_helper2(lista_encomendas_copia, caminho)


#-----------------------------//menu novo\\---------------------------------
#continuar com esta ideia, mas mudar a forma de se fazer as contas

def menu_entrega(lista_encomendas,  ordered_deliveries, caminho):
    builder = Build(caminho)
    builder.expand_graph()
    distancia = 0

    lista_encomendas_copia = lista_encomendas.copy()

    for encomenda_id, specific_encomenda_path in ordered_deliveries:
        encomenda = builder.obter_encomenda_por_id(encomenda_id, lista_encomendas_copia)

        distancia += len (specific_encomenda_path) 
    
    peso_total = calcular_peso_total_encomendas(lista_encomendas)
    transporte = escolher_meio_transporte(peso_total, encomenda)
    tempo_total = calcular_tempo_viagem_total(distancia, transporte, peso_total, len(lista_encomendas))
    tempo = minutos_para_horas_minutos(tempo_total)
    co2 = calcular_co2(distancia, transporte)            
    print ("------------------------------Dados da Entrega----------------------------")
    print (f"| Peso total transportado : {peso_total} KG                                       |")
    print (f"| Distância percorrida em KM : {distancia*10} KM                                     |")
    print (f"| Meio de transporte usado na entrega: {transporte}                             |")
    print (f"| CO2 gasto para a entrega: {co2} CM3 de CO2                                |")
    print (f"| Tempo Gasto na Viagem (HH.MM): {tempo}                                    |")
    print("--------------------------------------------------------------------------")


    menu_avaliacao(lista_encomendas, ordered_deliveries, caminho)

#-----------------------------//menu novo\\---------------------------------

def menu_preço(lista_encomendas, ordered_deliveries, caminho):
    builder = Build(caminho)
    builder.expand_graph()

    for encomenda_id, specific_encomenda_path in ordered_deliveries:
        encomenda = builder.obter_encomenda_por_id(encomenda_id, lista_encomendas)

        print(f"-----------------------------------Preço {encomenda_id}---------------------------------")
        encomenda_price = calcular_preco_encomenda(encomenda, len(specific_encomenda_path))
        encomenda_price_str = f"{encomenda_price:.2f}"
        print(f"|        A encomenda de ID {encomenda_id} a {encomenda_price_str} € .                                   |")
        print("---------------------------------------------------------------------------")

    
    menu_entrega(lista_encomendas, ordered_deliveries, caminho)

#-----------------------------//menu novo\\---------------------------------

def menu_helper (lista_encomendas, ordered_deliveries, caminho):
    print ("---------------------------------Menu Mediador-------------------------------")
    print ("|1 -> Ver os dados da entrega                                               |")   
    print ("|2 -> Sair                                                                  |")
    print ("-----------------------------------------------------------------------------")
    input1 = int(input())

    if input1 == 1:
        
        menu_preço(lista_encomendas, ordered_deliveries, caminho)
    
    elif input1 == 2:
        menu_principal(caminho)

    else:
        menu()

#-----------------------------//menu novo\\---------------------------------

def menu_guloso(caminho, lista_encomendas):
    print ("----------------------------------Procura A*---------------------------------")
    print ("|1 -> Caminho feito por cada encomenda                                      |")
    print ("|2 -> Caminho feito por uma encomenda                                       |")
    print ("|3 -> Desenho do caminho de uma encomenda em formato de  Grafo              |")
    print ("|4 -> Informações                                                           |")
    print ("|5 -> Sair                                                                  |")
    print ("-----------------------------------------------------------------------------")

    input1 = int (input())

    if input1 == 1:
        builder = Build(caminho)
        builder.expand_graph()
        lista_encomendas_copia = lista_encomendas.copy()
        ordered_deliveries = builder.calculate_and_print_best_path(0, lista_encomendas_copia, search_algorithm='greedy')
        for i, path in enumerate(ordered_deliveries, start=1):
            print(f'{path}')

        menu_guloso(caminho, lista_encomendas)

    if input1 == 2:

        builder = Build(caminho)
        builder.expand_graph()

        lista_encomendas_copia = lista_encomendas.copy()
        ordered_deliveries = builder.calculate_and_print_best_path(0, lista_encomendas_copia, search_algorithm='greedy')
        print("--------------------------------------------")
        print("Encomenda que deseja ver (id = XXXX):", end=" ")
        target_encomenda_id = str(input())
        print("--------------------------------------------")
        specific_encomenda_path = builder.get_specific_encomenda_path(target_encomenda_id, ordered_deliveries)

        if specific_encomenda_path:
            print(f"Caminho para a encomenda com ID {target_encomenda_id} : ", specific_encomenda_path)

            menu_guloso(caminho, lista_encomendas)
        else:
            print(f"Encomenda com ID {target_encomenda_id} não encontrada.")

            menu_principal(caminho)

    elif input1 == 3:

        builder = Build(caminho)
        builder.expand_graph()

        lista_encomendas_copia = lista_encomendas.copy()
        ordered_deliveries = builder.calculate_and_print_best_path(0, lista_encomendas_copia, search_algorithm='greedy')

        print("--------------------------------------------")
        print("Encomenda que deseja ver (id = XXXX):", end=" ")
        target_encomenda_id = str(input())
        print("--------------------------------------------")
        specific_encomenda_path = builder.get_specific_encomenda_path(target_encomenda_id, ordered_deliveries)

        if specific_encomenda_path:

            with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    builder.highlight_path(specific_encomenda_path)

            menu_aestrela(caminho, lista_encomendas)
        else:
            print(f"Encomenda com ID {target_encomenda_id} não encontrada.")
            menu_encomendas(caminho, lista_encomendas)
        
    elif input1 == 4:
        builder = Build(caminho)
        builder.expand_graph()
        lista_encomendas_copia = lista_encomendas.copy()
        ordered_deliveries = builder.calculate_and_print_best_path(0, lista_encomendas_copia, search_algorithm='a_star')
        #print ("a_estrela: ", lista_encomendas)
        menu_helper(lista_encomendas, ordered_deliveries, caminho)

    elif input1 == 5:
        menu_info(caminho,  lista_encomendas)

#-----------------------------//menu novo\\---------------------------------

def menu_aestrela(caminho, lista_encomendas):
    print ("----------------------------------Procura A*---------------------------------")
    print ("|1 -> Caminho feito por cada encomenda                                      |")
    print ("|2 -> Caminho feito por uma encomenda                                       |")
    print ("|3 -> Desenho do caminho de uma encomenda em formato de  Grafo              |")
    print ("|4 -> Informações                                                           |")
    print ("|5 -> Sair                                                                  |")
    print("------------------------------------------------------------------------------")

    input1 = int (input())

    if input1 == 1:
        builder = Build(caminho)
        builder.expand_graph()
        lista_encomendas_copia = lista_encomendas.copy()
        ordered_deliveries = builder.calculate_and_print_best_path(0, lista_encomendas_copia, search_algorithm='a_star')
        for i, path in enumerate(ordered_deliveries, start=1):
            print(f'{path}')

        menu_aestrela(caminho, lista_encomendas)

    if input1 == 2:

        builder = Build(caminho)
        builder.expand_graph()

        lista_encomendas_copia = lista_encomendas.copy()
        ordered_deliveries = builder.calculate_and_print_best_path(0, lista_encomendas_copia, search_algorithm='a_star')
        print("--------------------------------------------")
        print("Encomenda que deseja ver (id = XXXX):", end=" ")
        target_encomenda_id = str(input())
        print("--------------------------------------------")
        specific_encomenda_path = builder.get_specific_encomenda_path(target_encomenda_id, ordered_deliveries)

        if specific_encomenda_path:
            print(f"Caminho para a encomenda com ID {target_encomenda_id} : ", specific_encomenda_path)

            menu_aestrela(caminho, lista_encomendas)
        else:
            print(f"Encomenda com ID {target_encomenda_id} não encontrada.")

            menu_principal(caminho)

    elif input1 == 3:

        builder = Build(caminho)
        builder.expand_graph()

        lista_encomendas_copia = lista_encomendas.copy()
        ordered_deliveries = builder.calculate_and_print_best_path(0, lista_encomendas_copia, search_algorithm='a_star')

        print("--------------------------------------------")
        print("Encomenda que deseja ver (id = XXXX):", end=" ")
        target_encomenda_id = str(input())
        print("--------------------------------------------")
        specific_encomenda_path = builder.get_specific_encomenda_path(target_encomenda_id, ordered_deliveries)

        if specific_encomenda_path:

            with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    builder.highlight_path(specific_encomenda_path)

            menu_aestrela(caminho, lista_encomendas)
        else:
            print(f"Encomenda com ID {target_encomenda_id} não encontrada.")
            menu_encomendas(caminho, lista_encomendas)
        
    elif input1 == 4:
        builder = Build(caminho)
        builder.expand_graph()
        lista_encomendas_copia = lista_encomendas.copy()
        ordered_deliveries = builder.calculate_and_print_best_path(0, lista_encomendas_copia, search_algorithm='a_star')
        #print ("a_estrela: ", lista_encomendas)
        menu_helper(lista_encomendas, ordered_deliveries, caminho)

    elif input1 == 5:
        menu_info(caminho,  lista_encomendas)



#-----------------------------//menu novo\\---------------------------------

def menu_info(caminho,  lista_encomendas):
    print ("-----------------------------Proura informada----------------------------")
    print ("|1 -> Procura A*                                                        |")
    print ("|2 -> Proura Gulosa                                                     |")
    print ("|3 -> Sair                                                              |")
    print ("-------------------------------------------------------------------------")

    input1 = int (input())

    if input1 == 1:
        
        menu_aestrela(caminho, lista_encomendas)

    elif input1 == 2:

        menu_guloso(caminho, lista_encomendas)
        
    elif input1 == 3:
        menu_procura(caminho, lista_encomendas)
    else:
        menu()

#-----------------------------//menu novo\\---------------------------------

def menu_bfs(caminho, lista_encomendas):
    print ("-----------------------------Procura em Largura------------------------------")
    print ("|1 -> Caminho feito por cada encomenda                                      |")
    print ("|2 -> Caminho feito por uma encomenda                                       |")
    print ("|3 -> Desenho do caminho de uma encomenda em formato de  Grafo              |")
    print ("|4 -> Informações                                                           |")
    print ("|5 -> Sair                                                                  |")
    print("------------------------------------------------------------------------------")

    input1 = int (input())

    if input1 == 1:
        builder = Build(caminho)
        builder.expand_graph()
        lista_encomendas_copia = lista_encomendas.copy()
        ordered_deliveries = builder.calculate_and_print_best_path(0, lista_encomendas_copia, search_algorithm='bfs')
        for i, path in enumerate(ordered_deliveries, start=1):
            print(f'{path}')

        menu_bfs(caminho, lista_encomendas)

    if input1 == 2:

        builder = Build(caminho)
        builder.expand_graph()

        lista_encomendas_copia = lista_encomendas.copy()
        ordered_deliveries = builder.calculate_and_print_best_path(0, lista_encomendas_copia, search_algorithm='bfs')
        print("--------------------------------------------")
        print("Encomenda que deseja ver (id = XXXX):", end=" ")
        target_encomenda_id = str(input())
        print("--------------------------------------------")
        specific_encomenda_path = builder.get_specific_encomenda_path(target_encomenda_id, ordered_deliveries)

        if specific_encomenda_path:
            print(f"Caminho para a encomenda com ID {target_encomenda_id} : ", specific_encomenda_path)

            menu_bfs(caminho, lista_encomendas)
        else:
            print(f"Encomenda com ID {target_encomenda_id} não encontrada.")

            menu_principal(caminho)

    elif input1 == 3:

        builder = Build(caminho)
        builder.expand_graph()

        lista_encomendas_copia = lista_encomendas.copy()
        ordered_deliveries = builder.calculate_and_print_best_path(0, lista_encomendas_copia, search_algorithm='bfs')

        print ("--------------------------------------------")
        print ("Encomenda que deseja ver (id = XXXX):", end=" ")
        target_encomenda_id = str(input())
        print ("--------------------------------------------")
        specific_encomenda_path = builder.get_specific_encomenda_path(target_encomenda_id, ordered_deliveries)

        if specific_encomenda_path:

            with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    builder.highlight_path(specific_encomenda_path)

            menu_bfs(caminho, lista_encomendas)
        else:
            print(f"Encomenda com ID {target_encomenda_id} não encontrada.")
            menu_encomendas(caminho, lista_encomendas)
        
    elif input1 == 4:
        builder = Build(caminho)
        builder.expand_graph()
        lista_encomendas_copia = lista_encomendas.copy()
        ordered_deliveries = builder.calculate_and_print_best_path(0, lista_encomendas_copia, search_algorithm='a_star')
        menu_helper(lista_encomendas, ordered_deliveries, caminho)

    elif input1 == 5:
        menu_ninfo(caminho, lista_encomendas)


#-----------------------------//menu novo\\---------------------------------

def menu_dfs(caminho, lista_encomendas):
    print ("---------------------------Procura em Profundidade---------------------------")
    print ("|1 -> Caminho feito por cada encomenda                                      |")
    print ("|2 -> Caminho feito por uma encomenda                                       |")
    print ("|3 -> Desenho do caminho de uma encomenda em formato de  Grafo              |")
    print ("|4 -> Informações                                                           |")
    print ("|5 -> Sair                                                                  |")
    print ("-----------------------------------------------------------------------------")

    input1 = int (input())

    if input1 == 1:
        builder = Build(caminho)
        builder.expand_graph()
        lista_encomendas_copia = lista_encomendas.copy()
        ordered_deliveries = builder.calculate_and_print_best_path(0, lista_encomendas_copia, search_algorithm='dfs')
        for i, path in enumerate(ordered_deliveries, start=1):
            print(f'{path}')

        menu_dfs(caminho, lista_encomendas)

    if input1 == 2:

        builder = Build(caminho)
        builder.expand_graph()

        lista_encomendas_copia = lista_encomendas.copy()
        ordered_deliveries = builder.calculate_and_print_best_path(0, lista_encomendas_copia, search_algorithm='dfs')
        print("--------------------------------------------")
        print("Encomenda que deseja ver (id = XXXX):", end=" ")
        target_encomenda_id = str(input())
        print("--------------------------------------------")
        specific_encomenda_path = builder.get_specific_encomenda_path(target_encomenda_id, ordered_deliveries)

        if specific_encomenda_path:
            print(f"Caminho para a encomenda com ID {target_encomenda_id} : ", specific_encomenda_path)

            menu_dfs(caminho, lista_encomendas)
        else:
            print(f"Encomenda com ID {target_encomenda_id} não encontrada.")

            menu_principal(caminho)

    elif input1 == 3:

        builder = Build(caminho)
        builder.expand_graph()

        lista_encomendas_copia = lista_encomendas.copy()
        ordered_deliveries = builder.calculate_and_print_best_path(0, lista_encomendas_copia, search_algorithm='dfs')

        print("--------------------------------------------")
        print("Encomenda que deseja ver (id = XXXX):", end=" ")
        target_encomenda_id = str(input())
        print("--------------------------------------------")
        specific_encomenda_path = builder.get_specific_encomenda_path(target_encomenda_id, ordered_deliveries)

        if specific_encomenda_path:

            with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    builder.highlight_path(specific_encomenda_path)

            menu_dfs(caminho, lista_encomendas)
        else:
            print(f"Encomenda com ID {target_encomenda_id} não encontrada.")
            menu_encomendas(caminho, lista_encomendas)
        
    elif input1 == 4:
        builder = Build(caminho)
        builder.expand_graph()
        lista_encomendas_copia = lista_encomendas.copy()
        ordered_deliveries = builder.calculate_and_print_best_path(0, lista_encomendas_copia, search_algorithm='a_star')
        menu_helper(lista_encomendas, ordered_deliveries, caminho)

    elif input1 == 5:
        menu_ninfo(caminho, lista_encomendas)

#-----------------------------//menu novo\\---------------------------------


def menu_ninfo(caminho, lista_encomendas):
    print ("---------------------------Procura não informada-------------------------")
    print ("|1 -> Procura em Profundidade                                           |")
    print ("|2 -> Proura em Largura                                                 |")
    print ("|3 -> Sair                                                              |")
    print ("-------------------------------------------------------------------------")

    input1 = int (input())

    if input1 == 1:

        menu_dfs(caminho, lista_encomendas)

    elif input1 == 2:
       
        menu_bfs(caminho, lista_encomendas)

    elif input1 == 3:
        menu_procura(caminho, lista_encomendas)

    else:
        menu()
#-----------------------------//menu novo\\---------------------------------


def menu_procura(caminho, lista_encomendas):
    print ("--------------------------Proura do melhor Path--------------------------")
    print ("|1 -> Procura não informada                                             |")
    print ("|2 -> Procura informada                                                 |")
    print ("|3 -> Sair                                                              |")
    print ("-------------------------------------------------------------------------")

    
    input1 = int(input())

    if input1 == 1:
        menu_ninfo(caminho, lista_encomendas)
    elif input1 == 2:
        menu_info(caminho, lista_encomendas)
    else:
        menu_principal(caminho)

#-----------------------------//menu novo\\---------------------------------

def menu_PlusEncomendas(caminho, lista_encomendas):

    print ("-----------------------Deseja fazer mais encomendas-----------------------")
    print ("|Sim                                                                     |") 
    print ("|Não                                                                     |")
    print ("--------------------------------------------------------------------------")

    input1 = input()

    if input1 in ["Sim", "sim", "SIM", "s", "S"]:
        menu_encomendas(caminho, lista_encomendas)   
    elif input1 in ["Não", "não", "NÃO", "n", "N", "nao", "Nao", "NAOs"]:
        menu_procura(caminho, lista_encomendas)

    else:
        menu()
#-----------------------------//menu novo\\---------------------------------


def menu_encomendas (caminho, lista_encomendas):
    print("------------------------Encomendas e especificações-----------------------")
    print("|Em quanto tempo quer que a sua encomenda seja entregue (minutos)        |") 
    print("|Qual o peso da encomenda em KG                                          |")
    print("|Qual o volume da encomenda em cm3                                       |")
    print("|Qual a sua morada (número do nodo)                                      |")
    print("--------------------------------------------------------------------------")
        
    print("Tempo:", end=" ")
    tempo_input = input()
    try:
        tempo = int(tempo_input)
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número válido.")
        menu_encomendas(caminho)

    print("Peso:", end=" ")
    peso_input = input()
    try:
        peso = float(peso_input.replace(',', '.'))
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número válido.")
        menu_encomendas(caminho)


    print("Volume:", end=" ")
    volume_input = input()
    try:
        volume = float(volume_input.replace(',', '.'))
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número válido.")
        menu_encomendas(caminho)

    print("Morada:", end=" ")
    morada_input = input()
    try:
        morada = int(morada_input)
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número válido.")
        menu_encomendas(caminho)
    
    encomenda = Encomenda (peso, volume, tempo, morada)
    lista_encomendas.append(encomenda)
    menu_PlusEncomendas(caminho, lista_encomendas)


#-----------------------------//menu novo\\---------------------------------


def menu_principal (caminho):

    print("------------------------------Menu Principal------------------------------")
    print("|1 -> Ver Nodos e Conexões                                               |")
    print("|2 -> Ver o mapa em forma de grafo                                       |")
    print("|3 -> Fazer encomendas                                                   |")
    print("|4 -> Ver o que acontece quando há concorrência e choques                |") #implementar em último, comecemos pelo básico
    print("|5 -> Sair                                                               |")
    print("--------------------------------------------------------------------------")
    opcao = int(input())


    if opcao == 1:

        builder = Build(caminho)
        builder.expand_graph()
        builder.print_graph()
        menu_principal(caminho)

    elif opcao == 2:

        builder = Build(caminho)
        builder.expand_graph()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            builder.visualize_graph()
        menu_principal(caminho)

    elif opcao == 3:
        lista_encomendas = []
        menu_encomendas(caminho, lista_encomendas)

    elif opcao == 4:
        menu_encomendas_2nd(caminho)

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