import time
from functools import wraps
from typing import Any, Callable


def log(filename: str = None) -> Callable[[Any], Callable[[tuple[Any, ...], dict[str, Any]], Any | None]]:
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
       а также ее результаты или возникшие ошибки. Принимает необязательный аргумент filename, который определяет,
       куда будут записываться логи (в файл или в консоль):"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.ctime()
            argument_func, kw_argument_func = args, kwargs
            function_name = func.__name__
            try:
                result = func(*args, **kwargs)
                end_time = time.ctime()
                if filename:
                    with open(f'{filename}.txt', 'w', encoding='utf-8') as file:
                        file.write(f'{function_name} -- {result}')
                    return result
                else:
                    print(f'{function_name} -- {result}')
                    return result
            except Exception as e:
                end_time = time.ctime()
                if filename:
                    with open(f'{filename}.txt', 'w', encoding='utf-8') as file:
                        file.write(f'В функции {function_name} произошла ошибка.\n'
                                   f'Входные аргументы:{argument_func if argument_func else ''}'
                                   f'{f', {kw_argument_func}' if kw_argument_func else ''}.\n'
                                   f'Начало выполнения функции: {start_time}.\n'
                                   f'Время ошибки {end_time}.\n'
                                   f'Сообщение ошибки: {e}')
                    return None
                else:
                    print(f'В функции {function_name} произошла ошибка.\n'
                          f'Входные аргументы:{argument_func if argument_func else ''}'
                          f'{f', {kw_argument_func}' if kw_argument_func else ''}.\n'
                          f'Начало выполнения функции: {start_time}.\n'
                          f'Время ошибки {end_time}.\n'
                          f'Сообщение ошибки: {e}')
                    return None
        return wrapper
    return decorator
