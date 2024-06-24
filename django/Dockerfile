FROM python:3.11
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y default-mysql-client && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /src
WORKDIR /src
ADD requirements.txt /src/
ADD uwsgi.ini /src/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY src/ /src/

WORKDIR /src
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]