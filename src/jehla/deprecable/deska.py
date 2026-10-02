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
    
    #vraci na jaké y pozici je nejbližší linka k zadanému y souřadnici
    def nejblizsi_linka(self,y):
        if(y<0 or y>self.delkay):
            return -1
        nejblizsi=np.round(y/self.mezilinkovy_prostor)*self.mezilinkovy_prostor
        return nejblizsi
    
    def uvnitr_desky(self,x,y)->bool:
        return True if (0<x<self.delkax and 0<y<self.delkay) else False
    
    def protina_linku(self,jehla)->bool:
        nejblizsi_linka=self.nejblizsi_linka(jehla.stredy)
        if(jehla.projekce_min<= nejblizsi_linka <= jehla.projekce_max):
            jehla.protla=True
            return True
        else:
            jehla.protla=False
            return False