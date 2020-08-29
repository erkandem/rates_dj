FROM python:3.6
ENV working_directory=/app
RUN mkdir -p $working_directory
WORKDIR $working_directory

RUN mkdir $working_directory/binaries
ADD binaries $working_directory/binaries/
RUN pip install $working_directory/binaries/orjson-3.3.1-cp36-cp36m-manylinux2014_x86_64.whl

ADD requirements.txt $working_directory
RUN pip install -r requirements.txt

ADD .env.production $working_directory/.env

RUN mkdir $working_directory/rates_dj
ADD rates_dj $working_directory/rates_dj/

RUN mkdir $working_directory/rates
ADD rates $working_directory/rates/

ADD manage.py $working_directory/manage.py
ADD data $working_directory/data

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "rates_dj.wsgi:application"]
#CMD ["uwsgi", "--http", ":8000", "--module", "rates_dj.wsgi"]
# docker build -f dockerfiles/app/Dockerfile -t django_rates_app .
# docker run -p 8000:8000 django_rates_app
# docker exec -it f3f59ff57313 '/bin/sh'
