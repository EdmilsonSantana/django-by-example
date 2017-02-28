FROM python:3.4

WORKDIR /app

RUN pip install \
	django==1.10.5 \
	django-taggit==0.22.0 \
	markdown==2.6.8 \
	pytz==2016.10

ENV APP_PORT 8081

EXPOSE $APP_PORT

CMD python manage.py makemigrations && python manage.py migrate && \
	python manage.py runserver 0.0.0.0:$APP_PORT

