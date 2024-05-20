from datetime import datetime
from typing import Any, Callable, Optional, Union


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор, который логирует вызов функции и ее результат
    """

    def decorator(func: Callable) -> Callable:
        """
        Внутренняя функция декоратора которая охватывает декорируемую функцию
        """

        def wrapper(*args: Any, **kwargs: Any) -> Union[str, Any]:
            """
            Выполняет логирование до и после вызова декорируемой функции
            """
            start = datetime.now()
            try:
                result = func(*args, **kwargs)
                status = "ok"
            except Exception as e:
                result = f"error: {type(e).__name__}"
                status = "error"
            end = datetime.now()
            log_message = f"{start} {func.__name__} {status} ({end - start}). Inputs: {args}, {kwargs}"
            if filename:
                with open(filename, "a") as f:
                    f.write(log_message + "\n")
            else:
                print(log_message)
            if status == "error":
                raise
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """
    Функция, которая складывает два числа(Пример)
    """
    return x + y
