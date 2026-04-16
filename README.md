# SoffIA - Asistente Virtual Inteligente

SoffIA es un asistente virtual basado en IA que utiliza Google Gemini para proporcionar respuestas inteligentes y conversacionales. Incluye múltiples interfaces: una moderna con PyQt5, una versión de consola y una interfaz antigua con Tkinter.

## Características

- **Interfaz Moderna (qtAgente.py)**: Interfaz gráfica moderna con PyQt5, narración de voz y manejo de errores.
- **Versión de Consola (agente.py)**: Versión de línea de comandos para uso básico.
- **Interfaz Antigua (tkAgente.py)**: Versión original con Tkinter.
- **Memoria Conversacional**: Mantiene el contexto de la conversación usando LangChain.
- **Narración de Voz**: Utiliza pyttsx3 para narrar las respuestas.
- **Reconocimiento de Voz**: Soporte para entrada de voz (speech_recognition).

## Requisitos

- Python 3.8+
- PyQt5
- google-generativeai
- langchain
- pyttsx3
- speech_recognition

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
pip install PyQt5 google-generativeai langchain pyttsx3 speech_recognition
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
web/SoffIA/
├── qtAgente.py      # Interfaz moderna con PyQt5
├── agente.py        # Versión de consola
├── tkAgente.py      # Interfaz antigua con Tkinter
├── agente.spec      # Configuración para PyInstaller
├── build/           # Archivos de compilación
└── README.md        # Este archivo
```

## Desarrollo

- **Autor**: Luciano Aliaga
- **Fecha**: 2025
- **Licencia**: MIT

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request en GitHub.

## Notas

- La interfaz moderna incluye bloqueo de entrada durante la narración para evitar conflictos.
- Todas las versiones mantienen memoria conversacional.
- El proyecto está optimizado para uso gratuito de Gemini con límites de quota.

¡Bienvenido al **Club Informático Chile**!  
Este repositorio está diseñado para que **cada miembro pueda presentarse** y aparecer en nuestra página web estática.

---

## ✅ ¿Cómo funciona?
- Tenemos un archivo `index.html` que muestra todas las presentaciones.
- Cada miembro agrega su **nombre**, una **breve reseña** y sus **enlaces de LinkedIn y GitHub**.
- Luego, subes tus cambios a través de un **Pull Request**.

---

## 🛠 ¿Cómo me agrego?
### 1. Haz un **fork** del repositorio
En la esquina superior derecha de esta página, haz clic en **Fork** para copiar el proyecto a tu cuenta.

### 2. Clona tu fork en tu PC
```bash
git clone https://github.com/TU-USUARIO/club-informatico-presentaciones.git
```

### 3. Edita el archivo `index.html`
Busca la sección
```html
<div class="presentaciones">
    <!-- Aquí los miembros agregan sus presentaciones -->
</div>
```

Agrega tu bloque de presentación **siguiendo este formato**:
```html
<div class="card">
    <h3>Tu Nombre</h3>
    <p>Escribe una breve reseña sobre ti: ¿qué te apasiona? ¿en qué trabajas o estudias?</p>
    <div class="links">
        <a href="https://linkedin.com/in/TU-USUARIO" target="_blank"><i class="fab fa-linkedin"></i></a>
        <a href="https://github.com/TU-USUARIO" target="_blank"><i class="fab fa-github"></i></a>
    </div>
</div>
```

📌 Ejemplo real:
```html
<div class="card">
    <h3>Carlos Carrasco</h3>
    <p>Desarrollador backend apasionado por Python y la tecnología open source. Aprendiendo DevOps y ciberseguridad.</p>
    <div class="links">
        <a href="https://linkedin.com/in/mg-carlos-carrasco/" target="_blank"><i class="fab fa-linkedin"></i></a>
        <a href="https://github.com/KrlitosForever" target="_blank"><i class="fab fa-github"></i></a>
    </div>
</div>
```

### 4. Guarda los cambios y súbelos a tu fork
```bash
git add .
git commit -m "Agregando mi presentación"
git push origin main
```

### 5. Crea un Pull Request
Vuelve a este repositorio original y crea un Pull Request para que revisemos y unamos tu cambio.

## ✅ ¿Qué debes considerar?
✔ Respeta el formato propuesto.   
✔ Usa íconos de LinkedIn y GitHub (ya están en la plantilla con Font Awesome).   
✔ No elimines ni modifiques otras presentaciones.   
✔ Sé breve, máximo 2-3 líneas en tu reseña.   

## ❓ ¿Tienes dudas?
Ve a la sección de Discussions ahí encontraras los siguientes foros:   
✔️ General   
✔️ Ideas   
✔️ Preguntas y Respuestas   

## 🎯 ¿Quieres contribuir más?

¡Perfecto! Puedes:
* Mejorar el diseño con CSS.
* Agregar soporte para fotos de perfil.
* Crear un formulario dinámico para generar el bloque HTML automáticamente.

## 🎉Ya eres parte del club 🎉
Puedes revisarte en el siguiente [Link](https://club-informatico.github.io/Intro-presentar/)

## Colaboradores

<a href="https://github.com/Club-Informatico/Intro-presentar/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Club-Informatico/Intro-presentar" />
</a>
>>>>>>> 9389792493984ead4276ab4c683a619ccba67c7e
