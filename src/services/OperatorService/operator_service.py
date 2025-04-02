from src.utils.csv_loader import load_csv_data

class OperatorService:
    def __init__(self):
        self.data = load_csv_data('operadoras.csv')  # Caminho do seu CSV

    def search_operator(self, search: str):
        try:
            if not search:
                return {"message": "Informe um termo para buscar."}

            filtered = [
                row for row in self.data
                if search.lower() in row['Nome_Fantasia'].lower()
            ]

            return filtered or {"message": "Nenhum resultado encontrado."}
        except Exception as e:
            raise Exception(f"Erro ao buscar operador: {str(e)}")