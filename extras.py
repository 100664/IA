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

def escolher_meio_transporte(distancia, tempo, peso):
    # Características dos meios de transporte
    bicicleta = {'peso_limite': 5, 'velocidade': 10, 'perda_velocidade': 0.6, 'poluicao': 0}
    mota = {'peso_limite': 20, 'velocidade': 35, 'perda_velocidade': 0.5, 'poluicao': 0.3}
    carro = {'peso_limite': 100, 'velocidade': 50, 'perda_velocidade': 0.1, 'poluicao': 2.3}

    # Verificar se é possível dividir a encomenda em partes menores
    if peso > carro['peso_limite']:
        return "Carro"

    # Calcular o tempo atrasado para cada meio de transporte
    tempo_atraso_bicicleta = max(0, tempo - (distancia / bicicleta['velocidade']))
    tempo_atraso_mota = max(0, tempo - (distancia / mota['velocidade']))
    tempo_atraso_carro = max(0, tempo - (distancia / carro['velocidade']))

    # Calcular satisfação do cliente considerando a ecologia
    satis_custo_bicicleta = tempo_atraso_bicicleta * bicicleta['poluicao']
    satis_custo_mota = tempo_atraso_mota * mota['poluicao']
    satis_custo_carro = tempo_atraso_carro * carro['poluicao']

    # Escolher meio de transporte com base nas condições
    if peso <= bicicleta['peso_limite'] and tempo_atraso_bicicleta <= tempo:
        return "Bicicleta"
    elif peso <= mota['peso_limite'] and tempo_atraso_mota <= tempo:
        if satis_custo_mota <= satis_custo_carro:
            return "Mota"
        else:
            return "Carro"
    else:
        return "Carro"
    
def calcular_co2_atraso(distancia, tempo, peso, meio_transporte):
    # Características dos meios de transporte
    bicicleta = {'poluicao': 0}
    mota = {'poluicao': 0.3}
    carro = {'poluicao': 2.3}

    # Calcular o atraso em horas no formato HH:MM
    atraso_horas = int(tempo)
    atraso_minutos = int((tempo - atraso_horas) * 60)
    atraso = "{:02}:{:02}".format(atraso_horas, atraso_minutos)

    # Calcular a quantidade de CO2 emitido
    if meio_transporte == "Bicicleta":
        co2_emitido = distancia * bicicleta['poluicao']
    elif meio_transporte == "Mota":
        co2_emitido = distancia * mota['poluicao']
    elif meio_transporte == "Carro":
        co2_emitido = distancia * carro['poluicao']
    else:
        co2_emitido = 0

    return co2_emitido, atraso
