# Curso de Introducción a Selenium con Python

Estas son mis notas del curso de la plataforma [Platzi](https://platzi.com/cursos/intro-selenium/).

En este [enlace](https://docs.google.com/document/d/1opeTnOY65KMb2qHWHjgPjswVeWEvRRyws8oxN2RuDiE/edit?usp=sharing) encontrarás los resúmenes de esta clase.

-------------------
**Breve Introducción**

Selenium es un framework de automatización de navegadores multilenguaje. Con él podrás simular las acciones de tus usuarios dentro de aplicaciones web con fines de testing, generar los reportes correspondientes, automatizar tareas repetitivas e incluso extraer datos de la web. Cualquier acción humana puede ser replicada y serás capaz de programarla.

- Sincronizar pruebas
- Interactuar con elementos
- Utilizar comandos básicos
- Preparar entorno de trabajo
--------------------
**Configurando el Entorno**
1. Ubicación de python: **where python** (En Linux es which python)
2. Versión de python: **python --version**
3. Tener instalado Anaconda para el manejo de los entornos virtuales
4. Verificamos la lista de entornos: **conda env list** o **conda info --envs**
5. Creamos el entorno: conda create -n <nombre_del_entorno> python=<version_python> anaconda
6. Verificamos que se halla creado con el comando del paso 4
7. Activamos el entorno: **conda activate** <nombre_del_entorno>
8. Verificamos la version de Python con el comando del paso 2
9. Actualizamos pip: **pip install -U pip** (Si sale error: **pip install --user -U pip**)
10. Instalar Selenium: **pip install selenium**
11. Verificar los paquetes: **pip list --local**
12. Abrimos Anaconda Navigator: **anaconda-navigator**
13. Ejecutamos VS Code en el Anaconda Navigator
14. Para desactivar el entorno:  **conda deactivate**

Exitos!! 🔥