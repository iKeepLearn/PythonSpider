#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from requests_html import HTMLSession

HEADERS = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        }
URL = 'https://daily.zhihu.com'

def get_requests(url,**kargs):
    session = HTMLSession()
    req = session.get(url,**kargs)
    return req.html


def get_tucao_url(html):
    tucao_url = html.find('a',containing='吐槽')
    url = [i.attrs['href'] for i in tucao_url ]
    return url


def get_tucao_content(html):
    tucao_content = html.find('.question')
    for i in tucao_content:
        print(i.text)
        b = i.find('a')
        print(b[0].attrs['href'])
        print('--' * 25)



def main():
    index_content = get_requests(URL,headers=HEADERS)
    tucao_url = get_tucao_url(index_content)
    if tucao_url:
        for i in tucao_url:
            url = URL + i
            print(url)
            tucao_content = get_requests(url,headers=HEADERS)
            get_tucao_content(tucao_content)

if __name__ == '__main__':
    main()














