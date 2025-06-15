from sqlalchemy import Column, String, Integer
from app.config import Base

# declara uma classe com os atributos relevantes do pokemon
# sujeito a mudanças eu acho

class Pokemon:
    def __init__(self, nome, tipo1, tipo2, altura, peso, cor, habitat):
        self.nomePkmn = nome
        self.tipo1Pkmn = tipo1
        self.tipo2Pkmn = tipo2
        self.alturaPkmn = altura
        self.pesoPkmn = peso
        self.corPkmn = cor
        self.habitatPkmn = habitat
        
    # compara os atributos da instancia com outra instancia
    # fiz isso tendo em vista q a primeira instancia vai ser sempre o chute e a segunda instancia vai ser sempre o sorteado
    # entao meio que acaba sendo comparar o chute com o sorteado
    # meio autoexplicativo
        
    def comparaComSorteado(self, sorteado):
        resultado = {}
        for atributo in ["nomePkmn", "tipo1Pkmn", "tipo2Pkmn", "alturaPkmn", "pesoPkmn", "corPkmn", "habitatPkmn"]:
            # S se acertou
            # N se errou
            resultado[atributo] = "S" if getattr(self, atributo) == getattr(sorteado, atributo) else "N"
        return resultado
    
# declara tabela de cache postgresql

class PokemonCache(Base):
    __tablename__ = "pokemonCache"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    tipo1 = Column(String)
    tipo2 = Column(String)
    altura = Column(String)
    peso = Column(String)
    cor = Column(String)
    habitat = Column(String)