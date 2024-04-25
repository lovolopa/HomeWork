from src.widget import mask_for_card_or_account, data_split
from src.processing import filter_by_state, sort_by_date, datas


print(mask_for_card_or_account("Счет 64686473678894779589"))
print(mask_for_card_or_account("Visa Classic 6831982476737658"))
print(data_split("2018-07-11T02:26:18.671407"))


print(filter_by_state(datas))
print(sort_by_date(datas))
