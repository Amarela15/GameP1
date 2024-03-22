import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
max_fails = 5
# Lista para almacenar las letras adivinadas
guessed_letters = []
word_displayed = []
ok = True
print("¡Bienvenido al juego de adivinanzas!")
# Me aseguro de que se escoja la dificultad adecuadamente
print("Primero que nada, escoge una dificultad: ")
while ok:
    dificultad = input("""
1: Fácil
2: Medio
3: Díficil
""")
    if (dificultad != "1" and dificultad != "2" and dificultad != "3"):
        print("Intente de nuevo, debe escoger un numero del 1 al 3")
        continue
    else:
        ok = False
# Configuro la Dificultad Fácil
palabra = []
if dificultad == "1":
    for letra in secret_word:
        if letra in "aáeéiíoóuú":
            palabra.append(letra)
            guessed_letters.append(letra) 
        else:
            palabra.append("_")
    word_displayed = "".join(palabra)
# Configuro la dificultad Media
elif dificultad == "2":
    guiones = "_" * (len(secret_word)- 2)
    palabra.append(secret_word[0])
    palabra.append(guiones)
    palabra.append(secret_word[-1])
    word_displayed = "".join(palabra)
    if secret_word.count(secret_word[0]) == 1:
        guessed_letters.append(secret_word[0])
    if secret_word.count(secret_word[-1]) == 1:
        guessed_letters.append(secret_word[-1])
#Configuro la dificultad Difícil   
else:
    word_displayed = "_" * len(secret_word)
    
print("Bien, comencemos. Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
fails = 0
while(fails < max_fails):
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()
     # Verificar si se ha ingresado un String vacío o un caracter no válido
     if not letter.isalpha():
         print("No has ingresado una letra. Intenta de nuevo.")
         continue
     # Verficar si se ha ingresado un solo carácter
     if len(letter) > 1:
         print("Ingresaste más de una letra. Intenta de nuevo.")
         continue
     # Verificar si la letra ya ha sido adivinada
     if letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra.")
         continue
     # Agregar la letra a la lista de letras adivinadas
     guessed_letters.append(letter)
     # Verificar si la letra está en la palabra secreta
     if letter in secret_word:
         print("¡Bien hecho! La letra está en la palabra.")
     else:
         # Aumenta el numero de fallos
         print("Lo siento, la letra no está en la palabra.")
         fails += 1
     # Mostrar la palabra parcialmente adivinada
     letters = []
     for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter)
         else:
             letters.append("_")
     if dificultad == "2":
         if secret_word[0] not in guessed_letters:
             letters[0] = secret_word[0]
         if secret_word[-1] not in guessed_letters:
             letters[-1] = secret_word[-1]
     word_displayed = "".join(letters)
     print(f"Palabra: {word_displayed}")
     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta:  {secret_word}")
         break
else:
     print(f"¡Oh no! Has agotado tus {max_fails} intentos.")
     print(f"La palabra secreta era: {secret_word}")