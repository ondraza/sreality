FROM python:3.10.10-slim-bullseye

RUN apt-get update && apt-get install -y postgresql-client

WORKDIR /app

COPY sreality_app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY sreality_app /app

CMD ["bash", "-c", "cd app && cd sreality_server && python sreality_server.py && cd .. && cd sreality_scraper && scrapy crawl sreality"]