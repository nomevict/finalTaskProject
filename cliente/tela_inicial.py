from PyQt5 import QtCore, QtGui, QtWidgets

class Tela_inicial(object):
    """
    Classe que configura a interface grafica da tela inicial.

    Responsavel por configurar a interface grafica da janela da tela inicial utilizando a biblioteca PyQt5.

    Attributes
    ----------
    cadastrar_telainicial__Button : QtWidgets.QPushButton
        Botão para cadastrar uma nova tarefa.
    buscar_tarefa_telainicial_Button_2 : QtWidgets.QPushButton
        Botão para encerrar o programa.
    sair_telainicial_Button_5 : QtWidgets.QPushButton
        Botão para voltar à tela anterior.
    buscar_tarefa_telainicial_Button : QtWidgets.QPushButton
        Botão para buscar tarefas.
    pushButton : QtWidgets.QPushButton
        Botão com um ícone de sino.
    line : QtWidgets.QFrame
        Linha separadora.
    label : QtWidgets.QLabel
        Rótulo com o texto "Focus Tasks".

    Methods
    -------
    setupUi(Cadastro)
        Configura a interface gráfica da tela inicial.
    retranslateUi(Cadastro)
        Traduz os textos exibidos na tela inicial.
    """

    def setupUi(self, Cadastro):
        """
        Configura a interface grafica da tela inicial.

        Este metodo cria e configura os elementos gráficos necessarios para a tela inicial.

        Parameters
        ----------
        Cadastro : QtWidgets.QWidget
            O objeto da janela principal em que a tela sera exibida.
        """
        Cadastro.setObjectName("Cadastro")
        Cadastro.resize(733, 628)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        Cadastro.setFont(font)
        Cadastro.setStyleSheet("background-color: rgb(0, 70, 112);")
        self.frame = QtWidgets.QFrame(Cadastro)
        self.frame.setGeometry(QtCore.QRect(150, 180, 431, 341))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0,0.2);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cadastrar_telainicial__Button = QtWidgets.QPushButton(self.frame)
        self.cadastrar_telainicial__Button.setGeometry(QtCore.QRect(110, 30, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cadastrar_telainicial__Button.setFont(font)
        self.cadastrar_telainicial__Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cadastrar_telainicial__Button.setStyleSheet("QPushButton{\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.cadastrar_telainicial__Button.setObjectName("cadastrar_telainicial__Button")
        self.buscar_tarefa_telainicial_Button_2 = QtWidgets.QPushButton(self.frame)
        self.buscar_tarefa_telainicial_Button_2.setGeometry(QtCore.QRect(110, 170, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buscar_tarefa_telainicial_Button_2.setFont(font)
        self.buscar_tarefa_telainicial_Button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buscar_tarefa_telainicial_Button_2.setStyleSheet("QPushButton{\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.buscar_tarefa_telainicial_Button_2.setObjectName("buscar_tarefa_telainicial_Button_2")
        self.sair_telainicial_Button_5 = QtWidgets.QPushButton(self.frame)
        self.sair_telainicial_Button_5.setGeometry(QtCore.QRect(170, 240, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sair_telainicial_Button_5.setFont(font)
        self.sair_telainicial_Button_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sair_telainicial_Button_5.setStyleSheet("QPushButton{\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.sair_telainicial_Button_5.setObjectName("sair_telainicial_Button_5")
        self.buscar_tarefa_telainicial_Button = QtWidgets.QPushButton(self.frame)
        self.buscar_tarefa_telainicial_Button.setGeometry(QtCore.QRect(110, 100, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buscar_tarefa_telainicial_Button.setFont(font)
        self.buscar_tarefa_telainicial_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buscar_tarefa_telainicial_Button.setStyleSheet("QPushButton{\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.buscar_tarefa_telainicial_Button.setObjectName("buscar_tarefa_telainicial_Button")
        self.pushButton = QtWidgets.QPushButton(Cadastro)
        self.pushButton.setGeometry(QtCore.QRect(560, 30, 51, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(Cadastro)
        self.line.setGeometry(QtCore.QRect(10, 140, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(Cadastro)
        self.label.setGeometry(QtCore.QRect(310, 80, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Cadastro)
        QtCore.QMetaObject.connectSlotsByName(Cadastro)

    def retranslateUi(self, Cadastro):
        """
        Traduz os textos exibidos na tela inicial.

        Este metodo define os textos exibidos nos campos de entrada, botoes e rotulo da tela inicial.

        Parameters
        ----------
        Cadastro : QtWidgets.QWidget
            O objeto da janela principal em que a tela está sendo exibida.
        """
        _translate = QtCore.QCoreApplication.translate
        Cadastro.setWindowTitle(_translate("Cadastro", "Form"))
        self.cadastrar_telainicial__Button.setText(_translate("Cadastro", "Cadastrar Tarefa"))
        self.buscar_tarefa_telainicial_Button_2.setText(_translate("Cadastro", "Encerrar Programa"))
        self.sair_telainicial_Button_5.setText(_translate("Cadastro", "Voltar"))
        self.buscar_tarefa_telainicial_Button.setText(_translate("Cadastro", "Buscar Tarefas"))
        self.pushButton.setText(_translate("Cadastro", "🔔 (1)"))
        self.label.setText(_translate("Cadastro", "<html><head/><body><p><span style=\" color:#ffffff;\">Focus Tasks</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Tela_inicial()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
