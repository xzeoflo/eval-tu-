from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app import actions, schemas
from app.utils.utils import get_db
from app.utils.pokeapi import get_pokemon_stats

router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all pokemons
        Default limit is 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons

@router.get("/stats", response_model=List[schemas.Pokemon])
def get_pokemons_stats(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
    Récupère les pokémons en DB et injecte les stats de l'API pour chacun
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    
    for pokemon in pokemons:
        pokemon.stats = get_pokemon_stats(pokemon.api_id)
        
    return pokemons
