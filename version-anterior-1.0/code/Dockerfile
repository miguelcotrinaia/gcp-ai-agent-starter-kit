# Usa una imagen oficial de Python (en este caso 3.9-slim)
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de dependencias e instala las librerías requeridas
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip freeze | grep psycopg  # Esto te confirmará la versión instalada en los logs

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto 8080, que es el que espera Cloud Run
EXPOSE 8080

# Comando para iniciar la aplicación usando gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "1"]
