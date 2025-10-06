def carica_da_file(file_path):
    """Carica i libri dal file"""
    # TODO
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            righe = [riga.strip() for riga in f if riga.strip()]
    except FileNotFoundError:
        return None

    try:
        n_sezioni = int(righe[0])
    except ValueError:
        return None

    biblioteca = [[] for _ in range(n_sezioni)]

    for riga in righe[1:]:
        parti = [p.strip() for p in riga.split(",")]
    if len(parti) != 5:
        return None
    titolo, autore, anno, pagine, sezione = parti
    try:
        anno = int(anno)
        pagine = int(pagine)
        sezione = int(sezione)
    except ValueError:
        return None

    if 1 <= sezione <= n_sezioni:
        libro = {
            "titolo": titolo,
            "autore": autore,
            "anno": anno,
            "pagine": pagine,
            "sezione": sezione
        }
    biblioteca[sezione - 1].append(libro)

    return biblioteca



def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
#"""Aggiunge un libro nella biblioteca"""
    # TODO
    if not (1 <= sezione <= len(biblioteca)):
        return None


    for sezione_libri in biblioteca:
        for libro in sezione_libri:
            if libro["titolo"].lower() == titolo.lower():
                return None


    nuovo_libro = {
    "titolo": titolo,
    "autore": autore,
    "anno": anno,
    "pagine": pagine,
    "sezione": sezione
    }


    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"{titolo},{autore},{anno},{pagine},{sezione}\n")
    except FileNotFoundError:
        return None


    biblioteca[sezione - 1].append(nuovo_libro)
    return nuovo_libro

def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO
    titolo = print("nome del libro")
    for sezione in biblioteca:
        for libro in sezione:
            if libro["titolo"].lower() == titolo.lower():
                return f"{libro['titolo']}, {libro['autore']}, {libro['anno']}, {libro['pagine']}, {libro['sezione']}"


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    if not (1 <= sezione <= len(biblioteca)):
        return None
    titoli = [libro["titolo"] for libro in biblioteca[sezione - 1]]
    return sorted(titoli)

def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print("Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

  
