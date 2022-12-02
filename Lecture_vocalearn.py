from Listes import *
import os

title = ["Le titre ici"]


def lecture_vocalearn():
    file = open("current_user.txt", "r")
    informations = file.readlines()
    current_pseudo = informations[0].strip()
    ending = False
    reset_bool = False
    if informations[1].strip() == "tutoiement":
        tutoiement = True
    else:
        tutoiement = False
    file.close()
    test = 0
    abandon = False
    while not abandon:
        reponse_valide = False
        while not reponse_valide:
            file = open("listes_existantes.txt", "r")
            informations = file.readlines()
            file.close()
            if tutoiement:
                print(f"Voici toutes les listes qui ont déjà été enregistrée \n")
            elif not tutoiement:
                print(f"Voici toutes les listes déjà existantes dans le programme \n")
            for test in range(len(informations)):
                print(informations[test])
            if tutoiement:
                reponse = str(input("Vas-y fais toi plaisir, c'est gratuit ! Laquelle ? Tu pourras tous les faire "
                                    "si tu veux ? Ou alors tu peux tout simplement quitter le mode. --> "))
            elif not tutoiement:
                reponse = str(input("Choisissez parmi toutes celles proposées ! Si vous le souhaiter vous pouvez quitter"
                                    "le mode d'apprentissage. --> "))
            if os.path.exists(f"{chemin}/Listes Vocalearn/{reponse}.txt"):
                reponse_valide = True
                fin = False
                title[0] = reponse
                if tutoiement:
                    print(f"Let's go !! Allons apprendre {reponse}. Tu vas tout déchirer !!")
                elif not tutoiement:
                    print(f"Maintenant que nous avons sélectionné la liste {reponse}, apprenons-la !")
            elif reponse in annulation :
                print("Fermeture du mode d'apprentissage...")
                reponse_valide = True
                fin = True
                abandon = True
            else:
                print("Liste inconnue !")
        if not abandon:
            print("Répond le terme correspondant à celui donné !")
            if tutoiement:
                print("Tu peux arrêter, ou recommencer depuis le début à tout moment, ta progression sera sauvegardé !")
            elif not tutoiement:
                print("Vous pouvez vous arrêtez à tout moment, ou bien recommencer à zéro, votre progression "
                      "sera sauvegardé")
            file = open(f"{chemin}/Listes Vocalearn/{title[0]}.txt", "r")
            informations = file.readlines()
            file.close()
            nb_terme_total = (len(informations)) / 3
            print(f"Nombre total de termes de la liste {nb_terme_total}")
            nb_terme_vu = 0
            nb_terme_appris = 0
            pc_terme_vu = (nb_terme_vu / nb_terme_total) * 100
            pc_terme_appris = (nb_terme_appris / nb_terme_total) * 100
            terme = 0
            definition = 1
            status = 2
            current_status = 0
        while not fin:
            testbool = False
            file = open(f"{chemin}/Listes Vocalearn/{title[0]}.txt", "r")
            informations = file.readlines()
            file.close()
            for test in range(10):
                if informations[status].strip() == chiffres[test]:
                    current_status = test
            # -----------------------------------------------------------------------------------------------------------------------
            if current_status == 0:
                testbool = True
                essai = False
                while current_status == 0:
                    reponse = str(input(f" -- >{informations[definition]}\n -->"))
                    if reponse == informations[terme].strip():
                        if tutoiement:
                            print("GG, incroyable, allez on passe à la suite ! A ce rythme là, ça va être super rapide !")
                        elif not tutoiement:
                            print("Bien joué, suivant !")
                        current_status = current_status + 2
                    elif reponse in reset_vocalearn:
                        print("Redémarrage de la progression de la liste...")
                        reset()
                        reset_bool = True
                        break
                    elif reponse in annulation:
                        print("Sauvegarde de la progression\n Fermeture...")
                        fin = True
                        ending = True
                        break
                    else:
                        print(f"Réponse incorrect, voici la bonne réponse : {informations[terme]}")
                        reponse_valide = False
                        while not reponse_valide:
                            reponse = str(input("En toute objectivité, ta réponse était-elle corecte ? Sinon appuie"
                                                " sur ENTER "))
                            if reponse in oui:
                                current_status = current_status + 2
                                print("Bien joué, alors ! Allez à la suivante !")
                                reponse_valide = True
                            elif reponse in non or len(reponse) == 0:
                                essai = True
                                while reponse != informations[terme].strip():
                                    reponse = str(input(f"Réécris, la bonne réponse : {informations[terme]}\n --> "))
                                    reponse_valide = True
                            elif reponse in reset_vocalearn:
                                print("Redémarrage de la progression de la liste...")
                                reset()
                                reset_bool = True
                                break
                            elif reponse in annulation:
                                print("Sauvegarde de la progression\n Fermeture...")
                                fin = True
                                ending = True
                                break
                            else:
                                if tutoiement:
                                    print("Je ne comprends pas ta réponse, c'est pas la plus compliqué quand même !"
                                          "Comme je n'arrête pas de le dire, c'est oui ou bien c'est non !")
                                elif not tutoiement:
                                    print("Je ne comprends pas votre réponse ! Réponse attendu : Oui/Non !")
                    if essai:
                        print("\n\n\n\n\n\n\n\n\n\n")
                if essai:
                    current_status = 1
                informations[status] = f"{chiffres[current_status]}\n"
                nb_terme_vu = nb_terme_vu + 1
            # --------------------------------------------------------------------------------------------------------------

            elif current_status == 1:
                testbool = True
                if tutoiement:
                    print("Allez, celui-là tu t'es déjà loupé précédément, tu peux le faire !")
                elif not tutoiement:
                    print("Voici un mot déjà vu précédément, où vous vous êtes trompé !")
                current_status = 0
                essai = False
                while current_status == 0:
                    reponse = str(input(f"-- > {informations[definition]}\n--> "))
                    if reponse == informations[terme].strip():
                        if tutoiement:
                            print("Bien joué ! Un de plus d'appris !")
                        elif not tutoiement:
                            print("Bien joué, suivant !")
                        current_status = current_status + 2
                    elif reponse in reset_vocalearn:
                        print("Redémarrage de la progression de la liste...")
                        reset()
                        reset_bool = True
                        break
                    elif reponse in annulation:
                        print("Sauvegarde de la progression\n Fermeture...")
                        fin = True
                        ending = True
                        break
                    else:
                        print(f"Réponse incorrect, voici la bonne réponse : {informations[terme]}")
                        reponse_valide = False
                        while not reponse_valide:
                            reponse = str(input("En toute objectivité, ta réponse était-elle corecte ? Sinon appuie"
                                                " sur ENTER "))
                            if reponse in oui:
                                current_status = current_status + 2
                                print("Bien joué, alors ! Allez à la suivante !")
                                reponse_valide = True
                            elif reponse in non or len(reponse) == 0:
                                essai = True
                                while reponse != informations[terme].strip():
                                    reponse = str(input(f"Réécris, la bonne réponse : {informations[terme]}\n --> "))
                                    reponse_valide = True
                            elif reponse in reset_vocalearn:
                                print("Redémarrage de la progression de la liste...")
                                reset()
                                reset_bool = True
                                break
                            elif reponse in annulation:
                                print("Sauvegarde de la progression\n Fermeture...")
                                fin = True
                                ending = True
                                break
                            else:
                                if tutoiement:
                                    print("Je ne comprends pas ta réponse, c'est pas la plus compliqué quand même !"
                                          "Comme je n'arrête pas de le dire, c'est oui ou bien c'est non !")
                                elif not tutoiement:
                                    print("Je ne comprends pas votre réponse ! Réponse attendu : Oui/Non !")
                    if essai:
                        print("\n\n\n\n\n\n\n\n\n\n")
                if essai:
                    current_status = 1
                informations[status] = f"{current_status}\n"
            # -------------------------------------------------------------------------------------------------
            elif current_status == 2:
                testbool = True
                essai = False
                while current_status == 2:
                    reponse = str(input(f"-- >{informations[terme]}\n --> "))
                    if reponse == informations[definition].strip():
                        if tutoiement:
                            print("Nice, ça c'est fait, next !")
                        elif not tutoiement:
                            print("C'est bien, on avance !")
                        current_status = 4
                    elif reponse in reset_vocalearn:
                        print("Redémarrage de la progression de la liste...")
                        reset()
                        reset_bool = True
                        break
                    elif reponse in annulation:
                        print("Sauvegarde de la progression\n Fermeture...")
                        fin = True
                        ending = True
                        break
                    else:
                        print(f"Mauvaise réponse..., la bonne c'est : {informations[definition]}")
                        reponse_valide = False
                        while not reponse_valide:
                            if tutoiement:
                                reponse = str(input("Pour toi, elle était bonne ta réponse ? Sinon appuie sur ENTER."))
                            elif not tutoiement:
                                reponse = str(input("Selon vous,votre réponse était-elle corecte ? Sinon "
                                                    "appuyez sur ENTER."))
                            if reponse in oui:
                                print("Alors bien joué, n'oublie pas que si tu ne joues pas le jeu, tu perdras "
                                      "plus de temps qu'autre chose !")
                                current_status = 4
                                reponse_valide = True
                            elif reponse in non or len(reponse) == 0:
                                essai = True
                                reponse_valide = True
                                print("Il n'y a pas de problème, c'est la partie la plus compliqué ! Allez c'est "
                                      "comme avant !")
                                while reponse != informations[definition].strip():
                                    reponse = str(input(f"Réécris la bonne réponse : {informations[definition]}\n --> "))
                            elif reponse in reset_vocalearn:
                                print("Redémarrage de la progression de la liste...")
                                reset()
                                reset_bool = True
                                break
                            elif reponse in annulation:
                                print("Sauvegarde de la progression\n Fermeture...")
                                fin = True
                                ending = True
                                break
                            else:
                                if tutoiement:
                                    print("Je ne comprends pas ta réponse ! C'est comme avant, c'est oui ou bien "
                                          "c'est non !")
                                elif not tutoiement:
                                    print("Je ne comprends pas votre réponse ! La réponse attendu est : Oui/Non")
                    if essai:
                        print("\n\n\n\n\n\n\n\n\n\n")
                if essai:
                    current_status = 3
                informations[status] = f"{chiffres[current_status]}\n"
                if current_status == 4:
                    nb_terme_appris = nb_terme_appris + 1
                # --------------------------------------------------------------------------------------------------------
            elif current_status == 3:
                testbool = True
                if tutoiement:
                    print("Alors lui, tu l'as déjà loupé tout à l'heure, tu l'as retenu ?")
                elif not tutoiement:
                    print("Voici, un de vos précédents échecs ! Allez vous refaire la même erreur ?")
                current_status = 2
                essai = False
                while current_status == 2:
                    reponse = str(input(f"-- > {informations[terme]}\n --> "))
                    if reponse == informations[definition].strip():
                        if tutoiement:
                            print("Nice, ça c'est fait, next !")
                        elif not tutoiement:
                            print("C'est bien, on avance !")
                        current_status = 4
                    elif reponse in reset_vocalearn:
                        print("Redémarrage de la progression de la liste...")
                        reset()
                        reset_bool = True
                        break
                    elif reponse in annulation:
                        print("Sauvegarde de la progression\n Fermeture...")
                        fin = True
                        ending = True
                        break
                    else:
                        print(f"Mauvaise réponse..., la bonne c'est : {informations[definition]}")
                        reponse_valide = False
                        while not reponse_valide:
                            if tutoiement:
                                reponse = str(input("Pour toi, elle était bonne ta réponse ? Sinon appuie sur ENTER."))
                            elif not tutoiement:
                                reponse = str(input("Selon vous,votre réponse était-elle corecte ? Sinon "
                                                    "appuyez sur ENTER."))
                            if reponse in oui:
                                print("Alors bien joué, n'oublie pas que si tu ne joues pas le jeu, tu perdras "
                                      "plus de temps qu'autre chose !")
                                current_status = 4
                                reponse_valide = True
                            elif reponse in non or len(reponse) == 0:
                                essai = True
                                reponse_valide = True
                                print("Il n'y a pas de problème, c'est la partie la plus compliqué ! Allez c'est "
                                      "comme avant !")
                                while reponse != informations[definition].strip():
                                    reponse = str(input(f"Réécris la bonne réponse : {informations[definition]}\n --> "))
                            elif reponse in reset_vocalearn:
                                print("Redémarrage de la progression de la liste...")
                                reset()
                                reset_bool = True
                                break
                            elif reponse in annulation:
                                print("Sauvegarde de la progression\n Fermeture...")
                                fin = True
                                ending = True
                                break
                            else:
                                if tutoiement:
                                    print("Je ne comprends pas ta réponse ! C'est comme avant, c'est oui ou bien "
                                          "c'est non !")
                                elif not tutoiement:
                                    print("Je ne comprends pas votre réponse ! La réponse attendu est : Oui/Non")
                    if essai:
                        print("\n\n\n\n\n\n\n\n\n\n")
                if essai:
                    current_status = 3
                informations[status] = f"{chiffres[current_status]}\n"
                if current_status == 4:
                    nb_terme_appris = nb_terme_appris + 1
            # -------------------------------------------------------------------------------------------------------------------
            terme = terme + 3
            definition = definition + 3
            status = status + 3
            if not reset_bool:
                file = open(f"{chemin}/Listes Vocalearn/{title[0]}.txt", "w")
                for test in range(len(informations)):
                    file.write(informations[test])
                file.close()
            if terme >= len(informations) or reset_bool:
                terme = 0
                definition = 1
                status = 2
            nb_terme_vu = 0
            nb_terme_appris = 0
            test_status = 2
            while test_status <= len(informations):
                if informations[test_status] == "\n":
                    informations[test_status] = "0"
                current_status = int(informations[test_status])
                if current_status > 0:
                    nb_terme_vu = nb_terme_vu + 1
                if current_status == 4:
                    nb_terme_appris = nb_terme_appris + 1
                test_status = test_status + 3
            pc_terme_vu = (nb_terme_vu / nb_terme_total) * 100
            pc_terme_appris = (nb_terme_appris / nb_terme_total) * 100
            if not ending and testbool and not abandon:
                if tutoiement:
                    print(
                        f"Petit point, sur ta progression ! Tu as appris {int(pc_terme_appris)}% et vu {int(pc_terme_vu)}% de "
                        f"la totalité des termes. Plus que {int(100 - pc_terme_appris)}% à apprendre")
                elif not tutoiement:
                    print(f"Voici votre avancée, sur la liste. {pc_terme_vu}% ont été étudié, et {pc_terme_appris}% ont été"
                          f"appris.")
                if pc_terme_appris == 100:
                    fin = True
                    print("Bien joué ! Tu as appris tout les termes de la liste !")
                    reset()
            reset_bool = False


def reset():
    file = open(f"{chemin}/Listes Vocalearn/{title[0]}.txt", "r")
    informations = file.readlines()
    file.close()
    reset_status = 2
    while reset_status <= len(informations):
        informations[reset_status] = "0\n"
        reset_status = reset_status + 3
    file = open(f"{chemin}/Listes Vocalearn/{title[0]}.txt", "w")
    for test in range(len(informations)):
        file.write(informations[test])
    file.close()
