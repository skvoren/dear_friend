import datetime
import time

import requests
from bs4 import BeautifulSoup

address = 'https://www.binance.com/en/news/flash'
adressNews = 'https://www.binance.com'
str = '/en/news/flash/'

soup = requests.get(address)

soup = BeautifulSoup(soup.text, 'lxml')
acordeons = soup.findAll('a')

links = []

for acordeon in acordeons:
    if str in acordeon.get('href'):
        links.append(acordeon.get('href'))

arr = []

for link in links:
    newsSoup = requests.get(adressNews + link)
    newsSoup = BeautifulSoup(soup.text, 'lxml')
    articles = soup.find_all('div')
    for article in articles:
        arr.append(article.text)
    time.sleep(1)

result = []

for row in arr:
    result.append(row.split())

print('Привет друг! Вводи количество букв в слове:')
length = input()
print('Хорошо, слово из ' + length + 'букв, теперь введи буквы которые зеленые ^ или желтые *, неизвестную букву помечай _')
print('Например - X^Y*_T^A^')
targetWord = input()
print('Теперь введи список букв которые серые на клавиатуре, в верхнем регистре, через пробел')
lettersNotInUse = input()

print(length)
print(targetWord)
print(lettersNotInUse)

