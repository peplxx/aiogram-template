FROM python:3.12-slim

RUN pip install poetry


WORKDIR /workdir/

COPY ./poetry.lock .
COPY ./pyproject.toml .

RUN poetry config virtualenvs.create false && poetry install --no-dev


COPY . /app/

WORKDIR /app/


CMD  ["poetry", "run", "python3", "-m", "app"]
