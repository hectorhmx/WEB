class Invertir:
  
  def __init__(self,list1):
    self.lista = list1
    self.par=0
    self.imp=0
  def voltear(self):
      for i in self.lista:
        if i%2==0:
          self.par=self.par+1
        else:
          self.imp=self.imp+1
      return self.par,self.imp  

lista= list(range(10))
a=Invertir(lista)

par,imp =a.voltear()
print("Par = {} Impar = {}".format(par,imp))