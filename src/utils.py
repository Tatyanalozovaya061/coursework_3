import json
from datetime import datetime


def load_operations(filename):
    """
    Загружается информация из json файла
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def find_completed_operations(data):
    """
    Выводятся выполненные операции
    """
    completed_data = []
    for pay in data:
        if pay.get('state') == 'EXECUTED':
            completed_data.append(pay)
    return completed_data


def sort_by_date(data):
    """
    Выводятся последние 5 транзакций, отсортированных по дате
    """
    data = sorted(data, key=lambda a: a['date'], reverse=True)
    return data[:5]


def formatted_date(data):
    """
    Форматирование даты
    """
    date = datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    return date


def mask_the_score(pay):
    """
    Маскирование счета
    """
    pay = pay.split()
    score = pay.pop()
    if len(score) == 20:
        score = f"**{score[-4:]}"
    else:
        score = f"{score[:4]} {score[4:6]}** **** {score[-4:]}"
    pay.append(score)
    return ' '.join(pay)


def get_formatted_data(data):
    formatted_data = []
    for pay in data:
        date = formatted_date(pay['date'])
        content = pay['description']
        to = mask_the_score(pay['to'])
        if 'from' in pay:
            from_score = mask_the_score(pay['from'])
        else:
            from_score = ''
        amount = f"{pay['operationAmount']['amount']} {pay['operationAmount']['currency']['name']}"
        formatted_data.append(f'''
{date} {content}
{from_score} -> {to}
{amount}
''')
    return formatted_data



