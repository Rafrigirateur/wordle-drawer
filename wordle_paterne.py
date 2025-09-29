import datetime
import requests
import os
import json
from PIL import Image
from dessinPaterne import drawPaternWords, drawPatern

reponseAccepteeOUI = ["OUI", "O", "OK", "YES", "Y"]

# Charger le Wordle du jour
try:
    date = datetime.date.today()
    url = f"https://www.nytimes.com/svc/wordle/v2/{date:%Y-%m-%d}.json"
    response = requests.get(url).json()
except:
    print("Le Wordle du jour est inaccessible, vous n'êtes peut-être pas connecté à internet.")
    exit(1)

print("Souhaitez-vous connaître la réponse au Wordle du jour ? : (oui/NON)")
try:
    userInput = input()
except KeyboardInterrupt:
    print("\nVous avez interrompu le programme\n")
    exit(1)

if userInput.upper() in reponseAccepteeOUI:
    print(f"\nRéponse au Wordle du jour : {response['solution']}")

solution = list(str(response['solution']).upper())
if userInput.upper() in reponseAccepteeOUI:
    print(solution)
print("")

# Charger la liste des mots
try:
    with open("combined_wordlist.txt", "r") as f:
        liste_mots = [ligne.strip().upper() for ligne in f if ligne.strip()]
except FileNotFoundError:
    print("Le fichier combined_wordlist.txt est introuvable.")
    exit(1)

# Fonction pour charger un paterne depuis un fichier JSON
def charger_paterne(nom_paterne):
    chemin = os.path.join("paternes", nom_paterne + ".json")
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Le fichier {chemin} est introuvable.")
        return None

# Vérifie qu’un mot correspond au pattern
def estValide(mot, solution, pattern):
    motUtilise = []
    for k in range(5):
        if mot[k] in motUtilise:
            return False
        if pattern[k] == "V":
            if mot[k] != solution[k]:
                return False
        elif pattern[k] == "J":
            motUtilise.append(mot[k])
            if mot[k] == solution[k] or mot[k] not in solution:
                return False
        elif pattern[k] == "G":
            if mot[k] in solution:
                return False
    return True

# Recherche les mots pour un paterne
def motsPaterne(paterne, nom_paterne):
    result = [None] * 6
    for m in range(6):
        found = False
        for mot in liste_mots:
            if estValide(mot, solution, paterne[m]):
                result[m] = mot
                found = True
                break
        if not found:
            print("Aucun mot trouvé pour le pattern :", paterne[m])
            break

    print("Souhaitez-vous afficher (répondre avec 0, 1, 2 ou 3)")
    print("1 : le paterne " + nom_paterne + " seul")
    print("2 : le paterne " + nom_paterne + " avec les lettres")
    print("3 : Les lettres seules pour réaliser le paterne " + nom_paterne)
    print("0 : Ne pas afficher le mot ou le paterne")

    try:
        userInput = input()
    except KeyboardInterrupt:
        print("\nVous avez interrompu le programme\n")
        exit(1)

    if userInput == "1":
        drawPatern(paterne, nom_paterne)
        Image.open(os.path.join("images", nom_paterne + ".png")).show()
    elif userInput == "2":
        drawPaternWords(paterne, result, nom_paterne)
        Image.open(os.path.join("images", nom_paterne + ".png")).show()
    elif userInput == "3":
        print("Voici les mots trouvés pour le paterne " + nom_paterne + " :")
        for mot in result:
            print(mot)
        print("")
    else:
        print("Vous avez choisi de ne pas afficher les mots trouvés\n")

# Lister tous les paternes disponibles dans le dossier "paternes"
def lister_paternes():
    dossier = "paternes"
    fichiers = os.listdir(dossier)
    paternes = [f[:-5] for f in fichiers if f.endswith(".json")]
    return sorted(paternes)

# --- Programme principal ---
liste_paternes = lister_paternes()

if not liste_paternes:
    print("Aucun paterne trouvé dans le dossier 'paternes'.")
    exit(1)


while True:
    print("Paternes disponibles :")
    for i, nom in enumerate(liste_paternes):
        print(f"{i + 1}. {nom}")

    print("\nEntrez le numéro ou le nom du paterne à afficher :")
    choix = input().strip()

    # Identifier le paterne choisi
    nom_selectionne = None
    if choix.isdigit():
        index = int(choix) - 1
        if 0 <= index < len(liste_paternes):
            nom_selectionne = liste_paternes[index]
    else:
        if choix in liste_paternes:
            nom_selectionne = choix

    if nom_selectionne:
        paterne = charger_paterne(nom_selectionne)
        if paterne:
            motsPaterne(paterne, nom_selectionne)
    else:
        break
