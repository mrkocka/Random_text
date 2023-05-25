import random
import time


def filemuvelet():
    print("Elkezdődött a filébe írás!")
    time.sleep(2)
    f = open("data.txt", "a", encoding="utf-8")
    f.write(x+"\n")
    f.close()
    print("A szöveg a data.txt filében van")

def randol_olvasás():
    with open ("data.txt", "r", encoding="utf-8") as f:
        sorok = f.readlines()
        if sorok:
            r_sor = random.choice(sorok)
            print(r_sor)
        else:
            print("Hiba a file üres!")

x = input("Kérem a mondtatot: ")


filemuvelet()

time.sleep(2)

print("Most pedig kiolvasok egy véletlen sort a filéből!")
time.sleep(2)

randol_olvasás()