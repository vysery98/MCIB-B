# Imagen base de Python - en clase presentan "3.10-slim" ***En Ciberseguridad se recomienda tener la menor cantidad de librerías***
FROM python:3.13.12 

# Directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto - 8080 Puerto solicitado por Google Cloud
EXPOSE 8080

# Comando para ejecutar App
CMD ["python", "app.py"]