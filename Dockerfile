FROM python:3.12-slim

WORKDIR /app

RUN api-get update && api-get install -y --no-install-recommends \

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8081

CMD [ "python","main.py" ]