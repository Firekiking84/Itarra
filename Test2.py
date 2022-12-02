from random import randint

vocTec = ["PE", "q", "Nrésolution", "Vnum", "Ndivision", "P(position du mobile)", "σ(avec N et S)", "σ(avec Rpe)", "Rpe et"
                                                                                                                " σp"
                                                                                                                "e et "
                                                                                                                "σe "
                                                                                                                "et s",
          "ε", "σ(avec E et ε)", "𝛕(avec T et S)", "Théorèmes des forces 1 et 2", "Translation Ec", "Rotation Ec", "Ec"
                                                                                                                    "(avec masse volumique)",
          "Puissance cinétique", "Précup", "Puissance solaire", "1Wh", "rapport engrenage",
          "Pméca", "Cu", "Pelec monophasé", "N", "G", "Ω"]

reponse = "Yo"
while reponse != "F":
    reponse = str(input("Quel liste ?"))
    if reponse == "T":
        while reponse != "F":
            x = randint(0, len(vocTec) - 1)
            reponse = str(input(vocTec[x]))
