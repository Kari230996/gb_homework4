# 4.4 - 4.5
import requests
from decimal import Decimal
import datetime as DT

date_str = "2021-11-13"
currency_date = DT.datetime.strptime(date_str, '%Y-%m-%d').date()  # конвертируем строку в дату


def currency_rates(val):
    val = val.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text  # используем библиотеку request и API

    if val not in response:
        return None

    find_currency = response.find(val)  # находим в строку название валюты
    cut_1 = response[find_currency::]  # срезаем

    start = cut_1.find('<Value>')
    cut_2 = cut_1[start:]

    end = cut_1.find('</Value>')
    cut_3 = cut_1[end:]

    cut_4 = cut_1[start:end]

    final_cut = cut_4[7::]

    # float_1 = float(final_cut.replace(',', '.').strip("'"))
    decimal_1 = Decimal(final_cut.replace(',', '.'))
    return f'Курс {val} на {currency_date} является {decimal_1} руб'










