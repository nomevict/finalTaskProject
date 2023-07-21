from PyQt5 import QtCore, QtGui, QtWidgets

class Tela_funcoes_tarefa(object):
    """
    Classe que configura a interface grafica das funções de uma tarefa.

    Responsavel por configurar a interface grafica da janela de funcoes de tarefa utilizando a biblioteca PyQt5.

    Attributes
    ----------
    cadastrar_telainicial__Button : QtWidgets.QPushButton
        Botão para acessar as tarefas concluídas.
    sair_telainicial_Button_5 : QtWidgets.QPushButton
        Botão para voltar à tela anterior.
    buscar_tarefa_telainicial_Button : QtWidgets.QPushButton
        Botão para acessar as tarefas pendentes.
    line : QtWidgets.QFrame
        Linha separadora.
    label : QtWidgets.QLabel
        Rótulo com o texto "Tasks".

    Methods
    -------
    setupUi(Cadastro)
        Configura a interface gráfica da tela de funções de tarefas.
    retranslateUi(Cadastro)
        Traduz os textos exibidos na tela de funções de tarefas.
    """

    def setupUi(self, Cadastro):
        """
        Configura a interface gráfica da tela de funções de tarefas.

        Este método cria e configura os elementos gráficos necessários para a tela de funções de tarefas.

        Parameters
        ----------
        Cadastro : QtWidgets.QWidget
            O objeto da janela principal em que a tela será exibida.
        """
        Cadastro.setObjectName("Cadastro")
        Cadastro.resize(699, 634)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        Cadastro.setFont(font)
        Cadastro.setStyleSheet("background-color: rgb(0, 70, 112);")
        self.frame = QtWidgets.QFrame(Cadastro)
        self.frame.setGeometry(QtCore.QRect(130, 190, 431, 291))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0,0.2);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cadastrar_telainicial__Button = QtWidgets.QPushButton(self.frame)
        self.cadastrar_telainicial__Button.setGeometry(QtCore.QRect(110, 120, 211, 61))
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
        self.sair_telainicial_Button_5 = QtWidgets.QPushButton(self.frame)
        self.sair_telainicial_Button_5.setGeometry(QtCore.QRect(170, 190, 81, 21))
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
        self.buscar_tarefa_telainicial_Button.setGeometry(QtCore.QRect(110, 50, 211, 61))
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
        self.line = QtWidgets.QFrame(Cadastro)
        self.line.setGeometry(QtCore.QRect(10, 140, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(Cadastro)
        self.label.setGeometry(QtCore.QRect(320, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Cadastro)
        QtCore.QMetaObject.connectSlotsByName(Cadastro)

    def retranslateUi(self, Cadastro):
        """
        Traduz os textos exibidos na tela de funções de tarefas.

        Este método define os textos exibidos nos campos de entrada, botões e rótulo da tela de funcoes de tarefa.

        Parameters
        ----------
        Cadastro : QtWidgets.QWidget
            O objeto da janela principal em que a tela está sendo exibida.
        """
        _translate = QtCore.QCoreApplication.translate
        Cadastro.setWindowTitle(_translate("Cadastro", "Form"))
        self.cadastrar_telainicial__Button.setText(_translate("Cadastro", "Tarefas Concluídas"))
        self.sair_telainicial_Button_5.setText(_translate("Cadastro", "Voltar"))
        self.buscar_tarefa_telainicial_Button.setText(_translate("Cadastro", "Tarefas pendentes"))
        self.label.setText(_translate("Cadastro", "<html><head/><body><p><span style=\" color:#ffffff;\">Tasks</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Tela_funcoes_tarefa()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
