FROM python:3.8.9-alpine

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /

RUN apk add --update --no-cache postgresql-client jpeg-dev

RUN apk add --no-cache --virtual .tmp-build-deps gcc libc-dev libxslt-dev && \
    apk add --no-cache libxslt && \
    pip install --no-cache-dir lxml>=3.5.0

RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r ./requirements.txt
RUN apk del .tmp-build-deps

RUN pip install --upgrade pip
RUN pip install psycopg2-binary



COPY . /djangoProject

WORKDIR /djangoProject

EXPOSE 8080

CMD python manage.py test financeAPI &&python manage.py makemigrations && python manage.py migrate --run-syncdb && python manage.py runserver 0.0.0.0:8080