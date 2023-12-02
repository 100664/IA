import datetime

def calcular_preco_encomenda(encomenda, distancia):
    peso = encomenda.get_peso()
    tempo = encomenda.get_tempo()

    preco_base = 5

    fator_peso = 0.2
    fator_tempo = 2.0
    fator_distancia = 0.1 

    preco_peso = peso * fator_peso
    preco_tempo = (100 / tempo) ** fator_tempo
    preco_distancia = distancia * fator_distancia

    preco_final = preco_base + preco_peso + preco_tempo + preco_distancia

    return preco_final


def escolher_meio_transporte(peso_total_encomendas, encomenda):


    bicicleta = {'peso_limite': 5, 'velocidade': 10, 'perda_velocidade': 0.6, 'poluicao': 0}
    mota = {'peso_limite': 20, 'velocidade': 35, 'perda_velocidade': 0.5, 'poluicao': 5}
    carro = {'peso_limite': 100, 'velocidade': 50, 'perda_velocidade': 0.1, 'poluicao': 13}
    camiao = {'peso_limite': 500, 'velocidade': 80, 'perda_velocidade': 0.05, 'poluicao': 25}

    if peso_total_encomendas > 100:
        return "Camião"
    elif 20 <= peso_total_encomendas <= 100:
        return "Carro"
    elif 5 <= peso_total_encomendas < 20:
        return "Mota"
    else:
        return "Bicicleta"
    
def calcular_tempo_viagem_total(distancia_total, meio_transporte, peso_total_encomendas, paragens):
    velocidade = {'Bicicleta': 10, 'Mota': 35, 'Carro': 50, 'Camião': 80}
    perda_velocidade = {'Bicicleta': 0.6, 'Mota': 0.5, 'Carro': 0.1, 'Camião': 0.05}
    
    andamento = distancia_total * 10
    
    tempo_viagem = andamento / max(velocidade[meio_transporte] - perda_velocidade[meio_transporte] * peso_total_encomendas, 1)
    
    tempo_viagem += 5 * paragens 


    return tempo_viagem

def calcular_co2(distancia, meio_transporte):
    poluicao = {'Bicicleta': 0, 'Mota': 5, 'Carro': 13, 'Camião': 25}
    return distancia * poluicao[meio_transporte]

def calcular_peso_total_encomendas(lista_encomendas):
        peso_total = sum(encomenda.peso for encomenda in lista_encomendas)
        return peso_total

def minutos_para_horas_minutos(minutos):
    horas = int(minutos // 60)
    minutos = int(minutos % 60)
    return "{:02d}:{:02d}".format(horas, minutos)

