from Listes import *
from Lecture_vocalearn import lecture_vocalearn
from Modif_Vocalearn import modif_vocalearn
import os


def vocalearn():
    chemin = os.getcwd()
    if os.path.exists(f"{chemin}/Listes Vocalearn"):
        print("Listes trouvées !")
    else:
        os.mkdir(f"{chemin}/Listes Vocalearn")
    file = open("current_user.txt", "r")
    informations = file.readlines()
    current_pseudo = informations[0].strip()
    if informations[1].strip() == "tutoiement":
        tutoiement = True
    else:
        tutoiement = False
    file.close()
    print(f"Bienvenue dans le mode d'apprentissage, {current_pseudo}")
    reponse = ""
    reponse_valide = False
    here_creation = False
    here_voir = False
    while not reponse_valide:
        lecture_liste = False
        if tutoiement:
            reponse = str(input("Est-ce qu'il existe déjà une liste de vocabulaire que tu souhaites apprendre "
                                "maintenant ? --> "))
        elif not tutoiement:
            reponse = str(input("Les termes que vous souhaitez acquérir sont-ils déjà enregistré ? --> "))
        if reponse in oui:
            lecture_vocalearn()
            reponse_valide = True
            lecture_liste = True
        elif reponse in non:
            fin = False
            while not fin:
                reponse_valide = False
                reponse_valide3 = False
                while not reponse_valide3:
                    if tutoiement:
                        reponse = str(input("Souhaites-tu voir les listes déjà faites ou bien en créer une autre, "
                                            "toute neuve ou encore en modifier une autre ? --> ")).split(" ")
                    elif not tutoiement:
                        reponse = str(input("Souhaitez-vous prendre connaissance des listes déjà existante ou voulez "
                                            "vous en créer une autre ou encore en modifier une autre ? --> ")).split(" ")
                    test = 0
                    for test in range(len(reponse)):
                        if reponse[test] in creation:
                            reponse_valide3 = True
                            here_creation = True
                        elif reponse[test] in voir:
                            reponse_valide3 = True
                            here_voir = True
                        elif reponse[test] in modification:
                            reponse_valide3 = True
                            modif_vocalearn()
                    if not reponse_valide3:
                        print(f"Votre réponse doit contenir les termes suivant : \n     -Pour créer une nouvelle "
                              f"liste:\n {creation}\n   -Pour connaître les listes déjà existante:\n        {voir}")
                        reponse_valide = False
                file = open("listes_existantes.txt", "r")
                informations = file.read()
                file.close()
                if here_voir:
                    print(f"Voici toutes les listes déjà enregistrée\n {informations}")
                    lecture_liste = True
                    fin = True
                elif here_creation:
                    reponse_valide = False
                    while not reponse_valide:
                        if tutoiement:
                            print("Bon bah, plus qu'à en créer une !")
                            reponse = str(input("Tu l'appelles comment ta liste ? --> "))
                        elif not tutoiement:
                            print("D'accord, alors créons-en une !")
                            reponse = str(input("Comment souhaitez-vous nommer votre liste ? --> "))
                        if reponse in informations:
                            reponse_valide = False
                            print(
                                f"Titre déjà existant ! Merci de ne pas créer de titre en double !\n Voici le nom des "
                                f"listes déjà existante : \n {informations}")
                        elif reponse not in informations:
                            reponse_valide = True
                    file = open("listes_existantes.txt", "a")
                    file.write(f"{reponse}\n")
                    file.close()
                    file = open(f"{chemin}/Listes Vocalearn/{reponse}.txt", "w+")
                    reponse_valide = False
                    nb_terme = 0
                    while not reponse_valide:
                        nb_terme = nb_terme + 1
                        reponse_valide2 = False
                        while not reponse_valide2:
                            if tutoiement:
                                reponse = str(input(f"Entre le terme n°{nb_terme} --> "))
                            elif not tutoiement:
                                reponse = str(input(f"Entrez le terme n°{nb_terme} --> "))
                            if len(reponse) < 2:
                                print("Nombre de caractère insuffisant ! Merci de mettre au moins 1 caractère !")
                                reponse_valide2 = False
                            elif len(reponse) >= 2:
                                reponse_valide2 = True
                        reponse_valide2 = False
                        file.write(reponse)
                        file.write("\n")
                        while not reponse_valide2:
                            if tutoiement:
                                reponse = str(input(f"Entre la définition ou la traduction du terme n°{nb_terme} -->"))
                            elif not tutoiement:
                                reponse = str(input(f"Entrez la définition ou la traduction du terme n°{nb_terme} -->"))
                            if len(reponse) < 2:
                                print("Nombre de caractère insuffisant ! Merci de mettre au moins 1 caratère !")
                                reponse_valide2 = False
                            elif len(reponse) >= 2:
                                reponse_valide2 = True
                        file.write(reponse)
                        file.write("\n")
                        file.write(f"0\n")
                        reponse_valide2 = False
                        while not reponse_valide2:
                            if nb_terme == 1:
                                reponse = str(input("Un autre ? Pour créer un autre terme, vous pouvez taper "
                                                    "sur ENTER, directement !"))
                                if reponse in oui:
                                    print("Alors ça marche que pour cette fois, il faudrait lire la "
                                          "consigne précédente")
                                    reponse_valide = False
                                    reponse_valide2 = True
                                elif len(reponse) <= 2:
                                    print("Ok, nice, je vois que tu as tout compris")
                                    reponse_valide = False
                                    reponse_valide2 = True
                                elif reponse in non or reponse in annulation:
                                    print("Au moins ce sera facile à apprendre ! Tu pourras retrouver ta liste en la "
                                          "redemandant au tout début du programme d'apprentissage")
                                    reponse_valide = True
                                    reponse_valide2 = True
                                else:
                                    if tutoiement:
                                        print("Ouah, je pensais pas bloquer sur une question si simple, mais la je "
                                              "comprends pas ta réponse !! C'est Oui ou bien c'est Non ! Ou Enter!")
                                    elif not tutoiement:
                                        print("Je ne comprends pas votre réponse, vous pouvez répondre par Oui NON "
                                              "ou bien en appuyant sur la touche enter")
                                    reponse_valide2 = False
                            elif nb_terme > 1:
                                reponse = str(input("Un autre ?"))
                                if reponse in non or reponse in annulation:
                                    print("Fermeture de la liste !")
                                    reponse_valide = True
                                    reponse_valide2 = True
                                elif len(reponse) <= 2 or reponse in oui:
                                    print("On continue !")
                                    reponse_valide = False
                                    reponse_valide2 = True
                                else:
                                    if tutoiement:
                                        print("Ouah, je pensais pas bloquer sur une question si simple, mais la je "
                                              "comprends pas ta réponse !! C'est Oui ou bien c'est Non ! Ou Enter!")
                                    elif not tutoiement:
                                        print("Je ne comprends pas votre réponse, vous pouvez répondre par Oui NON ou"
                                              " bien en appuyant sur la touche enter")
                                    reponse_valide2 = False
                                    file.close()
                reponse_valide2 = False
                while not reponse_valide2:
                    if tutoiement:
                        reponse = str(input("Est-ce que tu souhaites quitter le programme d'apprentissage ? Ou "
                                            "continuer pour apprendre la liste que tu viens de créer, ou en "
                                            "créer une autre ?")).split(" ")
                    elif not tutoiement:
                        reponse = str(input("Souhaitez-vous continuer à appréhender des listes, ou pour en"
                                            "créer d'autres, ou bien souhaitez-vous passer à une autre activité"
                                            "")).split(" ")
                    for test in range(len(reponse)):
                        if reponse[test] in annulation:
                            print("Annulation")
                            fin = True
                            reponse_valide = True
                            reponse_valide2 = True
                        elif reponse[test] in continuer:
                            print("Continuer")
                            fin = False
                            reponse_valide = True
                            reponse_valide2 = True
                    if not reponse_valide2:
                        print("Je ne comprends pas ta réponse !")
        if not reponse_valide and not lecture_liste:
            if tutoiement:
                print("Je comprends pas ta réponse, c'est Oui ou bien c'est Non, comme dirais Angèle")
            elif not tutoiement:
                print(f"Je ne comprends pas votre réponse {current_pseudo}, vous devez répondre par Oui ou par Non")
