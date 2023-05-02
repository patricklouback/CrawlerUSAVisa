# CrawlerUSAVisa

Robô Crawler para Agendamento de Visto no Consulado Americano
Este é um projeto de robô crawler em Python com Selenium e BeautifulSoup para automatizar o processo de agendamento de visto no Consulado Americano.

## Instalação
Antes de usar este projeto, certifique-se de ter as seguintes dependências instaladas:

Python 3
Selenium
BeautifulSoup
ChromeDriver
Você pode instalar o Selenium e o BeautifulSoup usando o pip:

## Copy code
pip install selenium
pip install beautifulsoup4
O ChromeDriver é o driver do navegador Chrome usado pelo Selenium para interagir com o site do Consulado Americano. Você pode baixar o ChromeDriver para o seu sistema operacional a partir do site oficial: https://sites.google.com/a/chromium.org/chromedriver/downloads

## Como usar
Para usar o robô crawler, basta executar o script crawler.py:

## Copy code
python main.py
O robô irá abrir o site do Consulado Americano, fazer login com as credenciais fornecidas no arquivo credentials.py e navegar até a tela de agendamento. O robô irá extrair a data mais próxima disponível para agendamento e imprimir no console.

## Contribuindo
Se você quiser contribuir para este projeto, sinta-se à vontade para criar um fork e enviar um pull request com suas mudanças. Certifique-se de seguir as diretrizes de contribuição do projeto.