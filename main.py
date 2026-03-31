from src.extrair_dados import extrair_dados
from src.tratar_dados import tratar_dados
from src.carregar_dados import carregar_dados

dados = extrair_dados()
dados_tratados = tratar_dados(dados)
carregar_dados(dados_tratados)

print("Pipeline executado com sucesso!")