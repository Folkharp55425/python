# Alternativ 1.  

# def hello(to="User"): 
#     print("Hello,", to)
    
# hello()
# name = input("What's your name? ")
# hello(name)

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="User"): 
    print("Hello,", to)

main()

#hur man gör en input text variabel och integrerar den i en print text

# Fråga om användarens namn
# name = input("what's your name?\n").strip().title()

# Separerar på Svaret per mellanrum = per ,
# first, last = name.split(" ")

# säg hej till användaren
# print(f"hello, {first}!")



# Sätt att ändra variabeln så att användar error inte saboterar svaret
# name = name.x()
#  ".strip()" Tar bort mellanrum höger och vänster av namnet
# ".Title()" Stor boxstav i början av varje ord i variabeln
# ".capitilize()" Gör endast stor bokstav av första bokstaven

# Olika alternativ att lösa det på. 
# name = input("what's your name?\n")
# version 1.
# print("hello,")
# print(name)
# version 2.
# print("hello, "+ name)
# Version 3.
# print(f"hello, {name}")