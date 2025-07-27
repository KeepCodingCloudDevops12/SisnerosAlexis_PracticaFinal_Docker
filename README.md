# Práctica Final de Docker: Microservicio Contador Full Stack

Este proyecto es la implementación de la práctica final de Docker para el bootcamp de KeepCoding. Consiste en una aplicación web completa con una arquitectura de tres capas (frontend, backend, base de datos), totalmente containerizada y orquestada con Docker Compose.

## 🌟 Arquitectura del Proyecto

El sistema está compuesto por tres servicios principales que se comunican a través de una red privada de Docker:

1.  **`frontend` (Proxy Inverso y UI):**
    *   Un servidor web **Nginx** que actúa como el único punto de entrada a la aplicación.
    *   Sirve una interfaz de usuario estática (HTML/CSS/JS) para interactuar con el contador.
    *   Actúa como **proxy inverso**, redirigiendo las peticiones que empiezan por `/api/` al servicio de backend.

2.  **`app` (API Backend):**
    *   Una API REST construida con **Python** y el framework **Flask**.
    *   Gestiona la lógica de negocio: se conecta a la base de datos para leer e incrementar el valor de un contador.
    *   No está expuesta directamente al exterior, solo es accesible a través del proxy Nginx.

3.  **`db` (Base de Datos):**
    *   Un servidor de base de datos **PostgreSQL**.
    *   Almacena el valor del contador.
    *   Utiliza un **volumen de Docker** para garantizar la persistencia de los datos, incluso si el contenedor se elimina.

## ✅ Hitos y Características Implementadas

*   **Containerización completa:** Cada componente de la arquitectura corre en su propio contenedor Docker.
*   **Orquestación con Docker Compose:** Se utiliza un único archivo `docker-compose.yml` para definir, construir y lanzar toda la aplicación.
*   **Dockerfile Multi-Etapa:** La imagen del backend se construye usando un *multistage build* para minimizar su tamaño final, separando el entorno de construcción del de ejecución.
*   **Persistencia de Datos:** El estado del contador sobrevive a reinicios de los contenedores gracias al uso de volúmenes de Docker.
*   **Configuración por Variables de Entorno:** Las credenciales de la base de datos se gestionan de forma segura a través de variables de entorno y un archivo `.env`.
*   **Imagen Pública en Docker Hub:** La imagen de la aplicación está disponible públicamente [aquí](https://hub.docker.com/r/alesisneros/docker-bootcamp-project).
*   **Análisis de Seguridad:** La imagen ha sido escaneada con **Trivy** para detectar vulnerabilidades, y se han aplicado parches a las dependencias de Python.

## 🛠️ Requisitos Previos

*   [Docker](https://www.docker.com/products/docker-desktop/)
*   [Docker Compose](https://docs.docker.com/compose/install/) (normalmente incluido en Docker Desktop)
*   [Git](https://git-scm.com/)

## 🚀 Instrucciones de Despliegue y Verificación

Sigue estos pasos para poner en marcha el proyecto en tu máquina local.

### 1. Clonar el Repositorio

```bash
git clone https://github.com/KeepCodingCloudDevops12/SisnerosAlexis_PracticaFinal_Docker.git
cd PracticaFinal_Docker

### 2: Crear el Archivo de Credenciales (`.env`)

Este paso es **CRUCIAL**. La aplicación no funcionará sin él. El repositorio incluye un archivo de ejemplo llamado `.env.example` para facilitar este proceso.

Debes crear tu propio archivo `.env` a partir del ejemplo.

**Opción A: Desde la terminal (recomendado)**
Simplemente copia el archivo de ejemplo con el siguiente comando:
```bash
cp .env.example .env