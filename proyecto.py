import random

def generarNombre(names, surnames):
    nombre= random.choice(names)
    apellido= random.choice(surnames)
    return f"{nombre} {apellido}"

def añadirNombre(lista,tipo):
    new = input(f"agregar un nuevo {tipo} para agregar: ").strip()
    if new:
      lista.append(new)
    print(f"{type.catalize()} añadido correctamente\n")
    print("acceso no valido. \n")

def main():
    names= ["Sofia", "Flor", "Rebeca", "Dinora", "Diana", "Natalia", "Marisol"]
    surnames=["Martinez", "Miranda", "Moran", "Hernandez", "Gonzales", "Santos","Mejia"]
    while True:
        print("\n Menu:")
        print("1- Generar nombre aleatorio")
        print("2- Añadir nombre personalizado")
        print("3- Añadir apellido personalizado")
        print("4- Exit")

        option = input("Choose a option: ")
        if option == "1":
            print(f"Nombre generado: {generarNombre(names, surnames)}\n")
        elif option == "2":
            añadirNombre(names, "nombre")
        elif option == "3":
            añadirNombre(surnames, "apellido")
        elif option == "4":
            print("Saliedno del programa...")
            break
        else:
            print("opcion incorrecta. Por favor intente de nuevo.\n")