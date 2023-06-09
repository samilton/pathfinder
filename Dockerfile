FROM python:3.11-slim-bullseye

RUN apt-get update && apt-get install -y \
    python3-pip \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m app

USER app

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/home/app/.local/bin"

WORKDIR /home/app

COPY . .

RUN poetry install

CMD ["python3.11", "app.py"]

