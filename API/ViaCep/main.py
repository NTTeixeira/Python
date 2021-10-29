import requests

url = 'https://viacep.com.br/ws/'
cep = str(input("Digite o CEP: "))
formato = '/json/'

r = requests.get(url + cep + formato)

if r.status_code == 200:
    print()
    print('JSON:', r.json())
    print()
else:
    print('Nao houve sucesso na requisicao.')
