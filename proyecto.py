import random

# Listas predefinidas de nombres y apellidos
nombres = ["Carlos", "Lucía", "Martín", "Sofía", "Fernando", "Valeria", "Javier", "Mariana"]
apellidos = ["Gómez", "Fernández", "López", "Martínez", "Pérez", "Sánchez", "Rodríguez", "Torres"]

def agregar_nombre():
    nombre = input("Ingrese un nuevo nombre (o presione Enter para omitir): ").strip()
    if nombre:
        nombres.append(nombre)
    
def agregar_apellido():
    apellido = input("Ingrese un nuevo apellido (o presione Enter para omitir): ").strip()
    if apellido:
        apellidos.append(apellido)

def generar_nombre():
    return f"{random.choice(nombres)} {random.choice(apellidos)}"

# Permitir al usuario agregar nombres y apellidos personalizados
print("Personalización de nombres y apellidos:")
agregar_nombre()
agregar_apellido()

# Generar y mostrar un nombre aleatorio
print("\nNombre aleatorio generado:")
print(generar_nombre())