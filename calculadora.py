"""
Módulo: calculadora.py
Descripción: Contiene funciones para calcular el área de un rectángulo
"""

def solicitar_datos():
    """
    Solicita al usuario su nombre, ancho y alto del rectángulo.
    Devuelve: nombre (str), ancho (float), alto (float)
    """
    nombre_usuario = input("Ingrese su nombre: ")
    try:
        ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))
        alto_rectangulo = float(input("Ingrese el alto del rectángulo: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        exit()
    return nombre_usuario, ancho_rectangulo, alto_rectangulo

def calcular_area(ancho, alto):
    """
    Calcula el área de un rectángulo.
    """
    return ancho * alto

def es_area_grande(area):
    """
    Devuelve True si el área es mayor a 50, False en caso contrario.
    """
    return area > 50

def mostrar_resultados(nombre, area, area_grande):
    """
    Muestra los resultados en pantalla.
    """
    print("\n--- RESULTADOS ---")
    print("Usuario:", nombre)
    print(f"Área del rectángulo: {area}")
    if area_grande:
        print("El rectángulo tiene un área grande.")
    else:
        print("El rectángulo tiene un área pequeña.")
