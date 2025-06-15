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
            "nomePkmn": f"{resultadoComparacao["nomePkmn"]}",
            "tipo1Pkmn": f"{resultadoComparacao["tipo1Pkmn"]}",
            "tipo2Pkmn": f"{resultadoComparacao["tipo2Pkmn"]}",
            "alturaPkmn": f"{resultadoComparacao["alturaPkmn"]}",
            "pesoPkmn": f"{resultadoComparacao["pesoPkmn"]}",
            "corPkmn": f"{resultadoComparacao["corPkmn"]}",
            "habitatPkmn": f"{resultadoComparacao["habitatPkmn"]}"
        }