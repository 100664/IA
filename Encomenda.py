class Encomenda:

    total_encomendas = 0 

    def __init__(self, peso, volume, tempo, morada):
        Encomenda.total_encomendas += 1
        self.id = Encomenda.total_encomendas 
        self.peso = peso
        self.volume = volume
        self.tempo = tempo
        self.morada = morada
    
    def __repr__(self):
        return f"Encomenda(ID={self.id}, Morada={self.morada})"

    def get_peso(self):
        return self.peso

    def get_volume(self):
        return self.volume

    def get_id(self):
        return self.id

    def get_tempo(self):
        return self.tempo

    def get_morada(self):
        return self.morada
    
