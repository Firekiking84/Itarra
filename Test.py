test1 = "en philosophie ou en ontologie, la substance définit ce qu'il y a de permanent dans les choses qui changent, et donc le fondement de tout accident".split(" ")
test2 = "en philosophie ou en ontologie, la substance désigne ce qu'il y a de permanent dans les choses qui changent, et donc le fondement de tout accident".split(" ")
for test in range(len(test1)):
    if test1[test] == test2[test]:
        print(f"Correct!")
    else:
        print(f"{test2[test]} est incorrect !")

total = 113
progression = 6
pourcentage = (progression / total) * 100
print(f"Tu as corrigé {int(pourcentage)}% de la totalité ! Plus que {int(100 - pourcentage)}%")

x = 10
for test in range(10):
    x = x + 1
    if x == 15:
        x = 0
    print(x)
print("--------")
x = 0
for test in range(10):
    x = x + 1
    if x == 0:
        print(x)

reponse = str(input("Appuie sur ENTER"))
print(len(reponse))
if len(reponse) == 0:
    print("Test ok !")
