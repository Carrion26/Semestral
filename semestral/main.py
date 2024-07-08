import module1
import module2
import prog3

def main():
    while True:
        print("\n \n 😄==== Menú ====😄")
        print("1. Ejecutar función de module1")
        print("2. Ejecutar función de module2")
        print("3. ejecutar el programa 3")
        print("q. Salir")
        choice = input("Elige una opción: ")
        print("\n")

        match choice:
            case "1":
                module1.sum_numbers()
            case "2":
                module2.rest_numbers()
            case "q":
                print("Saliendo...")
            case "3":
                prog3.sum_numbers()
                break
            case _:
                print("Opción no válida, intenta de nuevo.")
                

if __name__ == "__main__":
    main()
