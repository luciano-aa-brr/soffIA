# Luciano Aliaga Analista programador 2025
import sys
import os
import pyttsx3
import time
import speech_recognition as sr
import google.generativeai as genai
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QPalette, QColor
from langchain.memory import ConversationBufferMemory

# Configurar API
api_key = "TU_CLAVE_FUE_REMOVIDA"
genai.configure(api_key=api_key)
modelo = genai.GenerativeModel("models/gemini-flash-latest")

class TTSWorker(QThread):
    finished = pyqtSignal()

    def __init__(self, text):
        super().__init__()
        self.text = text
        self.engine = None
        self._stop_requested = False

    def run(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1)
        self.engine.say(self.text)
        try:
            self.engine.runAndWait()
        except RuntimeError:
            pass
        self.finished.emit()

    def stop(self):
        self._stop_requested = True
        if self.engine is not None:
            try:
                self.engine.stop()
            except Exception:
                pass

class SoffIAWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.memoria = ConversationBufferMemory()
        self.tts_worker = None
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

    def set_busy(self, busy: bool):
        self.inputField.setEnabled(not busy)
        self.sendButton.setEnabled(not busy)
        self.statusLabel.setText("SoffIA está hablando..." if busy else "")

    def procesarPregunta(self):
        if self.tts_worker is not None and self.tts_worker.isRunning():
            self.chatArea.append("SoffIA: Espera un momento, aún estoy hablando...\n")
            return

        inputUsuario = self.inputField.text().strip()
        if not inputUsuario:
            return

        self.chatArea.append(f"Tú: {inputUsuario}")
        self.inputField.clear()

        context = self.memoria.load_memory_variables({}).get("history", "")
        prompt = f"Historial de conversación:\n{context}\n\nUsuario: {inputUsuario}\nAgente:"

        try:
            respuesta = modelo.generate_content(prompt)
            respuesta_text = respuesta.text
            self.memoria.save_context({"input": inputUsuario}, {"output": respuesta_text})

            self.chatArea.append(f"SoffIA: {respuesta_text}\n")
            self.chatArea.verticalScrollBar().setValue(self.chatArea.verticalScrollBar().maximum())

            self.tts_worker = TTSWorker(respuesta_text)
            self.tts_worker.finished.connect(self.on_tts_finished)
            self.tts_worker.start()
            self.set_busy(True)
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.chatArea.append(f"{error_msg}\n")
            print(error_msg)  # Para depurar en consola

    def on_tts_finished(self):
        self.set_busy(False)
        self.tts_worker = None

    def closeEvent(self, event):
        if self.tts_worker is not None and self.tts_worker.isRunning():
            self.tts_worker.stop()
            self.tts_worker.wait(500)
        event.accept()

    def salir(self):
        if self.tts_worker is not None and self.tts_worker.isRunning():
            self.tts_worker.stop()
            self.tts_worker.wait(500)

        self.set_busy(True)
        farewell_worker = TTSWorker("Gracias por usar SoffIA. ¡Hasta luego!")
        farewell_worker.finished.connect(QApplication.quit)
        farewell_worker.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SoffIAWindow()
    window.show()
    sys.exit(app.exec_())