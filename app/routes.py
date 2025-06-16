from app.services import criaIdAleatorio, pegaPokemonPorId, pegaPokemonPorNome, getDatabase
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()
pokemon_sorteado_da_vez = None

# rota sorteia, deve receber uma requisiçao post sem parametros para sortear
@router.post("/pkmn/sorteia") 
def sorteiaPkmnAleatorio(db: Session = Depends(getDatabase)):
    global pokemon_sorteado_da_vez
    
    # define o pokemon e a pokemon species do pokemon secreto
    idPkmnAleatorio = criaIdAleatorio()
    pokemon_sorteado_da_vez = pegaPokemonPorId(idPkmnAleatorio, db)
    
    return {
        "poggers": "sorteei kk boa sorte"
    }

# rota chute, deve receber o nome do pokemon como um chute
@router.post("/pkmn/chute/{nome}")
def chutePkmnPorNome(nome: str, db: Session = Depends(getDatabase)):
    global pokemon_sorteado_da_vez
    
    # barra se tentar chutar sem sortear primeiro
    if pokemon_sorteado_da_vez is None:
        return {"imbecil": "envia post pra /pkmn/sorteia primeiro"}
    
    # instancia um pokemon novo com base no nome chutado
    chute = pegaPokemonPorNome(nome, db)
    
    # se acertar, mostra o nome do pokemon
    # se errar, mostra quais atributos do chute estavam certos e quais atributos estavam errados
    if chute == pokemon_sorteado_da_vez:
        return {
            "mensagem": f"boa acertou dog o pokemon secreto era {pokemon_sorteado_da_vez.nomePkmn}"
        }
    else:
        resultadoComparacao = chute.comparaComSorteado(pokemon_sorteado_da_vez)
        
        return {
            "Sprite": f"{resultadoComparacao["spriteUrl"]}",
            "Nome": f"{resultadoComparacao["nomePkmn"]}",
            "Tipo 1": f"{resultadoComparacao["tipo1Pkmn"]}",
            "Tipo 2": f"{resultadoComparacao["tipo2Pkmn"]}",
            "Altura": f"{resultadoComparacao["alturaPkmn"]}",
            "Peso": f"{resultadoComparacao["pesoPkmn"]}",
            "Cor": f"{resultadoComparacao["corPkmn"]}",
            "Habitat": f"{resultadoComparacao["habitatPkmn"]}",
            "Geração": f"{resultadoComparacao["geracao"]}"
        }