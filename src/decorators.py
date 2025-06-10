import time
from functools import wraps


def log(filename = None):
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
                        file.write(f'В функции {function_name} произошла ошибка.\nВходные аргументы:{argument_func if argument_func else ''}'
                                   f'{f', {kw_argument_func}' if kw_argument_func else ''}.\nНачало выполнения функции: {start_time}.\nВремя ошибки {end_time}.\nСообщение ошибки: {e}')
                    return None
                else:
                    return (f'В функции {function_name} произошла ошибка.\nВходные аргументы:{argument_func if argument_func else ''}'
                            f'{f', {kw_argument_func}' if kw_argument_func else ''}.\nНачало выполнения функции: {start_time}.\nВремя ошибки {end_time}.\nСообщение ошибки: {e}')
        return wrapper
    return decorator
