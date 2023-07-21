# importacao do banco de dados
import mysql.connector
from mysql.connector import Error

# importacao das classes
from usuario import Usuario
from datetime import datetime, date
import json  # Add this import to use JSON serialization

class Banco:
    """
    Classe responsavel por manipular as tarefas.

    Esta classe e responsavel por fazer o cadastro e as manipulacoes necessarias de uma tarefa.

    Attributes
    ----------
    usuario : Usuario
        O usuario atualmente logado.
    connection : obj
        O objeto de conexao com o banco de dados.
    cursor : obj
        O objeto de cursor para executar consultas SQL.

    Methods
    -------
    create_connection()
        Cria uma conexao com o banco de dados MySQL.

    close_connection()
        Fecha a conexao com o banco de dados.

    get_id_usuario()
        Retorna o ID do usuario atualmente logado.

    buscar_usuario(username)
        Busca um usuario pelo nome de usuario no banco de dados.

    cadastrar_usuario_bd(usuario)
        Cadastra um usuario no banco de dados.

    obter_quantidade_tarefas()
        Obtem a quantidade de tarefas nao concluidas do usuario atualmente logado.

    loginUsuario(username, password)
        Faz o login de um usuario.

    cadastrar_tarefas(tarefa)
        Cadastra uma nova tarefa no banco de dados.

    excluirTarefa(id_tarefa)
        Exclui uma tarefa do banco de dados.

    reativarTarefa(id_tarefa)
        Reativa uma tarefa previamente concluida.

    concluirTarefa(id_tarefa)
        Marca uma tarefa como concluida.

    listarTarefasConcluidas()
        Lista as tarefas concluidas do usuario atualmente logado.

    listarTarefasNaoConcluidas()
        Lista as tarefas nao concluidas do usuario atualmente logado.
    """

    def __init__(self):
        """
        Metodo construtor que é definido dentro de uma classe.
        """
        self.usuario = None
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor()

    def create_connection(self):
        """
        Cria uma conexao com o banco de dados MySQL.

        Este metodo estabelece uma conexao com um banco de dados MySQLe utiliza os parametros e plugin de autenticacao para se conectar ao Banco.

        Returns:
        -------
        obj
            Objeto de conexao com o banco de dados.

        Raises:
        -------
        Error
            Se ocorrer algum erro ao conectar ao banco de dados.
        """
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='C0mpL3xP@$$',
                database='project_tarefa',
                auth_plugin='mysql_native_password'
            )
            return connection
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def close_connection(self):
        """
        Fecha a conexao com o banco de dados.

        Este metodo verifica se ha uma conexao aberta com o banco de dados. 
        """
        if self.connection:
            self.connection.commit()
            self.connection.close()

    def get_id_usuario(self):
        """
        Retorna o ID do usuario atualmente logado.

        Este metodo retorna o ID do usuario que esta atualmente logado no sistema.

        Returns:
        -------
        int
            ID do usuario.
        """
        return self.id_usuario

    def buscar_usuario(self, username):
        """
        Busca um usuario pelo ID no banco de dados.

        Este metodo realiza uma consulta no banco de dados para buscar um usuario com base no nome de usuario fornecido. 

        Parameters:
        ----------
        username : str
            O nome de usuario a ser buscado.

        Returns:
        -------
        Usuario
            O objeto de usuario encontrado, ou None se nao encontrado.

        Raises:
        -------
        Error
            Se ocorrer algum erro ao buscar o usuario no banco de dados.
        """
        try:
            query = "SELECT * FROM usuario WHERE username = %s"
            values = (username,)
            self.cursor.execute(query, values)
            result = self.cursor.fetchone()

            if result:
                id_usuario, nome, email, nome_usuario, senha = result
                usuario = Usuario(nome, email, nome_usuario, senha, id_usuario)
                return usuario
        except Error as e:
            print(f"Erro ao buscar o usuario: {e}")

    def cadastrar_usuario_bd(self, usuario):
        """
        Cadastra um usuario no banco de dados.

        Este metodo realiza o cadastro no banco de dados de um usuario com base nas informacoes fornecidas. 

        Parameters:
        ----------
        usuario : Usuario
            O objeto de usuario a ser cadastrado.

        Returns:
        -------
        bool
            True se o usuario foi cadastrado com sucesso, False caso contrario.

        Raises:
        -------
        Error
            Se ocorrer algum erro ao cadastrar o usuario no banco de dados.
        """
        try:
            # Verificar se o usuario ja existe no banco de dados
            usuario_existente = self.buscar_usuario(usuario.username)
            if usuario_existente is None:
                # Inserir o novo usuario na tabela
                query_usuario = "INSERT INTO usuario (nome, email, username, password) VALUES (%s, %s, %s, %s)"
                values_usuario = (usuario.nome, usuario.email, usuario.username, usuario.senha)
                self.cursor.execute(query_usuario, values_usuario)
                self.connection.commit()
                print(f'Usuario {usuario.username} cadastrado com sucesso!')
                return True
            else:
                print("Usuario ja cadastrado.")
                return False
        except Error as e:
            print(f"Erro ao cadastrar o usuario: {e}")
            return False
        
    def obter_tarefas_pendentes(self):
        """
        Obtem a quantidade de tarefas não concluídas do usuário atualmente logado.

        Este método retorna a quantidade de tarefas não concluídas do usuário atualmente logado.

        Returns:
        -------
        int
            A quantidade de tarefas não concluídas.

        Raises:
        -------
        Error
            Se ocorrer algum erro ao obter a quantidade de tarefas não concluídas.
        """
        try:
            if self.usuario is None:
                print("Usuário não logado.")
                return False

            query = "SELECT COUNT(*) FROM tarefa WHERE id_usuario = %s AND concluido = 0"
            values = (self.usuario.id_usuario,)
            self.cursor.execute(query, values)
            result = self.cursor.fetchone()

            if result:
                quantidade_tarefas = result[0]

                # Obter vencimento e título das tarefas
                query_vencimento_titulo = "SELECT prazo, titulo FROM tarefa WHERE id_usuario = %s AND concluido = 0"
                self.cursor.execute(query_vencimento_titulo, values)
                resultados_vencimento_titulo = self.cursor.fetchall()
                tarefas_pendentes = []

                for vencimento_titulo in resultados_vencimento_titulo:
                    prazo = vencimento_titulo[0]
                    dias_restantes = (prazo - date.today()).days
                    titulo = vencimento_titulo[1]
                    tarefas_pendentes.append({"dias_restantes": dias_restantes, "titulo": titulo})

                return {"quantidade_tarefas": quantidade_tarefas, "tarefas_pendentes": tarefas_pendentes}
            else:
                print("Nenhuma tarefa não concluída encontrada.")
                return False
        except Error as e:
            print(f"Erro ao obter a quantidade de tarefas não concluídas: {e}")
            return False

    def loginUsuario(self, username, password):
        """
        Faz o login de um usuario.
        
        Busca o usuario no banco de dados pelo username e a senha.

        Parameters:
        ----------
        username : str
            O nome de usuario do usuario.
        password : str
            A senha do usuario.

        Returns:
        -------
        bool
            True se o login foi bem-sucedido, False caso contrario.

        Raises:
        -------
        Error
            Se ocorrer algum erro ao fazer o login do usuario.
        """
        try:
            # Buscar o usuario pelo nome de usuario (username) e senha
            query = "SELECT * FROM usuario WHERE username = %s AND password = %s"
            values = (username, password)
            self.cursor.execute(query, values)
            result = self.cursor.fetchone()

            if result:
                self.usuario = Usuario(result[1], result[2], result[3], result[4], id_usuario=result[0])
                print("Login bem-sucedido!")
                return True
            else:
                print("Credenciais invalidas.")
                return False
        except Error as e:
            print(f"Erro ao fazer login: {e}")

    def cadastrar_tarefas(self, tarefa):
        """
        Cadastra uma nova tarefa no banco de dados.

        Este metodo realiza o cadastro no banco de dados de uma tarefa com base nas informacoes fornecidas. 

        Parameters:
        ----------
        tarefa : Tarefa
            O objeto de tarefa a ser cadastrado.

        Returns:
        --------
        bool
            True se a tarefa foi cadastrada com sucesso, False caso contrario.

        Raises:
        -------
        Error
            Se ocorrer algum erro ao cadastrar a tarefa no banco de dados.
        """
        if self.usuario is None:
            print("Usuario nao logado.")
            return False
        try:
            # Inserir a nova tarefa na tabela
            query_tarefa = "INSERT INTO tarefa (titulo, descricao, prazo, id_usuario) " \
                        "VALUES (%s, %s, %s, %s)"
            values_tarefa = (tarefa.titulo, tarefa.descricao, tarefa.prazo, self.usuario.id_usuario)
            self.cursor.execute(query_tarefa, values_tarefa)
            self.connection.commit()
            print(f"Tarefa {tarefa.titulo} cadastrada com sucesso!")
            return True
        except Error as e:
            print(f"Erro ao cadastrar a tarefa: {e}")
            return False

    def excluirTarefa(self, id_tarefa):
        """
        Exclui uma tarefa do banco de dados por meio do id da tarefa.

        Este metodo recebe o ID da tarefa a ser excluida e realiza a exclusao correspondente no banco de dados, a alteracao e confirmada atraves do commit.

        Parameters:
        ----------
        id_tarefa : int
            O ID da tarefa a ser excluida.

        Returns:
        -------
        bool
            True se a tarefa foi excluida com sucesso, False caso contrario.

        Raises:
        -------
        Error
            Se ocorrer algum erro ao excluir a tarefa do banco de dados.
        """
        try:
            query = "DELETE FROM tarefa WHERE id_tarefa = %s"
            values = (id_tarefa,)
            self.cursor.execute(query, values)
            self.connection.commit()
            print(f"Tarefa {id_tarefa} excluida com sucesso!")
            return True
        except Error as e:
            print(f"Erro ao excluir a tarefa: {e}")
            return False
        
    def atualizar_tarefa(self, id_tarefa, novo_titulo, nova_descricao, novo_prazo):
        """
        Atualiza uma tarefa existente no banco de dados.

        Este metodo recebe o ID da tarefa a ser atualizada, juntamente com as novas informacoes. E Atualiza os campos correspondentes no banco de dados.

        Parameters:
        ----------
        id_tarefa : int
            O ID da tarefa a ser atualizada.
        novo_titulo : str
            O novo titulo da tarefa.
        nova_descricao : str
            A nova descricao da tarefa.
        novo_prazo : str
            O novo prazo da tarefa.

        Returns:
        -------
        bool
            True se a tarefa foi atualizada com sucesso, False caso contrario.

        Raises:
        -------
        Error
            Se ocorrer algum erro ao atualizar a tarefa no banco de dados.
        """
        try:
            sql = "UPDATE tarefa SET titulo = %s, descricao = %s, prazo = %s WHERE id_tarefa = %s"
            values = (novo_titulo, nova_descricao, novo_prazo, id_tarefa)

            # Execute a consulta SQL
            self.cursor.execute(sql, values)
            self.connection.commit()

            # Verifique se a atualização foi bem-sucedida
            if self.cursor.rowcount > 0:
                print(f"Tarefa {id_tarefa} atualizada com sucesso!")
                return True
            else:
                print("Nenhuma tarefa encontrada com o ID fornecido.")
                return False
        except Error as e:
            print(f"Erro ao atualizar a tarefa no banco de dados: {e}")
            return False

    def reativarTarefa(self, id_tarefa):
        """
        Reativa uma tarefa previamente concluida.

        Este metodo recebe o ID da tarefa a ser reativada e atualiza o status da tarefa para nao concluida = 0 no banco de dados.

        Parameters:
        ----------
        id_tarefa : int
            O ID da tarefa a ser reativada.

        Returns:
        -------
        bool
            True se a tarefa foi reativada com sucesso, False caso contrario.

        Raises:
        -------
        Error
            Se ocorrer algum erro ao reativar a tarefa no banco de dados.
        """
        try:
            query = "UPDATE tarefa SET concluido = 0 WHERE id_tarefa = %s"
            values = (id_tarefa,)
            self.cursor.execute(query, values)
            self.connection.commit()
            print(f"Tarefa {id_tarefa} reativada com sucesso!")
            return True
        except Error as e:
            print(f"Erro ao reativar a tarefa: {e}")
            return False

    def concluirTarefa(self, id_tarefa):
        """
        Marca uma tarefa como concluida.

        Este metodo recebe o ID da tarefa a ser concluida e atualiza o status da tarefa para concluída = 1 no banco de dados.

        Parameters:
        ----------
        id_tarefa : int
            O ID da tarefa a ser concluida.

        Returns:
        -------
        bool
            True se a tarefa foi concluida com sucesso, False caso contrario.

        Raises:
        -------
        Error
            Se ocorrer algum erro ao concluir a tarefa no banco de dados.
        """
        try:
            query = "UPDATE tarefa SET concluido = 1 WHERE id_tarefa = %s"
            values = (id_tarefa,)
            self.cursor.execute(query, values)
            self.connection.commit()
            print(f"Tarefa {id_tarefa} concluida com sucesso!")
            return True
        except Error as e:
            print(f"Erro ao concluir a tarefa: {e}")
            return False

    def listarTarefasConcluidas(self):
        """
        Lista as tarefas concluidas do usuario atualmente logado.

        As informacoes das tarefas (ID, titulo, descricao e prazo) sao formatadas em uma string, separadas por ponto e virgula.

        Returns:
        -------
        str
            Uma string formatada contendo as informacoes das tarefas concluidas, separadas por ponto e virgula.
        False
            Se nao houverem tarefas concluidas ou o usuario nao estiver logado.

        Raises:
        -------
        Error
            Se ocorrer algum erro ao listar as tarefas concluidas do usuario.
        """
        try:
            # Verificar se o usuario existe no banco de dados
            if self.usuario is None:
                print("Usuario nao logado.")
                return False

            # Buscar as tarefas concluidas do usuario pelo ID
            query = "SELECT id_tarefa, titulo, descricao, prazo FROM tarefa WHERE id_usuario = %s AND concluido = 1"
            values = (self.usuario.id_usuario,)
            self.cursor.execute(query, values)
            results = self.cursor.fetchall()

            if results:
                enviar = ''
                for result in results:
                    enviar += f'{result[0]} - {result[1]} - {result[2]} - {result[3]};'
                return enviar
            else:
                return False
        except Error as e:
            print(f"Erro ao listar as tarefas concluidas: {e}")
            return False

    def listarTarefasNaoConcluidas(self):
        """
        Lista as tarefas nao concluidas do usuario atualmente logado.

        As informacoes das tarefas (ID, titulo, descricao e prazo) sao formatadas em uma string, separadas por ponto e virgula.

        Returns:
        -------
        str
            Uma string formatada contendo as informacoes das tarefas nao concluidas, separadas por ponto e virgula.
        False
            Se nao houverem tarefas nao concluidas ou o usuario nao estiver logado.

        Raises:
        -------
        Error
            Se ocorrer algum erro ao listar as tarefas nao concluidas do usuario.
        """
        try:
            # Verificar se o usuario existe no banco de dados
            if self.usuario is None:
                print("Usuario nao logado.")
                return False

            # Buscar as tarefas nao concluidas do usuario pelo ID
            query = "SELECT id_tarefa, titulo, descricao, prazo FROM tarefa WHERE id_usuario = %s AND concluido = 0"
            values = (self.usuario.id_usuario,)
            self.cursor.execute(query, values)
            results = self.cursor.fetchall()

            if results:
                enviar = ''
                for result in results:
                    enviar += f'{result[0]} - {result[1]} - {result[2]} - {result[3]};'
                return enviar
            else:
                return False
        except Error as e:
            print(f"Erro ao listar as tarefas nao concluidas: {e}")
            return False

if __name__ == "__main__":
    banco = Banco()
    banco.create_connection()
    banco.close_connection()
