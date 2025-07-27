# Práctica Final de Docker: Microservicio Full Stack con Monitoreo

Este proyecto es la implementación de la práctica final de Docker para el bootcamp de KeepCoding. Consiste en una aplicación web completa con una arquitectura avanzada de microservicios, totalmente containerizada, orquestada con Docker Compose e integrada con una pila de monitoreo profesional.

## 🌟 Arquitectura del Proyecto

El sistema está compuesto por **cinco servicios** que se comunican a través de una red privada de Docker:

### Servicios Principales
1.  **`frontend` (Proxy Inverso y UI):** Un servidor web **Nginx** que actúa como el único punto de entrada a la aplicación. Sirve una interfaz de usuario estática y redirige las peticiones de API (`/api/*`) al backend.
2.  **`app` (API Backend):** Una API REST con **Python/Flask** que gestiona la lógica de negocio. Se conecta a la base de datos para leer e incrementar un contador y expone métricas para Prometheus en el endpoint `/metrics`.
3.  **`db` (Base de Datos):** Un servidor de base de datos **PostgreSQL** que almacena el estado del contador de forma persistente usando un volumen de Docker.

### Pila de Monitoreo
4.  **`prometheus` (Recolección de Métricas):** Un servidor **Prometheus** configurado para "raspar" (scrape) periódicamente el endpoint `/metrics` del servicio `app`, recolectando datos de rendimiento como latencias y número de peticiones.
5.  **`grafana` (Visualización y Dashboards):** Una instancia de **Grafana** conectada a Prometheus como fuente de datos. Permite visualizar las métricas en tiempo real a través de dashboards interactivos.

## ✅ Hitos y Características Implementadas

*   **Arquitectura Completa de 5 Servicios:** Despliegue de una aplicación realista con frontend, backend, base de datos y pila de monitoreo.
*   **Orquestación con Docker Compose:** Un único archivo `docker-compose.yml` gestiona toda la arquitectura.
*   **Dockerfile Multi-Etapa y Optimizado:** La imagen del backend se construye usando un *multistage build* para minimizar su tamaño final.
*   **Persistencia de Datos:** Se utilizan volúmenes de Docker para los datos de PostgreSQL y Grafana, asegurando que ni los datos ni los dashboards se pierdan al reiniciar.
*   **Logging Estructurado (JSON):** El backend está configurado para generar logs en formato JSON, facilitando su análisis y procesamiento por sistemas externos.
*   **Monitoreo de Métricas Profesionales:** Integración de **Prometheus y Grafana** para la recolección y visualización de métricas de la aplicación.
*   **Configuración Segura:** Gestión de credenciales a través de variables de entorno y un archivo `.env.example`.
*   **Imagen Pública en Docker Hub:** La imagen de la aplicación está disponible públicamente.
*   **Análisis de Seguridad:** Escaneo de vulnerabilidades de la imagen con **Trivy**.

## 🛠️ Requisitos Previos

*   [Docker](https://www.docker.com/products/docker-desktop/) & Docker Compose
*   [Git](https://git-scm.com/)

## 🚀 Guía de Despliegue y Verificación

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/KeepCodingCloudDevops12/SisnerosAlexis_PracticaFinal_Docker.git
cd  PracticaFinal_Docker

### Paso 2: Crear el Archivo de Credenciales (.env)
Este paso es CRUCIAL y la aplicación no funcionará sin él. Simplemente copia el archivo de ejemplo proporcionado:
Generated bash
cp .env.example .env

```bash

### Paso 3: Construir y Ejecutar Toda la Pila
Este comando construirá las imágenes necesarias y levantará los cinco servicios en segundo plano.
Generated bash
docker-compose up --build -d

```bash

### Paso 4: Verificar la Funcionalidad

Espera unos 20-30 segundos para que todos los servicios se inicien por completo.
Verificar la Aplicación Web:
Abre tu navegador y ve a ➡️ http://localhost ⬅️
Deberías ver la interfaz del contador. Prueba el botón "Incrementar" para confirmar que la aplicación funciona.
Verificar la Pila de Monitoreo:
Prometheus: Abre http://localhost:9090. Ve a Status -> Targets. Deberías ver el target flask-app con el estado UP (en verde).
Grafana: Abre http://localhost:3000. Inicia sesión con admin / admin. (Te pedirá cambiar la contraseña).
Para ver las métricas, necesitas configurar Prometheus como fuente de datos (URL: http://prometheus:9090) y crear un panel simple.
Verificar los Logs en JSON:
Ejecuta docker-compose logs app en tu terminal. Verás que la salida está estructurada en formato JSON.
Paso 5: Detener la Aplicación
Para detener y eliminar todos los componentes del proyecto:
Generated bash
# Detiene y elimina contenedores y redes
docker-compose down

# Si además quieres eliminar TODOS los datos (contador y dashboards de Grafana):
docker-compose down -v

```bash

Bonus: Visualización de Contenedores con Portainer (Opcional)
Si prefieres una UI para gestionar los contenedores en lugar de la terminal, puedes desplegar Portainer de forma independiente.
Crear el volumen: docker volume create portainer_data
Desplegar el contenedor:
Generated bash
docker run -d -p 9443:9443 --name portainer \
    --restart=always \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v portainer_data:/data \
    portainer/portainer-ce:latest

Bash
Acceder: Navega a https://localhost:9443 (acepta la advertencia de seguridad). La primera vez, configura la contraseña de admin.