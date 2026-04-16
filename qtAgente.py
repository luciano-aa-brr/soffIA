# Luciano Aliaga Analista programador 2025
import sys
import os
import google.generativeai as genai
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor
from langchain.memory import ConversationBufferMemory

import os

# Configurar API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY environment variable not set")
    exit(1)
genai.configure(api_key=api_key)
modelo = genai.GenerativeModel("models/gemini-flash-latest")

class SoffIAWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.memoria = ConversationBufferMemory()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("SoffIA - Chatbot Moderno")
        self.setGeometry(300, 300, 800, 600)

        # Paleta de colores moderna
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(240, 248, 255))  # Alice Blue
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        self.setPalette(palette)

        layout = QVBoxLayout()

        # Título
        title = QLabel("SoffIA - Asistente Virtual")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Área de chat
        self.chatArea = QTextEdit()
        self.chatArea.setReadOnly(True)
        self.chatArea.setFont(QFont("Arial", 12))
        layout.addWidget(self.chatArea)

        # Área de entrada
        inputLayout = QHBoxLayout()
        self.inputField = QLineEdit()
        self.inputField.setFont(QFont("Arial", 12))
        self.inputField.returnPressed.connect(self.procesarPregunta)
        inputLayout.addWidget(self.inputField)

        self.sendButton = QPushButton("Enviar")
        self.sendButton.clicked.connect(self.procesarPregunta)
        inputLayout.addWidget(self.sendButton)

        self.exitButton = QPushButton("Salir")
        self.exitButton.clicked.connect(self.salir)
        inputLayout.addWidget(self.exitButton)

        self.statusLabel = QLabel("")
        self.statusLabel.setFont(QFont("Arial", 10))
        self.statusLabel.setStyleSheet("color: gray")
        layout.addWidget(self.statusLabel)

        layout.addLayout(inputLayout)

        self.setLayout(layout)

    def procesarPregunta(self):
        inputUsuario = self.inputField.text().strip()
        if not inputUsuario:
            return

        self.chatArea.append(f"Tú: {inputUsuario}\n")
        self.inputField.clear()
        self.statusLabel.setText("SoffIA está pensando...")

        context = self.memoria.load_memory_variables({}).get("history", "")
        prompt = f"Historial de conversación:\n{context}\n\nUsuario: {inputUsuario}\nAgente:"

        try:
            respuesta = modelo.generate_content(prompt)
            respuesta_text = respuesta.text
            self.memoria.save_context({"input": inputUsuario}, {"output": respuesta_text})

            self.chatArea.append(f"SoffIA: {respuesta_text}\n")
            self.chatArea.verticalScrollBar().setValue(self.chatArea.verticalScrollBar().maximum())
            self.statusLabel.setText("")
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.chatArea.append(f"{error_msg}\n")
            self.statusLabel.setText("")
            print(error_msg)  # Para depurar en consola

    def salir(self):
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SoffIAWindow()
    window.show()
    sys.exit(app.exec_())