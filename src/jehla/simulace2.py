from jehla.jehla import jehla
from jehla.deska2 import deska

import numpy as np

class simulace:
     def __init__(self,delkax,mezilinkovy_prostor,pocet_linek,delka_jehly,pocet_jehel):
          if delka_jehly > mezilinkovy_prostor:
            raise ValueError("Délka jehly nesmí být větší než mezilinkový prostor.")
          if pocet_linek < 2:
            raise ValueError("Je potřeba alespoň 2 linky.")
          if delka_jehly <= 0 or mezilinkovy_prostor <= 0 or pocet_jehel < 1:
               raise ValueError("Parametry musí být kladné.")
          self.deska=deska(delkax,mezilinkovy_prostor,pocet_linek)
          self.delka_jehly=delka_jehly
          self.pocet_jehel=pocet_jehel
          self.jehly=[]
          self.hozeno=0
          self.pretnuto=0
        
     def pridej_jehlu(self)->bool:
          d = self.deska.mezilinkovy_prostor
          stredx = np.random.uniform(0, self.deska.delkax)
          stredy = np.random.uniform(d, d * self.deska.pocet_linek)
          rotace=np.random.uniform(0,np.pi)
          if not self.deska.uvnitr_desky(stredx,stredy):
               return False
          
          j=jehla(stredx,stredy,self.delka_jehly,rotace)
          self.deska.protina_linku(j)
          self.jehly.append(j)
          self.hozeno+=1
          if j.protla:
               self.pretnuto+=1
          return True
          
     @property     
     def pretinajici_linky(self):
          cislo=0
          for i in range(self.pocet_jehel):
               if(self.jehly[i].protla):
                         cislo+=1
          return cislo
     
     def pi(self):
          if(self.pretnuto == 0):
               return 0
          return 2*self.hozeno*self.delka_jehly/(self.pretnuto*self.deska.mezilinkovy_prostor)
     
     def per_to_tam_bez_vizualizace(self):
          d = self.deska.mezilinkovy_prostor
          pozice_jehel = np.random.uniform(d, d * self.deska.pocet_linek, size=self.pocet_jehel)
          rotace_jehel=np.random.uniform(0,np.pi,size=self.pocet_jehel)
          pulka_yprumetu=np.sin(rotace_jehel)*self.delka_jehly/2
          y_min=pozice_jehel-pulka_yprumetu
          y_max=pozice_jehel+pulka_yprumetu
          k=np.floor(y_max/d)
          protnuto=(np.floor(y_min/d)!=k)&(k>=1)&(k<=self.deska.pocet_linek)
          self.hozeno=self.pocet_jehel
          self.pretnuto=int(np.sum(protnuto))
