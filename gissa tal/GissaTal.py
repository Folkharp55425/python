import random

print("\n hello")
print("-----------------------------------------------------------------\n")
print("-GissaTalet-\n\n")

print("gissa ett tal mellan 1 till 10, du får 3 försök på dig\n")
slumptal = random.randint(1, 10)

i = 0
t = ("slumptal")
r = ("gissatal")
hittat = False

while i < 3:
    gissatal =input("mata in tal: ")

    if t == r:
        hittat = True
        print("\n Rätt svar! \n")
        break
    i += 1

    if hittat:
        print("\nRätt!, Du är ett äkta smartskaft")
    else:
        print("\nHur dålig är du?")

    print("\n-----------------------------------------------------------")