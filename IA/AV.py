from random import randint
from Listes import *


def av_mode():
    print("Sortie des commandes simples ! \nBienvenu dans le mode Assistant virtuel, où les réponses seront générés par"
          "Intelligence Artificiel !\nVous pouvez le quitter à n'importe quel moment en tapant STOP !")
    file = open(f"{chemin}/current_user.txt", "r")
    informations = file.readlines()
    file.close()
    current_pseudo = informations[0].strip()
    tutoiement = False
    if informations[1].strip() == "tutoiement":
        tutoiement = True
    elif informations[1].strip() == "vouvoiement":
        tutoiement = False
    x = randint(0, 5)
    print(f"Itarra : {hello_Itarra[x]} !")
    fin = False
    while not fin:
        if tutoiement:
            reponse = str(input(f"Oui {current_pseudo} ? ")).split(" ")
        elif not tutoiement:
            reponse = str(input(f"Avez-vous besoin de quelque chose {current_pseudo} ?")).split(" ")

        x = 0;
        file = open(f"{chemin}/IA/Vocabulaire/nourriture.txt", "r")
        nourriture = file.readlines()
        file.close()
        file = open(f"{chemin}/IA/Vocabulaire/Itarra.txt", "r")
        target_itarra_list = file.readlines()
        file.close()
        file = open(f"{chemin}/IA/Vocabulaire/user.txt", "r")
        target_user_list = file.readlines()
        file.close()

        print(nourriture)
        print(target_user_list)
        print(target_itarra_list)
        topic_nourriture = False
        target_user = False
        target_itarra = False

        for x in range(len(reponse)):

            print(reponse[x])
            #Recherche thème de la phrase

            if f"{reponse[x]}\n" in nourriture:
                topic_nourriture = True


            #Recherche cible de la phrase

            elif f"{reponse[x]}\n" in target_itarra_list:
                target_itarra = True
            elif f"{reponse[x]}\n" in target_user_list:
                target_user = True


            #Commande menu

            elif reponse in annulation:
                fin = True

            #Apprentissage des mots inconnues

            else:
                if tutoiement:
                    print(f"{current_pseudo}, je connais pas ce mot : {reponse[x]}!! Apprend-le moi !")
                elif not tutoiement:
                    print(f"{current_pseudo}, je ne connais pas ce mot : {reponse[x]}, pouvez-vous me l'apprendre ?")

                file = open(f"{chemin}/IA/nametest.txt", "r")
                informations = file.readlines()
                file.close()
                len_file = 0
                for len_file in range(len(informations)):
                    print(f"Catégorie n°{len_file}: {informations[len_file]}\n")
                reponse_valide = False
                while not reponse_valide:
                    if tutoiement:
                        reponse2 = str(input("Dis moi s'il correspond à une de ces catégories !")).split(" ")
                    elif not tutoiement:
                        reponse2 = str(input("Dites-moi si l'une de ces catégories correspond au mot !")).split(" ")
                    test = 0
                    ncategorie = 0
                    for test in range(len(reponse)-1):
                        print(test)
                        if reponse2[test] in nombres :
                            ncategorie = int(reponse2[test])
                            if ncategorie > len(informations):
                                if tutoiement:
                                    print("Je crois que tu as dû te tromper, le chiffre que tu as entrée ne correspond"
                                          " à aucune de ces catégories!")
                                elif not tutoiement:
                                    print("Votre réponse ne correspond à aucune des catégories !")
                            else:
                                reponse_valide = True
                                if tutoiement:
                                    print("Ok, merci, je note ! ;)")
                                elif not tutoiement:
                                    print("Très bien, merci, je rajoute ce mot dans ma mémoire.")

                                file = open(f"{chemin}/IA/Vocabulaire/{informations[ncategorie].strip()}.txt", "a")
                                file.write(f"{reponse[x]}\n")
                                file.close()
                        elif reponse2[test] in non:
                            print("(PASSAGE DEV) Toute entrée est importante pour l'évolution d'Itarra, elle doit donc "
                                  "être pris sérieusement et avec rigueur !")
                            reponse2 = str(input("Ecris le nom d'une catégorie, qui correspondrait "
                                                 "au mot : ")).split(" ")
                            file = open(f"{chemin}/IA/Vocabulaire/{reponse2}.txt", "w+")
                            file.write(reponse[x])
                            file.close()
                            file = open(f"{chemin}/IA/nametest.txt", "a")
                            file.write(reponse2)
                            file.close()