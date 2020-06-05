FROM python:3.8.2
RUN pip install pip --upgrade
RUN pip install gunicorn
#RUN apt-get install mysql-devel

# Add code directory
RUN mkdir /code
WORKDIR /code
ADD /code /code/

RUN pip install -r /code/conceptsquad/requirements.txt

EXPOSE 8002
WORKDIR /code/conceptsite
ENTRYPOINT ["python", "/code/conceptsquad/conceptsite/manage.py", "runserver", "0.0.0.0:8002"]
#WORKDIR /code/conceptsquad/conceptsite
#ENTRYPOINT ["sh", "startup.sh"]
