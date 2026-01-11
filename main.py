"""
Archivo principal: main.py
Descripción: Ejecuta el programa de cálculo de área de un rectángulo
"""

from calculadora import solicitar_datos, calcular_area, es_area_grande, mostrar_resultados

def main():
    # Solicitar datos al usuario
    nombre, ancho, alto = solicitar_datos()
    
    # Calcular área
    area = calcular_area(ancho, alto)
    
    # Evaluar si el área es grande
    area_grande = es_area_grande(area)
    
    # Mostrar resultados
    mostrar_resultados(nombre, area, area_grande)

# Punto de entrada del programa
if __name__ == "__main__":
    main()
