def mask_for_card(card_num: str) -> str:
    """
    mask_for_card данная функция принимает card_num и маскрует цифры с 7 по 12
    """
    return f"{card_num[0:4]} {card_num[5:7]}** **** {card_num[-4:]}"


def masck_for_account(mask_num: str) -> str:
    """
    masck_for_account данная функция принимает mask_num и шифрует две цифры с конца , а именно 5 И 6
    """
    return f"**{mask_num[-4:]}"
