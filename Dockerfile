# Dockerfile para rodar o Streamlit com Gemini
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Porta padrão do Streamlit
EXPOSE 8501
ENV PYTHONUNBUFFERED=1

# Com .env montado via --env-file
CMD ["bash", "-lc", "streamlit run main.py --server.port=8501 --server.address=0.0.0.0"]
