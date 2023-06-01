import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import argparse


def is_bitlink(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    parsed_url = urlparse(url)
    bitlink_id = f'{parsed_url.netloc}{parsed_url.path}'
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_id}',
                            headers=headers)
    return response.ok


def shorten_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    long_url = {
        'long_url': url
    }
    response = requests.post('https://api-ssl.bitly.com/v4/shorten',
                             headers=headers,
                             json=long_url)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, link):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    parsed_link = urlparse(link)
    bitlink_id = f'{parsed_link.netloc}{parsed_link.path}'
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_id}/clicks/summary',
                            headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def main():
    load_dotenv()
    token = os.getenv('TOKEN_BITLY')
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Введите URL или ссылку Bitlink')
    args = parser.parse_args()
    try:
        if is_bitlink(token, args.url):
            clicks_count = count_clicks(token, args.url)
            print('Количество кликов по битлинку: ', clicks_count)
        else:
            short_url = shorten_link(token, args.url)
            print('Битлинк: ', short_url)
    except requests.exceptions.HTTPError as error:
        print(f'Произошла ошибка: {error}')


if __name__ == '__main__':
    main()
