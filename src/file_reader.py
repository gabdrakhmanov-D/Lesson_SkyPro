import pandas as pd


def csv_file_reader(path_to_file: str) -> list:
    """Функция для считывания финансовых операций из CSV, принимает путь к файлу CSV в качестве аргумента.
    Возвращает список словарей с транзакциями."""

    csv_df = pd.read_csv(path_to_file, delimiter=';')
    return csv_df.to_dict('records')


def excel_file_reader(path_to_file: str) -> list:
    """Функция для считывания финансовых операций из Excel, принимает путь к файлу Excel в качестве аргумента.
    Возвращает список словарей с транзакциями."""

    excel_df = pd.read_excel(path_to_file)
    return excel_df.to_dict('records')
