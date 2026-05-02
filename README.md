# Limpia Código con IA
====================================================

## Descripción

Code Cleaner AI es una herramienta de línea de comandos (CLI) que utiliza modelos de lenguaje para sugerir optimizaciones en código existente, reduciendo el tamaño del código y mejorando la legibilidad.

### Features

* Recomienda cambios en el código
* Puede trabajar con varios lenguajes

## Instalación

Puedes instalar Code Cleaner AI utilizando pip:
```bash
pip install code-cleaner-ai
```
O clonar este repositorio y ejecutar:
```bash
python setup.py install
```

## Uso

1. Ejecuta la herramienta con el comando `code-cleaner-ai` seguido del nombre de tu archivo o directorio:
```bash
code-cleaner-ai my_file.py
```
2. La herramienta sugerirá cambios en el código y te mostrará una lista de recomendaciones.

## Estructura del Proyecto

* `__init__.py`: Archivo de inicialización para el paquete.
* `main.py`: Archivo principal que ejecuta la lógica de la herramienta.
* `tests/test_main.py`: Pruebas unitarias para el archivo `main.py`.
* `requirements/requirements.txt`: Dependencias del proyecto.
* `requirements/package.json`: Archivo JSON con dependencias adicionales.
* `src/code_cleaner_ai/model.py`: Modelo de lenguaje utilizado por la herramienta.
* `src/code_cleaner_ai/utils.py`: Utilidades y funciones auxiliares.

## Contribución

¡Contribuye a Code Cleaner AI!

1. Clona el repositorio: `git clone https://github.com/your-username/code-cleaner-ai.git`
2. Crea una rama para tus cambios: `git branch feature/my-feature`
3. Realiza tus cambios y prueba la herramienta.
4. Comunica tus cambios con nosotros enviando un pull request.

## Licencia

Code Cleaner AI está bajo la licencia MIT. Puedes encontrar más información en el archivo [LICENSE](LICENSE).

### Badges

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)