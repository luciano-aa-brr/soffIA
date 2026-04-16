import os
import time
import google.generativeai as genai
from langchain.memory import ConversationBufferMemory

def limpiar():
    os.system("cls")

def pausa():
    time.sleep(2)

import os

# Configuracion api
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY environment variable not set")
    exit(1)
genai.configure(api_key=api_key)
modelo = genai.GenerativeModel("models/gemini-flash-latest")

#inicializar memoria
memoria = ConversationBufferMemory()

def chatBot():

    limpiar()
    print(f"{"*"*23}\n¡Bienvenido al SofIA!\n{"*"*23}")

    while True:
        pausa()
        inputUsuario = input("Ingresa tu pregunta o tema: ")
        context = memoria.load_memory_variables({}).get("history", "")
        
        # Crear prompt con historial
        prompt = (f"Historial de conversación:\n{context}\n\nUsuario:{inputUsuario}\nAgente:")
        # Generar respuesta 
        respuesta = modelo.generate_content(prompt)
        # Guardar en memoria
        memoria.save_context({"input": inputUsuario}, {"output": respuesta.text})
        
        # Mostrar respuesta
        limpiar()
        print(f"\nSofIA está pensando...\n{"*"*25}")
        pausa()
        limpiar()
        print(f"{"*"*50}\nSofIA: {respuesta.text}\n{"*"*50}")
        pausa()

        # continuar??
        continuar = input("¿Quieres hacer otra pregunta?\n1=Si\n2=No\n").strip().lower()
        if continuar != '1':
            limpiar()
            print(f"{"*"*30}\n¡Gracias por utilizar SofIA!\n{"*"*30}")
            break

#ejecutar
chatBot()