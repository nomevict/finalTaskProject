from banco import Banco
from tarefa import Tarefa
from usuario import Usuario

import threading
import socket

class ThreadCliente(threading.Thread):
    """
    Classe que representa um cliente do banco.

    Esta classe e responsavel por lidar com as solicitacoes de um cliente conectado ao servidor do banco.

    Attributes
    ----------
    con : objeto
        A conexao da maquina que o cliente esta usando.
    address : objeto
        O endereco da maquina que o cliente esta usando.
    bank : Banco
        A instancia do objeto Banco para manipulacao de dados do banco.

    Methods
    -------
    run():
        Executa a thread atual, lidando com as solicitacoes do cliente.
    iniciar_servidor():
        Inicia o servidor, permitindo a conexao dos clientes.
    """
    def __init__(self, address, con):
        """
        Parameters:
        ----------
        address : tuple
            O endereco do cliente.
        con : socket object
            O objeto de conexao do cliente.
        """
        threading.Thread.__init__(self) 
        self.con = con
        self.address = address
        self.bank = Banco()
        print(f'Conectado com {address}')

    def run(self):
        """ 
        A funcao run e responsavel por receber comandos enviados pelo cliente. 
        
        Processa esses comandos e envia respostas de volta ao cliente.
        """
        lock = threading.Lock()
        while True:
            msg_cliente = self.con.recv(1024).decode()
            comando = msg_cliente.split(',')

            # Login do usuario
            if comando[0] == 'usuario':
                retorno_cliente = self.bank.loginUsuario(comando[1], comando[2])
                if retorno_cliente:
                    self.con.send('1'.encode())
                else:
                    self.con.send('0'.encode())
 
            # Cadastro de usuario
            elif comando[0] == 'cad_usuario':
                usuario = Usuario(comando[1], comando[2], comando[3], comando[4])
                success = self.bank.cadastrar_usuario_bd(usuario)
                
                if success:
                    self.con.send('1'.encode())
                else:
                    self.con.send('0'.encode())

            # Listar tarefas
            elif comando[0] == 'abrir':
                with lock:
                    retorno_cliente = self.bank.listarTarefasNaoConcluidas()

                if retorno_cliente:
                    self.con.send(retorno_cliente.encode())
                else:
                    self.con.send('0'.encode())

            # Listar tarefas concluidas
            elif comando[0] == 'abrir_con':
                with lock:
                    retorno_cliente = self.bank.listarTarefasConcluidas()

                if retorno_cliente:
                    self.con.send(retorno_cliente.encode())
                else:
                    self.con.send('0'.encode())

            # Cadastro de tarefa
            elif comando[0] == 'cad_tarefa':
                titulo = comando[1]
                descricao = comando[2]
                prazo = comando[3]
                tarefa = Tarefa(titulo, descricao, prazo, self.bank.usuario.id_usuario)
                success = self.bank.cadastrar_tarefas(tarefa)

                if success:
                    self.con.send('1'.encode())
                else:
                    self.con.send('3'.encode())

            # Notificação
            elif comando[0] == 'notificacao':
                with lock:
                    retorno_cliente = self.bank.obter_tarefas_pendentes()

                    if retorno_cliente is not False:
                        quantidade_tarefas = retorno_cliente.get("quantidade_tarefas")
                        tarefas_pendentes = retorno_cliente.get("tarefas_pendentes")
                        if quantidade_tarefas is not None and tarefas_pendentes is not None:
                            vencimento_tarefas = [f"{tarefa['dias_restantes']}|{tarefa['titulo']}" for tarefa in tarefas_pendentes]
                            self.con.send(f"{quantidade_tarefas},{','.join(vencimento_tarefas)}".encode())
                        else:
                            self.con.send('0'.encode())
                    else:
                        self.con.send('0'.encode())
                        
            # Excluir tarefa
            elif comando[0] == 'excluir_tarefa':
                lock.acquire()
                try:
                    success = self.bank.excluirTarefa(comando[1])
                    if success:
                        self.con.send('1'.encode())
                    else:
                        self.con.send('0'.encode())
                finally:
                    lock.release()

            # Atualizar tarefa
            elif comando[0] == 'atualizar_tarefa':
                id_tarefa = int(comando[1])
                novo_titulo = comando[2]
                nova_descricao = comando[3]
                novo_prazo = comando[4]
                
                success = self.bank.atualizar_tarefa(id_tarefa, novo_titulo, nova_descricao, novo_prazo)
                
                if success:
                    self.con.send('1'.encode())
                else:
                    self.con.send('0'.encode())

            # Reativar tarefa
            elif comando[0] == 'reativar_tarefa':
                lock.acquire()
                try:
                    success = self.bank.reativarTarefa(comando[1])
                    if success:
                        self.con.send('1'.encode())
                    else:
                        self.con.send('0'.encode())
                finally:
                    lock.release()

            # Concluir tarefa
            elif comando[0] == 'concluir_tarefa':
                lock.acquire()
                try:
                    success = self.bank.concluirTarefa(comando[1])
                    if success:
                        self.con.send('1'.encode())
                    else:
                        self.con.send('0'.encode())
                finally:
                    lock.release()

            # Sair
            elif comando[0] == 'sair':
                self.con.close()
                print(f'Conexao {self.con} ENCERRADA')
                break

def iniciar_servidor():
    """
    Cria um socket para o servidor e gerencia as solicitacoes dos usuarios, encaminhando-as para o banco.

    Este metodo cria um socket para o servidor, define o endereço IP e a porta para a comunicacao. Em seguida, ele aguarda conexoes de clientes.

    """
    ip = '192.168.18.36'
    port = 9017

    addr = (ip, port)  # Define a tupla de endereço
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_socket.bind(addr)

    while True:
        serv_socket.listen(10)

        print('Aguardando conexão...\n')
        conexao, cliente = serv_socket.accept()
        newthread = ThreadCliente(cliente, conexao)
        newthread.start()

if __name__ == '__main__':
    iniciar_servidor()
