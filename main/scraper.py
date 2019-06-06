import requests
import random
from requests.exceptions import RequestException
from lxml import html
from main.scraper_helpers.extractors import *
from main.scraper_helpers import config
from main.models import Product
from bs4 import BeautifulSoup


def get_product_url(asin):
    return 'https://www.amazon.com/dp/%s' % asin


def get_proxy():
    '''
    Function to rotate over proxies to avoid getting blocked
    '''
    if not config.proxies or len(config.proxies) == 0:
        return None

    proxy_ip = random.choice(config.proxies)
    return {
        "http": proxy_ip,
        "https": proxy_ip
    }


def get_user_agent():
    '''
    Function to rotate over proxies to avoid getting blocked
    '''
    user_agent = random.choice(config.user_agent_list)
    return user_agent


def get_request_headers():
    headers = config.headers
    headers['User-Agent'] = get_user_agent()
    return headers

# Make Request
#   Success: parse data and save product to db
#   Fail: try again with different proxy & user_agent


def make_request(asin):
    url = get_product_url(asin)
    headers = get_request_headers()
    # proxies = get_proxy()
    try:
        response = requests.get(url, headers=headers)
    except RequestException as e:
        print ("except", e)
        make_request(asin)

    if response.status_code != 200:
        return None

    else:
        print(response)
        print(BeautifulSoup(response.text), response.text)
        tree = html.fromstring(response.content)
        # tree = BeautifulSoup(response.text)
        return tree

    return response


def parse_response(response, asin):
    title = get_product_title(response)
    sale_price = get_sale_price(response)
    category = get_product_category(response)
    original_price = get_product_original_price(response)
    url = get_product_url(asin)
    product_dimensions = get_product_dimension(response)
    img = get_product_img(response)
    rank = get_product_rank(response)

    data = {
        'name': title,
        'sale_price': sale_price,
        'category': category,
        'price': original_price,
        'url': url,
        'product_dimensions': product_dimensions,
        'asin': asin,
        'image': img,
        'rank': rank,
    }
    print("DATA", data)

    print(response)

    return data


def save_product(product_dict):
    product = Product(**product_dict)
    product.save()
