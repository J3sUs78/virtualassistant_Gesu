import speech_recognition as sr
import pyttsx3 as psx3
import pywhatkit as pwtk

name = 'Gesu'

# Inicializar el reconocedor y el motor de voz
listener = sr.Recognizer()
engine = psx3.init()

# Configurar la voz de la computadora
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Convertir texto a voz
def talk(content):
    engine.say(content)
    engine.runAndWait()

# Escuchar la entrada del usuario
def listen():
    try:
        with sr.Microphone() as source:
            print('Hola, estoy escuchando lo que me dices...')
            pc = listener.listen(source)
            rec = listener.recognize_google(pc)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
    except:
        print('Error en reconocimiento')
    return rec

# Ejecutar la reproducción de música
def run_Asist():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproce', '')
        print('Reproduciendo Musiquita :3...' + music)
        talk('Reproduciendo...' + music)
        pwtk.playonyt(music)

# Realizar operaciones matemáticas
def perform_operation():
    rec = listen()
    if 'suma' in rec:
        numbers = rec.replace('suma', '')
        num_list = numbers.split()
        if len(num_list) == 2:
            try:
                num1 = int(num_list[0])
                num2 = int(num_list[1])
                result = num1 + num2
                print(f"La suma de {num1} y {num2} es: {result}")
                talk(f"La suma de {num1} y {num2} es: {result}")
            except ValueError:
                print("Error: Ingresa números válidos.")
                talk("Error: Ingresa números válidos.")
        else:
            print("Error: Ingresa dos números para realizar la suma.")
            talk("Error: Ingresa dos números para realizar la suma.")
    else:
        print("Error: No se reconoce la operación.")
        talk("Error: No se reconoce la operación.")

# Función principal
if __name__ == '__main__':
    op = 0
    while op != 3:
        print('Bienvenido al menú principal')
        talk('Bienvenido al menú principal')
        print('1. Ejecutar música')
        talk('Opción 1: Ejecutar música')
        print('2. Realizar operación matemática')
        talk('Opción 2: Realizar operación matemática')
        print('3. Salir')
        talk('Opción 3: Salir')
        op = int(input('Opción: '))
        if op == 1:
            run_Asist()
        elif op == 2:
            talk('Por favor, di la operación que deseas realizar.')
            perform_operation()
        elif op == 3:
            print('¡Hasta luego!')
            talk('¡Hasta luego!')
