# tests/test_carrito.py

import pytest
from src.carrito import Carrito, Producto
from src.factories import ProductoFactory
def test_agregar_producto_nuevo(carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item con el producto y cantidad 1.
    """
    # Arrange
    # carrito = Carrito() #Ejercicio 5
    producto = ProductoFactory(nombre="Laptop", precio=1000.00)
    
    # Act
    carrito.agregar_producto(producto)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == "Laptop"
    assert items[0].cantidad == 1


def test_agregar_producto_existente_incrementa_cantidad(carrito, producto_generico_1):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se agrega el mismo producto nuevamente aumentando la cantidad.
    Assert: Se verifica que la cantidad del producto se incrementa en el item.
    """
    # Arrange
    # carrito = Carrito() # Ejercicio 5
    # producto = ProductoFactory(nombre="Mouse", precio=50.00)
    
    # Ejercicio 5
    carrito.agregar_producto(producto_generico_1, cantidad=1)
    
    # Act
    carrito.agregar_producto(producto_generico_1, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_remover_producto(carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con cantidad 3.
    Act: Se remueve una unidad del producto.
    Assert: Se verifica que la cantidad del producto se reduce a 2.
    """
    # Arrange
    # carrito = Carrito() # Ejercicio 5
    producto = ProductoFactory(nombre="Teclado", precio=75.00)
    carrito.agregar_producto(producto, cantidad=3)
    
    # Act
    carrito.remover_producto(producto, cantidad=1)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 2


def test_remover_producto_completo(carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se remueve la totalidad de la cantidad del producto.
    Assert: Se verifica que el producto es eliminado del carrito.
    """
    # Arrange
    # carrito = Carrito() # Ejercicio 5
    producto = ProductoFactory(nombre="Monitor", precio=300.00)
    carrito.agregar_producto(producto, cantidad=2)
    
    # Act
    carrito.remover_producto(producto, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_actualizar_cantidad_producto(carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 5.
    Assert: Se verifica que la cantidad se actualiza correctamente.
    """
    # Arrange
    # carrito = Carrito() # Ejercicio 5
    producto = ProductoFactory(nombre="Auriculares", precio=150.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act
    carrito.actualizar_cantidad(producto, nueva_cantidad=5)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 5


def test_actualizar_cantidad_a_cero_remueve_producto(carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 0.
    Assert: Se verifica que el producto se elimina del carrito.
    """
    # Arrange
    # carrito = Carrito() # Ejercicio 5
    producto = ProductoFactory(nombre="Cargador", precio=25.00)
    carrito.agregar_producto(producto, cantidad=3)
    
    # Act
    carrito.actualizar_cantidad(producto, nueva_cantidad=0)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_calcular_total(carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos con distintas cantidades.
    Act: Se calcula el total del carrito.
    Assert: Se verifica que el total es la suma correcta de cada item (precio * cantidad).
    """
    # Arrange
    # carrito = Carrito() # Ejercicio 5
    producto1 = ProductoFactory(nombre="Impresora", precio=200.00,stock=3)
    producto2 = ProductoFactory(nombre="Escáner", precio=150.00)
    carrito.agregar_producto(producto1, cantidad=2)  # Total 400
    carrito.agregar_producto(producto2, cantidad=1)  # Total 150
    
    # Act
    total = carrito.calcular_total()
    
    # Assert
    assert total == 550.00


def test_aplicar_descuento(carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con una cantidad determinada.
    Act: Se aplica un descuento del 10% al total.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    # carrito = Carrito() # Ejercicio 5
    producto = ProductoFactory(nombre="Tablet", precio=500.00)
    carrito.agregar_producto(producto, cantidad=2)  # Total 1000
    
    # Act
    total_con_descuento = carrito.aplicar_descuento(10)
    
    # Assert
    assert total_con_descuento == 900.00


def test_aplicar_descuento_limites(carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act y Assert: Se verifica que aplicar un descuento fuera del rango [0, 100] genere un error.
    """
    # Arrange
    # carrito = Carrito() # Ejercicio 5
    producto = ProductoFactory(nombre="Smartphone", precio=800.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act y Assert
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(150)
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(-5)
        
# Ejercicio 1
def test_vaciar_carrito(carrito):
    
    # Arrange
    # carrito = Carrito() # Ejercicio 5
    producto1 = ProductoFactory(nombre="Licuadora", precio=1350.00)
    producto2 = ProductoFactory(nombre="Tostadora", precio=650.00)
    producto3 = ProductoFactory(nombre="Television", precio=2215.00)
    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)
    carrito.agregar_producto(producto3)
    
    # Act
    carrito.vaciar()
    
    # Assert
    assert carrito.obtener_items() == []
    assert carrito.calcular_total() == 0
    
# Ejercicio 2
def test_decuento_condicional_exitoso(carrito):
    # Arrange
    # carrito = Carrito() # Ejercicio 5
    producto1 = ProductoFactory(nombre="Licuadora", precio=1350.00)
    producto2 = ProductoFactory(nombre="Tostadora", precio=650.00)
    producto3 = ProductoFactory(nombre="Television", precio=2215.00)
    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)
    carrito.agregar_producto(producto3)
    
    # Act
    minimo = 500
    descuento = 15
    total_a_pagar = carrito.aplicar_descuento_condicional(15, 500)
    # Assert
    assert total_a_pagar == 3582.75
    
def test_decuento_condicional_exitoso(carrito):
    
    # Arrange
    # carrito = Carrito() # Ejercicio 5
    producto1 = ProductoFactory(nombre="Licuadora", precio=50.00)
    producto2 = ProductoFactory(nombre="Tostadora", precio=150.00)
    producto3 = ProductoFactory(nombre="Television", precio=200.00)
    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)
    carrito.agregar_producto(producto3)
    
    # Act
    minimo = 500
    descuento = 15
    total_a_pagar = carrito.aplicar_descuento_condicional(15, 500)
    print("FLAG FLAG FLAG->",total_a_pagar)
    # Assert
    assert total_a_pagar != 340.00

# Ejercicio 3    
def test_agregar_producto_en_stock(carrito):
    # Arrange
    # carrito = Carrito() # Ejercicio 5
    producto = ProductoFactory(nombre="Licuadora", precio=50.00, stock=5)
    
    # Act
    carrito.agregar_producto(producto, 4)
    
    # Assert
    item = carrito.obtener_items().pop()
    assert item.cantidad == 4
    
def test_agregar_producto_no_en_stock(carrito):
    # Arrange
    # carrito = Carrito() # Ejercicio 5
    producto = ProductoFactory(nombre="Licuadora", precio=50.00, stock=5)
    
    # Act y Assert
    # with pytest.raises(ValueError):
    #     carrito.agregar_producto(producto, 6)
    
    # Act
    with pytest.raises(ValueError) as exc_info:
        carrito.agregar_producto(producto, 6)
    
    # Assert
    assert str(exc_info.value) == "No hay stock disponible"

# Ejercicio 4
def test_ordenar_lista_de_productos_criterio_definido(carrito):
    # Arrange
    # carrito = Carrito() # Ejercicio 5
    producto1 = ProductoFactory(nombre="Tostadora", precio=150.00)
    producto2 = ProductoFactory(nombre="Licuadora", precio=50.00)
    producto3 = ProductoFactory(nombre="Television", precio=200.00)
    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)
    carrito.agregar_producto(producto3)
    
    # Act
    
    list_byPrice = carrito.obtener_items_ordenados('precio')
    list_byName = carrito.obtener_items_ordenados('nombre')
    
    # Assert
    assert [item.producto.precio for item in list_byPrice] == [50.00,150.00,200.00]
    assert [item.producto.nombre for item in list_byName] == ['Licuadora','Television','Tostadora']
    
def test_ordenar_lista_de_productos_criterio_no_definido(carrito):
    # Arrange
    # carrito = Carrito() # Ejercicio 5
    producto1 = ProductoFactory(nombre="Tostadora", precio=150.00)
    producto2 = ProductoFactory(nombre="Licuadora", precio=50.00)
    producto3 = ProductoFactory(nombre="Television", precio=200.00)
    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)
    carrito.agregar_producto(producto3)
    
    # Act y Assert
    
    with pytest.raises(ValueError) as exc_info:
        list = carrito.obtener_items_ordenados('color')
    
    assert str(exc_info.value) == "Criterio no definido"
    
# Ejercicio 6

@pytest.mark.parametrize("porcentaje, total_esperado", [
    (0, 1000.0),
    (10, 900.0),
    (50, 500.0),
    (100, 0.0),
])
def test_aplicar_descuento_muchos_parametros(porcentaje,total_esperado):
    # Arrange
    carrito = Carrito()
    
    producto = ProductoFactory(nombre="Tablet", precio=1000.00)
    carrito.agregar_producto(producto) 
    
    # Act
    total_con_descuento = carrito.aplicar_descuento(porcentaje)
    
    # Assert
    assert total_con_descuento == total_esperado
    
@pytest.mark.parametrize("nueva_cantidad, espera_excepcion", [
    (3, False),      # válido
    (0, False),      # válido, debe eliminar el item
    (-1, True),      # inválido
])
def test_actualizar_cantidad_parametrizado(nueva_cantidad, espera_excepcion):
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Libro", precio=100, stock=2)
    carrito.agregar_producto(producto, cantidad=2)


    # Act y Assert
    if espera_excepcion:
        with pytest.raises(ValueError):
            carrito.actualizar_cantidad(producto, nueva_cantidad)
    else:
        carrito.actualizar_cantidad(producto, nueva_cantidad)
        items = carrito.obtener_items()
        if nueva_cantidad == 0:
            assert len(items) == 0
        else:
            assert carrito.obtener_items().pop().cantidad == nueva_cantidad
            
# Ejercicio 7
def test_calcular_impuestos_exitoso(carrito):
    
    # Arrange
    producto = ProductoFactory(nombre= "Producto", precio=250.00)
    carrito.agregar_producto(producto, cantidad=4) # Total = 1000
    
    # Act
    impuesto = carrito.calcular_impuestos(10) # 10% de 1000 = 100
    
    #Assert
    assert impuesto == 100.00
def test_calcular_impuestos_fallido(carrito):
    
    # Arrange
    producto = ProductoFactory(nombre= "Producto", precio=250.00)
    carrito.agregar_producto(producto, cantidad=2) # Total = 500
    
    
    # Act
    with pytest.raises(ValueError) as exc_info:
        carrito.calcular_impuestos(101)
    
    # Assert
    assert str(exc_info.value) == "El porcentaje debe estar entre 0 y 100"