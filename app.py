import requests
from bs4 import BeautifulSoup
from datetime import datetime

# URL do site
url = "file:///path/to/your/index.html"  # Altere para o caminho correto do seu arquivo HTML

# Realizar a requisição HTTP para obter o conteúdo da página
response = requests.get(url)
content = response.content

# Parsear o conteúdo HTML usando BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Encontrar a seção de produtos
products_section = soup.find('section', id='products')

# Encontrar todos os produtos dentro da seção de produtos
products = products_section.find_all('div', class_='product')

# Obter a data e hora atuais
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'Data e hora da raspagem: {timestamp}')
print('---')

# Iterar sobre os produtos e extrair informações
for product in products:
    name = product.find('h3').text
    price = product.find('p', class_='price').text
    description = product.find_all('p')[1].text
    
    print(f'Name: {name}')
    print(f'Price: {price}')
    print(f'Description: {description}')
    print('---')
