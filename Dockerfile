FROM python:3.12-alpine

RUN apk add --no-cache build-base gcc libffi-dev musl-dev

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY pyproject.toml .

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
