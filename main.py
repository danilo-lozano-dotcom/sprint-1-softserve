import re # Importación de la librería re para trabajar con expresiones regulares

# Listas para almacenar correos electrónicos de estudiantes y docentes. Se inicializan vacías:
estudiantes = []
docentes = []

formato_correo = r'^[\w\.-]+@[\w\.-]+\.\w+$' # Expresión regular para validar el formato del correo electrónico


# Función para registar un correo electrónico en la lista de estudiantes o docentes:
def registrar_correo():
    while True:
        correo = input("\nIngresa el correo electrónico: ").strip().lower()
        print(f"\nCorreo ingresado: {correo}")
        
        if re.match(formato_correo, correo):
            if correo in estudiantes or correo in docentes:
                print("¡Advertencia! El correo ya está registrado.")
                break
            
            if correo.endswith('@estudiante.utv.edu.co'):
                estudiantes.append(correo)
                print("¡Correo registrado como estudiante!")
                break
            
            elif correo.endswith('@utv.edu.co'):
                docentes.append(correo)
                print("¡Correo registrado como docente!")
                break
            
            else:
                print("¡Advertencia! El correo no pertenece a ningún estudiante o docente.")
                break
        else:
            print("¡Advertencia! El formato del correo es inválido.")
            break
            
    while True:
        print("\n" + "*" * 29)
        print("1. Registrar un correo nuevo")
        print("2. Regresar al menú principal")
        print("3. Salir")
        print("-" * 29)
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            break 
        elif opcion == "2":
            return  # Regresa al menú principal (termina la función)
        elif opcion == "3":
            print("Saliendo de la aplicación...")
            exit()  # Termina el programa
        else:
            print("Opción no válida. Intente nuevamente.")


# Función ver la lista de correos electrónicos registrados de estudiantes y docentes:
def ver_correos():
    while True:
        print("\nCorreos de estudiantes:")
        for correo in estudiantes:
            print(f" - {correo}")
        
        print("\nCorreos de docentes:")
        for correo in docentes:
            print(f" - {correo}")
            
        if not regresar_o_salir():
            break
  
        
# Función para buscar un correo electrónico en la lista de estudiantes o docentes:
def buscar_correo():
    while True:
        correo_buscar = input("\nIngresa parte o la totalidad del correo a buscar: ").strip().lower()
        coincidencias = []
        
        for n in estudiantes:
            if correo_buscar in n:
                coincidencias.append(n)
                
        for n in docentes:
            if correo_buscar in n:
                coincidencias.append(n)
        
        if coincidencias:
            print("\nCoincidencias encontradas:")
            for c in coincidencias:
                print(f" - {c}")
        else:
            print("\nNo se encontraron coincidencias.")
            
        if not regresar_o_salir():
                break
        

# Función para regresar al menú principal o salir del programa:        
def regresar_o_salir():
    while True:
        print("\n" + "*" * 29)
        print("1. Regresar al menú principal")
        print("2. Salir")
        print("-" * 29)
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            return False
        elif opcion == "2":
            print("Saliendo de la aplicación...")
            exit()
        else:
            print("Opción no válida. Intenta nuevamente.")

        
# Función para mostrar el menú de opciones:       
def menu():
    
    while True:
        print("\n" + "*" * 50)
        print("*{:^48}*".format("VALIDADOR Y GESTOR DE CORREOS ELECTRÓNICOS"))
        print("*" * 50)
        print("\n---------------- Menú de Opciones ----------------")
        print("\n1. Registrar nuevo correo electrónico")
        print("2. Ver correos registrados")
        print("3. Buscar correo específico")
        print("4. Salir")
        print("*" * 50)
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            registrar_correo()
        elif opcion == '2':
            ver_correos()
        elif opcion == '3':
            buscar_correo()
        elif opcion == '4':
            print("Saliendo de la aplicación...")
            break
        else:
            print("\nOpción inválida. Intenta nuevamente.")

# Punto de entrada del programa (función principal menu()):
if __name__ == "__main__":
    menu()
    
## Ejemplos de correos:
    # Estudiantes: juan.ruiz@estudiante.utv.edu.co, juan.perez@estudiante.utv.edu.co, ana.lopez@estudiante.utv.edu.co
    # Docentes: pedro.perez@utv.edu.co, pablo.lopez@utv.edu.co, luis.casas@utv.edu.co, juan.casas1@utv.edu.co
