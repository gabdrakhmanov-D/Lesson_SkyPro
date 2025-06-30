import io
from unittest.mock import patch, Mock, MagicMock
from main import main


def test_main_json(monkeypatch, examples_for_generators, answer_json_executed):
    """Тест успешного выполнения программы с файлом json"""
    captured_output = io.StringIO()
    with (patch('sys.stdout', new=captured_output),
        patch('main.get_dict_transactions') as mock_get):
        mock_get.return_value = examples_for_generators
        responses = iter(['1', 'EXECUTED', 'да', 'убыванию', 'да', 'да', 'счет'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        main()
        assert captured_output.getvalue() == answer_json_executed


def test_main_csv(monkeypatch, example_csv_and_xlsx, answer_csv_executed):
    """Тест успешного выполнения программы с файлом csv"""
    captured_output = io.StringIO()
    with (patch('sys.stdout', new=captured_output),
          patch('main.csv_file_reader') as mock_get):

        mock_get.return_value = example_csv_and_xlsx
        responses = iter(['2', 'EXECUTED', 'да', 'убыванию', 'да', 'да', 'счет'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        main()
        assert captured_output.getvalue() == answer_csv_executed


def test_main_xlsx(monkeypatch, example_csv_and_xlsx, answer_xlsx_executed):
    """Тест успешного выполнения программы с файлом xlsx"""
    captured_output = io.StringIO()
    with (patch('sys.stdout', new=captured_output),
          patch('main.excel_file_reader') as mock_get):

        mock_get.return_value = example_csv_and_xlsx
        responses = iter(['3', 'EXECUTED', 'да', 'возрастанию', 'да', 'да', 'счет'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        main()
        assert captured_output.getvalue() == answer_xlsx_executed


def test_main_no_match(monkeypatch, examples_for_generators, answer_no_match):
    """Тест случая отсутствия совпадений"""
    captured_output = io.StringIO()
    with (patch('sys.stdout', new=captured_output),
          patch('main.get_dict_transactions') as mock_get):
        mock_get.return_value = examples_for_generators
        responses = iter(['1', 'pending', 'да', 'убыванию', 'да', 'да', 'счет'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        main()
        assert captured_output.getvalue() == answer_no_match


def test_main_json_wrong_input(monkeypatch, examples_for_generators, incorrect_input_words):
    """Тест успешного выполнения программы с файлом json, но некорректными вводными параметрами"""
    captured_output = io.StringIO()
    with (patch('sys.stdout', new=captured_output),
          patch('main.get_dict_transactions') as mock_get):
        mock_get.return_value = examples_for_generators
        responses = iter(['1', 'EXECUTED','д', 'да', 'у', 'убыванию', 'да', 'д', 'да', 'счет'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        main()
        assert captured_output.getvalue() == incorrect_input_words


def test_xlsx_wrong_input(monkeypatch, example_csv_and_xlsx, high_sort_xlsx):
    """Тест успешного выполнения программы с файлом xlsx и некорректными вводными параметрами"""
    captured_output = io.StringIO()
    with (patch('sys.stdout', new=captured_output),
          patch('main.excel_file_reader') as mock_get):

        mock_get.return_value = example_csv_and_xlsx
        responses = iter(['5', '3', 'XECU','EXECUTED','д', 'нет', 'фы', 'нет', 'нет'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        main()
        assert captured_output.getvalue() == high_sort_xlsx
