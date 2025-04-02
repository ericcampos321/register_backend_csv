from pydantic import BaseModel

class OperatorSchema(BaseModel):
    reg_ans: str
    cnpj_operadora: str
    nome_operadora: str
    modalidade: str

    class Config:
        orm_mode = True
