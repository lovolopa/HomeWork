from masks import masck_for_account, mask_for_card


def mask_for_card_or_account(number_input: str) -> str:
    """
    Данная функция максирует у счета либо карты номер
    """
    num = number_input.split(" ")
    if num[0] == "Счет":
        return f"Счет {masck_for_account(num[-1])}"
    else:
        return f"{' '.join(num[:-1])} {mask_for_card(num[-1])}"


def data_split(data: str) -> str:
    """
    Эта функция разделяет дату по букве 'Т' а потом еще по '-' и вывводит дату через точку
    """
    split_data = data.split("T")
    day_month_year = split_data[0].split("-")
    return f"{day_month_year[2]}.{day_month_year[1]}.{day_month_year[0]}"


print(mask_for_card_or_account("Счет 64686473678894779589"))
print(mask_for_card_or_account("Visa Classic 6831982476737658"))
print(data_split("2018-07-11T02:26:18.671407"))
