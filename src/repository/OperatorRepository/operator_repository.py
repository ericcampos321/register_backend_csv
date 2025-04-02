from src.utils.csv_loader import read_csv_file


class OperatorRepository:
    def search_operator(self, search: str):
        if not search:
            raise Exception("Informe um termo para buscar.")
        try:
            operators = read_csv_file("operadoras.csv")

            # Filtra operadoras que contenham o termo
            filtered = [
                op for op in operators if search.lower() in op["Nome_Fantasia"].lower()
            ]

            # Ordena para quem começa com o termo aparecer primeiro
            filtered.sort(
                key=lambda op: (
                    not op["Nome_Fantasia"].lower().startswith(search.lower()),
                    op["Nome_Fantasia"],
                )
            )
            return filtered
        except Exception as e:
            raise Exception(f"Erro ao buscar operadores: {str(e)}")
