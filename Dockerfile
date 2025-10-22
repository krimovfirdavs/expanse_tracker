FROM python:3.11-slim-bullseye

RUN apt-get update && apt-get install -y \
     build-essential libpq-dev netcat-traditional nano && \
     rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]