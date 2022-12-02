from Listes import *
import os


def enigma_machine():
    letters_number = 0
    file = open("current_user.txt", "r")
    informations = file.readlines()
    file.close()
    current_pseudo = informations[0].strip()
    tutoiement = False
    free = False
    if informations[1].strip() == "tutoiement":
        tutoiement = True
    elif informations[1].strip() == "vouvoiement":
        tutoiement = False
    if tutoiement:
        print("Je vais crypté ton message avec le fonctionnement de la machine Enigma de la Seconde Guerre Mondiale")
    elif not tutoiement:
        print("Je vais crypté votre message avec le fonction de la machine Enigma")
    test = informations[2]
    convert_values = int(test)
    test = convert_values
    test = test + 1
    convert_values = str(test)
    informations[2] = convert_values
    file = open(f"{current_pseudo}.txt", "w+")
    file.write("")
    file.close()
    file = open("current_user.txt", "w+")
    file.write("")
    file.close()
    for test2 in range(3):
        file = open(f"{current_pseudo}.txt", "a")
        file.write(informations[test2])
        file.close()
        file = open("current_user.txt", "a")
        file.write(informations[test2])
        file.close()
    chemin = os.getcwd()
    os.mkdir(f"{chemin}\crypted_message_{test}_{current_pseudo}")
    file = open(f"{chemin}\crypted_message_{test}_{current_pseudo}\crypted_message_{test}_{current_pseudo}.txt", "w+")
    coded_message = str(input("Quel est votre message secret ? --> "))
    if tutoiement:
        slot1 = str(input("Choisis le rotor du premier emplacement (réponse de 1 à 8)! --> "))
    elif not tutoiement:
        slot1 = str(input("Choisissez le rotor du premier emplacement (réponse de 1 à 8)! --> "))
    file.write(f"Paramètres : \n   Choix des rotors : \n        Premier rotor : n°{slot1}\n")
    if tutoiement:
        slot2 = str(input("Choisis le rotor du deuxième emplacement (réponse de 1 à 8)! --> "))
    elif not tutoiement:
        slot2 = str(input("Choisissez le rotor du deuxième emplacement (réponse de 1 à 8)! --> "))
    file.write(f"       Deuxième rotor : n°{slot2}\n")
    if tutoiement:
        slot3 = str(input("Choisis le rotor du troisième emplacement (réponse de 1 à 8)! --> "))
    elif not tutoiement:
        slot3 = str(input("Choisissez le rotor du troisième emplacement (réponse de 1 à 8)! --> "))
    file.write(f"       Troisième rotor : n°{slot3}\n")
    if tutoiement:
        slot4 = str(input("Choisis le rotor du quatrième emplacement (réponse de 1 à 8)! --> "))
    elif not tutoiement:
        slot4 = str(input("Choisissez le rotor du quatrième emplacement (réponse de 1 à 8)! --> "))
    file.write(f"       Quatrième rotor : n°{slot4}\n")
    reponse_valide = False
    while not reponse_valide:
        if tutoiement:
            reponse = str(input("Souhaites-tu le mode militaire, plus compliqué à décoder mais plus long à mettre en "
                                "place ! --> "))
        elif not tutoiement:
            reponse = str(input("Souhaitez-vous crypter votre message avec le mode militaire ? Plus longue "
                                "préparation pour une meilleure protection ! --> "))
        standard = False
        if reponse in oui:
            file.write(f"   Mode avancé:\n      Mode militaire : \n")
            already_used = []
            if tutoiement:
                print("Tu vas maintenant devoir associé par chaque lettre de l'alphabet à une autre lettre de "
                      "l'alphabet.")
            elif not tutoiement:
                print("Vous allez maintenant devoir associé en douze paires l'alphabet")
            test2 = 0
            while len(already_used) < 26:
                reponse_valide = False
                file.write(f"   Réflexions des lettres :\n ")
                while not reponse_valide:
                    if alphabet[test2] not in already_used:
                        reponse = str(input(f"La paire de {alphabet[test2]} --> "))
                        if reponse in alphabet:
                            reponse_valide = True
                            if reponse in already_used:
                                print("Déjà utilisé !")
                                reponse_valide = False
                            else:
                                already_used.append(alphabet[test2])
                                if reponse not in already_used:
                                    already_used.append(reponse)
                                file.write(f"       {alphabet[test2]} --> {reponse}\n")
                                file2 = open(f"{chemin}\crypted_message_{test}_{current_pseudo}\switch_letters_"
                                             f"{alphabet[test2]}_crypted_message_{test}_{current_pseudo}.txt", "w+")
                                file2.write(reponse)
                                file2.close()
                                file2 = open(f"{chemin}\crypted_message_{test}_{current_pseudo}\switch_letters_"
                                             f"{reponse}_crypted_message_{test}_{current_pseudo}.txt", "w+")
                                file2.write(alphabet[test2])
                                file2.close()
                    elif alphabet[test2] in already_used:
                        reponse_valide = True
                    else:
                        if tutoiement:
                            print("Euh faut juste marquer une lettre de l'alphabet... C'est pas bien compliqué "
                                  "pourtant")
                        elif not tutoiement:
                            print("Je ne comprends pas votre réponse, votre réponse doit être une lettre de l'alphabet")
                test2 = test2 + 1
        elif reponse in non:
            standard = True
            reponse_valide = True
            file.write(f"  Mode avancé:\n      Mode Standard")
            if tutoiement:
                print("Ton message vas être codé dans le mode standard !")
            elif not tutoiement:
                print("Votre message sera crypté dans le mode standart")
            file.write(f"   Réflexions des lettres :\n ")
            for test2 in range(26):
                file.write(f"       {alphabet[test2]} --> {alphabet[25 - test2]}\n")
                file2 = open(f"{chemin}\crypted_message_{test}_{current_pseudo}\switch_letters_{alphabet[test2]}"
                             f"_crypted_message_{test}_{current_pseudo}.txt", "w+")
                file2.write(alphabet[test2])
                file2.close()
    decalage1 = 0
    decalage2 = 0
    decalage3 = 0
    decalage4 = 0
    reponse_valide = False
    while not reponse_valide:
        reponse = str(input("Choississez le paramétrage du premier rotor (réponse de 0 à 25)--> "))
        if reponse in nombres:
            reponse_valide = True
            for x in range(27):
                if reponse == nombres[x]:
                    decalage1 = x
        else:
            if tutoiement:
                print("Je ne comprends pas ! Assure-toi d'avoir inscrit un nombre entre 0 et 25 inclus")
            elif not tutoiement:
                print("Désolé, je ne comprends pas votre réponse ! Etes-vous sûr d'avoir inclus un nombre de 0 à 26 "
                      "inclus")
    file.write(f"   Paramétrage :\n         Rotor n°1: {reponse}\n")
    reponse_valide = False
    while not reponse_valide:
        reponse = str(input("Choississez le paramétrage du deuxième rotor (réponse de 0 à 25)--> "))
        if reponse in nombres:
            reponse_valide = True
            for x in range(27):
                if reponse == nombres[x]:
                    decalage2 = x
        else:
            if tutoiement:
                print("Je ne comprends pas ! Assure-toi d'avoir inscrit un nombre entre 0 et 26 inclus")
            elif not tutoiement:
                print("Désolé, je ne comprends pas votre réponse ! Etes-vous sûr d'avoir inclus un nombre de 0 à 26 "
                      "inclus")
    file.write(f"   Paramétrage :\n         Rotor n°2: {reponse}\n")
    reponse = str(input("Choississez le paramétrage du troisième rotor (réponse de 0 à 25) --> "))
    reponse_valide = False
    while not reponse_valide:
        if reponse in nombres:
            reponse_valide = True
            for x in range(27):
                if reponse == nombres[x]:
                    decalage3 = x
        else:
            if tutoiement:
                print("Je ne comprends pas ! Assure-toi d'avoir inscrit un nombre entre 0 et 25 inclus")
            elif not tutoiement:
                print("Désolé, je ne comprends pas votre réponse ! Etes-vous sûr d'avoir inclus un nombre de 0 à 26 "
                      "inclus")
    file.write(f"   Paramétrage :\n         Rotor n°: {reponse}\n")
    reponse_valide = False
    while not reponse_valide:
        reponse = str(input("Choississez le paramétrage du quatrième rotor (réponse de 0 à 25)--> "))
        if reponse in nombres:
            reponse_valide = True
            for x in range(27):
                if reponse == nombres[x]:
                    decalage4 = x
        else:
            if tutoiement:
                print("Je ne comprends pas ! Assure-toi d'avoir inscrit un nombre entre 0 et 26 inclus")
            elif not tutoiement:
                print("Désolé, je ne comprends pas votre réponse ! Etes-vous sûr d'avoir inclus un nombre de 0 à 26 "
                      "inclus")
    file.write(f"   Paramétrage :\n         Rotor n°1: {reponse}\n")
    letter_choice = 0
    crypted_letter = []
    file.write(f"\nMessage à crypter : {coded_message}\n")
    for test2 in range(len(coded_message)):
        if coded_message[test2] == " ":
            crypted_letter.append(" ")
            continue
        else:
            # Début du cryptage des lettres
            traited_letter = coded_message[test2]
            print(f"La lettre initiale est {traited_letter}")
            # Switch lettre selon ce qui a été déterminé avant
            file2 = open(f"{chemin}\crypted_message_{test}_{current_pseudo}\switch_letters_{coded_message[test2]}"
                         f"_crypted_message_{test}_{current_pseudo}.txt", "r")
            traited_letter = file2.read()
            file2.close()
            ok = False
            if standard:
                for test3 in range(26):  # Tableau de réflection, switch lettre
                    if traited_letter == alphabet[test3] and not ok:
                        traited_letter = connect_board[test3]
                        ok = True
            # Recherche position correspondante sur rotor fixe
            # C'est à dire de la position où il y a la même lettre que celle traitée
            for test3 in range(26):
                test_rotor = rotor_fixe1[test3]
                if traited_letter == test_rotor:
                    break
            # Définition du décalage brut
            letter_choice = test3
            # Addition du décalage défini précédemment
            for x in range(decalage1):
                letter_choice = letter_choice - 1
                if letter_choice == -1:  # Remise à zéro à 26, nombre d'emplacement (0 compris) du rotor
                    letter_choice = 25
            print(f"La transformation de la lettre {letters_number} est {traited_letter} ! L'emplacement de la "
                  f"lettre est {letter_choice}")
            if slot1 == "1":  # Recherche du rotor choisi
                traited_letter = rotor1[letter_choice]  # Changement de la lettre traitée par celle du rotor
                # à l'emplacement souhaitée
            elif slot1 == "2":
                traited_letter = rotor2[letter_choice]
            elif slot1 == "3":
                traited_letter = rotor3[letter_choice]
            elif slot1 == "4":
                traited_letter = rotor4[letter_choice]
            elif slot1 == "5":
                traited_letter = rotor5[letter_choice]
            elif slot1 == "6":
                traited_letter = rotor6[letter_choice]
            elif slot1 == "7":
                traited_letter = rotor7[letter_choice]
            elif slot1 == "8":
                traited_letter = rotor8[letter_choice]
            # Recherche position correspondante sur rotor fixe
            # C'est à dire de la position où il y a la même lettre que celle traitée
            for test3 in range(26):
                test_rotor = rotor_fixe2[test3]
                if traited_letter == test_rotor:
                    break
            letter_choice = test3
            print(f"La transformation de la lettre {letters_number} est {traited_letter} ! L'emplacement de la "
                  f"lettre est {letter_choice}")
            # Addition des décalages défini
            for x in range(decalage2):
                letter_choice = letter_choice - 1
                if letter_choice == -1:
                    letter_choice = 25
            if slot2 == "1":  # Recherche du rotor défini pour cet emplacement
                traited_letter = rotor1[letter_choice]  # Définition de la lettre correspondante
            elif slot2 == "2":
                traited_letter = rotor2[letter_choice]
            elif slot2 == "3":
                traited_letter = rotor3[letter_choice]
            elif slot2 == "4":
                traited_letter = rotor4[letter_choice]
            elif slot2 == "5":
                traited_letter = rotor5[letter_choice]
            elif slot2 == "6":
                traited_letter = rotor6[letter_choice]
            elif slot2 == "7":
                traited_letter = rotor7[letter_choice]
            elif slot2 == "8":
                traited_letter = rotor8[letter_choice]
            # Recherche de l'emplacement correspondant
            for test3 in range(26):
                test_rotor = rotor_fixe3[test3]
                if traited_letter == test_rotor:
                    break
            letter_choice = test3
            print(f"La transformation de la lettre {letters_number} est {traited_letter} ! L'emplacement de la "
                  f"lettre est {letter_choice}")
            # Addition des décalages défini
            for x in range(decalage3):
                letter_choice = letter_choice - 1
                if letter_choice == -1:
                    letter_choice = 25
            if slot3 == "1":  # Recherche du rotor présent à cet emplacement
                traited_letter = rotor1[letter_choice]  # Définition de la lettre correspondante
            elif slot3 == "2":
                traited_letter = rotor2[letter_choice]
            elif slot3 == "3":
                traited_letter = rotor3[letter_choice]
            elif slot3 == "4":
                traited_letter = rotor4[letter_choice]
            elif slot3 == "5":
                traited_letter = rotor5[letter_choice]
            elif slot3 == "6":
                traited_letter = rotor6[letter_choice]
            elif slot3 == "7":
                traited_letter = rotor7[letter_choice]
            elif slot3 == "8":
                traited_letter = rotor8[letter_choice]
            print(f"La transformation de la lettre {letters_number} est {traited_letter} ! L'emplacement de la "
                  f"lettre est {letter_choice}")
            # Recherche du bon emplacement
            for test3 in range(26):
                test_rotor = rotor_fixe4[test3]
                if traited_letter == test_rotor:
                    break
            letter_choice = test3
            # Addition décalage défini
            for x in range(decalage4):
                letter_choice = letter_choice - 1
                if letter_choice == -1:
                    letter_choice = 25
            if slot4 == "1":  # Recherche du rotor présent à l'emplacement
                traited_letter = rotor1[letter_choice]  # Définition de la lettre correspondante
            elif slot4 == "2":
                traited_letter = rotor2[letter_choice]
            elif slot4 == "3":
                traited_letter = rotor3[letter_choice]
            elif slot4 == "4":
                traited_letter = rotor4[letter_choice]
            elif slot4 == "5":
                traited_letter = rotor5[letter_choice]
            elif slot4 == "6":
                traited_letter = rotor6[letter_choice]
            elif slot4 == "7":
                traited_letter = rotor7[letter_choice]
            elif slot4 == "8":
                traited_letter = rotor8[letter_choice]
            # Fin du tour aller, début du tour retour
            print(f"La transformation de la lettre {letters_number} est {traited_letter} ! L'emplacement de la "
                  f"lettre est {letter_choice}")
            # Réflecteur :
            ok = False
            for test3 in range(26):  # Réflecteur, switch lettre
                if traited_letter == alphabet[test3] and not ok:
                    traited_letter = reflector[test3]
                    ok = True
            print(f"La valeur de la lettre après le réflecteur : {traited_letter}")
            if slot4 == "1":  # Recherche du rotor présent sur cet emplacement
                print("Check 4!")
                for test3 in range(26):
                    test_rotor = rotor1[test3]
                    if traited_letter == test_rotor:  # Recherche de la lettre correspondante sur le rotor movible
                        print("Check 4.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3  # Définition de l'emplacement sur le rotor
                        for x in range(decalage4):  # Addition du décalage
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        # Définition de la lettre traitée par rapport au paramètre défini précédemment
                        traited_letter = rotor_fixe4[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot4 == "2":  # Recherche du rotor présent sur cet emplacement
                print("Check 4!")
                for test3 in range(26):
                    test_rotor = rotor2[test3]
                    if traited_letter == test_rotor:
                        print("Check 4.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage4):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe4[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot4 == "3":  # Recherche du rotor présent sur cet emplacement
                print("Check 4!")
                for test3 in range(26):
                    test_rotor = rotor3[test3]
                    if traited_letter == test_rotor:
                        print("Check 4.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage4):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe4[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot4 == "4":  # Recherche du rotor présent sur cet emplacement
                print("Check 4!")
                for test3 in range(26):
                    test_rotor = rotor4[test3]
                    if traited_letter == test_rotor:
                        print("Check 4.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage4):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe4[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot4 == "5":  # Recherche du rotor présent sur cet emplacement
                print("Check 4!")
                for test3 in range(26):
                    test_rotor = rotor5[test3]
                    if traited_letter == test_rotor:
                        print("Check 4.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage4):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe4[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot4 == "6":  # Recherche du rotor présent sur cet emplacement
                print("Check 4!")
                for test3 in range(26):
                    test_rotor = rotor6[test3]
                    if traited_letter == test_rotor:
                        print("Check 4.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage4):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe4[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot4 == "7":  # Recherche du rotor présent sur cet emplacement
                print("Check 4!")
                for test3 in range(26):
                    test_rotor = rotor7[test3]
                    if traited_letter == test_rotor:
                        print("Check 4.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage4):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe4[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot4 == "8":  # Recherche du rotor présent sur cet emplacement
                print("Check 4!")
                for test3 in range(26):
                    test_rotor = rotor8[test3]
                    if traited_letter == test_rotor:
                        print("Check 4.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage4):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe4[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break

            # Check du 3ème emplacement
            print(f"La transformation de la lettre {letters_number} est {traited_letter} !")
            if slot3 == "1":
                print("Check 3!")
                for test3 in range(26):
                    test_rotor = rotor1[test3]
                    if traited_letter == test_rotor:
                        print("Check 3.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage3):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe3[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot3 == "2":
                print("Check 3!")
                for test3 in range(26):
                    test_rotor = rotor2[test3]
                    if traited_letter == test_rotor:
                        print("Check 3.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage3):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe3[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot3 == "3":
                print("Check 3!")
                for test3 in range(26):
                    test_rotor = rotor3[test3]
                    if traited_letter == test_rotor:
                        print("Check 3.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage3):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe3[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot3 == "4":
                print("Check 3!")
                for test3 in range(26):
                    test_rotor = rotor4[test3]
                    if traited_letter == test_rotor:
                        letter_choice = test3
                        for x in range(decalage3):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe3[letter_choice]
                        break
            elif slot3 == "5":
                print("Check 3!")
                for test3 in range(26):
                    test_rotor = rotor5[test3]
                    if traited_letter == test_rotor:
                        letter_choice = test3
                        for x in range(decalage3):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe3[letter_choice]
                        break
            elif slot3 == "6":
                for test3 in range(26):
                    test_rotor = rotor6[test3]
                    if traited_letter == test_rotor:
                        letter_choice = test3
                        for x in range(decalage3):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe3[letter_choice]
                        break
            elif slot3 == "7":
                for test3 in range(26):
                    test_rotor = rotor7[test3]
                    if traited_letter == test_rotor:
                        letter_choice = test3
                        for x in range(decalage3):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe3[letter_choice]
                        break
            elif slot3 == "8":
                print("Check 3!")
                for test3 in range(26):
                    test_rotor = rotor8[test3]
                    if traited_letter == test_rotor:
                        letter_choice = test3
                        for x in range(decalage3):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe3[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            print(f"La transformation de la lettre {letters_number} est {traited_letter} !")

            # Check du 2ème emplacement
            if slot2 == "1":
                print("Check 2!")
                for test3 in range(26):
                    test_rotor = rotor1[test3]
                    if traited_letter == test_rotor:
                        print("Check 2.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage2):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe2[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot2 == "2":
                print("Check 2!")
                for test3 in range(26):
                    test_rotor = rotor2[test3]
                    if traited_letter == test_rotor:
                        print("Check 2.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage2):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe2[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot2 == "3":
                print("Check 2!")
                for test3 in range(26):
                    test_rotor = rotor3[test3]
                    if traited_letter == test_rotor:
                        print("Check 2.2!")
                        letter_choice = test3
                        for x in range(decalage2):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe2[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot2 == "4":
                print("Check 2!")
                for test3 in range(26):
                    test_rotor = rotor4[test3]
                    if traited_letter == test_rotor:
                        print("Check 2.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage2):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe2[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot2 == "5":
                print("Check 2!")
                for test3 in range(26):
                    test_rotor = rotor5[test3]
                    if traited_letter == test_rotor:
                        print("Check 2.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage2):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe2[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot2 == "6":
                print("Check 2!")
                for test3 in range(26):
                    test_rotor = rotor6[test3]
                    if traited_letter == test_rotor:
                        print("Check 2.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage2):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe2[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot2 == "7":
                print("Check 2!")
                for test3 in range(26):
                    test_rotor = rotor7[test3]
                    if traited_letter == test_rotor:
                        print("Check 2.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage2):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe2[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot2 == "8":
                print("Check 2!")
                for test3 in range(26):
                    test_rotor = rotor8[test3]
                    if traited_letter == test_rotor:
                        print("Check 2.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage2):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe2[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            print(f"La transformation de la lettre {letters_number} est {traited_letter} !")

            # Check du premier emplacement
            if slot1 == "1":
                print("Check 1!")
                for test3 in range(26):
                    test_rotor = rotor1[test3]
                    if traited_letter == test_rotor:
                        print("Check 1.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage1):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        print(f"La valeur de letter_choice est {letter_choice}")
                        traited_letter = rotor_fixe1[letter_choice]
                        break
            elif slot1 == "2":
                print("Check 1!")
                for test3 in range(26):
                    test_rotor = rotor2[test3]
                    if traited_letter == test_rotor:
                        print("Check 1.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage1):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe1[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot1 == "3":
                print("Check 1!")
                for test3 in range(26):
                    test_rotor = rotor3[test3]
                    if traited_letter == test_rotor:
                        print("Check 1.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage1):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe1[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot1 == "4":
                print("Check 1!")
                for test3 in range(26):
                    test_rotor = rotor4[test3]
                    if traited_letter == test_rotor:
                        print("Check 1.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage1):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        traited_letter = rotor_fixe1[letter_choice]
                        print(f"La valeur de letter_choice est {letter_choice}")
                        break
            elif slot1 == "5":
                print("Check 1!")
                for test3 in range(26):
                    test_rotor = rotor5[test3]
                    if traited_letter == test_rotor:
                        print("Check 1.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage1):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        print(f"La valeur de letter_choice est {letter_choice}")
                        traited_letter = rotor_fixe1[letter_choice]
                        break
            elif slot1 == "6":
                print("Check 1!")
                for test3 in range(26):
                    test_rotor = rotor6[test3]
                    if traited_letter == test_rotor:
                        print("Check 1.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage1):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        print(f"La valeur de letter_choice est {letter_choice}")
                        traited_letter = rotor_fixe1[letter_choice]
                        break
            elif slot1 == "7":
                print("Check 1!")
                for test3 in range(26):
                    test_rotor = rotor7[test3]
                    if traited_letter == test_rotor:
                        print("Check 1.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage1):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        print(f"La valeur de letter_choice est {letter_choice}")
                        traited_letter = rotor_fixe1[letter_choice]
                        break
            elif slot1 == "8":
                print("Check 1!")
                for test3 in range(26):
                    test_rotor = rotor8[test3]
                    if traited_letter == test_rotor:
                        print("Check 1.2!")
                        print(f"La valeur de test_rotor est {test_rotor}")
                        letter_choice = test3
                        for x in range(decalage1):
                            letter_choice = letter_choice + 1
                            if letter_choice == 26:
                                letter_choice = 0
                        print(f"La valeur de letter_choice est {letter_choice}")
                        traited_letter = rotor_fixe1[letter_choice]
                        break
            print(f"La transformation de la lettre {letters_number} est {traited_letter} !")
            # tableau de réflection dans l'autre sens
            ok = False
            if standard:
                for test3 in range(26):  # Tableau de réflection, switch lettre
                    if traited_letter == alphabet[test3] and not ok:
                        traited_letter = connect_board[test3]
                        ok = True
            elif not standard:
                file2 = open(f"{chemin}\crypted_message_{test}_{current_pseudo}\switch_letters_{traited_letter}"
                             f"_crypted_message_{test}_{current_pseudo}.txt", "r")
                traited_letter = file2.read()
                file2.close()
            # Passage à la lettre suivante
            letters_number = letters_number + 1
            # On avance le rotor de 1 emplacement et si il a finit...
            decalage1 = decalage1 + 1
            if decalage1 == 26:
                decalage1 = 0
                decalage2 = decalage2 + 1
                if decalage2 == 26:
                    decalage2 = 0
                    decalage3 = decalage3 + 1
                    if decalage3 == 26:
                        decalage3 = 0
                        decalage4 = decalage4 + 1
                        if decalage4 == 26:
                            decalage4 = 0
            print(f"Le décalage du premier rotor : {decalage1}, le décalage du deuxième rotor : {decalage2}, le "
                  f"décalage du troisième rotor : {decalage3}, et le décalage du dernier rotor : {decalage4}")
            crypted_letter.append(traited_letter)
            print(f"La valeur finale de traited letter {traited_letter}")
    print("Cryptage terminé !")
    file.write(f"Message codé : ")
    for test in range(len(crypted_letter)):
        file.write(crypted_letter[test].strip())
    file.close()