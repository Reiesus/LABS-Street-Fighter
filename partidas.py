from typing import NamedTuple,List, Tuple
from collections import defaultdict
import csv
from datetime import *
 
Partida = NamedTuple("Partida", [
    ("pj1", str),
    ("pj2", str),
    ("puntuacion", int),
    ("tiempo", float),
    ("fecha_hora", datetime),
    ("golpes_pj1", List[str]),
    ("golpes_pj2", List[str]),
    ("movimiento_final", str),
    ("combo_finish", bool),
    ("ganador", str),
    ])



def lee_partidas(ruta:str)->List[Partida]:
    res=list()
    with open(ruta, encoding='utf-8')as f:
        lector=csv.reader(f)
        next(lector)
        for pj1,pj2,puntuacion,tiempo,fecha_hora,golpes_pj1,golpes_pj2,movimiento_final,combo_finish,ganador in lector:
            res.append(Partida(pj1,pj2,int(puntuacion),float(tiempo),
                               datetime.strptime(fecha_hora,"%Y-%m-%d %H:%M:%S"), 
                               parseaLista(golpes_pj1),
                               parseaLista(golpes_pj2), movimiento_final,
                               parseaBool(combo_finish),ganador))
    return res

def parseaBool(c:str)->bool:
    return c=="1"

def parseaLista(g:str)->List[str]:
    res=list()
    partes=g.replace("[","").replace("]","").split(',')
    for f in partes:
        res.append(f.strip())
    return res

def victora_mas_rapida (partidas:List[Partida])->Tuple[str,float]:
    maximo=partidas[0]
    for p in partidas:
        if p.tiempo<maximo.tiempo:
            maximo=p
    return (maximo.pj1,maximo.pj2,maximo.tiempo)

def top_ratio_medio_personajes(partidas: List[Partida], n: int) -> List[str]:
    suma_ratios = defaultdict(float)
    victorias = defaultdict(int)

    for p in partidas:
        ratio = p.puntuacion / p.tiempo
        if p.ganador == p.pj1:
            suma_ratios[p.pj1] += ratio
            victorias[p.pj1] += 1
        elif p.ganador == p.pj2:
            suma_ratios[p.pj2] += ratio
            victorias[p.pj2] += 1

    medias = {
        personaje: suma_ratios[personaje] / victorias[personaje]
        for personaje in suma_ratios
        if victorias[personaje] > 0
    }

    ordenados = sorted(medias.items(), key=lambda x: x[1]) 
    return [nombre for nombre, _ in ordenados[:n]]


def enemigos_mas_debiles (partidas:List[Partida], personaje:str)->Tuple[List[str],List[int]]:
    res=defaultdict(int)
    for p in partidas:
        if p.ganador==personaje:
            if personaje==p.pj1:
                res[p.pj2]+=1
            if personaje==p.pj2:
                res[p.pj1]+=1
        
    if not res:
        return ([], 0)
    
    max_victorias = max(res.values())
    enemigos = [enemigo for enemigo, v in res.items() if v == max_victorias]

    return (enemigos, max_victorias)

def movimientos_comunes(partidas: List[Partida], personaje1: str, personaje2: str) -> List[str]:
    res = list()
    for p in partidas:
        if (p.pj1 == personaje1 and p.pj2 == personaje2):
            for g1 in p.golpes_pj1:
                for g2 in p.golpes_pj2:
                    if g1 == g2 and g1 not in res:
                        res.append(g1)
    return res

def dia_mas_combo_finish(partidas: List[Partida]) -> str:
    res = defaultdict(int)
    for p in partidas:
        if p.combo_finish:
            res[dia_semana(p.fecha_hora.weekday())] += 1
    if not res:
        return "No hay combos finish registrados"
    return max(res.items(), key=lambda x: x[1])[0]

def dia_semana(dia: int) -> str:
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return dias[dia] if 0 <= dia <= 6 else "Día inválido"
