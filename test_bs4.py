import requests
from bs4 import BeautifulSoup

url = 'https://www.perekrestok.ru/cat/mc/25/gotovaa-eda'
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

products = soup.find_all(class_='product-card__title')
prices = soup.find_all(class_='price-new')

product_prices = dict(zip(products, prices))

for product in product_prices:
    print('{} - {}'.format(product.text, product_prices[product].text))