from PyQt5 import QtCore, QtGui, QtWidgets

class Tela_cadastroUsuario(object):
    """
    Classe que configura a interface grafica de cadastrar o usuario.

    Responsavel por configurar a interface grafica da janela de cadastro de usuario utilizando a biblioteca PyQt5.

    Attributes
    ----------
    nome_lineEdit : QtWidgets.QLineEdit
        Campo de entrada para o nome do usuário.
    email_lineEdit : QtWidgets.QLineEdit
        Campo de entrada para o email do usuário.
    username_lineEdit : QtWidgets.QLineEdit
        Campo de entrada para o nome de usuário.
    password_lineEdit : QtWidgets.QLineEdit
        Campo de entrada para a senha do usuário.
    cadastrar_Button : QtWidgets.QPushButton
        Botão para cadastrar o usuário.
    voltar_Button : QtWidgets.QPushButton
        Botão para voltar à tela anterior.
    label : QtWidgets.QLabel
        Rótulo com o texto "CADASTRE-SE, USUARIO".

    Methods
    -------
    setupUi(Cadastro)
        Configura a interface gráfica da tela de cadastro de usuário.
    retranslateUi(Cadastro)
        Traduz os textos exibidos na tela de cadastro de usuário.
    """

    def setupUi(self, Cadastro):
        """
        Configura a interface gráfica da tela de cadastro de usuário.

        Este método cria e configura os elementos gráficos necessários para a tela de cadastro de usuário.

        Parameters
        ----------
        Cadastro : QtWidgets.QWidget
            O objeto da janela principal em que a tela será exibida.
        """
        Cadastro.setObjectName("Cadastro")
        Cadastro.resize(591, 428)
        Cadastro.setStyleSheet("background-color: rgb(0, 70, 112);")
        self.frame = QtWidgets.QFrame(Cadastro)
        self.frame.setGeometry(QtCore.QRect(110, 80, 351, 301))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0,0.2);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nome_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.nome_lineEdit.setGeometry(QtCore.QRect(80, 80, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nome_lineEdit.setFont(font)
        self.nome_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nome_lineEdit.setText("")
        self.nome_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.nome_lineEdit.setObjectName("nome_lineEdit")
        self.email_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.email_lineEdit.setGeometry(QtCore.QRect(80, 110, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.email_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.username_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.username_lineEdit.setGeometry(QtCore.QRect(80, 140, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username_lineEdit.setText("")
        self.username_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.password_lineEdit.setGeometry(QtCore.QRect(80, 170, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)  # Oculta a digitação da senha
        self.password_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.cadastrar_Button = QtWidgets.QPushButton(self.frame)
        self.cadastrar_Button.setGeometry(QtCore.QRect(140, 200, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cadastrar_Button.setFont(font)
        self.cadastrar_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cadastrar_Button.setStyleSheet("QPushButton{\n"
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
        self.cadastrar_Button.setObjectName("cadastrar_Button")
        self.voltar_Button = QtWidgets.QPushButton(self.frame)
        self.voltar_Button.setGeometry(QtCore.QRect(140, 230, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.voltar_Button.setFont(font)
        self.voltar_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.voltar_Button.setStyleSheet("QPushButton{\n"
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
        self.voltar_Button.setObjectName("voltar_Button")
        self.label = QtWidgets.QLabel(Cadastro)
        self.label.setGeometry(QtCore.QRect(200, 50, 181, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Cadastro)
        QtCore.QMetaObject.connectSlotsByName(Cadastro)

    def retranslateUi(self, Cadastro):
        """
        Traduz os textos exibidos na tela de cadastro de tarefa.

        Este método define os textos exibidos nos campos de entrada, botões e rótulo da tela de cadastro de usuario.

        Parameters
        ----------
        Cadastro : QtWidgets.QWidget
            O objeto da janela principal em que a tela está sendo exibida.
        """
        _translate = QtCore.QCoreApplication.translate
        Cadastro.setWindowTitle(_translate("Cadastro", "Form"))
        self.nome_lineEdit.setPlaceholderText(_translate("Cadastro", "Nome"))
        self.email_lineEdit.setPlaceholderText(_translate("Cadastro", "Email"))
        self.username_lineEdit.setPlaceholderText(_translate("Cadastro", "Username"))
        self.password_lineEdit.setPlaceholderText(_translate("Cadastro", "Password"))
        self.cadastrar_Button.setText(_translate("Cadastro", "Cadastrar"))
        self.voltar_Button.setText(_translate("Cadastro", "Voltar"))
        self.label.setText(_translate("Cadastro", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">CADASTRE-SE, USUARIO</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cadastro = QtWidgets.QWidget()
    ui = Tela_cadastroUsuario()
    ui.setupUi(Cadastro)
    Cadastro.show()
    sys.exit(app.exec_())
