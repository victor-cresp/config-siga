from typing import Dict, List
import json

def criacaoJsonCaching(caminhoJson: str, paginasPerdidas: Dict):
    """
    Criação do arquivo JSON para armazenar as páginas que não foram processadas durante a
    extração dos dados da API do PNCP.

    Args: 

    paginasPerdidas: Páginas não processadas durante o processo de extração da API. 

    CaminhoJson: Caminho do arquivo Json que contém as páginas perdidas durante o processo de
    extração da API do PNCP.
    """
    with open(caminhoJson, 'w', encoding = 'utf-8') as f:
        json.dump(paginasPerdidas, f, ensure_ascii = False, indent = 2)

def recuperarPaginasPerdidas(caminhoJson: str) -> List[int]:
    """
    Abre o arquivo JSON que contém as páginas não processadas durantes o processo de extração de dados
    da API e recupera o total de páginas.

    Args:  

    CaminhoJson: Caminho do arquivo Json que contém as páginas perdidas durante o processo de
    extração da API do PNCP.

    Response:

    Lista de todos as páginas não processadas no processo de extração de dados da API.

    """
    with open(caminhoJson, 'r', encoding = 'utf-8') as f:
        conteudo = json.load(f)
        paginas_perdidas = conteudo["paginas_perdidas"]
        listaPaginaPerdidas = list(paginas_perdidas.values())
    return listaPaginaPerdidas