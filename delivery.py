class Estado:
    def __init__(self, estafetas, encomendas):
        self.estafetas = estafetas
        self.encomendas = encomendas

class Operador:
    def __init__(self, nome, pre_condicoes, efeitos, custo):
        self.nome = nome
        self.pre_condicoes = pre_condicoes
        self.efeitos = efeitos
        self.custo = custo

class Problema:
    def __init__(self, estado_inicial, estado_objetivo, operadores):
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo
        self.operadores = operadores

class No:
    def __init__(self, estado, pai=None, operador=None, custo=0, heuristica=0):
        self.estado = estado
        self.pai = pai
        self.operador = operador
        self.custo = custo
        self.heuristica = heuristica

# Implementação de Busca em Largura
def busca_em_largura(problema):
    fila = [No(problema.estado_inicial)]
    while fila:
        no = fila.pop(0)
        if no.estado == problema.estado_objetivo:
            return no
        for operador in problema.operadores:
            if operador.pre_condicoes(no.estado):
                novo_estado = operador.efeitos(no.estado)
                novo_no = No(novo_estado, pai=no, operador=operador, custo=no.custo + operador.custo)
                fila.append(novo_no)
    return None

# Implementação de A* (busca informada)
def a_estrela(problema, heuristica):
    fila = [No(problema.estado_inicial, heuristica=heuristica(problema.estado_inicial))]
    while fila:
        fila.sort(key=lambda x: x.custo + x.heuristica)
        no = fila.pop(0)
        if no.estado == problema.estado_objetivo:
            return no
        for operador in problema.operadores:
            if operador.pre_condicoes(no.estado):
                novo_estado = operador.efeitos(no.estado)
                novo_no = No(novo_estado, pai=no, operador=operador, custo=no.custo + operador.custo, heuristica=heuristica(novo_estado))
                fila.append(novo_no)
    return None
