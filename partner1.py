import requests
from bs4 import BeautifulSoup as bs
import json

base_url = 'http://66.vld.msudrf.ru/'  # главная страница судьи
details_url = 'http://66.vld.msudrf.ru/modules.php?name=info_pages&id=1700'  # страница с реквизитами


def get_html(url):  # Функция проверят доступ к урлу, отдает кусок html
    user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0'}
    try:
        req = requests.get(url, headers=user_agent)
        req.raise_for_status()
        return req.text
    except(requests.RequestException, ValueError):
        print('У нас сетевая ошибка')
        return False



def get_data(url_with_data, url_with_details): # Функция скрапит страницы и достает данные из html, ожидате на вход урлы
    html_with_data = get_html(url_with_data)
    html_with_details = get_html(url_with_details)
    if html_with_data and html_with_details:
        data_soup = bs(html_with_data, 'html.parser')
        details_soup = bs(html_with_details, 'html.parser')
        data = data_soup('div', class_='info-block')
        details = details_soup.find('div', {'id': 'divINFODocText1700'}).get_text()
        judge = data[0].find('p').get_text()
        assistant = data[0].find_all('p')[2].get_text()
        secretary = data[0].find_all('p')[4].get_text()
        number1 = data[0].find_all('span')[4].get_text().split()[0]
        number2 = data[0].find_all('span')[7].get_text().split()[0]
        email = data[0].find('a').get_text().split()[0]
        reception_days = data[1].find_all('li')[1].get_text(), data[1].find_all('li')[2].get_text()
        schedule = data[1].find_all('li')[3].get_text(), data[1].find_all('li')[4].get_text()
        lunch_break = data[1].find_all('li')[5].get_text()
        weekend = data[1].find_all('li')[6].get_text()
        ufk = " ".join(details.split()[3:14])
        inn = details.split()[16]
        kpp = details.split()[19]
        rc = details.split()[23]
        bik = details.split()[36]
        main_data = {'Мировой судья': judge, 'Помощник': assistant, 'Секретарь': secretary, 'Номер телефона':
            [number1, number2], 'email': email, 'Рабочие дни' : reception_days, 'График': schedule, 'Обед': lunch_break,
            'Выходные': weekend, 'УФК': ufk, 'ИНН': inn, 'КПП': kpp, 'Расчетный счет': rc, 'БИК': bik}
        return main_data
    return False


data = get_data(base_url, details_url)  # Помещаю результат выполнения функции в переменную


with open('data.json', 'w', encoding='utf-8') as write_file:  # Записываю результат в json файл
    json.dump(data, write_file, ensure_ascii=False)


#  В конечном счете я не очень понял задачу, если нужно было просто соскрапить данные со страницы то я это
#  сделал без труда, если нужно было написать код который сам себя проверял бы и был бы универсален для любой страницы
#  то я тоже способен сделать это! Просто наверно не очень понял задание..



