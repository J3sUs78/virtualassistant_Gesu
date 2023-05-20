import speech_recognition as sr
import pyttsx3 as psx3
import pywhatkit as pwtk
from pygame import mixer
import wikipedia as wk
import datetime as dt
import keyboard as kb
import time
import os

# Name assistant
name = 'ronson'

# Inicializar el reconocedor y el motor de voz
listener = sr.Recognizer()
engine = psx3.init()

# Configurar la voz de la computadora
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# Configurar volumen
engine.setProperty('volume', 0.8)
# Configurar velocidad
engine.setProperty('rate', 180)
# Configurar tono
engine.setProperty('pitch', 1.3)

# Convertir texto a voz


def talk(content):
    engine.say(content)
    engine.runAndWait()

# Escuchar la entrada del usuario


def listen():
    try:
        with sr.Microphone() as source:
            talk('Escuchando')
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
    except:
        print('Error en reconocimiento')
    return rec

# Ejecutar la reproducción de música


def run_Asist():
    
    while True:
        rec = listen()
        
        if rec == 'duerme':
            break
        
        if 'reproduce' in rec:
            
            music = rec.replace('reproduce', '')
            
            talk('Reproduciendo su Peticion mister...' + music)
            
            pwtk.playonyt(music)
            
        elif 'busca' in rec:
            search = rec.replace('busca', '')
            wk.set_lang("es")
            wiki = wk.summary(search, 1)
            print(search + " : " + wiki)
            talk(wiki)
        elif 'suma' in rec:
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
        elif 'alarma' in rec:
            hour = rec.replace('alarma', '')
            hour = hour.strip()
            print("Alarma configurada a las " + hour + " horas")
            talk("Alarma configurada a las " + hour + " horas")
            set_alarm(hour)

                


def calculate_probability():

    # Ejemplo de cálculo de probabilidad de obtener al menos un número par al lanzar un dado
    total_outcomes = 10  # Total de resultados posibles al lanzar un dado
    desired_outcomes = 5  # Número de resultados deseados (números pares)

    # Calcula la probabilidad del suceso deseado
    probability_desired = desired_outcomes / total_outcomes

    # Calcula la probabilidad del suceso contrario
    probability_complement = 1 - probability_desired
    return probability_complement

def set_alarm(hour):
    talk("Alarma activada a las " + hour + " horas")
    while True:
        current_time = dt.datetime.now().strftime('%H:%M')
        if current_time == hour:
            print("¡DESPIERTA!")
            mixer.init()
            mixer.music.load("alarmsound.mp3")
            mixer.music.play()
        elif current_time > hour:
            break


# Función principal
if __name__ == '__main__':
    op = 0
    while op != 6:
        talk('Bienvenido al menú principal')
        print('Bienvenido al menú principal')
        print('1. Ejecutar música')
        print('2. Realizar operación matemática')
        print('3. Buscar Info.')
        print('4. Activar Alarma.')
        print('5. Sacar Probabilidad')
        print('6. salir')
        op = int(input('Opción: '))
        

        if op in [1, 2, 3, 4]:
            run_Asist()
        elif op == 5:
            probability = calculate_probability()
            print("La probabilidad de obtener al menos un número par es:", probability)
        elif op == 6:
            talk('Gracias por tu visita nos vemos...')
            break
