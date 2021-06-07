def computer():
    wallet = 5000
    computer_price = 50000

    # le prix de l'ordinateur est inferieur a 1000€
    if computer_price <= wallet or computer_price > 1000:
        print("L'achat est possible")
        wallet -= computer_price
    else:
        print("L'achat est impossible, vous n'avez que {}€".format(
            wallet))  # format va mettre sa valeur dans {} en trouvant le bon format

    text = ("L'achat est possible", "L'achat est impossible")[computer_price <= 1000]  # condition ternaire
    print(text)

    print(wallet)


def mdp():
    # systeme de verification de mdp
    password = input("Entrer votre mot de passe")
    password_length = len(password)

    # verifier si le mot de passe est inferieur a 8 caracteres

    if password_length <= 8:
        print("Mot de passe trop court !")
    elif 8 < password_length < 12:
        print("Mot de passe moyen")
    else:
        print("Mot de passe parfait")

    print(password_length)


def cinema():
    age = int(input("quel age avez vous ? "))
    pop_corn = input("Souhaitez-vous du pop corn ? oui, non ?")
    if age < 18 and pop_corn == "oui":
        print("la place de cinéma est a 7€ car vous avez {} ans plus 5€ pour le pop corn le cinéma vous coute donc 12€".format(age))
    elif age < 18 and pop_corn == "non":
        print("vous avez {} ans la place de cinéma est donc a 7€".format(age))
    elif age >= 18 and pop_corn =="oui":
        print("la place de cinéma est a 12€ car vous avez {} ans plus 5€ pour le pop corn le cinéma vous coute donc 17€".format(age))
    else:
        print("la place de cinéma est a 12€ car vous avez {} ans".format(age))


if __name__ == '__main__':
    # mdp()
    # computer()
    cinema()