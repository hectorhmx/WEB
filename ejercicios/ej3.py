import random

def adivina(valor,suerte):
    if(valor==suerte):
      return False
    else:
      print("Error")
      return True

suerte=random.randrange(1,9)
seguir = True;

while (seguir):
  entrada=int(input("Dime un numero"))
  seguir=adivina(entrada,suerte)  
print("Bien logrado")


