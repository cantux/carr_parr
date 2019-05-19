import requests
from bs4 import BeautifulSoup

import csv

import re
import datetime

class Ser():
    pass

# following is depracated with new site design.
# item_count = get_item_count(cat_soup)
# page_count = int(item_count / 24) + 2
# def get_item_count(cat_soup):
#     pagination_bar = cat_soup.find('div', attrs={'class': 'pagination-bar'})
#     raw_item_count = pagination_bar.find('div', attrs={'class': "total-pr-col"})
#     item_count = re.search(r"\d+", raw_item_count.text).group(0)
#     return int(item_count)

class ProductRetriever_gen():
    def __init__(self, cat_link):
        self.cat_link = cat_link
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        response = requests.get(self.cat_link + '?page={}'.format(self.num))
        cat_page = response.text
        cat_soup = BeautifulSoup(cat_page, 'html.parser')
 
        if not check_no_product_found(cat_soup): 
            self.num += 1
            return (cat_soup, self.cat_link)
        else:
            raise StopIteration()

def check_no_product_found(soup):
    return soup.find('div', attrs={'id': 'noProductFound'}) is not None

def append_items(products, cat_soup, cat_link):
    product_list = cat_soup.find('ul', attrs={'class': 'product-listing product-grid container-fluid add_to_cart'})
    for product in product_list.find_all('li'):
        s = Ser()
        s.product_brand_name = product.find('input', attrs={"id": "productBrandNamePost"})['value']
        s.product_code = product.find('input', attrs={"id": "productCodePost"})['value']
        s.product_price = product.find('input', attrs={"id": "productPricePost"})['value']
        s.product_name = product.find('input', attrs={"id": "productNamePost"})['value']
        s.product_main_category = product.find('input', attrs={"id": "productMainCategoryPost"})['value']
        s.product_link = product.find('a')['href']
        s_dict = s.__dict__
        s_dict.update({"category_link": cat_link})
        print("items:" + str(s_dict))
        products.append(s_dict)

def parse(category_dict):
    for (cat_type, cat_link) in category_dict.items():

        products = list()

        for (cat_soup, cat_link) in ProductRetriever_gen(cat_link):
           print("current: " + str(cat_link))
           append_items(products, cat_soup, cat_link)

        # open a csv file with append, so old data will not be erased
        with open('/home/ubuntu/data_{0}_{1}.csv'.format(cat_type, datetime.datetime.now()), 'a') as csv_file:
            writer = csv.writer(csv_file)
            for p in products:
                writer.writerow(p.values())


if __name__ == "__main__":
    category_dict = {
        "meyve_sebze": "https://www.carrefoursa.com/tr/meyve-sebze/c/1014",
        "et_sarkuteri_balik": "https://www.carrefoursa.com/tr/et-sarkuteri-balik/c/1044",
        "sut_kahvaltilik": "https://www.carrefoursa.com/tr/sut-ve-kahvaltilik/c/1310",
        "gida_yemek_malzemeleri": "https://www.carrefoursa.com/tr/gida-ve-yemek-malzemeleri/c/1110",
        "icecekler": "https://www.carrefoursa.com/tr/icecekler/c/1409"
    }

    parse(category_dict)

#     for (i, x) in enumerate(ProductRetriever_gen("https://www.carrefoursa.com/tr/meyve-sebze/c/1014")):
#         print(i)

