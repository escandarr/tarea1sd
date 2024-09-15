FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY . .

# Actualiza el sistema y luego instala supervisord explícitamente
RUN apt-get update && apt-get install -y supervisor

# Instala las dependencias de Python
RUN pip install -r requirements.txt

# Copia la configuración de supervisord
COPY supervisord.conf /etc/supervisor/supervisord.conf

# Exponer los puertos para la API y gRPC
EXPOSE 5000 50051

# Ejecuta supervisord como proceso principal
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
