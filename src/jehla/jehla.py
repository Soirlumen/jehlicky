import numpy as np


class Jehla:
    def __init__(self, stredx, stredy, delka, rotace):
        self.stredx = stredx
        self.stredy = stredy
        self.delka = delka
        self.rotace = rotace
        self.protla = False

    @property
    def x1(self):
        x1 = self.stredx - (self.delka / 2) * (np.cos(self.rotace))
        return x1

    @property
    def y1(self):
        y1 = self.stredy - (self.delka / 2) * np.sin(self.rotace)
        return y1

    @property
    def x2(self):
        x2 = self.stredx + (self.delka / 2) * (np.cos(self.rotace))
        return x2

    @property
    def y2(self):
        y2 = self.stredy + (self.delka / 2) * np.sin(self.rotace)
        return y2

    @property
    def projekce_min(self):
        y_d_p = self.stredy - np.abs(self.delka / 2 * np.sin(self.rotace))
        return y_d_p

    @property
    def projekce_max(self):
        y_n_p = self.stredy + np.abs(self.delka / 2 * np.sin(self.rotace))
        return y_n_p
