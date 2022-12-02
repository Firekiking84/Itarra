from Listes import *
from Authentification import authentification
from Lecture_horaire import lecture_horaire
from Gestion_schedule import gestion_schedule
from Creation_schedule import creation_schedule
from Enigma_machine import enigma_machine
from Vocalearn import vocalearn
from IA.AV import av_mode


def echangeur():
    file = open("current_user.txt", "r")
    informations = file.readlines()
    current_pseudo = informations[0].strip()
    if informations[1].strip() == "tutoiement":
        tutoiement = True
    elif informations[1].strip() == "vouvoiement":
        tutoiement = False
    if tutoiement:
        reponse = str(input(f"Oui ? Besoin de quelques chose {current_pseudo} ?")).split(" ")
    elif not tutoiement:
        reponse = str(input(f"Une question, {current_pseudo} ?")).split(" ")
    test = 0
    repondu = False
    here_compte = False
    here_utilisateur = False
    here_emploi_du_temps = 0
    Target_Itarra = False
    Extinction = False
    Lancement = False
    here_after = False
    here_demain = False
    here_cryptage = False
    here_switch_account = False
    here_pouvoir = False
    here_vocabulaire = False
    here_apprendre = False
    here_vouloir = False
    here_mode = False
    here_IA = False
    while test < len(reponse):
        if reponse[test] in hello:
            repondu = True
            if tutoiement:
                print(f"Yo {current_pseudo}!")
            elif not tutoiement:
                print(f"Bonjour {current_pseudo}!")
        elif reponse[test] in utilisateur:
            here_utilisateur = True
        elif reponse[test] in switch_account:
            here_switch_account = True
        elif reponse[test] in CL_changement:
            here_CL_changement = True
        elif reponse[test] in compte:
            here_compte = True
        elif reponse[test] in emploi_du_temps:
            here_emploi_du_temps = here_emploi_du_temps + 1
        elif reponse[test] in creation:
            here_creation = True
        elif reponse[test] in Itarra:
            Target_Itarra = True
        elif reponse[test] in Eteind:
            Extinction = True
        elif reponse[test] in Start:
            Lancement = True
        elif reponse[test] in after:
            here_after = True
        elif reponse[test] in demain:
            here_demain = True
        elif reponse[test] in cryptage:
            here_cryptage = True
        elif reponse[test] in pouvoir:
            here_pouvoir = True
        elif reponse[test] in vouloir:
            here_vouloir = True
        elif reponse[test] in apprendre:
            here_apprendre = True
        elif reponse[test] in vocabulaire:
            here_vocabulaire = True
        elif reponse[test] in mode:
            here_mode = True
        elif reponse[test] in IA:
            here_IA = True
        else:
            if tutoiement:
                print(f"Oh la la ! Le mot --> {reponse[test]},je connais pas ! Pour tout problème, ou pour en"
                      " savoir plus sur moi, tape {help}")
            elif not tutoiement:
                print(f"Je ne comprends pas le mot : {reponse[test]}. Pour toute incompréhension, vous pouvez taper"
                      " {help}, pour avoir de l'aide")
        test = test + 1
    if here_compte and here_CL_changement or here_utilisateur and here_switch_account:
        authentification()
        repondu = True
    elif here_emploi_du_temps == 3:
        if here_creation:
            creation_schedule()
            repondu = True
        elif not here_creation:
            gestion_schedule()
            repondu = True
    elif Target_Itarra and Extinction:
        repondu = True
        if tutoiement:
            print(f"A plus {current_pseudo}!!")
        elif not tutoiement:
            print(f"Au revoir {current_pseudo}")
        status_Itarra[0] = "0"
    elif Lancement and here_demain:
        lecture_horaire()
        repondu = True
    elif Itarra and here_cryptage and here_pouvoir or here_vouloir and here_utilisateur and here_cryptage:
        enigma_machine()
        repondu = True
    elif here_utilisateur and here_vocabulaire and here_apprendre:
        vocalearn()
        repondu = True
    elif here_mode and here_IA:
        av_mode()
        repondu = True
    if not repondu:
        if tutoiement:
            print("Désolé, je comprends pas ce que tu dis ! Attends une MAJ ou revois l'orthographe")
        elif not tutoiement:
            print("Je suis désolé, je ne comprends pas votre question ! Merci d'attendre d'autres mise à jour ou de "
                  "revoir votre orthographe")