class Calcular:

  def voltear(self,n):
      if n==0:
        return 1
      return(n*self.voltear(n-1))


a=Calcular()
print(a.voltear(5))

