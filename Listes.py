import os

chemin = os.getcwd()
hello_Itarra = ["Coucou", "Salut", "Bonjour", "Hello", "Yo", "Wesh",]
hello = ["Coucou", "Salut", "Bonjour", "Hello", "hello", "yo", "Yo", "Wesh", "coucou", "salut", "bonjour", "CC", "cc",
         "Salut,", "Bonjour,", "Hello,", "hello,", "yo,", "Yo,", "Wesh,", "coucou,", "salut,", "bonjour,",
         "CC,", "cc,", "re", "Coucou,"]
oui = ["yes", "Oui", "oui", "J'accepte", "Yes", "OUI"]
non = ["no", "No", "Non", "non", "refuse", "nn", "NN", "NON"]
utilisateur = ["moi", "Moi", "Je", "je"]
switch_account = ["Déconnecte", "deco", "déco", "Deconnecte", "deconnecte", "déconnecte"]
CL_changement = ["Changer", "changer", "Change", "Switch", "change", "switch"]
compte = ["compte", "pseudo", "account", "Compte", "Pseudo"]
creation = ["Nouveau", "créer", "Créer", "Création", "création", "créé"]
emploi_du_temps = ["Emploi", "emploi", "du", "temps"]
jour_de_la_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche", "lundi", "mardi",
                      "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
annulation = ["Stop", "Cancel", "stop", "Arrête", "Arrete", "arrete", "cancel", "m'arrete", "m'arrête", "j'arrete",
              "j'arrête", "J'arrete", "J'arrête", "pars", "Part", "part", "Pars", "sortir", "arrêter", "STOP"]
continuer = ["continue", "continu", "Continue", "Continu", "reste", "Reste", "continuer", "rester"]
negation = ["Ne", "pas", "ne"]
Itarra = ["Itarra", "toi", "tu"]
Eteind = ["Stop", "Eteint", "éteint", "Arrête", "Arrete", "arrete", "arrête"]
status_Itarra = ["1"]
Start = ["Commence", "débute", "début", "commence", "start", "Start", "Lance", "lance", "démarre", "Démarre", "demarre"]
demain = ["Demain", "demain"]
after = ["Après", "après"]
voir = ["regarder", "lire", "observer", "contempler", "voir"]
week_end = ["Samedi", "Dimanche", "samedi", "dimanche"]
chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
cryptage = ["Code", "crypter", "codé", "crypté", "coder", "encoder", "code", "Crypter", "Codé", "Crypté", "Coder",
            "Encoder", "Code"]
pouvoir = ["Peux", "Pouvais", "peux", "pouvais"]
vouloir = ["veux", "voudrais", "aimerais"]
vocabulaire = ["définition", "définitions", "mots", "mot", "vocabulaire", "Vocabulaire", "termes", "terme", "date",
               "dates"]
apprendre = ["apprendre", "acquérir", "étudier"]
rotor1 = ['g', 'e', 'p', 'l', 'm', 'k', 's', 'b', 'r', 'i', 'a', 'z', 'w', 'j', 'f', 'd', 'n', 'q', 'c', 'y', 'u', 'x',
          'h', 'v', 't', 'o']
rotor2 = ['x', 'l', 'd', 'p', 'm', 'u', 'n', 'v', 'q', 'o', 'c', 'z', 'r', 'e', 'a', 't', 'k', 'g', 'j', 'h', 'y', 'b',
          's', 'i', 'f', 'w']
rotor3 = ['q', 'b', 't', 'g', 'w', 'y', 'c', 'm', 'l', 's', 'k', 'o', 'h', 'n', 'a', 'e', 'u', 'd', 'j', 'z', 'r', 'p',
          'x', 'f', 'i', 'v']
rotor4 = ['s', 'u', 'x', 'j', 'g', 'i', 'y', 'p', 'v', 'n', 'a', 'l', 't', 'd', 'k', 'w', 'b', 'h', 'c', 'f', 'e', 'o',
          'r', 'q', 'z', 'm']
rotor5 = ['p', 'a', 'y', 'b', 'n', 'w', 'o', 'g', 'e', 'r', 'f', 'c', 'k', 's', 'z', 'h', 'q', 'u', 'j', 'i', 'd', 't',
          'm', 'x', 'v', 'l']
rotor6 = ['n', 'b', 'f', 'c', 'y', 'i', 'v', 'r', 'a', 't', 'j', 'g', 'q', 'p', 'o', 's', 'x', 'm', 'd', 'l', 'z', 'h',
          'u', 'k', 'e', 'w']
rotor7 = ['g', 'a', 'f', 'j', 'w', 'e', 'd', 'm', 'z', 'v', 'p', 'l', 'c', 's', 'i', 'r', 'b', 'x', 'y', 't', 'k', 'o',
          'h', 'n', 'q', 'u']
rotor8 = ['r', 'j', 'q', 'v', 'n', 'w', 's', 'z', 'u', 'm', 't', 'l', 'd', 'g', 'k', 'i', 'x', 'a', 'c', 'o', 'y', 'f',
          'e', 'h', 'b', 'p']
rotor_fixe1 = ['s', 'p', 'n', 'a', 'r', 'b', 'c', 'f', 'm', 'v', 'g', 'l', 't', 'j', 'k', 'q', 'x', 'i', 'z', 'y', 'u',
               'o', 'w', 'd', 'e', 'h']
rotor_fixe2 = ['p', 'f', 'd', 'e', 'k', 'r', 'a', 't', 'y', 'i', 'n', 'l', 'm', 'x', 'b', 'v', 'z', 'c', 's', 'h', 'w',
               'o', 'u', 'q', 'g', 'j']
rotor_fixe3 = ['r', 'z', 'm', 'h', 'l', 'y', 'x', 'c', 'i', 'b', 'f', 'p', 'q', 'a', 'g', 's', 'd', 'v', 'o', 'w', 'u',
               'k', 'j', 'e', 't', 'n']
rotor_fixe4 = ['b', 'w', 'q', 'p', 'k', 'r', 't', 'f', 'o', 'l', 'u', 'a', 'c', 'n', 's', 'g', 'e', 'y', 'i', 'm', 'd',
               'v', 'j', 'z', 'h', 'x']
connect_board = ["z", "h", "w", "y", "t", "s", "n", "b", "v", "m", "p", "u", "j", "g", "r", "k", "x", "o", "f", "e",
                 "l", "i", "c", "q", "d", "a"]
reflector = ["d", "u", "j", "a", "p", "y", "m", "w", "v", "c", "x", "o", "g", "s", "l", "e", "z", "t", "n", "r", "b",
             "i", "h", "k", "f", "q"]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]
nombres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
           "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37",
           "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50"]
joueur_tournoi = []
pret = ["Pret", "Prêt", "pret", "prêt", "Ready", "Go", "ready", "go"]
modification = ["modification", "modifier", "changer", "revoir", "modifié", "changé", "Changer"]
ajouter = ["Rajoute", "rajouter", "ajouter", "Ajouter", "rajouté", "ajouté", "Ajouté"]
reset_vocalearn = ["restart", "reset", "recommence", "redémarre", "relance"]
mode = ["Mode", "mode", "mod", "Mod"]
IA = ["Intelligence", "intelligence", "Artificiel", "artificiel", "Artificielle", "artificielle", "Assistant",
      "Assistante", "assistante", "assistant", "IA", "ia"]
