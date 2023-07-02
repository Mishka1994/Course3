def get_date_operation(operation):
    """
        Функция возвращает дату выполнения операции в формате: число.месяц.год
        :param operation:
        :return: дату проведения операции
        """
    date = operation['date'].split('T')[0]
    date = date.split('-')[::-1]
    return '.'.join(date)


def get_description_operation(operation):
    """
        Функция возвращает описание к операции.
        :param operation: Словарь с данными.
        :return: Описание операции.
        """
    return operation['description']


def get_name_and_number_product_from(operation):
    """
    Функция возвращает название продукта и его зашифрованный номер.
    :param operation: Словарь с данными.
    :return: Название продукта и зашифрованный номер.
    """
    # Получаем название продукта
    name_product = operation['from'].split(' ')[:-1]
    name_product =''.join(name_product)
    # Получаем номер продукта
    number_product = operation['from'].split(' ')[-1]
    # В соответствии с названием продукта скрываем часть его номера.
    if name_product == 'Счет':
        number_product = f'**{number_product[-4:]}'
    else:
        number_product = f'{number_product[0:4]} {number_product[4:6]}** **** {number_product[-4:]}'
    return name_product, number_product


def get_name_and_number_product_to(operation):
    """
    Функция возвращает название продукта, куда были переведены средства,
    а также его зашифрованный номер.
    :param operation: Словарь с данными.
    :return: Возвращает название продукта и его зашифрованный номер.
    """
    # Получаем имя продукта
    name_product = operation['to'].split(' ')[:-1]
    name_product = ''.join(name_product)
    # Получаем номер продукта
    number_product = operation['to'].split(' ')[-1]
    # В соответствии с названием продукта скрываем часть его номера.
    if name_product == 'Счет':
        number_product = f'**{number_product[-4:]}'
    else:
        number_product = f'{number_product[0:4]} {number_product[4:6]}** **** {number_product[-4:]}'
    return name_product, number_product


def get_amount_operation(operation):
    """
    Функция возвращает кол-во средств, переведенных в операции.
    """
    amount = operation['operationAmount']['amount']
    return amount


def get_currency_operation(operation):
    """
    Функция возвращает название валюты
    """
    currency = operation['operationAmount']['currency']['name']
    return currency
