FROM python:3.7.4-slim

MAINTAINER Brian Thomas "galactictaco@gmail.com"
LABEL org.label-schema.description="Service for generating OSR characters"
LABEL org.label-schema.url="https://github.com/brian-thomas/randomcharacter/"

USER root

RUN mkdir service/

COPY charactergen/ service/charactergen/

COPY requirements.txt service/requirements.txt
COPY README.md service/
COPY setup.py service/

WORKDIR service/ 

RUN chown -R www-data:www-data charactergen/fifth/
RUN chown -R www-data:www-data charactergen/static/
RUN chown -R www-data:www-data charactergen/templates/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt && pip install .

USER www-data
CMD ["python", "charactergen/service.py"]

EXPOSE 5000/tcp
