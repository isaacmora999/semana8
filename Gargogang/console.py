import speech_recognition as sr

def escuchar_comando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Habla ahora (por ejemplo, 'uno', 'dos', 'tres', 'salir')...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        comando = r.recognize_google(audio, language='es-ES')
        print(f"Comando reconocido: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        print("No entendí lo que dijiste.")
    except sr.RequestError:
        print("Error al conectarse al servicio de reconocimiento.")
    return ""

def menu():
    while True:
        tipo_entrada = input("¿Quieres usar voz o teclado? (voz/teclado): ").strip().lower()

        if tipo_entrada not in ["voz", "teclado"]:
            print("Opción inválida. Intente de nuevo.")
            continue

        print("\n--- Menú ---")
        print("1. Agregar caso")
        print("2. Mostrar casos")
        print("3. Eliminar último caso")
        print("4. Salir")

        if tipo_entrada == "voz":
            comando = escuchar_comando()
            if "uno" in comando:
                opcion = "1"
            elif "dos" in comando:
                opcion = "2"
            elif "tres" in comando:
                opcion = "3"
            elif "cuatro" in comando or "salir" in comando:
                opcion = "4"
            else:
                print("Comando no reconocido.")
                continue
        else:
            opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ciudadano = input("Ingrese el nombre del ciudadano: ")
            caso = input("Describa el caso: ")
            guardar_caso(ciudadano, caso)
        elif opcion == "2":
            casos = obtener_casos()
            if casos:
                for i, c in enumerate(casos, start=1):
                    print(f"{i}. {c['ciudadano']}: {c['caso']}")
            else:
                print("No hay casos registrados.")
        elif opcion == "3":
            eliminar_ultimo_caso()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
