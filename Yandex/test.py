import datetime


class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def get_name_items(self):
        return self.__name_items

    @property
    def get_number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):

        try:
            self.__name_items.append(name)
            if len(name) == 0 or len(name) > 40:

        except ValueError:
            print('Нельзя добавить товар, если в его названии нет символов или их больше 40')
