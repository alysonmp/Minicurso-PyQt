from PyQt6 import QtWidgets
import sys
from ControleAgenda import ControleAgenda

app = QtWidgets.QApplication(sys.argv)
janela = ControleAgenda()
janela.show()
sys.exit(app.exec())