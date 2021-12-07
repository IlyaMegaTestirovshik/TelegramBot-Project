import requests
import json
from config import keys

class APIException (Exception):
    pass
class CurrencyConverter:
    @staticmethod
    def get_price(quote:str,base:str,amount:str):



        if quote == base:
            raise APIException (f'���������� ��������� ���������� ������ {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException (f'�� ������� ���������� ������ {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException (f'�� ������� ���������� ������ {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException (f'�� ������� ���������� ����������� {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        total_base=total_base*amount

        return total_base
