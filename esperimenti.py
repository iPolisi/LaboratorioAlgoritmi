import random
import time
from abr_normale import ABRNormale
from abr_flag import ABRFlag
from abr_lista import ABRLista

def genera_dati(dimensione, perc_duplicati):
    
    num_unici = int(dimensione * (1 - perc_duplicati))
    if num_unici == 0:
        num_unici = 1 
        
    
    chiavi_uniche = random.sample(range(dimensione * 10), num_unici)
    dati = list(chiavi_uniche)
    
    
    duplicati_necessari = dimensione - num_unici
    for _ in range(duplicati_necessari):
        dati.append(random.choice(chiavi_uniche))
        
    
    random.shuffle(dati)
    return dati

def esegui_test_inserimento():
   
    dimensioni = [1000, 5000, 10000]
    percentuali = [0.0, 0.25, 0.50, 0.75, 0.90] 
    
    print(f"{'Dimensione':<12} | {'% Duplicati':<12} | {'Normale (s)':<15} | {'Flag (s)':<15} | {'Lista (s)':<15}")
    print("-" * 75)
    
    for dim in dimensioni:
        for perc in percentuali:
            
            dati_test = genera_dati(dim, perc)
            
            
            abr_normale = ABRNormale()
            inizio = time.perf_counter()
            for chiave in dati_test:
                abr_normale.insert(chiave)
            tempo_normale = time.perf_counter() - inizio
            
            
            abr_flag = ABRFlag()
            inizio = time.perf_counter()
            for chiave in dati_test:
                abr_flag.insert(chiave)
            tempo_flag = time.perf_counter() - inizio
            
            
            abr_lista = ABRLista()
            inizio = time.perf_counter()
            for chiave in dati_test:
                abr_lista.insert(chiave)
            tempo_lista = time.perf_counter() - inizio
            
            print(f"{dim:<12} | {perc*100:<11.0f}% | {tempo_normale:<15.6f} | {tempo_flag:<15.6f} | {tempo_lista:<15.6f}")