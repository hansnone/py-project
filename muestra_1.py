def calculadora(num1, num2, operador):
  """
  Función que realiza operaciones matemáticas básicas.

  Args:
    num1: Primer número (float).
    num2: Segundo número (float).
    operador: Operación a realizar (+, -, *, /).

  Returns:
    Resultado de la operación (float).
  """

  if operador == "+":
    return num1 + num2
  elif operador == "-":
    return num1 - num2
  elif operador == "*":
    return num1 * num2
  elif operador == "/":
    if num2 == 0:
      raise ZeroDivisionError("No se puede dividir por cero")
    return num1 / num2
  else:
    raise ValueError("Operador no válido")

# Ejemplo de uso
try:
  resultado = calculadora(10, 0, "+")
  print(f"10 + 5 = {resultado}")

  resultado = calculadora(10, 0, "-")
  print(f"10 - 5 = {resultado}")

  resultado = calculadora(10, 0, "*")
  print(f"10 * 5 = {resultado}")

  resultado = calculadora(10, 0, "/")
  print(f"10 / 5 = {resultado}")

except ZeroDivisionError:
  print("Error: No se puede dividir por cero")
except ValueError:
  print("Error: Operador no válido")