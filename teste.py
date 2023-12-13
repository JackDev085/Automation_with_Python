import requests 
from bs4 import BeautifulSoup
import pprint
import os
url ='https://www.dell.com/pt-br/shop/deals/promocao-notebook-gamer?gacd=9657105-15013-5761040-275878141-0&dgc=ST&cid=71700000107532436&gclsrc=3p.ds&&gclid=3e3ee2250bc0155b8d8a875cd14dbc48&gclsrc=3p.ds&msclkid=3e3ee2250bc0155b8d8a875cd14dbc48&utm_source=bing&utm_medium=cpc&utm_campaign=BR_AP_TXT_Gaming-Desktops&utm_term=pc%20gamer%20completo&utm_content=Core'

response = requests.get(url).text

tratamento = BeautifulSoup(response, 'html.parser')
i=0
tratamento.parent
for produto in tratamento.select('#deals-middle-content-zone > div.category-box'):
  if i == 10:
    break
  pprint.pprint(produto.text)
  i+=1
