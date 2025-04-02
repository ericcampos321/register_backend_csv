import csv

def load_csv_data(filepath: str):
    try:
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            data = [row for row in reader]
        return data
    except Exception as e:
        raise Exception(f"Erro ao carregar CSV: {str(e)}")