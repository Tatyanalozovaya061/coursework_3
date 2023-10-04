from src import utils


# def test_load_operations():
#     data = utils.load_operations('..\\operations.json')
#     assert isinstance(data, list)


def test_find_completed_operations(test_data):
    result = utils.find_completed_operations(test_data)
    # result = [x['state'] for x in result]
    assert [x['state'] for x in result] == ['EXECUTED', 'EXECUTED', 'EXECUTED', 'EXECUTED']


def test_sort_by_date(test_data):
    result = utils.sort_by_date(test_data)
    assert [x['date'] for x in result] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364', '2019-04-04T23:20:05.206878', '2018-06-30T02:08:58.425572', '2018-03-23T10:45:06.972075']


# def test_mask_the_score(test_data):
#     data = utils.mask_the_score(test_data)
#     print(data)
#     # pay = pay.split()
#     # pay = [x['from'] for x in pay]
#     # assert [x['from'] for x in pay] == '**6952'
#     # assert [x['from'] for x in pay] == '1596 83** **** 5199'


def test_get_formatted_data(test_data):
    data = utils.get_formatted_data(test_data)
    # print(data)
    assert data == ['\n26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n', '\n03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD\n', '\n30.06.2018 Перевод организации\nСчет **6952 -> Счет **6702\n9824.07 USD\n', '\n23.03.2018 Открытие вклада\n -> Счет **2431\n48223.05 руб.\n', '\n04.04.2019 Перевод со счета на счет\nСчет **8542 -> Счет **4188\n79114.93 USD\n']
