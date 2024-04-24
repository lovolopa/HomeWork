from datetime import datetime

datas = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(data, state="EXECUTED"):
    """
    Данная функция фильтрует данные по статусу
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data, reverse=True):
    """
    Данная функция сортирует данные по дате
    """
    return sorted(data, key=lambda item: datetime.fromisoformat(item['date']), reverse=reverse)


print(filter_by_state(datas))
print(sort_by_date(datas))
