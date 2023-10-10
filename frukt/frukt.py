import random

#skapar en tupple med frukter
frukter = ("Apelsin", "Päron", "Banan")
looping = True


def print_fruit(userinput):
    fnr =int(userinput)
    print(f"\n {frukter[fnr-1]} Kommer här! \n")

while True:
    print("-------------------------------------")
    print("\n-:FruktAutomat:-\n")

    i = 1
    for frukt in frukter:
        print(f"{str(i)} : {frukt}")
        i += 1
        #Print(str(i) + ": " + frukt) = print(f"{str(i)} : {frukt}")

    fruktnr = input("\nMata in siffra för vald frukt: ")
    print_fruit(fruktnr)

    go = input("Vill du välja en frukt till? j/N? ")
    print("\n")
    if (go == "n"):
        break

print("-------------------------------------")
print("Föresten, du får en frukt till!")
slumpfruktnr = random.randint(1, 3)
print_fruit(slumpfruktnr)