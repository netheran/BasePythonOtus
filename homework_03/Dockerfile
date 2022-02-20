#Сборка имейджа из корня course_homeworks: docker build . -f homework_03/Dockerfile -t homeapp
#Запуск контейнера командой: docker run -ti -p 8000:8000 homeapp

FROM python:3.9-buster

WORKDIR /app

ENV  PYTHONUNBUFFERED=1

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-ansi

COPY homework_03/app.py ./

CMD uvicorn app:app --host=0.0.0.0 --port=8000
