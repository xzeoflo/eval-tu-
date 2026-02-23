import requests

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_data(api_id):
    """ Récupère les données brutes depuis PokeAPI """
    return requests.get(f"{base_url}/pokemon/{api_id}", timeout=10).json()

def get_pokemon_name(api_id):
    """ Récupère le nom d'un pokemon """
    return get_pokemon_data(api_id)['name']

def get_pokemon_stats(api_id):
    """ Récupère les stats et les formate en dictionnaire """
    data = get_pokemon_data(api_id)
    return {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}

def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
    Compare chaque stat 1 par 1.
    Le Pokémon avec le plus de stats supérieures gagne.
    """
    first_score = 0
    second_score = 0

    for stat_name in first_pokemon_stats:
        val1 = first_pokemon_stats.get(stat_name, 0)
        val2 = second_pokemon_stats.get(stat_name, 0)

        if val1 > val2:
            first_score += 1
        elif val2 > val1:
            second_score += 1

    if first_score > second_score:
        return 1  
    elif second_score > first_score:
        return -1 
    return 0      

def battle_pokemon(first_api_id, second_api_id):
    """
    Simule le combat en utilisant la comparaison par duel de stats.
    """
    
    stats1 = get_pokemon_stats(first_api_id)
    stats2 = get_pokemon_stats(second_api_id)
    
    name1 = get_pokemon_name(first_api_id)
    name2 = get_pokemon_name(second_api_id)
    
    battle_result = battle_compare_stats(stats1, stats2)
    
    if battle_result > 0:
        return {"winner": name1, "status": "victory"}
    elif battle_result < 0:
        return {"winner": name2, "status": "victory"}
    else:
        return {"winner": "draw", "status": "tie"}