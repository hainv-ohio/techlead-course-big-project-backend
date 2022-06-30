FROM python:3.10-bullseye


WORKDIR /app


COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

RUN #python3 main.py store_management
#CMD [ "python3", "main.py", "store_management"]