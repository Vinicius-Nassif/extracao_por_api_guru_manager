import requests
import pandas as pd
from tk import token 

class API_transactions():
    def __init__(self, url, arquivo):
        # Alocando argumentos
        self.url = url 
        self.nome_arquivo = arquivo

        # Inicializando objetos
        self.data_transaction = []
        self.response = []
        self.data = []
    
    def acesso(self):
        # Definindo as variáveis da API de transações e o token
        ## Inserindo a chave 
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type":"aplication/json",
            "Accept":"application/json"
        }
        self.response = requests.get(self.url, headers=headers)

    def extracao(self):
        self.data = self.response.json()
        transactions = self.data['data']

        # Automação da busca
        for transaction in transactions:
            id = transaction['payment']['acquirer']['tid']
            contato = transaction['contact']['name']
            produto = transaction['product']['name']
            valor_total = transaction['payment']['total']
            parcelas = transaction['payment']['installments']['qty']
            parcelas_valor = transaction['payment']['installments']['value']
            metodo_pagamento = transaction['payment']['method']
            status_pagamento = transaction['payment']['acquirer']['message']
        
            print(id)
            print(contato)
            print(produto)
            print(valor_total)
            print(parcelas)
            print(parcelas_valor)
            print(metodo_pagamento)
            print(status_pagamento)

            valor_total = f"R${valor_total}"
            forma_pagamento = f"{parcelas}x de R${parcelas_valor}"

            #quebra de linha
            print()

            # Criação do dataframe
            self.data_transaction.append(
                        [id, contato, produto, 
                        valor_total, forma_pagamento, metodo_pagamento, 
                        status_pagamento])

    def criar_tabela(self):
        dados = pd.DataFrame(self.data_transaction, columns=[
                                            'ID', 'Contato', 'Produto', 
                                            'Valor Total', 'Parcelamento', 'Método', 
                                            'Status'])
        dados.to_excel('transactions.xlsx', index=False)

if __name__=='__main__':
    produtos = API_transactions(url="https://digitalmanager.guru/api/v1/transactions/", arquivo='transactions.xlsx')
    produtos.acesso()
    print('Acesso concedido!')
    produtos.extracao()
    print('extração realizada com sucesso!')
    produtos.criar_tabela()
    print('Tabela criada com sucesso!')
    print('Tarefa concluída!')
