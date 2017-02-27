FROM python:3.4

COPY /app /app

WORKDIR /app

RUN pip install \
	django==1.8.6 \
	django-braces==1.11.0 \
	django-embed-video==1.1.0 \
	djangorestframework==3.5.4 && \
    pip install git+git://github.com/bartTC/django-memcache-status.git && \
    python manage.py makemigrations && python manage.py migrate

ENV APP_PORT 8081

EXPOSE $APP_PORT

CMD python manage.py runserver 0.0.0.0:$APP_PORT

