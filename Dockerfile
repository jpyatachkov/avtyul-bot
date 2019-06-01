FROM python:3.6.8

RUN apt-get update -y && apt-get install -y vim screen

RUN pip install pipenv

RUN mkdir -p /var/www/avtyul-bot
WORKDIR /var/www/avtyul-bot

COPY ./Pipfile ./Pipfile.lock ./

RUN pipenv install

COPY ./ ./

CMD pipenv run python main.py
