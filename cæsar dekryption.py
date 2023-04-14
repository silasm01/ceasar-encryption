import string

# Her har jeg defineret de 5 højeste forekommende bogstaver på dansk.
freq = {"E": 16.6, "R": 8.0, "N": 7.7, "T": 7.2, "D": 6.7} #

# Denne funktion tager en liste og et tal og finder det tal i listen som er tættest på talet
def closest(lst, K):   
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

def frek_analyse(txt, alfabet):
    # Laver en liste som skal bruges til at gemme de forskelige keys med optællinger af bogstaverne i dem
    score = []
    # Går igennem alle keys der er op til længden af alfabetet
    for key in range(0, len(alfabet)):
        # Laver en dictionary som bruges til at optælle mængden af hvert tegn
        optælling = {bogstav: 0 for bogstav in alfabet}
        # Går igennem alle tegn i teksten
        for character in txt:
            if character in optælling:
                # Sætter variablen tegn til tegnets index adderet med keyen. Den tjekker også om tegnet er uden for alfabetet og minusser med alfabetes længde.
                tegn = alfabet.index(character)+key if alfabet.index(character)+key < len(alfabet) else alfabet.index(character)+key-len(alfabet)
                optælling[alfabet[tegn]] += 1

        # Går igennem de 5 mest brugte bogstaver i dansk sprog.
        for char_freq in freq:
            if optælling[char_freq] != 0:
                # Optæller hvor mange gange hver af de 5 bogstaver bliver brugt
                try:
                    score[key] += freq[char_freq]-len(txt)/optælling[char_freq]
                except:
                    score.append(freq[char_freq]-len(txt)/optælling[char_freq])
        print(f'\nKey {key}: {score[key]}')

    return score.index(closest(score, sum(freq.values())))

def dekrypter(txt, alfabet, key):
    # Går igennem alle tegn i teksten
    for character in txt:
        # Checker om tegnet er en del af det brugerspecifirede alfabet.
        if character in alfabet:
            # Checker om tegnet rykket tilbage med keyen er under 0 og hvis den er skal den addere længden af alfabetet på.
            if alfabet.index(character)-(len(alfabet)-1-key) > 0:
                print(alfabet[alfabet.index(character)-(len(alfabet)-key)], end ="")
            else:
                print(alfabet[alfabet.index(character)-(len(alfabet)-key)+len(alfabet)], end ="")
        else:
            # Printer alle tegn som ikke er en del af alfabet uden at tilføje en key
            print(character, end ="")

def menu():
    # Tager input fra brugeren
    match input("Hvordan vil du indsætte teksten? \n1. Copy Paste (Skal være i en linje)\n2. Fra Fil"):
        case "1":
            # Gemmer inputet fra brugeren som tekst.
            txt = input("Ok, paste teksen her: ")
        case "2":
            # Tager input fra brugeren om lokationen af filen.
            file_path = input("Hvor ligger filen? (Default: tekst.txt): ")
            # Sætter file_path til default værdien hvis brugeren ikke giver et input
            file_path = "tekst.txt" if file_path == "" else file_path
            # Gemmer filens indhold som tekst
            try:
                with open(file_path, encoding="utf-8") as file: #TODO ERROR HANDLING
                    txt = file.read()
            except:
                print("Filen kunne ikke åbnes prøv igen")
                menu()
        case _:
            # Kører menu() forfra hvis brugeren ikke giver et gyldigt input.
            print("Ugyldigt valg")
            menu()

    # Tager input fra brugeren om alfabetet de vil bruge
    alfabet = input(f"Hvilket alfabet vil du bruge? (Default: {string.ascii_uppercase}): ")
    # Sætter alfabet til default alfabet hvis brugeren ikke giver et input
    alfabet = string.ascii_uppercase if alfabet == "" else alfabet
    # Kører frekvens analysen hvor teksten of alfabetet er sendt med
    key = frek_analyse(txt, alfabet)

    # Dekrypterer teksten hvis brugeren vil
    match input(f"Keyen er med stor sandstynlighed: \033[32m {len(alfabet)- key}→({key}←) \033[00m\nVil du dekryptere teksten? (Y/n) "):
        case "n":
            return
        case _:
            print(dekrypter(txt, alfabet, key))
menu()