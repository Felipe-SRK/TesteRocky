# IMPORTAÇÃO DO ARQUIVO JSON
import json
from pprint import pprint


def db_json():
    with open('broken-database.json', encoding='utf-8') as f:
        return json.load(f)


data = db_json()
# FUNÇÃO PARA LEITURA E RESOLUÇÃO DO PRIMEIRO PROBLEMA
baseData = []
for product in data:
    # CORRIGIR NOME
    product['name'] = product['name'].replace('ø', 'o').replace(
        'æ', 'a').replace('¢', 'c').replace('ß', 'b')
    # CORRIGIR PREÇO
    product['price'] = float(product['price'])
    # FUNÇÃO CORRIGINDO A QUANTIDADE
    if 'quantity' not in product:
        product['quantity'] = 0
    baseData.append(product)
# FUNÇÃO PARA EXPORTAR O ARQUIVO COM O NOME "SAIDA.JSON"
with open('saida.json', 'w', encoding='utf-8') as json_file:
    json.dump(baseData, json_file, ensure_ascii=False)


# INICIO DA SEGUNDA PARTE DE RESOLUCÃO

# IMPORTANDO O ARQUIVO FORMATADO
def base_correct():
    with open('saida.json', encoding='utf-8') as g:
        return json.load(g)


data = base_correct()
# ORDENANDO O ARQUIVO PARA LEITURA CORRETA
list1 = sorted(data, key=lambda k: (k['category'], k['id']))
pprint(list1)

# FUNÇÃO PARA DAR O RESULTADO DO ESTOQUE POR CATEGORIA
def CategoryCust(list1):
    category = []
    value = []
    for i in range(len(list1)):
        if list1[i]["category"] in category:
            value[category.index(list1[i]["category"])] = value[category.index(
                list1[i]["category"])] + list1[i]["price"] * list1[i]["quantity"]
        else:
            category.append(list1[i]["category"])
            value.append(list1[i]["price"] * list1[i]["quantity"])
    pprint("Valor dos Produtos por Categoria Estocado:")
    for i in range(len(category)):
        pprint(category[i] + " = " + "{0:.2f}".format(value[i]))
    pprint("Resultado = " + "{0:.2f}".format(sum(value)))
pprint(CategoryCust(list1))
