import json

#Lendo JSON "exemplo.json"
with open('exemplo.json',encoding='utf-8') as arquivo_json: #arquivo_json  é usada para interagir com o arquivo físico
    data = json.load(arquivo_json) #Converter arquivo JSON -> Dicionário Python
    print(type(data))
    print(data['nome'])
    print(data['email'])

print('---------------------------------------------')

# Ao invés de abrir um arquivo JSON externo, eu criei um dicionario, e vou salvar ele em JSON
computador_json = {
    'marca': 'Dell',
    'preco': 1500,
    'estoque': True   
}

#Salvando esse dicionario como JSON em um arquivo
with open('computador_salvei.json', 'w', encoding='utf-8') as arquivo_json: 
    json.dump(computador_json, arquivo_json)


#Lendo JSON "computador_salvei.json"
with open('computador_salvei.json',encoding='utf-8') as arquivo_json: #arquivo_json  é usada para interagir com o arquivo físico
    data = json.load(arquivo_json) #Converter arquivo JSON -> Dicionário Python
    print(type(data))
    print(data['marca'])
    print(data['estoque'])

