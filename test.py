def main():
    # recolter une premier note
    note1 = int(input("Entrer la premiere note"))
    # recolter une seconde note
    note2 = int(input("Entrer la seconde note"))
    # recolter une troisieme note
    note3 = int(input("Entrer la dernier note"))
    # calculer la moyenne
    result = (note1 + note2 + note3) / 3
    # afficher le resultat
    print("La moyenne de l'élève est de " + str(result))


if __name__ == '__main__':
    main()