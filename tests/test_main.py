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
        responses = iter(['3', 'EXECUTED', 'да', 'убыванию', 'да', 'да', 'счет'])
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