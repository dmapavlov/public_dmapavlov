import requests
import re

A = requests.get(input())  # вводим url первого сайта откуда будем парсить url'ы
B = input()  # вводим второй url, который будем искать

# парсинг первого URL и создание листа со ссылками urls
url_pattern = r'https://[\S]+.html'  # регулярное выражение, это pattern, по кторому надо искать url
urls = re.findall(url_pattern, A.text)  # применяем регулярное выражение для поиска url в тексте
response = 'No'

# итерируемся по списку urls, и находим B в C
for i in urls:
    C = requests.get(i)  # идем глубже в каждый url и ищем там ссылку на B
    C1 = re.findall(url_pattern, C.text)  # применяем регулярное выражение для поиска url в тексте
    if B in C1:
        response = 'Yes'

print(response)