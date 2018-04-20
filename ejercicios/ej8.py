class Buscar:
  
  def __init__(self,list1):
    self.lista = list1

  def voltear(self):
      for i in self.lista:
        if(i%3==0):
            continue
        elif(i==0):
            print(i)
        else:
            print(i)

lista= list(range(0,7))
a=Buscar(lista)
a.voltear()
