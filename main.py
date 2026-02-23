"""This is the main entry point of the application,
 where the FastAPI app is created and the API routers for trainers, pokemons, and items are included with their respective prefixes."""
from fastapi import FastAPI
from app.routers import trainers, pokemons, items


app = FastAPI()


app.include_router(trainers.router,
                   prefix="/trainers")
app.include_router(items.router,
                   prefix="/items")
app.include_router(pokemons.router,
                   prefix="/pokemons")
