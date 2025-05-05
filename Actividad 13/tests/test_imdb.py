"""
Casos de prueba para el mocking
"""

import os
import pytest
import sys

# # Agregar el directorio raíz al sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# from models import IMDb

# Paso 1: Probar búsqueda por título

@pytest.mark.skip(reason="FLAG FLAG FLAG")
def test_search_by_title():
    """Prueba de búsqueda por título"""
    imdb = IMDb("k_12345678")
    resultados = imdb.search_titles("Bambi")
    assert resultados is not None
    assert resultados.get("errorMessage") is None
    assert resultados.get("results") is not None
    assert resultados["results"][0]["id"] == "tt1375666"
