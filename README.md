# Proyecto Bootcamp Docker: Microservicio Contador con Flask y PostgreSQL

Este proyecto es una práctica para el bootcamp de KeepCoding que implementa un microservicio simple capaz de leer y escribir en una base de datos, todo desplegado con Docker Compose.

## Descripción de la Aplicación

La aplicación es una API REST simple construida con Flask (Python) que expone un contador. El valor de este contador persiste en una base de datos PostgreSQL.

La API tiene 3 rutas (endpoints):
- `GET /`: Devuelve un mensaje de estado para verificar que la API está funcionando.
- `GET /counter`: Devuelve el valor actual del contador desde la base de datos.
- `POST /counter/increment`: Incrementa en 1 el valor del contador en la base de datos.

## Funcionamiento de la Aplicación

La arquitectura consta de dos componentes principales orquestados por Docker Compose:
1.  **`app`**: Un contenedor con la aplicación Flask/Python.
2.  **`db`**: Un contenedor con la base de datos PostgreSQL.

La aplicación se conecta a la base de datos utilizando el nombre del servicio `db` como host. Los datos de la base de datos se guardan en un volumen de Docker para garantizar la persistencia incluso si el contenedor se elimina y se vuelve a crear.

## Requisitos para Ejecutar

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Docker Compose](https://docs.docker.com/compose/install/) (incluido en Docker Desktop)
- Git

## Instrucciones para Ejecución

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/<tu-usuario>/docker-bootcamp-project.git
    cd docker-bootcamp-project
    ```

2.  **Crear el archivo de configuración:**
    Crea un archivo llamado `.env` en la raíz del proyecto y añade las siguientes variables. Este archivo define las credenciales de la base de datos.
    ```
    POSTGRES_DB=bootcampdb
    POSTGRES_USER=bootcampuser
    POSTGRES_PASSWORD=supersecretpassword
    ```

3.  **Construir y ejecutar los contenedores:**
    Este comando construirá la imagen de la aplicación (si no existe) y levantará ambos servicios en segundo plano (`-d`).
    ```bash
    docker-compose up --build -d
    ```

4.  **Verificar el funcionamiento:**
    - **Verificar los logs:** Puedes ver los logs de la aplicación para asegurarte de que se conectó correctamente a la base de datos.
      ```bash
      docker-compose logs -f app
      ```
      Deberías ver mensajes como "¡Conexión a la base de datos exitosa!" e "¡Aplicación lista para recibir peticiones!". Presiona `Ctrl+C` para salir.

    - **Probar la API con `curl`:**
      ```bash
      # Verificar estado
      curl http://localhost:5000/

      # Obtener valor inicial (debería ser 0)
      curl http://localhost:5000/counter

      # Incrementar el valor
      curl -X POST http://localhost:5000/counter/increment

      # Verificar el nuevo valor (debería ser 1)
      curl http://localhost:5000/counter
      ```

5.  **Detener la aplicación:**
    Para detener y eliminar los contenedores, ejecuta:
    ```bash
    docker-compose down
    ```
    Si quieres eliminar también el volumen de la base de datos (se perderán todos los datos), ejecuta:
    ```bash
    docker-compose down -v
    ```

## Configuración

La aplicación se configura mediante variables de entorno, definidas en el archivo `.env`.

| Variable | Descripción | Default en `docker-compose.yml` |
| --- | --- | --- |
| `POSTGRES_DB` | Nombre de la base de datos. | `bootcampdb` |
| `POSTGRES_USER` | Usuario de la base de datos. | `bootcampuser` |
| `POSTGRES_PASSWORD`| Contraseña del usuario. | `supersecretpassword` |
| `DB_HOST` | Host de la base de datos. | `db` |
