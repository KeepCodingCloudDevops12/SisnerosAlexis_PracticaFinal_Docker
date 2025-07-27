# --- ETAPA 1: BUILDER ---
# Usamos una imagen completa de Python para instalar dependencias.
# Le ponemos un alias "builder" para referenciarla luego.
FROM python:3.9-alpine as builder

# Establecemos el directorio de trabajo
WORKDIR /install

# Copiamos solo el archivo de requerimientos para aprovechar el cache de Docker
COPY app/requirements.txt .

# Instalamos las dependencias en un directorio local
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# --- ETAPA 2: FINAL ---
# Usamos una imagen "slim" que es mucho más ligera.
FROM python:3.9-alpine

# Establecemos el directorio de trabajo en la imagen final
WORKDIR /app

# Copiamos las dependencias YA INSTALADAS desde la etapa "builder"
COPY --from=builder /install /usr/local

# Copiamos el código de nuestra aplicación
COPY ./app .

# Variable de entorno para que Python no genere archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Variable de entorno para que Flask se ejecute en modo producción
ENV FLASK_ENV production

# Exponemos el puerto en el que corre nuestra aplicación
EXPOSE 5000

# El comando que se ejecutará cuando el contenedor inicie
# Usamos gunicorn para un servidor WSGI más robusto que el de desarrollo de Flask
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]