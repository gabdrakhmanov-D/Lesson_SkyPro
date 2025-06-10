import os

from src.decorators import log


def test_log(capsys):
    @log()
    def test_func(a, b):
        return a / b

    test_func(5, 5)
    captured = capsys.readouterr()
    assert captured.out == "test_func -- 1.0\n"


def test_log_error(capsys):
    @log()
    def test_func(a, b):
        return a / b
    test_func(5, 0)
    captured = capsys.readouterr()
    for word in ["В функции test_func произошла ошибка.\n", "Входные аргументы:(5, 0).\n",
                 "Начало выполнения функции: ", "Время ошибки ", "Сообщение ошибки: division by zero"]:
        assert word in captured.out


def test_log_write_to_file(tmp_path):
    os.chdir(tmp_path)

    @log('test')
    def test_func(a, b):
        return a / b

    test_func(5, 5)
    file = open('test.txt', 'r', encoding='utf-8')
    result = file.read()
    assert result == "test_func -- 1.0"


def test_log_write_to_file_error(tmp_path):
    os.chdir(tmp_path)

    @log('test')
    def test_func(a, b):
        return a / b

    test_func(5, 0)
    with open('test.txt', 'r', encoding='utf-8') as file:
        result = file.read()

    for word in ["В функции test_func произошла ошибка.\n", "Входные аргументы:(5, 0).\n",
                 "Начало выполнения функции: ", "Время ошибки ", "Сообщение ошибки: division by zero"]:
        assert word in result
