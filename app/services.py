import random
from app.models import Pokemon, PokemonCache
import pokebase as pb
from sqlalchemy.orm import Session
from app.config import SessionLocal

# a magia do banco de dados
def getDatabase():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# pega um id aleatorio de 1 a 1025
def criaIdAleatorio():
    return random.randint(0, 1025)
    
# cria pb.pokemon por id
# cria pb.pokemon_species por id
def pegaPokemonPorId(id, db: Session):
    # procura no banco pelo id
    cache = db.query(PokemonCache).filter(PokemonCache.nrPokedex == id).first()
    
    # se existir no banco pega de lá e retorna aqui mesmo
    if cache:
        return Pokemon(
            nrPokedex=cache.nrPokedex,
            nome=cache.nome,
            tipo1=cache.tipo1,
            tipo2=cache.tipo2,
            altura=cache.altura,
            peso=cache.peso,
            cor=cache.cor,
            habitat=cache.habitat,
            spriteUrl=cache.spriteUrl
        )
        
    # se nao existir, pega do pb e insere lá
    pkmn = pb.pokemon(id)
    especie = pb.pokemon_species(id)
    pkmnMontado = montaPokemon(pkmn, especie)
    insereCache = PokemonCache(
        nrPokedex=pkmnMontado.nrPokedex,
        nome=pkmnMontado.nomePkmn,
        tipo1=pkmnMontado.tipo1Pkmn,
        tipo2=pkmnMontado.tipo2Pkmn,
        altura=pkmnMontado.alturaPkmn,
        peso=pkmnMontado.pesoPkmn,
        cor=pkmnMontado.corPkmn,
        habitat=pkmnMontado.habitatPkmn,
        spriteUrl=pkmnMontado.spriteUrl
    )
    db.add(insereCache)
    db.commit()
    
    return pkmnMontado

# cria pb.pokemon por nome
# cria pb.pokemon_species por nome
def pegaPokemonPorNome(nome, db: Session):
    # procura no banco pelo nome
    cache = db.query(PokemonCache).filter(PokemonCache.nome == nome).first()
    
    # mesma coisa da outra funcao
    # talvez eu deveria tentar fazer uma funcao pra diminuir codigo repetido?
    # vou pensar nisso depois
    if cache:
        return Pokemon(
            nrPokedex=cache.nrPokedex,
            nome=cache.nome,
            tipo1=cache.tipo1,
            tipo2=cache.tipo2,
            altura=cache.altura,
            peso=cache.peso,
            cor=cache.cor,
            habitat=cache.habitat,
            spriteUrl=cache.spriteUrl
        )
        
    pkmn = pb.pokemon(nome)
    especie = pb.pokemon_species(nome)
    pkmnMontado = montaPokemon(pkmn, especie)
    insereCache = PokemonCache(
        nrPokedex=pkmnMontado.nrPokedex,
        nome=pkmnMontado.nomePkmn,
        tipo1=pkmnMontado.tipo1Pkmn,
        tipo2=pkmnMontado.tipo2Pkmn,
        altura=pkmnMontado.alturaPkmn,
        peso=pkmnMontado.pesoPkmn,
        cor=pkmnMontado.corPkmn,
        habitat=pkmnMontado.habitatPkmn,
        spriteUrl=pkmnMontado.spriteUrl
    )
    db.add(insereCache)
    db.commit()
    
    return pkmnMontado

# basicamente monta o pokemon com base no pb.pokemon e pb.pokemon_species
def montaPokemon(pkmn, especie):
    # circula entre os dois possiveis tipos que um pokemon pode ter
    tipos = [t.type.name for t in pkmn.types]
    # tipo1 nao é checado pois todo pokemon tem tipo 1
    tipo1 = tipos[0]
    # tipo 2 é checado pra ver se existe, caso n seja retorna "n/a"
    tipo2 = tipos[1] if len(tipos) >= 2 else "n/a"
    # altura em metros, por algum motivo o atributo original vem sem decimal??
    altura = f"{pkmn.height / 10}m"
    # peso em kgs, mesmo motivo do de cima
    peso = f"{pkmn.weight / 10}kg"
    # nome da cor em ingles
    cor = especie.color.name
    # nome do habitat em ingles
    # checa se existe pois um pokemon pode nao ter especie
    habitat = especie.habitat.name if especie.habitat else "n/a"
    # pega esse sprite em especifico
    sprite = pkmn.sprites.front_default

    # retorna os atributos instanciando a classe pokemon
    return Pokemon(
        nrPokedex=pkmn.id,
        nome=pkmn.name,
        tipo1=tipo1,
        tipo2=tipo2,
        altura=altura,
        peso=peso,
        cor=cor,
        habitat=habitat,
        spriteUrl=sprite
    )