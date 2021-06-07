def main():
    wallet = int(input("Combien d'argent avez vous dans votre porte monnaie ? "))
    video_games = int(50)
    new_wallet = wallet - video_games

    if wallet >= video_games:
        print(
            "vous aviez " + str(wallet) + "€ une fois le jeux video acheter il vous reste " + str(new_wallet) + "€ ")
    else:
        print("vous n'avez pas suffisament d'argent pour acheter votre jeux cellui ci coute "+ str(video_games) + " et vous avez "+str(wallet))


if __name__ == '__main__':
    main()
