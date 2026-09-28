import numpy as np

class deska:
    def __init__(self,delkax,delkay,pocet_linek):
        self.delkax=delkax
        self.delkay=delkay
        self.pocet_linek=pocet_linek

    @property
    def mezilinkovy_prostor(self):
        prostor=self.delkay/(self.pocet_linek+1)
        return prostor

    #indexujeme od nuly:)
    def n_ta_linka(self,n):
        if(n>=self.pocet_linek):
            return -1
        if(n<0):
            return -1
        return self.mezilinkovy_prostor*(n+1)
    
    def nejblizsi_linka(self,y):
        nejblizsi=np.max(1,np.min(np.round(y/self.mezilinkovy_prostor)))
        return nejblizsi
    
    def uvnitr_desky(self,x,y)->bool:
        return True if (0<x<self.delkax & 0<y<self.delkay) else False