import json
import os


def load_operations(file_name):
    file_path = os.path.join('..', file_name)
    with open(file_path, 'r', encoding='utf8') as file:
        return json.load(file)


def operations_sort():
    operations = sorted(operations, key=operations, reverse=True)
    return operations


def filter_operations():
    operations = []
    for i in load_operations():
        if 'state' == 'EXECUTED':
            operations.append(i)
        else:
            continue
    return operations


def operations_pick():
    i = 0
    last_operations = []
    while i < 5:
        last_operations.append(filter_operations())
        i += 1


def date_form(date):
    date = date.split('T')[0].split('-')
    return f'{2}.{1}.{0}'


def mask_card(card_dt):
    card_dt = card_dt.split(" ")
    return f'{card_dt[-1][:4]}{card_dt[-1][4:6], "** **** ", {card_dt[-1][:-14]}}'


def mask_bill(bill_dt):
    bill_dt = bill_dt.split
    return f'**{bill_dt[-1][-5:]}'
