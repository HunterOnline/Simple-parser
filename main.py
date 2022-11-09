import requests
from bs4 import BeautifulSoup

url = 'https://home-club.com.ua/ua/sku-90507603?gclid=CjwKCAjwzY2bBhB6EiwAPpUpZhSieA2DRWXhLcbNCpIvJcC9dLHc534Djx5FKNpL9iXaLZlSQaNyLBoCEwYQAvD_BwE'

headers = {
    "Accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}


def get_requests(url, headers):
    try:
        rec = requests.get(url, headers=headers)
        response = rec.text
        print('status:200')
        return response
    except Exception as ex:
        print(ex)


def html_content(html_response):
    try:
        with open("index.html", "w") as file:
            file.write(html_response)
            print('write success html_file!')
    except Exception as ex:
        print(ex)


def get_item_context():
    try:
        with open("index.html") as file:
            context = file.read()
            soup_context = BeautifulSoup(context, 'lxml')
        item_context = soup_context.find_all(class_="additional-details")[0]
        item_list = [text for text in item_context.stripped_strings]
        key = item_list[::2]
        vel = item_list[1::2]
        item_text = dict(zip(key, vel))
        del item_text['Дата поставки під замовлення:']
        return item_text

    except Exception as ex:
        print(ex)


def write_file():
    try:
        with open("item.txt", "w") as file:
            for key, vel in get_item_context().items():
                file.write(key + vel + '\n')

        print("Файл Готовий!")


    except Exception as ex:
        print(ex)





if __name__ == '__main__':
    html_response = get_requests(url, headers)
    html_content(html_response=html_response)
    print(get_item_context())
    write_file()
