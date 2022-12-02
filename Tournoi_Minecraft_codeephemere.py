import os
from Listes import *
from Classement import classement_tournoi


def tournoi_mc_ephemere():
    chemin = os.getcwd()
    fin = False
    print("Bienvenue sur l'interface, du tournoi The Network, sur Minecraft !!")
    print("Voici l'ordre des épreuves :\n     -Dé à coudre\n     -Tir à l'arc\n     -La course de bateau\n     "
          "-Le Jump\n     -Le TNT Run\n     -Le Splif\n     -La bataille de boule de neige\n     -Le Labyrinthe")
    reponse = ""
    reponse_valide = False
    nombre_participant = 0
    os.mkdir(f"{chemin}\Le_grand_tournoi")
    while not fin:
        nombre_participant = nombre_participant + 1
        reponse = str(input("Insérez le pseudo du joueur !"))
        joueur_tournoi.append(reponse)
        os.mkdir(f"{chemin}\Le_grand_tournoi\{nombre_participant-1}")
        file = open(f"{chemin}\Le_grand_tournoi\{nombre_participant-1}\{reponse}.txt", "w+")
        file.write(f"{reponse}\n")
        file.write("0")
        file.close()
        reponse_valide = False
        while not reponse_valide:
            reponse = str(input("Encore un autre participant ? (Oui/Non)"))
            if reponse in oui:
                reponse_valide = True
            elif reponse in non:
                reponse_valide = True
                fin = True
            else:
                print("Je ne comprends pas ta réponse, c'est oui ou bien c'est non !")
    print(f"{nombre_participant}participent à se tournoi !")
    file = open(f"{chemin}\Le_grand_tournoi\Information_tournoi.txt", "w+")
    file.write(nombres[nombre_participant])
    file.close()
    reponse_valide = False
    while not reponse_valide:
        reponse= str(input("Echauffement... (Ecrire prêt pour démarrer le tournoi)"))
        if reponse in pret:
            reponse_valide = True
