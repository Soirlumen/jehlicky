from jehla import jehla
from deska import deska

import numpy as np

class simulace:
     def __init__(self,delkax,delkay,pocet_linek,delka_jehly,pocet_jehel):
        self.deska=deska(delkax,delkay,pocet_linek)
        self.delka_jehly=delka_jehly
        self.pocet_jehel=pocet_jehel
        self.jehly=[]
        self.pretnuto=0
        
     def pridej_jehlu(self)->bool:
          stredx=np.random.uniform(0,self.deska.delkax)
          stredy=np.random.uniform(0,self.deska.delkay)
          rotace=np.random.uniform(0,np.pi)
          if(self.deska.uvnitr_desky(stredx,stredy)):
               self.jehly.append(jehla(stredx,stredy,self.delka_jehly,rotace))
               if (self.deska.protina_linku(self.jehly[-1])):
                    self.jehly[-1].protla=True
               return True
          else:
               return False
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
          return 2*self.pocet_jehel*self.delka_jehly/(self.pretinajici_linky*self.deska.mezilinkovy_prostor)
     
     def per_to_tam_bez_vizualizace(self):
          pozice_jehel=np.random.uniform(0,self.deska.delkay,size=self.pocet_jehel)
          rotace_jehel=np.random.uniform(0,np.pi,size=self.pocet_jehel)
          pulka_yprumetu=np.sin(rotace_jehel)*self.delka_jehly/2
          y_min=pozice_jehel-pulka_yprumetu
          y_max=pozice_jehel+pulka_yprumetu
          d=self.deska.mezilinkovy_prostor
          protnuto=np.floor(y_min/d)!=np.floor(y_max/d)
          self.pretnuto=np.sum(protnuto)