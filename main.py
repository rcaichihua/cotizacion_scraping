from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.chrome.service import Service

def get_soup(url):
  options = webdriver.ChromeOptions() 
  options.add_experimental_option('excludeSwitches', ['enable-logging']) 
  service = Service('driver/chromedriver.exe') 
  driver = webdriver.Chrome(service=service, options=options)

  driver.get(url)
  sleep(3)
  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser')
  driver.close()
  return soup

def get_securex_objects(soup):
  CompraDolares = soup.find_all('div', {'class':'col-md-5 col-xs-5 text-center'})
  for i, CompraDolar in enumerate(CompraDolares):
    name = CompraDolar.find('span', {'class':'fs-16-bold'}).text
    tipocambio = CompraDolar.find('span', {'style':'font-weight: 600 !important;'}).text
    print(f'{i + 1 }. Compra {tipocambio}')

def init():
  print("web Scraping Cotización")
  securex = f'https://securex.pe'

  securex_soup = get_soup(securex)

  get_securex_objects(securex_soup)

if __name__ == "__main__":
  init()