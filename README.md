# Projeto: Sistema de Gerenciamento de Tarefas

## Este é um projeto de um Sistema de Gerenciamento de Tarefas desenvolvido utilizando a biblioteca PyQt5 para a interface gráfica e sockets para a comunicação entre cliente e servidor. O sistema permite que os usuários realizem o cadastro, busca, edição e conclusão de tarefas.

## Funcionalidades

### Interface Gráfica
O sistema possui uma interface gráfica que é composta por diferentes telas, representadas pelas classes abaixo:

- Tela_login: Tela de login, onde o usuário pode inserir suas credenciais para acessar o sistema.
- Tela_inicial: Tela principal do sistema após o login, onde são exibidas as principais opções e informações sobre tarefas.
- Tela_cadastroUsuario: Tela de cadastro de novo usuário, onde é possível criar uma nova conta no sistema.
- Tela_cadastroTarefa: Tela de cadastro de tarefas, onde os usuários podem inserir os detalhes de uma nova tarefa a ser realizada.
- Tela_buscar_tarefa: Tela de busca de tarefas, onde são exibidas as tarefas cadastradas e disponíveis para edição ou exclusão.
- Tela_ativar: Tela de tarefas concluídas, onde as tarefas concluídas podem ser visualizadas e reativadas, se necessário.
- Tela_funcoes_tarefa: Tela com funções de tarefa, onde os usuários podem acessar opções adicionais relacionadas às tarefas, como busca, conclusão e edição.

### Funcionalidades do Servidor
O servidor é responsável por gerenciar as operações do sistema e atender as solicitações dos clientes. Algumas das funcionalidades do servidor incluem:

- Cadastro de Usuário: O servidor recebe as informações de um novo usuário (nome, e-mail, nome de usuário e senha) e realiza o cadastro, verificando se o nome de usuário já está em uso.
- Login: O servidor recebe as credenciais de login (nome de usuário e senha) e autentica o usuário, permitindo o acesso ao sistema se as informações forem válidas.
- Cadastro de Tarefa: O servidor recebe as informações de uma nova tarefa (nome, descrição e prazo) e realiza o cadastro, associando-a ao usuário logado.
- Busca de Tarefas: O servidor fornece ao cliente a lista de tarefas cadastradas para o usuário logado, incluindo tarefas concluídas e pendentes.
- Edição de Tarefa: O servidor recebe informações atualizadas de uma tarefa (nome, descrição e prazo) e realiza a atualização dos dados da tarefa correspondente.
- Conclusão de Tarefa: O servidor recebe a solicitação de conclusão de uma tarefa e a marca como concluída.
- Tarefas Concluídas: O servidor fornece ao cliente a lista de tarefas concluídas para o usuário logado.
- Reativação de Tarefa: O servidor recebe a solicitação de reativação de uma tarefa concluída e a marca como pendente novamente, entre outras.

### Comunicação Cliente-Servidor
O sistema utiliza sockets para a comunicação entre cliente e servidor. O cliente é responsável por enviar as solicitações ao servidor e receber as respostas correspondentes.

### Funcionalidades das Funções
A classe Main é a classe principal do sistema e gerencia a lógica de controle da interface do usuário, interação com o servidor e manipulação de eventos. Algumas das principais funções da classe Main incluem:

- abrir_tela_login(): Abre a tela de login do sistema.
- abrir_tela_inicial(): Abre a tela inicial do sistema após o login.
- abrir_tela_cadastro_usuario(): Abre a tela de cadastro de novo usuário.
- abrir_tela_cadastro_tarefa(): Abre a tela de cadastro de nova tarefa.
- abrir_funcoes_tarefa(): Abre a tela com funções adicionais relacionadas às tarefas.
- sair(): Encerra a conexão do cliente com o servidor e fecha a aplicação.
- quantidade_tarefas_pendentes(): Recebe uma mensagem do servidor e exibe uma caixa de diálogo com a quantidade de tarefas pendentes para o usuário logado.
- cadastrar_usuario(): Cadastra um novo usuário com base nos dados fornecidos.
- abrir_tela_tarefa_concluida(): Abre a tela de tarefas concluídas.
- abrir_tela_buscar_tarefa(): Abre a tela de busca de tarefas.

Essas funções são responsáveis por permitir a navegação entre as telas, interação com o servidor para realizar operações como cadastro, busca e edição de tarefas, além de exibir informações ao usuário por meio de caixas de diálogo.

### Banco de Dados
O sistema utiliza um banco de dados para armazenar as informações dos usuários e tarefas. É importante garantir que o banco de dados esteja configurado corretamente e acessível para o funcionamento adequado do sistema.

Algumas funções relacionadas ao cadastro e manipulação de tarefas podem conter verificações adicionais para garantir a integridade e segurança dos dados, como validação de campos e tratamento de exceções. Estas verificações podem ser implementadas de acordo com as necessidades específicas do projeto.

O projeto utiliza uma estrutura básica de interface gráfica para a demonstração das funcionalidades. É possível estender e personalizar a interface para melhor atender aos requisitos do projeto final.

Esse é um resumo das principais funcionalidades do sistema de gerenciamento de tarefas. Para a implementação completa e funcional do projeto, é necessário integrar o código fornecido com as classes de interface gráfica (Tela_login, Tela_inicial, etc.) e as classes responsáveis por realizar as operações no servidor. Além disso, podem ser implementadas outras funcionalidades adicionais conforme as necessidades do projeto.

## Observações
O projeto utiliza o módulo socket para a comunicação entre cliente e servidor. Certifique-se de que o servidor esteja em execução e acessível no endereço IP e porta especificados (10.180.44.80:9017). Caso o endereço ou a porta do servidor sejam diferentes, é necessário atualizar esses valores no código.

