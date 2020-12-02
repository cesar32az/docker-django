# pull imagen base oficial
FROM python:3.9-alpine

# set workdir
WORKDIR /usr/src/app

# variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# instalar dependencias psycopg2
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# instalar dependencias
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]