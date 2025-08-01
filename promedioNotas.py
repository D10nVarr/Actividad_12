try:
    cant_estudiantes=int(input("Ingrese la cantidad de estudiantes: "))
    estudiantes={}

    for i in range(cant_estudiantes):
        notas=[]
        carnet=input(f"Ingrese el carnet carnet del estudiante {i+1}: ")
        nombre=input(f"Ingrese el nombre del estudiante {i+1}: ")
        cant_notas=int(input("Ingrese la cantidad de notas: "))
        for j in range(cant_notas):
            nota=int(input(f"Ingrese el nota del nota {j+1}:"))
            notas.append(nota)

        estudiantes[carnet]={
            "Nombre": nombre,
            "Promedio": sum(notas)/cant_notas,
        }
except ValueError:
    print("El valor ingresado no corresponde al formato requerido")

except TypeError:
    print("Operación no válida entre formatos de datos ingresados")

except ZeroDivisionError:
    print("La división del promedio presente un error por división con 0")
except Exception as e:
    print(f"Error inesperado {e}")

else:
    for carnet, notas in estudiantes.items():
        print(f"\nEl estudiante {notas['Nombre']} tiene {notas['Promedio']} de promedio")