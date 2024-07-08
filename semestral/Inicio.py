import prog1
import prog2
import prog3
import prog4
import prog5
import prog6
import prog7
import prog8
import prog9
import prog10
import prog11
import prog12
import prog13
import prog14
import prog15
import prog16
import prog17
import prog18
import prog19
import prog20
import prog21
import prog22
import prog23
import prog24
import prog25
import prog26
import prog27
import prog28
import prog29
import prog30
import prog31
import prog32
import prog33
import prog34
import prog35
import prog36
import prog37
import prog38
import prog39
import prog40
import prog41
import prog42
import prog43
import prog44
import prog45

def main():
    while True:
        print("\n \n 😄==== Menú ====😄")
        print("1. Ejecutar  while Suma de numeros")
        print("2. Ejecutar while Sumar numeros hasta un limite")
        print("3. Ejecutar while contar hasta un numero dado")
        print("4. Ejecutar while sumar digitos de un numero")
        print("5. Ejecutar while adivinar un numero")
        print("6. Ejecutar while Mostrar multiplos de un numero")
        print("7. Ejecutar while validar entrada")
        print("8. Ejecutar while Contador de digitos")
        print("9. Ejecutar while Convertir de decimal a binario")
        print("10. Ejecutar while Simular un cajero automatico")
        print("11. Ejecutar for tabla de multiplicar")
        print("12. Ejecutar for sumar numeros pares del 1 al 100")
        print("13. Ejecutar for contar vocales en una cadena")
        print("14. Ejecutar for Imprimir una serie de numeros")
        print("15. Ejecutar for imprimir numeros impares hasta el numero dado")
        print("16. Ejecutar for sumar los primeros N numeros naturales")
        print("17. Ejecutar for determinar si un numero es primo")
        print("18. Ejecutar for convertir grados Celsius a Fahrenheit")
        print("19. Ejecutar for dibujar un triangulo de asteriocos")
        print("20. Ejecutar for repetir una cadena")
        print("21. Ejecutar Calcular el precio con descuento")
        print("22. Ejecutar Calcular el salario neto")
        print("23. Ejecutar  Calcular la tarifa de un taxi")
        print("24. Ejecutar  Clasificar el IMC")
        print("25. Ejecutar  Clasificar la categoría de edad")
        print("26. Ejecutar  Comparar dos números")
        print("27. Ejecutar  Determinar el tipo de licencia de conducir")
        print("28. Ejecutar Determinar la categoría de un trabajador")
        print("29. Ejecutar  Determinar si un año es un siglo")
        print("30. Ejecutar Determinar si un carácter es una letra o un dígito")
        print("31. Ejecutar Determinar si un carácter es una vocal")
        print("32. Ejecutar Determinar si un número es divisible por 3 y 5")
        print("33. Ejecutar Determinar si un número es primo")
        print("34. Ejecutar Determinar si una persona es adolescente")
        print("35. Ejecutar Verificar si un nombre es corto, mediano o largo")
        print("36. Ejecutar Verificar si un número es múltiplo de 5")
        print("37. Ejecutar Verificar si un número es positivo, negativo o cero")
        print("38. Ejecutar Verificar si un número está en un rango")
        print("39. Ejecutar Verificar si un triángulo es válido")
        print("40. Ejecutar Verificar si una palabra tiene más de 5 letras")
        print("41. Ejecutar Sacar radio y altura de un circulo")
        print("42. Ejecutar Encontrar la hipotenuza")
        print("43. Ejecutar Encontrar area y perimetro")
        print("44. Ejecutar Calculadoraa de Descuento")
        print("45. Ejecutar Calculadoraa de Salario")
         

        print("s. Salir")
        choice = input("Elige una opción: ")
        print("\n")

        match choice:
            case "1":
                prog1.sum_numbers()
            case "2":
                prog2.rest_numbers()
            case "3":
                prog3.sum_numbers()
            case "4":
                prog4.sum_numbers()
            case "5":
                prog5.sum_numbers()
            case "6":
                prog6.sum_numbers()
            case "7":
                prog7.sum_numbers()
            case "8":
                prog8.sum_numbers()
            case "9":
                prog9.sum_numbers()
            case "10":
                prog10.sum_numbers()
            case "11":
                prog11.sum_numbers()
            case "12":
                prog12.sum_numbers()
            case "13":
                prog13.sum_numbers()
            case "14":
                prog14.sum_numbers()
            case "15":
                prog15.sum_numbers()
            case "16":
                prog16.sum_numbers()
            case "17":
                prog17.sum_numbers()
            case "18":
                prog18.sum_numbers()
            case "19":
                prog19.sum_numbers()
            case "20":
                prog20.sum_numbers()
            case "21":
                prog21.sum_numbers()
            case "22":
                prog22.sum_numbers()
            case "23":
                prog23.sum_numbers()
            case "24":
                prog24.sum_numbers()
            case "25":
                prog25.sum_numbers()
            case "26":
                prog26.sum_numbers()
            case "27":
                prog27.sum_numbers()
            case "28":
                prog28.sum_numbers()
            case "29":
                prog29.sum_numbers()
            case "30":
                prog30.sum_numbers()
            case "31":
                prog31.sum_numbers()
            case "32":
                prog32.sum_numbers()
            case "33":
                prog33.sum_numbers()
            case "34":
                prog34.sum_numbers()
            case "35":
                prog35.sum_numbers()
            case "36":
                prog36.sum_numbers()
            case "37":
                prog37.sum_numbers()
            case "38":
                prog38.sum_numbers()
            case "39":
                prog39.sum_numbers()
            case "40":
                prog40.sum_numbers()
            case "41":
                prog41.sum_numbers()
            case "42":
                prog42.sum_numbers()
            case "43":
                prog43.sum_numbers()
            case "44":
                prog44.sum_numbers()
            case "45":
                prog45.sum_numbers()
            
            
            case "s":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida, intenta de nuevo.")
                

if __name__ == "__main__":
    main()
