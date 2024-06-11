from src.logger import logger_setup

logger = logger_setup()


def mask_for_card(card_num: str) -> str:
    """
    mask_for_card данная функция принимает card_num и маскрует цифры с 7 по 12
    """
    if len(card_num) == 16:
        logger.info("Функция mask_for_card работает успешно")
        return f"{card_num[0:4]} {card_num[5:7]}** **** {card_num[-4:]}"
    else:
        logger.error("С функция mask_for_card что-то не так")
    return card_num


def masck_for_account(mask_num: str) -> str:
    """
    masck_for_account данная функция принимает mask_num и шифрует две цифры с конца , а именно 5 И 6
    """
    if len(mask_num) == 21:
        logger.info("Функция masck_for_account работает успешно")
        return f"**{mask_num[-4:]}"
    else:
        logger.error("С функцей masck_for_account что-то не так")
    return mask_num


# Проверка
mask_for_card("1234567890123456")
masck_for_account("123456789012345678901")
