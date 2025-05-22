from main.caching import criacaoJsonCaching, recuperarPaginasPerdidas

import pytest

def test_paginasPerdidas():
    caminho_json = 'teste24224.json'
    dicionarioTeste = {
    "paginas_perdidas": {
        "1": 234,
        "2": 333,
        "3": 425
    }
}
    criacaoJsonCaching(caminho_json, dicionarioTeste)
    assert recuperarPaginasPerdidas(caminho_json) == [234, 333, 425]