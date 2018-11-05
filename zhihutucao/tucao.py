#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

HEADERS = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        }
URL = 'https://daily.zhihu.com'

def get_requests(url,**kargs):
    req = requests.get(url,**kargs)
    return req.text


def get_tucao_url(html):
    soup = BeautifulSoup(html,'html.parser')
    tucao_url = soup.select('.title')
    url = []
    for i in tucao_url:
        if '吐槽' in i.string:
            url.append(i.parent['href'])
    return url


def get_tucao_content(html):
    soup = BeautifulSoup(html,'html.parser')
    tucao_content = soup.select('.question')
    for i,c in enumerate(tucao_content):
        print('吐槽' + str(i+1) +':' + c.h2.string)
        print('--' * (len(c.h2.string) + 5))
        for i in c.select('.answer'):
            print('作者: ' + i.span.string)
            print(parse_answer(i.select('.content')))
        print('=' * 100)


def parse_answer(content):
    answer = str(content)
    answer = answer.replace('<p>','')
    answer = answer.replace('</p>','')
    answer = answer.replace('[<div class="content">','')
    answer = answer.replace('</div>]','')
    return answer

def main():
    index_content = get_requests(URL,headers=HEADERS)
    tucao_url = get_tucao_url(index_content)
    if tucao_url:
        for i in tucao_url:
            url = URL + i
            print(url)
            print('=' * 100)
            tucao_content = get_requests(url,headers=HEADERS)
            get_tucao_content(tucao_content)

if __name__ == '__main__':
    main()














