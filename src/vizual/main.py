import sys
import const
import colors
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout,QWidget, QSpinBox, QLabel, QSlider, QGraphicsView, QGraphicsScene, QFormLayout
from PySide6.QtCore import Qt, QTimer, QRectF
from PySide6.QtGui import QPen, QColor, QBrush, QPainter
from jehla.simulace2 import simulace
SIRKA_DESKY = getattr(const, "SIRKA_DESKY", 600)


class Form(QMainWindow):
     def __init__(self, parent = None):
          super().__init__(parent)
          self.setWindowTitle("Jehličky")
          self.resize(1000, 600)
          self.sim = None
          self.timer = QTimer(self)

          self.widgety()
          self.layouty()
          self.signaly()

     def widgety(self):
          self.spinbox_pocet_jehel = QSpinBox()
          self.spinbox_pocet_jehel.setRange(1, const.MAX_JEHEL)
          self.spinbox_pocet_jehel.setValue(min(1000, const.MAX_JEHEL))
          self.spinbox_pocet_linek = QSpinBox()
          self.spinbox_pocet_linek.setRange(1, const.MAX_LINEK)
          self.spinbox_pocet_linek.setValue(min(5, const.MAX_LINEK))

          self.slider_mezera = QSlider(Qt.Horizontal)
          self.slider_mezera.setRange(10, 200)
          self.slider_mezera.setValue(50)
          self.label_mezera = QLabel("50")

          self.spinbox_delka_jehly = QSpinBox()
          self.spinbox_delka_jehly.setRange(1, 50)
          self.spinbox_delka_jehly.setValue(25)

          self.spinbox_time = QSpinBox()
          self.spinbox_time.setRange(1, 1000)
          self.spinbox_time.setValue(10)
          self.spinbox_time.setSuffix(" ms")

          self.btn_spustit = QPushButton("Spustit simulaci")
          self.label_vysledek = QLabel(self.text_vysledku(0, 0, 0, 0))
          self.btn_spustit_bez_vizualizace = QPushButton("Spustit bez vizualizace")

          self.scene = QGraphicsScene()
          self.view = QGraphicsView(self.scene)
          self.view.setRenderHint(QPainter.Antialiasing)
          self.view.setMinimumWidth(600)

     def layouty(self):
          form_layout = QFormLayout()
          form_layout.addRow("Počet jehel:", self.spinbox_pocet_jehel)
          form_layout.addRow("Počet linek:", self.spinbox_pocet_linek)
          form_layout.addRow("Délka jehly:", self.spinbox_delka_jehly)
          form_layout.addRow("Prodleva dopadu:", self.spinbox_time)
          mezera_layout = QHBoxLayout()
          mezera_layout.addWidget(self.slider_mezera)
          mezera_layout.addWidget(self.label_mezera)
          form_layout.addRow("Mezilinkový prostor:",mezera_layout)
          left_layout = QVBoxLayout()
          left_layout.addLayout(form_layout)
          left_layout.addWidget(self.btn_spustit)
          left_layout.addWidget(self.btn_spustit_bez_vizualizace)
          left_layout.addWidget(self.label_vysledek)
          left_layout.addStretch()
          main_layout = QHBoxLayout()
          main_layout.addLayout(left_layout)
          main_layout.addWidget(self.view, 1)
          cw = QWidget()
          cw.setLayout(main_layout)
          self.setCentralWidget(cw)

     def signaly(self):
          self.btn_spustit.clicked.connect(self.spustit_simulaci)
          self.btn_spustit_bez_vizualizace.clicked.connect(self.spustit_simulaci_bez_vizualizace)
          self.slider_mezera.valueChanged.connect(self.kontrola_delky_jehly)
          self.timer.timeout.connect(self.krok)

     def kontrola_delky_jehly(self, hodnota_mezery):
          self.label_mezera.setText(str(hodnota_mezery))
          self.spinbox_delka_jehly.setMaximum(hodnota_mezery)
     def spustit_simulaci(self):
          if self.timer.isActive():      # stejné tlačítko zastavuje simulaci
               self.zastavit()
               return
          self.sim=simulace(delkax=SIRKA_DESKY,mezilinkovy_prostor=self.slider_mezera.value(),
               pocet_linek=self.spinbox_pocet_linek.value(), delka_jehly=self.spinbox_delka_jehly.value(),
               pocet_jehel=self.spinbox_pocet_jehel.value())
          self.vykresli_desku()
          self.aktualizuj_vysledek()
          self.nastav_ovladani(False)
          self.btn_spustit.setText("Zastavit")
          self.timer.start(self.spinbox_time.value())

     def zastavit(self):
          self.timer.stop()
          self.nastav_ovladani(True)
          self.btn_spustit.setText("Spustit simulaci")

     def nastav_ovladani(self, povoleno):
          for w in (self.spinbox_pocet_jehel,self.spinbox_pocet_linek,self.spinbox_delka_jehly,self.spinbox_time,self.slider_mezera):
               w.setEnabled(povoleno)

     def krok(self):
          if self.sim.hozeno>=self.sim.pocet_jehel:
               self.zastavit()
               return
          if self.sim.pridej_jehlu():
               self.vykresli_jehlu(self.sim.jehly[-1])
               self.aktualizuj_vysledek()

     def spustit_simulaci_bez_vizualizace(self):
          self.sim=simulace(delkax=SIRKA_DESKY,mezilinkovy_prostor=self.slider_mezera.value(),
               pocet_linek=self.spinbox_pocet_linek.value(), delka_jehly=self.spinbox_delka_jehly.value(),
               pocet_jehel=self.spinbox_pocet_jehel.value())
          self.sim.per_to_tam_bez_vizualizace()
          self.label_vysledek.setText(self.text_vysledku(self.sim.hozeno, self.sim.pocet_jehel, self.sim.pretnuto, self.sim.pi()))
     def vykresli_desku(self):
          d=self.sim.deska
          self.scene.clear()
          self.scene.addRect(QRectF(0,0,d.delkax,d.delkay),QPen(colors.thistle),QBrush(colors.shadow_grey))
          pen_linka = QPen(colors.muted_teal, 1.5)
          pen_linka.setCosmetic(True)
          for n in range(d.pocet_linek):
               y = d.n_ta_linka(n)
               self.scene.addLine(0, y, d.delkax, y, pen_linka)
          okraj = 10
          self.scene.setSceneRect(-okraj, -okraj, d.delkax + 2 * okraj, d.delkay + 2 * okraj)
          self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

     def vykresli_jehlu(self, j):
          barva = colors.beige if j.protla else colors.raspberry
          pen = QPen(barva, 2)
          pen.setCosmetic(True)   # tloušťka se nemění se zoomem
          self.scene.addLine(j.x1, j.y1, j.x2, j.y2, pen)

     @staticmethod
     def text_vysledku(hozeno, celkem, protnuto, pi):
          return (f"Hozeno: {hozeno} / {celkem}\n"
                    f"Protnuto: {protnuto}\n"
                    f"Aproximace π: {pi:.5f}")

     def aktualizuj_vysledek(self):
          s = self.sim
          self.label_vysledek.setText(
               self.text_vysledku(s.hozeno, s.pocet_jehel, s.pretnuto, s.pi()))
     def resizeEvent(self, event):
          super().resizeEvent(event)
          if self.sim is not None:
               self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)



if __name__ == '__main__':
     app = QApplication(sys.argv)
     form = Form()
     form.show()
     sys.exit(app.exec())