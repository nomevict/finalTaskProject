from PyQt5 import QtCore, QtGui, QtWidgets

class Tela_cadastroTarefa(object):
    """
    Classe que configura a interface grafica de cadastrar a tarefa.

    Responsavel por configurar a interface grafica da janela de cadastro das tarefas utilizando a biblioteca PyQt5.

    Attributes
    ----------
    idtarefa_lineEdit : QtWidgets.QLineEdit
        Campo de entrada para o ID da tarefa.
    prazo_lineEdit : QtWidgets.QLineEdit
        Campo de entrada para o prazo da tarefa.
    cadastrar_tarefa_Button : QtWidgets.QPushButton
        Botão para cadastrar a tarefa.
    voltar_tarefa_Button : QtWidgets.QPushButton
        Botão para voltar à tela anterior.
    descricao_textEdit : QtWidgets.QTextEdit
        Campo de entrada para a descrição da tarefa.
    label : QtWidgets.QLabel
        Rótulo com o texto "CADASTRE A TAREFA, USUARIO".

    Methods
    -------
    setupUi(Cadastro)
        Configura a interface do usuário da tela de cadastro de tarefa.
    retranslateUi(Cadastro)
        Traduz os textos exibidos na tela de cadastro de tarefa.
    """

    def setupUi(self, Cadastro):
        """
        Configura a interface do usuário da tela de cadastro de tarefa.

        Este método cria e configura os elementos gráficos necessários para a tela de cadastro de tarefa.

        Parameters
        ----------
        Cadastro : QtWidgets.QWidget
            O objeto da janela principal em que a tela será exibida.
        """
        Cadastro.setObjectName("Cadastro")
        Cadastro.resize(611, 495)
        Cadastro.setStyleSheet("background-color: rgb(0, 70, 112);")
        self.frame = QtWidgets.QFrame(Cadastro)
        self.frame.setGeometry(QtCore.QRect(100, 100, 421, 331))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0,0.2);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.idtarefa_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.idtarefa_lineEdit.setGeometry(QtCore.QRect(80, 40, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.idtarefa_lineEdit.setFont(font)
        self.idtarefa_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.idtarefa_lineEdit.setText("")
        self.idtarefa_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.idtarefa_lineEdit.setObjectName("idtarefa_lineEdit")
        self.prazo_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.prazo_lineEdit.setGeometry(QtCore.QRect(80, 200, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prazo_lineEdit.setFont(font)
        self.prazo_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.prazo_lineEdit.setText("")
        self.prazo_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.prazo_lineEdit.setObjectName("prazo_lineEdit")
        self.cadastrar_tarefa_Button = QtWidgets.QPushButton(self.frame)
        self.cadastrar_tarefa_Button.setGeometry(QtCore.QRect(170, 230, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cadastrar_tarefa_Button.setFont(font)
        self.cadastrar_tarefa_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cadastrar_tarefa_Button.setStyleSheet("QPushButton{\n"
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
        self.cadastrar_tarefa_Button.setObjectName("cadastrar_tarefa_Button")
        self.voltar_tarefa_Button = QtWidgets.QPushButton(self.frame)
        self.voltar_tarefa_Button.setGeometry(QtCore.QRect(170, 260, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.voltar_tarefa_Button.setFont(font)
        self.voltar_tarefa_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.voltar_tarefa_Button.setStyleSheet("QPushButton{\n"
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
        self.voltar_tarefa_Button.setObjectName("voltar_tarefa_Button")
        self.descricao_textEdit = QtWidgets.QTextEdit(self.frame)
        self.descricao_textEdit.setGeometry(QtCore.QRect(80, 70, 261, 121))
        self.descricao_textEdit.setObjectName("descricao_textEdit")
        self.descricao_textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Cadastro)
        self.label.setGeometry(QtCore.QRect(180, 60, 241, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Cadastro)
        QtCore.QMetaObject.connectSlotsByName(Cadastro)

    def retranslateUi(self, Cadastro):
        """
        Traduz os textos exibidos na tela de cadastro de tarefa.

        Este método define os textos exibidos nos campos de entrada, botões e rótulo da tela de cadastro de tarefa.

        Parameters
        ----------
        Cadastro : QtWidgets.QWidget
            O objeto da janela principal.
        """
        _translate = QtCore.QCoreApplication.translate
        Cadastro.setWindowTitle(_translate("Cadastro", "Form"))
        self.idtarefa_lineEdit.setPlaceholderText(_translate("Cadastro", "Titulo"))
        self.prazo_lineEdit.setPlaceholderText(_translate("Cadastro", "Prazo"))
        self.cadastrar_tarefa_Button.setText(_translate("Cadastro", "Cadastrar"))
        self.voltar_tarefa_Button.setText(_translate("Cadastro", "Voltar"))
        self.descricao_textEdit.setPlaceholderText(_translate("Cadastro", "Digite sua tarefa.."))
        self.label.setText(_translate("Cadastro", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">CADASTRE A TAREFA, USUARIO</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cadastro = QtWidgets.QWidget()
    ui = Tela_cadastroTarefa()
    ui.setupUi(Cadastro)
    Cadastro.show()
    sys.exit(app.exec_())
