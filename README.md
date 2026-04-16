# SoffIA - Asistente Virtual Inteligente

SoffIA es un asistente virtual basado en IA que utiliza Google Gemini para proporcionar respuestas inteligentes y conversacionales. Incluye múltiples interfaces: una moderna con PyQt5, una versión de consola y una interfaz antigua con Tkinter.

## Características

- **Interfaz Moderna (qtAgente.py)**: Interfaz gráfica moderna con PyQt5 para chat de texto.
- **Versión de Consola (agente.py)**: Versión de línea de comandos para uso básico.
- **Interfaz Antigua (tkAgente.py)**: Versión original con Tkinter.
- **Memoria Conversacional**: Mantiene el contexto de la conversación usando LangChain.
- **Modo Offline**: Funciona sin conexión a internet para respuestas basadas en conocimiento general.

## Requisitos

- Python 3.8+
- PyQt5
- google-generativeai
- langchain

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/luciano-aa-brr/soffIA.git
cd soffIA
```

2. Crea un entorno virtual:
```bash
python -m venv .venv
.venv\Scripts\activate  # En Windows
```

3. Instala las dependencias:
```bash
pip install PyQt5 google-generativeai langchain
```

4. Configura tu clave API de Google Gemini:
```bash
# En PowerShell
$env:GEMINI_API_KEY = "tu_clave_api_aqui"
```

## Uso

### Interfaz Moderna
```bash
python qtAgente.py
```

### Versión de Consola
```bash
python agente.py
```

### Interfaz Antigua
```bash
python tkAgente.py
```

## Configuración

- **Clave API**: Define la variable de entorno `GEMINI_API_KEY` con tu clave de Google Gemini.
- **Modelo**: Actualmente usa `models/gemini-flash-latest` para optimizar costos.

## Estructura del Proyecto

```
SoffIA/
├── qtAgente.py      # Interfaz moderna con PyQt5
├── agente.py        # Versión de consola
├── tkAgente.py      # Interfaz antigua con Tkinter
├── agente.spec      # Configuración para PyInstaller
├── build/           # Archivos de compilación
├── .gitignore       # Archivos a ignorar
├── LICENSE          # Licencia del proyecto
└── README.md        # Este archivo
```

