import string

# Her har jeg defineret de 5 højeste forekommende bogstaver på dansk.
freq = {"E": 16.6, "R": 8.0, "N": 7.7, "T": 7.2, "D": 6.7} #

# Denne funktion tager en liste og et tal og finder det tal i listen som er tættest på talet
def closest(lst, K):   
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

def frek_analyse(txt, alfabet):
    temp = []
    for i in range(0, 25):
        optælling = {bogstav: 0 for bogstav in alfabet}
        for k in txt:
            if k in optælling:
                o = int(hex(ord(k)+i), 16)
                if o > 90: #TODO AUTO detekt tal
                    o -= 26 #TODO AUTO detekt tal
                elif o < 65: #TODO AUTO detekt tal
                    o += 26 #TODO AUTO detekt tal
                optælling[chr(o)] += 1

        for f in freq:
            if optælling[f] != 0:
                try:
                    temp[i] += freq[f]-len(txt)/optælling[f]
                except:
                    temp.append(freq[f]-len(txt)/optælling[f])
        print(f'\nKey {i}: {temp[i]}')

    print(f"Keyen er med stor sandstynlighed: \033[32m {26- temp.index(closest(temp, sum(freq.values())))}→({temp.index(closest(temp, sum(freq.values())))}←)")

    print("\033[00m")

def menu():
    match input("Hvordan vil du indsætte teksten? \n1. Copy Paste (Skal være i en linje)\n2. Fra Fil"):
        case "1":
            txt = input("Ok, paste teksen her: ")
        case "2":
            fil_path = input("Hvor ligger filen? (Default: tekst.txt): ")
            fil_path = "tekst.txt" if fil_path == "" else fil_path
            with open(fil_path, 'r') as file:
                txt = file.read(string.ascii_uppercase)
        case _:
            print("Ugyldigt valg")
            menu()

    match input(f"Hvilket alfabet vil du bruge? (Default: {string.ascii_uppercase}): "):
        case "":
            alf = string.ascii_uppercase
            frek_analyse(txt, alf)

menu()