class Usuario:
    """
    Classe que representa um usuario.

    Responsavel pelo armazenamento e manipulacao dos atributos de um usuario.

    Attributes
    ----------
    id_usuario : int
        O ID do usuario.
    nome : str
        O nome do usuario.
    email : str
        O email do usuario.
    username : str
        O nome de usuario do usuario.
    senha : str
        A senha do usuario.

    Methods
    -------
    get_id_usuario(self)
        Retorna o ID do usuario.
    set_id_usuario(self, id_usuario)
        Define o ID do usuario.
    get_nome(self)
        Retorna o nome do usuario.
    set_nome(self, nome)
        Define o nome do usuario.
    get_email(self)
        Retorna o email do usuario.
    set_email(self, email)
        Define o email do usuario.
    get_username(self)
        Retorna o nome de usuario do usuario.
    set_username(self, username)
        Define o nome de usuario do usuario.
    get_senha(self)
        Retorna a senha do usuario.
    set_senha(self, senha)
        Define a senha do usuario.
    """

    def __init__(self, nome, email, username, senha, id_usuario=None):
        """
        Parameters
        ----------
        nome : str
            O nome do usuario.
        email : str
            O email do usuario.
        username : str
            O nome de usuario do usuario.
        senha : str
            A senha do usuario.
        id_usuario : int, optional
            O ID do usuario (padrao e None).
        """
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.username = username
        self.senha = senha

    def get_id_usuario(self):
        """
        Metodo getter.

        Retorna o ID do usuario.

        Returns
        -------
        int
            O ID do usuario.
        """
        return self.id_usuario

    def set_id_usuario(self, id_usuario):
        """
        Metodo setter.

        Define o ID do usuario.

        Parameters
        ----------
        id_usuario : int
            O ID do usuario.
        """
        self.id_usuario = id_usuario

    def get_nome(self):
        """
        Metodo getter.

        Retorna o nome do usuario.

        Returns
        -------
        str
            O nome do usuario.
        """
        return self.nome

    def set_nome(self, nome):
        """
        Metodo setter.

        Define o nome do usuario.

        Parameters
        ----------
        nome : str
            O nome do usuario.
        """
        self.nome = nome

    def get_email(self):
        """
        Metodo getter.

        Retorna o email do usuario.

        Returns
        -------
        str
            O email do usuario.
        """
        return self.email

    def set_email(self, email):
        """
        Metodo setter.

        Define o email do usuario.

        Parameters
        ----------
        email : str
            O email do usuario.
        """
        self.email = email

    def get_username(self):
        """
        Metodo getter.

        Retorna o nome de usuario do usuario.

        Returns
        -------
        str
            O nome de usuario do usuario.
        """
        return self.username

    def set_username(self, username):
        """
        Metodo setter.

        Define o nome de usuario do usuario.

        Parameters
        ----------
        username : str
            O nome de usuario do usuario.
        """
        self.username = username

    def get_senha(self):
        """
        Metodo getter.

        Retorna a senha do usuario.

        Returns
        -------
        str
            A senha do usuario.
        """
        return self.senha

    def set_senha(self, senha):
        """
        Metodo setter.

        Define a senha do usuario.

        Parameters
        ----------
        senha : str
            A senha do usuario.
        """
        self.senha = senha
