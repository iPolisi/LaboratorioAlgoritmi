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
    """
    Esegue il benchmark di inserimento per i tre alberi, misurando tempo e altezza.
    """
    dimensioni = [1000, 5000, 10000]
    percentuali = [0.0, 0.25, 0.50, 0.75, 0.90] # Da 0% a 90% di duplicati
    
    # Intestazione della tabella allargata per includere le altezze (H)
    print(f"{'Dim.':<8} | {'% Dup.':<7} | {'T. Norm (s)':<12} | {'T. Flag (s)':<12} | {'T. Lista (s)':<12} | {'H. Norm':<8} | {'H. Flag':<8} | {'H. Lista':<8}")
    print("-" * 95)
    
    for dim in dimensioni:
        for perc in percentuali:
            dati_test = genera_dati(dim, perc)
            
            # Test ABR Normale
            abr_normale = ABRNormale()
            inizio = time.perf_counter()
            for chiave in dati_test:
                abr_normale.insert(chiave)
            tempo_normale = time.perf_counter() - inizio
            alt_normale = abr_normale.get_altezza()
            
            # Test ABR Flag
            abr_flag = ABRFlag()
            inizio = time.perf_counter()
            for chiave in dati_test:
                abr_flag.insert(chiave)
            tempo_flag = time.perf_counter() - inizio
            alt_flag = abr_flag.get_altezza()
            
            # Test ABR Lista
            abr_lista = ABRLista()
            inizio = time.perf_counter()
            for chiave in dati_test:
                abr_lista.insert(chiave)
            tempo_lista = time.perf_counter() - inizio
            alt_lista = abr_lista.get_altezza()
            
            # Stampa dei risultati formattati
            print(f"{dim:<8} | {perc*100:<6.0f}% | {tempo_normale:<12.6f} | {tempo_flag:<12.6f} | {tempo_lista:<12.6f} | {alt_normale:<8} | {alt_flag:<8} | {alt_lista:<8}")