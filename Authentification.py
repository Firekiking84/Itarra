from Listes import *
import os


def authentification():
    test = 0
    repondu = False
    reponse_valide = False
    connected = False
    if os.path.exists("current_user.txt"):
        file = open("current_user.txt", "r")
        informations = file.readlines()
        file.close()
        current_pseudo = informations[0].strip()
        current_politesse = informations[1].strip()
        while not reponse_valide:
            connu = str(input(f"Est-ce toujours {current_pseudo} ?"))
            if connu in oui:
                reponse_valide = True
                connected = True
                print(f"Connecté au compte {current_pseudo}")
                return
            elif connu in non:
                reponse_valide = True
            else:
                print("Je ne comprends pas votre réponse ! (Oui/Non)")
    if not connected:
        while not repondu:
            connu = str(input("Salut, désolé je n'ai pas encore de yeux ? Je vous connais déjà ?")).split(" ")
            while test < len(connu):
                if connu[test] in oui:
                    repondu = True
                    while not connected:
                        old_account = str(input("Quel est votre pseudo ? "))
                        if os.path.exists(old_account + ".txt"):
                            file = open(old_account + ".txt", "r")
                            informations = file.readlines()
                            file2 = open("current_user.txt", "w+")
                            file2.write(informations[0])
                            file2.write(informations[1])
                            file2.write(informations[2])
                            file2.close()
                            connected = True
                            file.close()
                            print(f"Connecté au compte {informations[0]}")
                            return
                        else:
                            print("Aucun compte ne correspond à ce pseudo ! Merci de réessayer...")
                elif connu[test] in non:
                    current_pseudo = str(input("Puis connaître votre pseudo ? "))
                    file = open("current_user.txt", "w+")
                    file2 = open(f"{current_pseudo}.txt", "w+")
                    file.write(f"{current_pseudo}\n")
                    file2.write(f"{current_pseudo}\n")
                    repondu = True
                    reponse_valide = False
                    while not reponse_valide:
                        current_politesse = str(input("Voulez vous que je vous tutoie ? ")).split(" ")
                        test = 0
                        while test < len(current_politesse) or not reponse_valide:
                            if current_politesse[test] in oui:
                                reponse_valide = True
                                file.write("tutoiement\n")
                                file2.write("tutoiement\n")
                                test = test + 1
                            elif current_politesse[test] in non:
                                reponse_valide = True
                                file.write("vouvoiement\n")
                                file2.write("vouvoiement\n")
                                test = test + 1
                            else:
                                print("Oh... Un mot en plus ? Mais comment tu as fait ?")
                                test = test + 1
                        file2.write("0")
                        file.write("0")
                        file.close()
                        file2.close()
                        if reponse_valide:
                            print(f"Le compte {current_pseudo} à bien été enregistré et la connexion et réussi !")
                        elif not reponse_valide:
                            print("Je ne comprends pas votre réponse ! Merci de réessayer ! ")
                if not repondu:
                    break
            if not repondu:
                print("Je ne comprends pas votre réponse ! Merci de réessayer ! ")