`J'ai adapté ce bot afin qu'il fonctionne à l'aide d'une commande discord via un bot mais je n'ai pas encore trouvé d'hébergeur pour le faire fonctionner 24h/24.
Cela arrivera incessament sous peu, merci de votre compréhension.`

Ce projet permet de générer des **motifs (paternes)** personnalisés à partir du Wordle du jour, en utilisant une base de mots et des fichiers JSON pour stocker les formes.

Les paternes sont affichés sous forme d’images similaires à une grille Wordle, avec la possibilité de :

* Voir uniquement le paterne coloré
* Voir le paterne coloré avec les mots associés
* Voir uniquement les mots nécessaires pour construire le paterne

---

## 📂 Structure du projet

```
.
├── wordle_paterne.py      # Programme principal
├── dessinPaterne.py       # Fonctions pour dessiner les paternes
├── combined_wordlist.txt  # Liste de mots pour générer les paternes
├── paternes/              # Dossier contenant les paternes en JSON
│   ├── zeub.json
│   ├── zeub_vert.json
│   ├── coeur.json
│   ├── epee.json
│   ├── croix.json
│   ├── croix_inversee.json
│   └── tree.json
└── images/                # Dossier généré automatiquement pour stocker les images créées
```

---

## ⚙️ Installation

### 1. Cloner le projet

```bash
git clone <url_du_projet>
cd <nom_du_dossier>
```

### 2. Créer un environnement virtuel (optionnel mais recommandé)

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

Si tu n’as pas encore de `requirements.txt`, voici son contenu minimal :

```txt
Pillow
requests
```

---

## 🚀 Utilisation

Lancer le programme principal :

```bash
python wordle_paterne.py
```

### Étapes :

1. Le programme récupère le **Wordle du jour** depuis le site du New York Times.
2. Il te demande si tu veux voir la solution du jour.
3. Il affiche la liste des paternes disponibles (fichiers JSON dans `paternes/`).
4. Tu peux choisir un paterne soit par **numéro**, soit par **nom**.
5. Tu choisis ensuite comment afficher le paterne :

   * `1` : seulement le paterne en couleurs
   * `2` : le paterne avec les mots trouvés
   * `3` : uniquement les mots utilisés
   * `0` : ne rien afficher

Les images générées sont automatiquement sauvegardées dans le dossier `images/`.

---

## 📄 Exemple de fichier JSON

Chaque paterne est défini dans un fichier `.json`. Exemple avec **coeur.json** :

```json
[
    ["G", "J", "G", "J", "G"],
    ["J", "G", "J", "G", "J"],
    ["J", "G", "G", "G", "J"],
    ["G", "J", "G", "J", "G"],
    ["G", "G", "J", "G", "G"],
    ["V", "V", "V", "V", "V"]
]
```

* `V` = Vert (lettre correcte à la bonne place)
* `J` = Jaune (lettre correcte à la mauvaise place)
* `G` = Gris (lettre absente)

---

## 🖼️ Exemple de rendu

Quand tu choisis le paterne `coeur`, tu obtiens une image comme :

<img width="339" height="405" alt="heart_wordle_paterne" src="https://github.com/user-attachments/assets/7fa7a538-d1e4-42dd-b3c4-11a6132e5571" /><img width="339" height="405" alt="SPOILER_heart_wordle_paterne" src="https://github.com/user-attachments/assets/3c505393-23a7-4c62-bdcd-b5444091b600" />

*(les couleurs sont affichées dans une image PNG dans `/images/`)*

---

## 🛠️ Améliorations possibles

* Ajouter de nouveaux paternes en créant simplement un fichier `.json` dans `paternes/`.
* Permettre de charger plusieurs paternes à la suite.
* Créer une interface graphique (Tkinter, PyQt, ou autre).

---
