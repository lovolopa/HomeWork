from src.masks import masck_for_account, mask_for_card


def mask_for_card_or_account(number_input: str) -> str:
    """
    Данная функция максирует у счета либо карты номер
    """
    num = number_input.split(" ")
    if num[0] == "Счет":
        return f"Счет {masck_for_account(num[-1])}"
    else:
        return f"{' '.join(num[:-1])} {mask_for_card(num[-1])}"


def convert_datetime_to_date(datetime_string: str) -> str:
    """Функция, которая принимает строку и возвращает строку с датой"""
    date_parts = datetime_string.split("T")[0].split("-")
    return f"{date_parts[2]}.{date_parts[1]}.{date_parts[0]}"
