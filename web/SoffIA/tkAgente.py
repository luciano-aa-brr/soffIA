# Luciano Aliaga Analista programador 2025
import tkinter as tk
import pyttsx3
import time
import speech_recognition as sr
import google.generativeai as genai
import os
from langchain.memory import ConversationBufferMemory

# Configurar API 
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
modelo = genai.GenerativeModel("gemini-pro")

def hablar(texto):
    maquina.say(texto)
    maquina.setProperty('rate', 150)  
    maquina.setProperty('volume', 1) 
    maquina.runAndWait()

def procesarPregunta(event=None):  
    inputUsuario = entradaUsuario.get()
    
    context = memoria.load_memory_variables({}).get("history", "")
    prompt = (f"Historial de conversación:\n{context}\n\nUsuario: {inputUsuario}\nAgente:")
    
    respuesta = modelo.generate_content(prompt)
    memoria.save_context({"input": inputUsuario}, {"output": respuesta.text})

    salidaTexto.config(state=tk.NORMAL)
    salidaTexto.insert(tk.END, f"\nSoffIA: {respuesta.text}\n")
    salidaTexto.config(state=tk.DISABLED)
    salidaTexto.see(tk.END) 
    
    entradaUsuario.delete(0, tk.END)  

    ventana.update_idletasks()

    hablar(respuesta.text)

def salir():
    ventana.quit()
    hablar("Gracias por usar SoffIA. ¡Hasta luego!")
    time.sleep(0.5)
    ventana.destroy()

maquina = pyttsx3.init()


memoria = ConversationBufferMemory()

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("SoffIA - Chatbot")
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

ancho_ventana = 600
alto_ventana = 500

pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
ventana.config(bg="cornflowerblue")

# salida
salidaTexto = tk.Text(ventana, width=65, height=25, state=tk.DISABLED)
salidaTexto.pack(pady=10)

# entrada
entradaUsuario = tk.Entry(ventana, width=50)
entradaUsuario.pack(pady=10)
entradaUsuario.bind("<Return>", procesarPregunta) 

frameBotones = tk.Frame(ventana)
frameBotones.pack(pady=5)
frameBotones.config(bg="cornflowerblue")

botonEnviar = tk.Button(frameBotones, text="Enviar", command=procesarPregunta)
botonEnviar.pack(side=tk.LEFT, padx=5)

botonSalir = tk.Button(frameBotones, text="salir", command=salir)
botonSalir.pack(side=tk.LEFT, padx=5)

botonEnviar.config(width=15)
botonSalir.config(width=15)

ventana.mainloop()


