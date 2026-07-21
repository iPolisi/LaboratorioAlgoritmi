from abr_base import ABRNormale
from abr_flag import ABRFlag
from abr_lista import ABRLista

def main():
    print("Inizializzazione degli Alberi Binari di Ricerca...")
    
    # Array di test con duplicati (il numero 5 compare 3 volte)
    dati_test = [10, 5, 15, 5, 8, 5, 12]
    print(f"Inserimento dei seguenti dati: {dati_test}\n")

    # Test Normale
    albero_normale = ABRNormale()
    for chiave in dati_test:
        albero_normale.insert(chiave)
    print("1. ABR Normale: popolato con successo.")

    # Test con Flag
    albero_flag = ABRFlag()
    for chiave in dati_test:
        albero_flag.insert(chiave)
    print("2. ABR con Flag: popolato con successo.")

    # Test con Lista
    albero_lista = ABRLista()
    for chiave in dati_test:
        albero_lista.insert(chiave)
    print("3. ABR con Lista: popolato con successo.")

if __name__ == "__main__":
    main()