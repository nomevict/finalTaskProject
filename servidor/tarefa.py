class Tarefa:
    """
    Classe que representa uma tarefa.

    Responsavel pelo armazenamento e manipulacao dos atributos de uma tarefa, relacionada a um usuario.

    Attributes
    ----------
    id_tarefa : int
        O ID da tarefa.
    titulo : str
        O titulo da tarefa.
    descricao : str
        A descricao da tarefa.
    prazo : str
        O prazo da tarefa.
    id_usuario : int
        O ID do usuario associado a tarefa.

    Methods
    -------
    get_id_tarefa(self)
        Retorna o ID da tarefa.
    set_id_tarefa(self, id_tarefa)
        Define o ID da tarefa.
    get_titulo(self)
        Retorna o titulo da tarefa.
    set_titulo(self, titulo)
        Define o titulo da tarefa.
    get_descricao(self)
        Retorna a descricao da tarefa.
    set_descricao(self, descricao)
        Define a descricao da tarefa.
    get_prazo(self)
        Retorna o prazo da tarefa.
    set_prazo(self, prazo)
        Define o prazo da tarefa.
    get_id_usuario(self)
        Retorna o ID do usuario associado a tarefa.
    set_id_usuario(self, id_usuario)
        Define o ID do usuario associado a tarefa.
    """

    def __init__(self, titulo, descricao, prazo, id_usuario, id_tarefa=None):
        """
        Parameters
        ----------
        titulo : str
            O titulo da tarefa.
        descricao : str
            A descricao da tarefa.
        prazo : str
            O prazo da tarefa.
        id_usuario : int
            O ID do usuario associado a tarefa.
        id_tarefa : int, optional
            O ID da tarefa (padrao e None).
        """
        self.id_tarefa = id_tarefa
        self.titulo = titulo
        self.descricao = descricao
        self.prazo = prazo
        self.id_usuario = id_usuario

    def get_id_tarefa(self):
        """
        Metodo getter.

        Retorna o ID da tarefa.

        Returns
        -------
        int
            O ID da tarefa.
        """
        return self.id_tarefa

    def set_id_tarefa(self, id_tarefa):
        """
        Metodo setter.

        Define o ID da tarefa.

        Parameters
        ----------
        id_tarefa : int
            O ID da tarefa.
        """
        self.id_tarefa = id_tarefa

    def get_titulo(self):
        """
        Metodo getter.

        Retorna o titulo da tarefa.

        Returns
        -------
        str
            O titulo da tarefa.
        """
        return self.titulo

    def set_titulo(self, titulo):
        """
        Metodo setter.

        Define o titulo da tarefa.

        Parameters
        ----------
        titulo : str
            O titulo da tarefa.
        """
        self.titulo = titulo

    def get_descricao(self):
        """
        Metodo getter.

        Retorna a descricao da tarefa.

        Returns
        -------
        str
            A descricao da tarefa.
        """
        return self.descricao

    def set_descricao(self, descricao):
        """
        Metodo setter.

        Define a descricao da tarefa.

        Parameters
        ----------
        descricao : str
            A descricao da tarefa.
        """
        self.descricao = descricao

    def get_prazo(self):
        """
        Metodo getter.

        Retorna o prazo da tarefa.

        Returns
        -------
        str
            O prazo da tarefa.
        """
        return self.prazo

    def set_prazo(self, prazo):
        """
        Metodo setter.

        Define o prazo da tarefa.

        Parameters
        ----------
        prazo : str
            O prazo da tarefa.
        """
        self.prazo = prazo

    def get_id_usuario(self):
        """
        Metodo getter.

        Retorna o ID do usuario associado a tarefa.

        Returns
        -------
        int
            O ID do usuario associado a tarefa.
        """
        return self.id_usuario

    def set_id_usuario(self, id_usuario):
        """
        Metodo setter.

        Define o ID do usuario associado a tarefa.

        Parameters
        ----------
        id_usuario : int
            O ID do usuario associado a tarefa.
        """
        self.id_usuario = id_usuario
