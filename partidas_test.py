from partidas import *
from typing import List

def test_lee_partidas(ruta:str):
    partidas = lee_partidas(ruta)
    print("1. Test de lee_peliculas:")
    print(f"Total registros leídos: {len(partidas)}")
    print("Mostrando los tres primeros registros:")
    for p in partidas[:3]:
        print(f"         {p}")

def test_victoria_mas_rapida(partidas: List[Partida]):
    res = victora_mas_rapida(partidas)
    pj1, pj2, tiempo = res
    print("\n2. Test victora_mas_rapida")
    print(f"La partida más rápida fue una entre {pj1} y {pj2} que duró {tiempo} segundos.")

def test_top_ratio_medio_personajes(partidas: List[Partida]):
    top3 = top_ratio_medio_personajes(partidas, 3)
    print("\n3. Test de top_ratio_medio_personajes")
    print(f"El top 3 de ratios medios es: {top3}")

def test_enemigos_mas_debiles(partidas: List[Partida], personaje: str):
    enemigos, n_victorias = enemigos_mas_debiles(partidas, personaje)
    print("\n4. Test de enemigo_mas_debil")
    print(f"Los enemigos más débiles de {personaje} son ({enemigos}, {n_victorias})")

def test_movimientos_comunes(partidas: List[Partida], pj1: str, pj2: str):
    comunes = set(movimientos_comunes(partidas, pj1, pj2))    
    print("\n5. Test de movimientos_comunes")
    print(f"Los movimientos repetidos entre {pj1} y {pj2} son: {comunes}")

def test_dia_mas_combo_finish(partidas: List[Partida]):
    dia = dia_mas_combo_finish(partidas)
    print("\n6. Test de dia_mas_combo_finish")
    print(f"El día que más Ultra Combo Finish ha habido es el {dia}")

if __name__ == "__main__":
    ruta = "data/games.csv"
    partidas = lee_partidas(ruta)

    test_lee_partidas(ruta)
    test_victoria_mas_rapida(partidas)
    test_top_ratio_medio_personajes(partidas)
    test_enemigos_mas_debiles(partidas, "Ken")
    test_movimientos_comunes(partidas, "Ryu", "Ken")
    test_dia_mas_combo_finish(partidas)
