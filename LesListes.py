from statistics import mean
from random import shuffle


def players():
    online_players = ["Yvan", "Anana", "Cleymax", "Bob"]
    print(online_players)
    print(online_players[0])
    print(online_players[len(online_players) - 1])

    # modifier pseudo de la liste
    online_players[0] = "YvanIkse"
    online_players.insert(2, "Morice")

    print(online_players[0])

    # en ajouter d'autre
    # on imagine qu'un joueur "Gameur123" se connecte
    online_players.append("Gameur123")
    online_players.extend(["Gogo", "babard"])

    print(online_players)

    # le joueur Anana se deco 2 facon de le supprimer de la lisye del ou pop
    del online_players[1]
    online_players.pop(1)

    # si vous souhaitez supprimer tout les elements de la liste
    online_players.clear()

    print(online_players)


def notation():
    notes = [
        8, 12, 10,
        9, 4, 20,
        14, 12, 1
    ]
    print(notes)
    shuffle(notes)  # melange la liste
    print(notes)
    # module : statistics mean fais la moyenne
    result = mean(notes)
    print("la moyenne de l'élève est de {}".format(result))


def text():
    text = input("Entrer une chaine de la forme (email-pseudo-mdp)").split("-")
    print(text)
    print("Salut {}, ton email {}, ton mot de passe {}".format(text[1], text[0], text[2]))


def tp_liste():
    generateur_phrases = input("donner un ou plusieurs mots sous la forme mot1/mot2/mot3/mot4/...").split("/")
    print(generateur_phrases)
    shuffle(generateur_phrases)
    print(generateur_phrases)

    generateur_len = len(generateur_phrases)
    if generateur_len < 10:
        print(generateur_phrases[0], generateur_phrases[1])
    else:
        print(generateur_phrases[len(generateur_phrases) - 1], generateur_phrases[len(generateur_phrases) - 2],
              generateur_phrases[len(generateur_phrases) - 3])


if __name__ == '__main__':
    # players()
    # notation()
    # text()
    tp_liste()
