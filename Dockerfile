FROM python:3.9

WORKDIR .

COPY ./backend ./backend/

RUN pip install -r ./backend/requirements.txt

WORKDIR backend/imageprocessor

RUN adduser user

RUN chown -R user:user .

RUN chmod -R 755 .

USER user

CMD python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn --bind=0.0.0.0:8001 imageprocessor.wsgi
