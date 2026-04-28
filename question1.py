"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

while True:
    try: 
        total_load = float(input())
        num_supports = int(input())
        load_per_support = total_load / num_supports
    except ValueError:
        print("Error: Por favor ingrese un número válido.")
    except ZeroDivisionError:
        print("Error: El número de puntos de soporte no puede ser cero.")
    else:
        print(f"Carga por punto de soporte: {load_per_support:.2f}")
        break
        