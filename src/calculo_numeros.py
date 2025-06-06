
class NumeroDebeSerPositivo(Exception):
    """Excepción personalizada para números negativos."""
    pass

def ingrese_numero():
    """
    Solicita al usuario ingresar un número y valida que sea positivo.
    
    Returns:
        int: el número ingresado si es válido.
        
    Raises:
        ValueError: Si la entrada no es un número válido.
        NumeroDebeSerPositivo: Si el número ingresado es negativo.
    """
    entrada = input("Ingrese un número: ")
    try:
        numero = int(entrada)
        if numero < 0:
            raise NumeroDebeSerPositivo("El número debe ser positivo")
    except ValueError:
        raise ValueError("La entrada debe ser un número válido") 
    


    return numero
# from src.calculo_numeros import ingrese_numero
def main():
    """
    Programa principal que solicita números al usuario y muestra los resultados.
    """
    while True:
        try:
            numero = ingrese_numero()
            print(f"Número válido: {numero}")
        except ValueError as e:
            print(f"Error: {e}")
        except NumeroDebeSerPositivo as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nPrograma finalizado.")
            break

if __name__ == "__main__":
    main() 
