import re

endereco = "rua sao sebastiao, n 249 bairro chico de paula, cidade Santos SP 11085-270"
padrao = "[0-9]{5}[-][0-9]{3}"
teste = "teste 123"
cep = re.search(padrao, endereco)
print(cep)
