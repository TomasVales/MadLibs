import random
import threading
from playsound import playsound  # Para efectos de sonido
from time import sleep
import pygame


# Función para generar palabras aleatorias
def palabra_aleatoria(tipo):
    opciones = {
        "sustantivo": ["dragón", "queso", "cactus", "platillo volador", "pingüino", "terrorista", "phoenix", "jett", "zombie"],
        "sustantivo_plural": ["gatos", "sombreros", "zombies", "estrellas", "unicornios"],
        "lugar": ["bosque encantado", "marte", "la playa", "el castillo", "el espacio"],
        "adjetivo": ["brillante", "espeluznante", "gigante", "pegajoso", "misterioso"],
        "verbo": ["corrió", "saltó", "lanzó", "voló", "escondió"],
        "celebridad": ["Taylor Swift", "Elon Musk", "Tom Cruise", "Shakira", "Messi"],
        "onomatopeya": ["boom", "crash", "bang", "wham", "splat"],
        "color": ["rojo", "azul", "verde", "amarillo", "morado"],
        "nombre":["hugo","luis","joaquin","tatiana","agustina","katarina"]
    }
    return random.choice(opciones[tipo])



def reproducir_sonido(archivo):
    try:
        pygame.mixer.init()
        pygame.mixer.Sound(archivo).play()
    except Exception as e:
        print(f"Error al reproducir sonido: {e}")


# Animación de emojis
def mostrar_animacion_final():
    animacion = ["✨", "🎉", "🔥", "💥", "⭐", "🌟"]
    for emoji in animacion:
        print(f"{emoji} ", end="", flush=True)
        sleep(0.5)
    print("\n")

# Menú de temas
def seleccionar_tema():
    print("¡Elige un tema para tu historia!")
    print("1. Valorant")
    print("2. DayZ")
    print("3. Counter Strike")
    print("4. League of Legends")
    tema = input("Selecciona el número del tema que prefieras: ")
    if tema == "1":
        return "Valorant"
    elif tema == "2":
        return "DayZ"
    elif tema == "3":
        return "Counter-Strike"
    elif tema == "4":
        return "League of Legends"
    else:
        print("Opción no válida. Tema por defecto: Valorant.")
        return "Valorant"

# Preguntar con temporizador
def preguntar_con_tiempo(pregunta, tipo, tiempo_limite):
    respuesta = [None]

    def capturar_respuesta():
        respuesta[0] = input(pregunta)

    hilo = threading.Thread(target=capturar_respuesta)
    hilo.start()
    hilo.join(timeout=tiempo_limite)
    
    if respuesta[0] is None:
        print("⏳ ¡Tiempo agotado! Se usará una palabra aleatoria.")
        return palabra_aleatoria(tipo)
    else:
        return respuesta[0]

# Historias para cada tema
historias_por_tema = {  
    "Valorant": [
        """En {lugar}, el agente {nombre} lideró al equipo hacia una tensa partida. Los {sustantivo_plural} enemigos ya 
        habían tomado el control del sitio B, colocando trampas por todas partes. Con su habilidad {adjetivo}, logró infiltrarse 
        en el perímetro. Cuando activó su {sustantivo}, una explosión resonó en el área, derribando a dos oponentes. Sin embargo, 
        el enemigo tenía un plan inesperado: un francotirador oculto que casi lo elimina. Con una comunicación impecable, el equipo 
        desactivó el Spike justo antes de la detonación.""",

        """La partida comenzó en {lugar}, un territorio lleno de pasillos estrechos y posiciones estratégicas. {nombre} avanzó 
        con cautela mientras los {sustantivo_plural} enemigos intentaban rodearlos. La presión aumentó cuando quedaban solo treinta 
        segundos para colocar el Spike. Usando un {sustantivo} especial, neutralizó al líder enemigo, abriendo paso para que su 
        equipo colocara el Spike. La ronda fue {adjetivo}, pero la victoria estuvo asegurada gracias al sacrificio de sus compañeros."""
    ],
    "DayZ": [
        """En las profundidades de {lugar}, {nombre} se encontraba al límite de sus fuerzas. Rodeado por {sustantivo_plural}, 
        sus recursos eran escasos. Encontró un refugio abandonado que contenía un {sustantivo}, lo que le dio esperanza para 
        sobrevivir. Pero, al caer la noche, el ambiente se tornó {adjetivo}. Los gritos de los infectados se escuchaban cerca, y 
        su única opción era correr hacia el bosque. Después de horas de lucha, divisó una luz en la distancia: un grupo de sobrevivientes 
        lo había encontrado justo a tiempo.""",

        """El día amaneció con una tranquilidad engañosa en {lugar}. {nombre} decidió aventurarse a buscar provisiones en un pueblo 
        cercano. Allí encontró una mochila llena de {sustantivo_plural}, pero al mismo tiempo atrajo la atención de un grupo de infectados. 
        Usando un {sustantivo}, intentó defenderse mientras corría hacia un edificio. La situación era {adjetivo}, ya que los infectados 
        rompían las puertas y ventanas. Finalmente, una explosión en las cercanías lo salvó: otro grupo de sobrevivientes había llegado 
        armado hasta los dientes."""
    ],
    "Counter-Strike": [
        """La misión en {lugar} comenzó de forma caótica. {nombre} lideraba al escuadrón de CT en un intento por desarmar la bomba 
        que los {sustantivo_plural} habían colocado. Con solo un {sustantivo}, enfrentó una lluvia de balas mientras cubría a su 
        compañero que desactivaba el dispositivo. El momento fue {adjetivo}, con explosiones resonando por todas partes. Finalmente, 
        el escuadrón salió victorioso, asegurando el lugar y ganando la ronda crucial para el equipo.""",

        """En el frío desolador de {lugar}, {nombre} avanzó lentamente junto a su equipo. Los {sustantivo_plural} enemigos habían 
        colocado francotiradores en las posiciones más altas. Usando un {sustantivo} especial, logró derribar al líder enemigo con un 
        disparo preciso. Sin embargo, la victoria no fue fácil: el enfrentamiento fue {adjetivo} y dejó a todos al borde del agotamiento. 
        Fue una ronda que ninguno de los jugadores olvidaría."""
    ],
    "League of Legends": [
        """En la Grieta del Invocador, {nombre} decidió ir hacia {lugar} para ayudar a sus aliados. Los {sustantivo_plural} enemigos 
        ya habían tomado la delantera, pero con un {sustantivo} mágico logró revertir la batalla. El momento fue {adjetivo}, con habilidades 
        volando por doquier. Finalmente, su equipo aseguró el Barón Nashor, llevando la partida hacia una victoria épica.""",

        """La partida comenzó con un enfrentamiento en {lugar}. {nombre} se enfrentó a los {sustantivo_plural}, quienes intentaban 
        derribar la torre. Con un {sustantivo} especial y movimientos estratégicos, logró dar vuelta a la situación. Todo parecía perdido, 
        pero un enfrentamiento {adjetivo} en el Dragón Anciano selló el destino del equipo enemigo. Fue una partida llena de tensión y 
        momentos inolvidables."""
    ]

}
# Generar historia aleatoria
def generar_historia(tema, palabras):
    historia_plantilla = random.choice(historias_por_tema[tema])
    return historia_plantilla.format(**palabras)

def modo_competitivo():
    jugadores = int(input("¿Cuántos jugadores participarán? "))
    historias = []
    
    for jugador in range(1, jugadores + 1):
        print(f"\nJugador {jugador}, ¡es tu turno!")
        tema = seleccionar_tema()
        palabras = {}
        tipos = ["nombre", "sustantivo", "sustantivo_plural", "lugar", "adjetivo"]

        for tipo in tipos:
            respuesta = preguntar_con_tiempo(f"{tipo.capitalize()}: ", tipo, 10)
            palabras[tipo] = respuesta
        
        historias.append((jugador, generar_historia(tema, palabras)))

    print("\n--- Historias ---")
    for jugador, historia in historias:
        print(f"Jugador {jugador}:\n{historia}\n")

    print("¡Es momento de votar por la mejor historia!")
    for jugador, _ in historias:
        print(f"Jugador {jugador}: {input('Vota por el mejor jugador (introduce su número): ')}")


# Jugar Mad Libs
def mad_libs():
    print("¡Bienvenido a Mad Libs!")
    tema = seleccionar_tema()
    print(f"Has elegido el tema: {tema}")
    print("¡Comencemos! Tienes 10 segundos para cada respuesta. 🕒")
    print("------------------------------------------")
    
    palabras = {}
    tipos = ["nombre", "sustantivo", "sustantivo_plural", "lugar", "adjetivo"]


    for i, tipo in enumerate(tipos):
        pregunta = f"Selecciona {'otro ' if i > 0 else ''}{tipo.replace('_', ' ')}: "
        respuesta = preguntar_con_tiempo(pregunta, tipo, 10)
        palabras[tipo] = respuesta
        reproducir_sonido("select.mp3")  # Efecto de sonido al seleccionar una palabra

    historia = generar_historia(tema, palabras)
    print("------------------------------------------")
    print(historia)
    print("------------------------------------------")
    
    reproducir_sonido("finish.mp3")  # Sonido al finalizar
    mostrar_animacion_final()  # Animación con emojis
    print("🎉 ¡Gracias por jugar a Mad Libs! 🎉")
    print("Creado por Tomas Vales.")


mad_libs()
