import requests
from bs4 import BeautifulSoup

import random

# 알파벳 리스트
oxford_urls = [
    'https://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/Oxford3000_A-B/?page=',
    'https://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/Oxford3000_C-D/?page=',
    'https://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/Oxford3000_E-G/?page=',
    'https://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/Oxford3000_H-K/?page=',
    'https://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/Oxford3000_L-N/?page=',
    'https://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/Oxford3000_O-P/?page=',
    'https://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/Oxford3000_Q-R/?page=',
    'https://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/Oxford3000_S/?page=',
    'https://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/Oxford3000_T/?page=',
    'https://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/Oxford3000_U-Z/?page='
]

# 로그 출력
word_list = []

for oxford_url in oxford_urls:
    count = 1
    while count < 5:
        # print(alphabet_item + str(count))
        response = requests.get(oxford_url + str(count), headers={'User-Agent':'Mozilla/5.0'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        alphabet_list = soup.select('#entrylist1 > ul > li > a')
        for alphabet_item in alphabet_list:
            word_list.append(alphabet_item.text) 
        count += 1

# print(word_list)
# print(len(word_list))

# 랜덤으로 뽑기
random_value = []

for i in range(0, 6):
    random_value.append(random.randint(1, len(word_list)))

for i in random_value:
    word_list[i]