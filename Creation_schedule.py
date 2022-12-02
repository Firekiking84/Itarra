from Listes import *


def creation_schedule():
    file = open("current_user.txt", "r")
    informations = file.readlines()
    current_pseudo = informations[0].strip()
    file.close()
    reponse_valide = False
    if informations[1].strip() == "tutoiement":
        tutoiement = True
    elif informations[1].strip() == "vouvoiement":
        tutoiement = False
    if tutoiement:
        print("Bon, comme tu m'as demandé, on va créer un emploi du temps pour un format lycée/collège")

    elif not tutoiement:
        print("Comme vous me l'avez demandé, nous allons créer un emploi du temps pour un format type lycée/collège")

    test = 0
    reponse_valide = False
    while not reponse_valide:
        if tutoiement:
            reponse = str(input("Toujours ok pour toi, on continue ?")).split(" ")
        elif not tutoiement:
            reponse = str(input("Êtes-vous toujours d'accord ? Pouvons-nous continuer ?")).split(" ")
        for test in range(len(reponse)):
            if reponse[test] in oui:
                reponse_valide = True
                if tutoiement:
                    print("Et bah let's go !")
                elif not tutoiement:
                    print("Très bien alors continuons !")
            elif reponse[test] in non or reponse[test] in annulation:
                reponse_valide = True
                if tutoiement:
                    print("Ok, pas de problème ! ")
                elif not tutoiement:
                    print("D'accord.")
                return
            else:
                reponse_valide = False
                if tutoiement:
                    print("Euh... Je crois qu'on s'est pas bien compris la réponse c'est oui ou non !")
                elif not tutoiement:
                    print("Je ne comprends pas votre réponse")
    file = open(f"{current_pseudo}_schedule.txt", "w")
    if tutoiement:
        print("Bon je vais commencer par les horaires...")
    elif not tutoiement:
        print("Nous allons d'abord commencer par les horaires...")
    test = 0
    for test in range(5):
        if tutoiement:
            matin = str(input(f"A qu'elle heure tu commences le {jour_de_la_semaine[test]} ? --> ")).split(" ")
            soir = str(input(f"A qu'elle heure tu finis le {jour_de_la_semaine[test]} ? --> ")).split(" ")
        elif not tutoiement:
            matin = str(input(f"A qu'elle heure commencez-vous le {jour_de_la_semaine[test]} ? --> ")).split(" ")
            soir = str(input(f"A qu'elle heure finissez-vous le {jour_de_la_semaine[test]} ? --> ")).split(" ")
        file.write(f"{matin}\n")
        file.write(f"{soir}\n")
    if tutoiement:
        print("Ça c'est fait, maintenant passons à tes heures de cours !")
    elif not tutoiement:
        print("Maintenant que nous avons fini, de passer en revu vos horaires, passons maintenant au contenu de vos"
              "journées.")
    reponse_valide = False
    while not reponse_valide:
        if tutoiement:
            reponse = str(input("Toujours ok ? On continue ? --> ")).split(" ")
        elif not tutoiement:
            reponse = str(input("Tout va bien ? Êtes-vous toujours d'accord pour continuer ? --> ")).split(" ")
        for test in range(len(reponse)):
            if reponse[test] in oui:
                reponse_valide = True
                if tutoiement:
                    print(f"Bon bah cool, allez on passe à la suite ! Toi, je t'aime bien {current_pseudo}")
                elif not tutoiement:
                    print(f"Très bien, je vois que vous me suivez bien ! Je vous apprécie {current_pseudo} nous "
                          "sommes sur une belle lancée")
            elif reponse[test] in non or reponse[test] in annulation:
                reponse_valide = True
                if tutoiement:
                    print(f"Dommage, on avait bien commencé ! Peut-être pour plus tard {current_pseudo} ?")
                elif tutoiement:
                    print(f"Dommage, nous avions bien amorcé ! Peut-être une autre fois {current_pseudo} ?")
                return
            else:
                reponse_valide = False
                if tutoiement:
                    print("Euh... C'est comme la dernière fois, c'est oui ou bien c'est non !")
                elif not tutoiement:
                    print("Je ne comprends pas votre réponse !")
    for test in range(5):
        reponse_valide = False
        reponse = ""
        while not reponse_valide:
            if tutoiement:
                reponse = str(input(f"Combien d'heure de cours as-tu le {jour_de_la_semaine[test]} ? --> "))
            elif not tutoiement:
                reponse = str(input(f"Combien d'heure de cours avez-vous le {jour_de_la_semaine[test]} ? --> "))
            for test2 in range(len(reponse)):
                if reponse[test2] in chiffres:
                    reponse_valide = True
                    for test3 in range(10):
                        if chiffres[test3] == reponse[test2]:
                            reponse_int = test3
                else:
                    if tutoiement:
                        print("Eh mais tu me prends pour qui ? Je veux des chiffres !!")
                    elif not tutoiement:
                        print("Je pense que vous vous êtes trompé car la réponse ne peut être composé par seulement des"
                              "chiffres")
                    reponse_valide = False
        if tutoiement:
            print("Peux-tu écrire avec la même orthographe un même mots jusqu'au bout. C'est très important pour la "
                  "suite !")
        elif not tutoiement:
            print("Pouvez vous écrire avec la même orthographe tout au long de cette partie. C'est très important "
                  "pour la suite !")
        file.write(f"{jour_de_la_semaine[test]}\n")
        informations = ""
        for test2 in range(reponse_int):
            test2 = test2 + 1
            if tutoiement:
                informations = str(input(f"T'as quoi à l'heure n°{test2} --> "))
            elif not tutoiement:
                informations = str(input(f"Qu'avez-vous à l'heure n°{test2} --> "))
            file.write(f"{informations}\n")
    if tutoiement:
        print("Bien, Bien, on avance bien, bon la dernière étape c'est que vas tu avoir besoin pour tout ça !")
    elif not tutoiement:
        print("Très bien, nous avons bientôt fini, dans cette dernière étape nous allons voir ce que vous avez besoin"
              "pour tout ce que vous m'avez dit précédemment.")
    reponse_valide = False
    while not reponse_valide:
        if tutoiement:
            reponse = str(input("On continue ? --> ")).split(" ")
        elif not tutoiement:
            reponse = str(input("Êtes-vous toujours prêt à continuer ? --> ")).split(" ")
        for test in range(len(reponse)):
            if reponse[test] in oui:
                reponse_valide = True
                if tutoiement:
                    print("Ouais, Ouais et Ouais, allez on va le finir ensemble cet emploi du temps !")
                elif not tutoiement:
                    print("Bien, nous allons pouvoir conclure cet emploi du temps une fois pour toute.")
            elif reponse[test] in non or reponse[test] in annulation:
                if tutoiement:
                    print("Bon, bah dommage... AH au fait tout ce que tu as fait est perdu... CHEH !")
                elif not tutoiement:
                    print("C'est dommage, étant donné qu'on avait presque fini, surtout dans le contexte où je ne peux"
                          "rien garder !")
                return
    file.close()
    matiere = []
    informations = []
    file = open(f"{current_pseudo}_schedule.txt", "r")
    informations = file.readlines()
    file.close()
    file = open(f"{current_pseudo}_schedule.txt", "a")
    test = 0
    test2 = 0
    test4 = 0
    while informations[test].strip() not in jour_de_la_semaine:
        test = test + 1
        if informations[test].strip() in jour_de_la_semaine:
            test4 = test
    for test in range(len(informations)):
        if informations[test].strip() not in jour_de_la_semaine and test >= test4:
            if informations[test] in matiere:
                print(f"{informations[test].strip()} on a déjà vu !")
            else:
                matiere.append(informations[test])
                if tutoiement:
                    reponse = str(input(f"Qu'à tu besoin pour ça : {informations[test].strip()} --> "))
                elif not tutoiement:
                    reponse = str(input(f"De quoi avez-vous besoin pour : {informations[test].strip} --> "))
                file.write(f"{informations[test].strip()}\n")
                file.write(f"{reponse}\n")
                reponse_valide = False
                while not reponse_valide:
                    reponse = str(input("Toujours nécessaire ? --> ")).split(" ")
                    for test2 in range(len(reponse)):
                        if reponse[test2] in oui:
                            reponse_valide = True
                            file.write("Obligatoire\n")
                        elif reponse[test2] in non:
                            reponse_valide = True
                            file.write("Facultatif\n")
                        else:
                            if tutoiement:
                                print("Oulà, je comprends pas ce que tu as dit ! Articule pour voir ?")
                            elif not tutoiement:
                                print("Je ne comprends pas votre réponse")
                fin = False
                while not fin:
                    reponse_valide = False
                    reponse = str(input("Autre chose ? --> ")).split(" ")
                    for test3 in range(len(reponse)):
                        if reponse[test3] in non:
                            fin = True
                        else:
                            file.write(f"{reponse}\n")
                            while not reponse_valide:
                                reponse = str(input("Toujours nécessaire ? --> ")).split(" ")
                                for test2 in range(len(reponse)):
                                    if reponse[test2] in oui:
                                        reponse_valide = True
                                        file.write("Obligatoire\n")
                                    elif reponse[test2] in non:
                                        reponse_valide = True
                                        file.write("Facultative\n")