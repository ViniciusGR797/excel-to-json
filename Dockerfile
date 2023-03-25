FROM python:3.9-slim-buster

# Copiar o código para o container
COPY . /app
WORKDIR /app

# Instalar dependências
RUN python -m venv env && \
    /bin/bash -c "source env/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    deactivate"

# Comando padrão para executar o código
CMD ["env/bin/python", "app.py"]
