# Importando Bibliotecas:
import requests
from bs4 import BeautifulSoup
import time

# Realizando a Raspagem das Informações:
def scrape_news():
    url = 'https://www.bbc.com/news'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch the site. Status code: {response.status_code}")
        return
    soup = BeautifulSoup(response.text, 'html.parser')

    # Selecionando manchetes principais
    articles = soup.select('.gs-c-promo-heading__title')
    if not articles:
        print("No articles found. The site structure might have changed.")
        return
    with open('news.txt','a',encoding='utf-8') as file:
        file.write(f'\n==== News Found in {time.ctime()} ====\n')
        for article in articles:
            title = article.text
            file.write(f'{title}\n')
    print(f'Data found and saved in \'news.txt\'')

# Agendando a Raspagem:
def schedule_scrapper():
    while True:
        scrape_news()
        print('Restart in 10 minutes...')
        time.sleep(1)

# Main:
if(__name__=="__main__"):
    print(f'Start System Web Scrapper...')
    schedule_scrapper()