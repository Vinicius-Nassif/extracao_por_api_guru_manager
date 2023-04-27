# Projeto Extração de Dados Via API - Digital Manager Guru

## 1. Introdução

A extração de dados via API é o processo de obtenção de informações de um sistema ou serviço online usando uma API (Interface de Programação de Aplicativos).

Uma API é um conjunto de rotinas, protocolos e ferramentas para a criação de aplicativos de software, permitindo que diferentes sistemas e serviços se comuniquem e troquem informações de forma padronizada. 

O objetivo deste trabalho é instrumentalizar o serviço de um freelancer responsável que deveria desenvolver um script Python que realize a extração de dados de um histórico de transações existentes no site www.digitalmanager.guru , faça algumas operações e em seguida gere um  arquivo .xlsx com as informações processadas. O script deve ser simples, eficiente e fácil de usar.

As informações desejadas são:

- ID da transação;
- Contato (nome do cliente);
- Produto;
- Valor total da transação;
- Número de parcelas;
- Valor dar parcelas;
- Método do pagamento; e 
- Status do pagamento.

O trabalho teve como paradigma uma empresa de Data Analytics que desejava compor seu banco de dados de transações para promover tomada de decisões. 

O intuito dessa atividade irá melhor expor a extração de dados via API por meio da divisão de módulos, variáveis, lógica de programação, laço de repetição, manipulação de arquivos, conforme demonstrado a seguir.



## 2. Módulos

Módulo é um arquivo contendo funções em *Python* para serem usados em outros programas da mesma linguagem.

Para instrumentalizar essa atividade de maneira organizada, foi realizada em dois módulos de código *Python*:

- tk.py; e
- transactions_guru.py.

Cada um será responsável por etapas do processo e serão abordados no decorrer desse trabalho.



## 3. tk.py

Nesse módulo, foi especificado apenas a variável Token recebendo a chave de acesso a plataforma que será importada no próximo script e, por motivos de segurança e respeito da Lei Geral de Proteção de Dados Pessoais (LGPD) - Lei 13.709/18, sua imagem foi suprimida da documentação.



## 4. transactions_guru.py

### 4.1 Bibliotecas

O Projeto teve início com a importação das bibliotecas e módulos utilizados na elaboração do código em python. 

![1](https://user-images.githubusercontent.com/111388699/234991708-9848dca9-30af-4c24-94a8-f57002909f49.png)

A biblioteca `requests` é utilizada para realizar requisições HTTP em Python. Neste script, ela é utilizada para realizar a requisição GET na API de transações e armazenar o resultado em uma variável.

A biblioteca `pandas` é utilizada para trabalhar com estruturas de dados em Python. Neste script, ela é utilizada para criar o dataframe com as informações extraídas da API e salvar essas informações em um arquivo excel.

A linha de código `from tk import token` importa a variável `token` do arquivo `tk.py`. Essa variável é utilizada como token de autorização para acessar a API de transações.



### 4.2 Código 

A classe `API_transactions` é o coração do script e é composta por quatro métodos:

#### `def__init__(self, doc_inicial, documento gerado):`

O método `__init__` é o construtor da classe. Ele recebe como argumentos a URL da API de transações e o nome do arquivo a ser gerado. 

![2](https://user-images.githubusercontent.com/111388699/234991745-4e2b50d7-3c04-4fee-a80b-95f53397c8c6.png)

Ele inicializa os seguintes objetos:

- `self.url`: recebe a URL passada como argumento;

- `self.nome_arquivo`: recebe o nome do arquivo passado como argumento;

- `self.data_transaction`: inicializa uma lista vazia que será usada para armazenar as transações;

- `self.response`: inicializa uma variável vazia que receberá a resposta da API;

- `self.data`: inicializa uma variável vazia que receberá os dados da API em formato JSON.

  

#### `def acesso(self):`

O método `acesso` é responsável por acessar a API de transações e obter as informações desejadas. Ele utiliza a biblioteca `requests` para fazer uma requisição GET à URL da API. 

![3](https://user-images.githubusercontent.com/111388699/234991779-0e556646-f86a-4bbe-aace-d00784a28546.png)

O token de acesso é inserido no header da requisição para autenticar a consulta. O resultado é armazenado em `self.response`.O token de acesso é inserido no header da requisição para autenticar a consulta e é definido um dicionário com as informações de autenticação em formato JSON para o tipo de conteúdo e da resposta da API.

O resultado é armazenado em `self.response`.



#### `def extracao(self):`

O método `extracao` é responsável por extrair as informações relevantes da resposta da API e armazená-las em uma lista. 

![4](https://user-images.githubusercontent.com/111388699/234991808-f83caa68-f792-4cbb-8a90-390723ec803d.png)

A função começa convertendo a resposta da requisição para um formato JSON, que é mais fácil de manipular. Em seguida, ela busca as transações na resposta da API e percorre cada uma delas em um laço `for`.

Para cada transação, a função extrai as seguintes informações:

- `id`: o identificador da transação.
- `contato`: o nome do cliente que fez a transação.
- `produto`: o nome do produto adquirido na transação.
- `valor_total`: o valor total da transação.
- `parcelas`: o número de parcelas da transação.
- `parcelas_valor`: o valor de cada parcela da transação.
- `metodo_pagamento`: o método de pagamento utilizado na transação.
- `status_pagamento`: o status do pagamento da transação.

Essas informações são então adicionadas ao dataframe `self.data_transaction` como uma nova linha.

Além disso, a função formata o valor total da transação e o valor de cada parcela para exibição no console e insere uma quebra de linha para melhorar a legibilidade da saída.

Ao final do método, as informações armazenadas no dataframe `self.data_transaction` serão utilizadas para criar uma tabela no formato de arquivo excel.

![5](https://user-images.githubusercontent.com/111388699/234991861-23c9dd78-7354-4394-a5df-5b2bc3ac3037.png)



#### `def criar_tabela(self):`

A função `criar_tabela` cria um DataFrame do Pandas a partir da lista `self.data_transaction` com as seguintes colunas: 'ID', 'Contato', 'Produto', 'Valor Total', 'Parcelamento', 'Método' e 'Status'.

Em seguida, a função utiliza o método `to_excel` para salvar o DataFrame em um arquivo Excel chamado 'transactions.xlsx', sem incluir a coluna de índice.

![6](https://user-images.githubusercontent.com/111388699/234991933-1ebc9e0d-cf14-4845-9c1c-564887a58fa5.png)



#### Execução com `if __name__ == "__main__"`

Este trecho de código representa a execução principal do script. Quando o módulo é executado diretamente, a condição `if __name__ == "__main__"` é verdadeira e o código dentro dela é executado.

![7](https://user-images.githubusercontent.com/111388699/234991961-5df7f431-90cc-4495-bba7-4d0ef8b9a241.png)

1. `produtos = API_transactions(url="https://digitalmanager.guru/api/v1/transactions/", arquivo='transactions.xlsx')`: Cria uma instância da classe `API_transactions` passando a URL da API e o nome do arquivo onde a tabela de transações será salva.
2. `produtos.acesso()`: Chama o método `acesso()` da instância criada, que realiza a solicitação GET na URL da API com o token de autenticação.
3. `print('Acesso concedido!')`: Imprime na tela a mensagem indicando que a conexão foi bem sucedida.
4. `produtos.extracao()`: Chama o método `extracao()` da instância criada, que extrai os dados da resposta da API e preenche a lista `self.data_transaction`.
5. `print('extração realizada com sucesso!')`: Imprime na tela a mensagem indicando que a extração foi realizada com sucesso.
6. `produtos.criar_tabela()`: Chama o método `criar_tabela()` da instância criada, que cria um DataFrame a partir da lista `self.data_transaction` e salva-o em um arquivo Excel.
7. `print('Tabela criada com sucesso!')`: Imprime na tela a mensagem indicando que a tabela foi criada com sucesso.
8. `print('Tarefa concluída!')`: Imprime na tela a mensagem indicando que a tarefa foi concluída com sucesso.



#### Demonstração da extração

Por motivos de segurança e respeito da Lei Geral de Proteção de Dados Pessoais (LGPD) - Lei 13.709/18, o arquivo .xlsx não poderá ser exibido nessa documentação.



## 5. Conclusão

Esse projeto foi criado para melhor elucidar o conhecimento trazido pela extração de dados via API, pois em seu desenvolvimento foi necessária a interação de bibliotecas do python, bem como entender conceitos e aplicações da lógica de programação.

O script desenvolvido é eficiente e cumpre com o objetivo de extrair informações de uma API, e gerar um arquivo excel com os dados processados, o que possibilitou o melhor conhecimento das transações da empresa de Data Analytics e uma melhor tomada de decisões. Portanto, essa é uma forma de utilizar a manipulação de dados a seu favor, seja para uso profissional ou pessoal. 
