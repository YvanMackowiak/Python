from random import randint


def boucle():
    # for : pour une valeur de départ (1) jusqu'a une valeur d'arriver (6) -1
    for num_client in range(1, 6):
        print("vous etes le client n°", num_client)

    # for each : pour chaque valeur d'une liste données
    blacklist = ["bouba@babou.fr", "yvanikse@gmail.com"]
    emails = ["yvanmackowiak@gmail.com", "yvansimpson@gmail.com", "bouba@babou.fr", "yvanikse@gmail.com"]

    for email in emails:
        if email in blacklist:
            print("Email {} interdit ! envoi impossible ...".format(email))
            break

        print("Email envoyé a:", email)

    # while : tant qu'une condition est vrai
    salary = 1500

    # tant que salaire < 2000€ , +120€
    while salary < 2000:
        # ajouter 120€ au salaire
        salary += 120
        print("votrre salaire et de ", salary, "€")

    print("Fin du programme")

    # un youtubeur Morice , 2500 abo
    suscribers_count = 2500

    # il gagne 10% d'audience sup par mois
    months = 0

    # on souhaite estimer, combien aura t'il d'abonnés aprés 2 ans (24mois)
    while months <= 24:
        # augmenter l'audience
        suscribers_count *= 1.10

        # afficher le nbr d'abonnée
        print("Vous avez actuellement {} abonnés !".format(suscribers_count))

        # on passe au mois suivant
        months += 1


def justePrix():
    # choisir un nombre aleatoire entre 1 et 1000
    just_price = randint(1, 1000)

    # statut du jeu (activé/désactivé)
    running = True

    # tant que le jeu est en cours d'éxécution
    while running:

        # demander à l'utilisateur d'entrer un prix dans la console
        user_price = int(input("Entrer un prix"))

        # si le prix est le meme que le juste prix
        if user_price == just_price:
            print("Trouvé !")
            # fin du jeu
            running = False

        # si le prix de l'utilisateur est supérieur au prix à trouver
        elif user_price > just_price:
            print("C'est moins")

        # si le prix de l'utilisateur est inférieur au prix à trouver
        elif user_price < just_price:
            print("C'est plus")

    # fin du jeu après la boucle
    print("Fin du jeu !")


if __name__ == '__main__':
    # boucle()
    justePrix()