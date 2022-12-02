import os
from Listes import *
import shutil


def classement_tournoi():
    test1 = 0
    test2 = 0
    chemin = os.getcwd()
    file = open(f"{chemin}/Le_grand_tournoi/Information_tournoi.txt", "r")
    informations = file.readlines()
    file.close()
    nombre_participant = informations[0].strip()
    int_nombre_participant = int(nombre_participant)
    modification = True
    player1 = 0
    player2 = 0
    while modification:
        modification = False
        for i in range(int_nombre_participant):
            test1 = 0
            test2 = 0
            for y in range(int_nombre_participant):
                if os.path.exists(f"{chemin}/Le_grand_tournoi/{i}/{joueur_tournoi[y]}.txt"):
                    player1 = y
                    file = open(f"{chemin}/Le_grand_tournoi/{i}/{joueur_tournoi[y]}.txt")
                    informations = file.readlines()
                    file.close()
                    test1 = int(informations[1].strip())
                    for n in range(int_nombre_participant):
                        if os.path.exists(f"{chemin}/Le_grand_tournoi/{i + 1}/{joueur_tournoi[n]}.txt"):
                            player2 = n
                            file = open(f'{chemin}/Le_grand_tournoi/{i + 1}/{joueur_tournoi[n]}.txt')
                            informations = file.readlines()
                            file.close()
                            test2 = int(informations[1].strip())
            if test1 < test2:
                modification = True
                shutil.move(f"{chemin}/Le_grand_tournoi/{i}/{joueur_tournoi[player1]}.txt", f'{chemin}/Le_grand_tournoi'
                                                                                            f'/{i + 1}')
                shutil.move(f'{chemin}/Le_grand_tournoi/{i + 1}/{joueur_tournoi[player2]}.txt', f"{chemin}/"
                                                                                                f"Le_grand_tournoi/{i}")
    file = open("Classement.txt", "w+")
    for i in range(int_nombre_participant):
        for y in range(int_nombre_participant):
            if os.path.exists(f"{chemin}/Le_grand_tournoi/{i}/{joueur_tournoi[y]}.txt"):
                print(f"Le n°{i} est {joueur_tournoi[y]}")
                file.write(f"{i}: {joueur_tournoi[y]}\n")