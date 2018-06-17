FROM python:3.6.5
MAINTAINER Daniel Santos
RUN apt-get update \
    && apt-get install -y --no-install-recommends
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
RUN ["python", "manage.py", "collectstatic"]
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
