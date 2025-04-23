import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory

@pytest.fixture
def carrito():
    return Carrito()    

@pytest.fixture
def producto_generico():
    return ProductoFactory()

@pytest.fixture
def producto_generico_1():
    return ProductoFactory(nombre="Generico", precio=100.0)

