"""Schemas Pydantic pour les modèles de données de l'application."""
from datetime import date
from typing import  List, Optional, Union
from pydantic import BaseModel

#
#  ITEM
#
class ItemBase(BaseModel):
    """Base schema for items."""
    name: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    """Schema for creating an item."""
    pass

class Item(ItemBase):
    """Schema for reading an item from the database."""
    id: int
    trainer_id: int

    class Config:
        """Enable ORM mode for compatibility with SQLAlchemy models."""
        orm_mode = True

#
#  POKEMON
#
class PokemonBase(BaseModel):
    """Base schema for pokemons."""
    api_id: int
    custom_name: Optional[str] = None

class PokemonCreate(PokemonBase):
    """Schema for creating a pokemon."""
    pass

class Pokemon(PokemonBase):
    """Schema for reading a pokemon from the database."""
    id: int
    name: str
    trainer_id: int
    stats: Optional[dict] = None

    class Config:
        """Enable ORM mode for compatibility with SQLAlchemy models."""
        orm_mode = True
#
#  TRAINER
#
class TrainerBase(BaseModel):
    """Base schema for trainers."""
    name: str
    birthdate: date

class TrainerCreate(TrainerBase):
    """Schema for creating a trainer."""
    pass

class Trainer(TrainerBase):
    """Schema for reading a trainer from the database, including related items and pokemons."""
    id: int
    inventory: List[Item] = []
    pokemons: List[Pokemon] = []

    class Config:
        """Enable ORM mode for compatibility with SQLAlchemy models."""
        orm_mode = True
