import numpy as np

class jehla:
    def init(self, stredx,stredy, delka, rotace):
        self.stredx=stredx
        self.stredy=stredy
        self.delka=delka
        self.rotace=rotace
        hitnuto=False
    @property
    def jeden_konec(self):
        x1=self.stredx-(self.delka/2)*(np.cos(self.rotace))
        y1=self.stredy-(self.delka/2)*np.sin(self.rotace)
        return x1,y1

    @property
    def druhy_konec(self):
        x2=self.stredx+(self.delka/2)*(np.cos(self.rotace))
        y2=self.stredy+(self.delka/2)*np.sin(self.rotace)
        return x2,y2
    @property
    def projekce_dole(self):
        y_d_p=self.stredy-np.abs(self.delka/2*np.sin(self.rotace))
        return y_d_p
    @property
    def projekce_hore(self):
        y_n_p=self.stredy+np.abs(self.delka/2*np.sin(self.rotace))
        return y_n_p