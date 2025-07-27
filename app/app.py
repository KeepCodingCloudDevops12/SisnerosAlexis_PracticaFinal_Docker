import os
import time
from flask import Flask, jsonify
import psycopg2
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# --- Configuración de la Base de Datos desde variables de entorno ---
db_name = os.getenv("POSTGRES_DB")
db_user = os.getenv("POSTGRES_USER")
db_pass = os.getenv("POSTGRES_PASSWORD")
db_host = os.getenv("DB_HOST", "db") # Usamos 'db' como default, el nombre del servicio en docker-compose
db_port = os.getenv("DB_PORT", "5432")
metrics = PrometheusMetrics(app)

def get_db_connection():
    """Establece conexión con la base de datos."""
    while True:
        try:
            conn = psycopg2.connect(
                dbname=db_name,
                user=db_user,
                password=db_pass,
                host=db_host,
                port=db_port
            )
            print("¡Conexión a la base de datos exitosa!")
            return conn
        except psycopg2.OperationalError as e:
            print(f"Error conectando a la base de datos: {e}")
            print("Reintentando en 5 segundos...")
            time.sleep(5)

def setup_database():
    """Crea la tabla 'counter' si no existe."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS counter (
            id SERIAL PRIMARY KEY,
            value INTEGER NOT NULL
        );
    """)
    # Si la tabla está vacía, inserta el valor inicial
    cur.execute("SELECT * FROM counter;")
    if cur.fetchone() is None:
        cur.execute("INSERT INTO counter (value) VALUES (0);")
        print("Tabla 'counter' inicializada con valor 0.")
    conn.commit()
    cur.close()
    conn.close()

# --- Rutas de la API ---
@app.route('/')
def index():
    """Ruta principal para verificar que la API está viva."""
    return jsonify({"status": "ok", "message": "API del contador funcionando"})

@app.route('/counter', methods=['GET'])
def get_counter():
    """Obtiene el valor actual del contador."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT value FROM counter WHERE id = 1;")
    value = cur.fetchone()[0]
    cur.close()
    conn.close()
    return jsonify({"current_value": value})

@app.route('/counter/increment', methods=['POST'])
def increment_counter():
    """Incrementa el contador en 1."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE counter SET value = value + 1 WHERE id = 1 RETURNING value;")
    new_value = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"new_value": new_value})

print("Iniciando configuración de la base de datos...")
setup_database()
print("¡Base de datos lista!")


if __name__ == '__main__':
    # Esto solo se usará si ejecutas 'python app.py' directamente
    app.run(host='0.0.0.0', port=5000)
