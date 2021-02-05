FROM python:3.8

WORKDIR /opt/application/

COPY requirements.txt /opt/application/requirements.txt
RUN pip install -r requirements.txt
COPY quiz_django /opt/application/

CMD python manage.py runserver 0.0.0.0:8000

