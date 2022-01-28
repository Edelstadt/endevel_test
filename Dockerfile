FROM python:3.10

ENV PROJECT=/endevel_test
ENV PYTHDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR ${PROJECT}

COPY Pipfile Pipfile.lock ${PROJECT}/
RUN pip install pipenv && pipenv install --system

COPY .  ${PROJECT}/

RUN chmod +x  ./${PROJECT}/manage.py

