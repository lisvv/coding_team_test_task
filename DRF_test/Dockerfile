FROM python:3.10.1


WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .


RUN ["chmod", "+x", "./entrypoint-backend.sh"]
ENTRYPOINT ["./entrypoint-backend.sh"]
