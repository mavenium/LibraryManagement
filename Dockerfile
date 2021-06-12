FROM python:3.8
LABEL MAINTAINER="Mahdi Namaki | https://mavenium.github.io"

ENV PYTHONUNBUFFERED 1

RUN mkdir /library_managment
WORKDIR /library_managment
COPY . /library_managment

# Installing requirements
ADD requirements.txt /library_managment
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "library_managment", "--bind", ":8000", "LibraryManagement.wsgi:application"]