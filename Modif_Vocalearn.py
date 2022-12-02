from Listes import *
import os


def modif_vocalearn():
    file = open("current_user.txt", "r")
    informations = file.readlines()
    file.close()
    pseudo = informations[0]

    if informations[1] == "tutoiement":
        tutoiement = True

    else:
        tutoiement = False

    file = open("listes_existantes.txt", "r")
    informations = file.readlines()
    file.close()

    reponse_valide = False
    while not reponse_valide:
        for x in range(len(informations)):
            print(informations[x])
        if tutoiement:
            print("Quelle liste veux-tu modifier ?")
            reponse = str(input("Pour en sélectionner une, écris le numéro de la liste --> "))

        elif not tutoiement:
            print("Quelle liste voulez-vous modifier ?")
            reponse = str(input("Pour en sélectionner une, écrivez le numéro de la liste --> "))
        if reponse in nombres:
            reponse_int = int(reponse)
            reponse_int = reponse_int - 1
            print("\n")
            if len(informations) >= reponse_int >= 0:
                reponse_valide = True
                print(informations[reponse_int])

            else:
                if tutoiement:
                    print("Le numéro que tu as entrée ne correspond à aucune liste !")

                elif not tutoiement:
                    print("Le numéro que vous avez entrée ne correspond à aucune liste !")
        else:
            if tutoiement:
                print("Ce n'est pas la bonne réponse ! Ou alors ta réponse est supérieur à 50 et le dev à eu la flemme "
                      "de faire plus. C'est un nombre qui est attendu !!")
            elif not tutoiement:
                print("La réponse attendu est un nombre, si votre nombre est supérieur à 50 merci de prévenir le "
                      "developpeur !")

    reponse_valide = False
    while not reponse_valide:
        if tutoiement:
            reponse = str(input("Souhaites-tu modifier les termes ou en rajouter ? --> ")).split(" ")

        elif not tutoiement:
            reponse = str(input("Souhaitez vous changer des termes ou en rajouter ? --> ")).split(" ")

        for x in range(len(reponse)):
            if reponse[x] in ajouter:
                reponse_valide = True
                ajout = True
            elif reponse[x] in modification:
                reponse_valide = True
                ajout = False
        if not reponse_valide:
            if tutoiement:
                print(f"Je ne comprends pas ta réponse, elle doit avoir soit {modification} \nSi tu veux la modifier"
                      f"soit {ajouter}, si tu veux rajouter des mots !")
            elif not tutoiement:
                print(f"Je ne comprends pas votre réponse, votre réponse doit comporter pour modifier une liste : \n"
                      f"{modification}\nOu par ajouter des termes : \n{ajouter}")

    path = f"{chemin}/Listes Vocalearn/"
    current_liste = informations[reponse_int].strip()
    file = open(f"{path}{current_liste}.txt", "r")
    informations = file.readlines()
    file.close()
    nb_terme = len(informations) / 3
    terme = 0
    definition = 1
    status = 2
    if not ajout:
        if tutoiement:
            print(
                "Tout les termes vont défiler, appuie sur ENTER pour passer au suivant, ou écris STOP pour modifier le "
                "terme ou la définition !")

        elif not tutoiement:
            print(
                "Tout les termes vont défiler, appuyez sur ENTER pour passer au suivant, ou écrivez STOP pour modifier "
                "le terme ou bien la définition !")

        while status < len(informations):
            reponse_valide = False

            while not reponse_valide:
                reponse = str(input(f"{informations[terme]} --> "))

                if len(reponse) == 0:
                    reponse_valide = True
                    print("Ok, next !")

                elif reponse == "STOP":
                    reponse_valide = True
                    reponse_valide2 = False
                    while not reponse_valide2:
                        if tutoiement:
                            reponse = str(input("Veux tu modifier le terme ? --> "))

                        elif not tutoiement:
                            reponse = str(input("Voulez-vous modifier le terme ? --> "))

                        if reponse in oui:
                            reponse_valide2 = True
                            if tutoiement:
                                informations[terme] = str(input("Entre le terme modifié : "))

                            elif not tutoiement:
                                informations[terme] = str(input("Entrez le terme modifié : "))
                            informations[terme] = f"{informations[terme]}\n"

                        elif reponse in non:
                            reponse_valide2 = True

                    reponse_valide2 = False
                    while not reponse_valide2:
                        if tutoiement:
                            reponse = str(input("Veux-tu modifier la définition ? --> "))

                        elif not tutoiement:
                            reponse = str(input("Voulez-vous modifier la définition ? --> "))

                        if reponse in oui:
                            print("Je suis passé par là !")
                            reponse_valide2 = True
                            if tutoiement:
                                print("Touché !")
                                informations[definition] = str(input("Entre la définition modifié : "))
                            elif not tutoiement:
                                informations[definition] = str(input("Entrez la définition modifié : "))
                            informations[definition] = f"{informations[definition]}\n"

                        elif reponse in non:
                            print("Non c'est non")
                            reponse_valide2 = True
                            if tutoiement:
                                print("Let's go, on passe au terme suivant !")
                            elif not tutoiement:
                                print("Nous en avons fini avec ce terme là, passons au suivant !")

                else:
                    print("Je ne comprends pas ? Appuie sur ENTER ou écris STOP")

            terme = terme + 3
            definition = definition + 3
            status = status + 3
            print("\n\n\n------------------------------\n\n\n")
        file = open(f"{path}{current_liste}.txt", "w+")
        for x in range(len(informations)):
            file.write(informations[x])
        file.close()

        reponse_valide = False
        while not reponse_valide:
            if tutoiement:
                reponse = str(input("Veux tu ajouter des termes ?"))

            elif not tutoiement:
                reponse = str(input("Voudrez vous ajouter des termes à la liste ?"))

            if reponse in oui:
                reponse_valide = True
                ajout = True

            elif reponse in non:
                reponse_valide = True
                print("Arrêt de la modification de la liste : ")
            else:
                if tutoiement:
                    print("Je ne comprends pas ta réponse ! C'est Oui ou bien c'est Non !")

                elif not tutoiement:
                    print("Je ne comprends pas votre réponse ! La réponse doit être Oui ou Non !")

    if ajout:
        file = open(f"{path}{current_liste}.txt", "a")
        if tutoiement:
            print("Tu seras obligé de terminer le terme à partir de moment où tu auras entré le terme, mais tu "
                  "pourras t'arrêter à ce même moment, en écrivant STOP !")
        elif not tutoiement:
            print("Vous serez obligé de terminer le terme, à partir du moment où vous aurez entré le terme, mais "
                  "vous pourrez vous arrêtez à ce même moment en écrivant STOP !")
        fin = False
        while not fin:
            nb_terme = nb_terme + 1
            if tutoiement:
                reponse = str(input(f"Entre le terme n°{int(nb_terme)} --> "))
            elif not tutoiement:
                reponse = str(input(f"Entrez le terme n°{int(nb_terme)} --> "))
            if reponse in annulation:
                fin = True
            if not fin:
                file.write(f"{reponse}\n")
                if tutoiement:
                    reponse = str(input(f"Entre la définition ou la traduction du terme n°{int(nb_terme)} --> "))
                elif not tutoiement:
                    reponse = str(input(f"Entrez la définition ou la traduction du terme n°{int(nb_terme)} --> "))
                file.write(f"{reponse}\n")
                file.write("0\n")
        file.close()
