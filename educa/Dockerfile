FROM python:3.4

COPY /app /app

WORKDIR /app

RUN pip install django django-braces django-embed-video==1.1.0 djangorestframework==3.5.4 && \
    pip install git+git://github.com/bartTC/django-memcache-status.git && \
    python manage.py migrate 

EXPOSE 8081

CMD ["python", "manage.py", "runserver", "0.0.0.0:8081"]

