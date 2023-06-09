import requests
import json

def consulta(cep):
    try:
        #url para consulta do Cep
        url_Api = f'https://viacep.com.br/ws/{cep}/json/'

        requisicao = requests.get(url_Api)
        dados_Json = requisicao.content
        dados = json.loads(dados_Json)

        dados_Logradouro = dados['logradouro']
        dados_Bairro = dados["bairro"]
        dados_Localidade = dados['localidade']
        #Se a Api não responder o logradouro, logo é um cep geral
        if dados_Logradouro == '':
            print(f"Cep geral: {dados_Localidade}")
        else:
            print(f"{dados_Logradouro}, {dados_Bairro}, {dados_Localidade}")

    #Except para caso o usuario insira um cep invalido
    except:
        print('Informe um CEP valido!')