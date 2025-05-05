import json
import pytest
import os
import sys
from unittest.mock import patch, Mock

# Agregar el directorio raíz al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.imdb import IMDb

# Paso 1

# Fixture para cargar los datos de IMDb desde un archivo JSON
@pytest.fixture(scope="session")
def imdb_data():
    """Carga las respuestas de IMDb necesarias para las pruebas"""
    with open("tests/fixtures/imdb_responses.json") as json_data:
        return json.load(json_data)

# Paso 1
class TestIMDbDatabase:
    """Casos de prueba para la base de datos de IMDb"""

    @pytest.fixture(autouse=True)
    def setup_class(self, imdb_data):
        """Configuración inicial para cargar los datos de IMDb"""
        self.imdb_data = imdb_data

    ######################################################################
    #  Casos de prueba
    ######################################################################

# Paso 1
    @patch("test_imdb_patched.IMDb.search_titles")
    def test_search_by_title(self, imdb_mock):
        """Prueba de búsqueda por título"""
        imdb_mock.return_value = self.imdb_data["GOOD_SEARCH"]
        imdb = IMDb("k_12345678")
        resultados = imdb.search_titles("Bambi")
        print("FLAG->",resultados)
        assert resultados is not None
        assert resultados.get("errorMessage") is None
        assert resultados.get("results") is not None
        assert resultados["results"][0]["id"] == "tt1375666"
