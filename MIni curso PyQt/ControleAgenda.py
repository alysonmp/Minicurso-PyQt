from interface import Ui_MainWindow
from PyQt6 import QtWidgets, QtCore
import sys
from Tarefa import Tarefa
from datetime import datetime

class ControleAgenda(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.lista = [
    Tarefa("Reunião de Projeto", "Discussão sobre o andamento do projeto X", "10/05/2025 09:00", "10/05/2025 11:00", "Reunião", "Agendado", True),
    Tarefa("Consulta Médica Sexta", "Consulta de rotina com o Dr. Silva", "12/05/2025 14:00", "12/05/2025 15:00", "Médico", "Confirmado", False),
    Tarefa("Trabalho de Grupo", "Reunião para entrega do trabalho final", "13/05/2025 10:00", "13/05/2025 12:00", "Trabalho", "Agendado", True),
    Tarefa("Jogo de Futebol", "Partida de futebol com os amigos", "14/05/2025 18:00", "14/05/2025 20:00", "Lazer", "Agendado", False),
    Tarefa("Descanso", "Pausa para descansar e relaxar", "15/05/2025 13:00", "15/05/2025 15:00", "Descanso", "Confirmado", False),
    ]
    
        self.ui.actionVisualizar.triggered.connect(self.mudaVisualizar)
        self.ui.actionCadastrar.triggered.connect(self.mudaCadastrar)

        self.ui.pushButton_ok.clicked.connect(self.cadastraTarefa)

        self.ui.comboBox_visualizar_titulo.currentIndexChanged.connect(self.preencherCampos)
        self.ui.pushButton_atualizar.clicked.connect(self.atualizaCampos)
        self.ui.pushButto_limpar.clicked.connect(self.limpaCampos)


    def mudaVisualizar(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.comboBox_visualizar_titulo.clear()
        for item in self.lista:
            self.ui.comboBox_visualizar_titulo.addItem(item.titulo)

    def mudaCadastrar(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def cadastraTarefa(self):
        titulo = self.ui.lineEdit_cadastro_titulo.text()
        self.ui.lineEdit_cadastro_titulo.setText("")

        descricao = self.ui.textEdit_cadastro_descricao.toPlainText()
        self.ui.textEdit_cadastro_descricao.setText("")

        inicio = self.ui.dateTimeEdit_cadastro_inicio.text()
        fim = self.ui.dateTimeEdit_cadastro_fim.text()
        
        tipo = self.ui.comboBox_cadastro_tipo.currentText()
        status = self.ui.comboBox_cadastro_status.currentText()
        urgente = self.ui.checkBox_cadastro.isChecked()

        tarefa = Tarefa(titulo, descricao, inicio, fim, tipo, status, urgente)
        self.lista.append(tarefa)

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setWindowTitle("Cadastro")
        msg.setText("Tarefa cadastrada com sucesso!")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

    def preencherCampos(self):
        selecao = self.ui.comboBox_visualizar_titulo.currentText()
        for item in self.lista:
            if selecao == item.titulo:
                self.ui.textEdit_visualizar_descricao.setText(item.descricao)

                dt = datetime.strptime(item.inicio, "%d/%m/%Y %H:%M")
                qt_dt = QtCore.QDateTime(dt.year, dt.month, dt.day, dt.hour, dt.minute)

                self.ui.dateTimeEdit_visualizar_inicio.setDateTime(qt_dt)

                dt = datetime.strptime(item.fim, "%d/%m/%Y %H:%M")
                qt_dt = QtCore.QDateTime(dt.year, dt.month, dt.day, dt.hour, dt.minute)

                self.ui.dateTimeEdit_visualizar_fim.setDateTime(qt_dt)

                self.ui.comboBox_visualizar_tipo.setCurrentText(item.tipo)
                self.ui.comboBox_visualizar_status.setCurrentText(item.status)
                self.ui.checkBox_visualizar.setChecked(item.urgente)

    def atualizaCampos(self):
        titulo = self.ui.comboBox_visualizar_titulo.currentText()
        descricao = self.ui.textEdit_visualizar_descricao.toPlainText()
        inicio = self.ui.dateTimeEdit_visualizar_inicio.text()
        fim = self.ui.dateTimeEdit_cadastro_fim.text()
        tipo = self.ui.comboBox_visualizar_tipo.currentText()
        status = self.ui.comboBox_visualizar_status.currentText()
        urgente = self.ui.checkBox_visualizar.isChecked()

        tarefa = Tarefa(titulo, descricao, inicio, fim, tipo, status, urgente)

        indice = self.ui.comboBox_visualizar_titulo.currentIndex()

        self.lista[indice] = tarefa

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setWindowTitle("Visualização")
        msg.setText("Tarefa atualizada com sucesso!")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

    def limpaCampos(self):
        self.ui.lineEdit_cadastro_titulo.setText("")
        self.ui.textEdit_visualizar_descricao.setText("")