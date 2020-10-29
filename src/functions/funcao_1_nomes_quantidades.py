# scrap para pegar preços na dental cremer
# scrap para funções de busca e retorno de valor (quantidade de buscas)

from bs4 import BeautifulSoup
import urllib.request

# lista de queries desejadas
desired_dental_cremer_queries = ['luva', 'resina','ricketts','ionomero']

# resultado da lista de queries encontradas
resultado_busca_queries = []

for query in desired_dental_cremer_queries:
    # Constracting http query
    url = 'https://busca.dentalcremer.com.br/busca?q=' + query
    # For avoid 403-error using User-Agent
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    response = urllib.request.urlopen( req )
    html = response.read()
    # Parsing response
    soup = BeautifulSoup(html, 'html.parser')



    # Extracting number of results
    resultStats = soup.find("div",{"class" : "neemu-total-products-container nm-mobile-hidden" })
    children = resultStats.findChildren("strong", recursive=False)
    for child in children:
       # transforma o resultado em número inteiro
        child = int(child.get_text())
        resultado_busca_queries.append(child) # cria lista com os valores da busca
        #print(child)
        #print("###########")

    # mostra o resultado com o child <strong>numero</strong>
    #resultStats = soup.find_all("div", class_="neemu-total-products-container nm-mobile-hidden")

# printa as duas listas para teste
print(desired_dental_cremer_queries,resultado_busca_queries)

# cria a tupla com o resultado buscado
tupla = tuple(zip(list(desired_dental_cremer_queries),list(resultado_busca_queries)))

print(tupla)
# Mostra a tupla e o resultado da busca
for x in tupla:
    print(f"Nome = {x[0]} , Buscas = {x[1]}")
