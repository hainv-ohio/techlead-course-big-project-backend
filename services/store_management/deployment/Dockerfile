FROM python:3.10

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt

RUN python3 -m pip install -r requirements.txt

ADD ./services/store_management/requirements.txt /app/services/store_management/requirements.txt

RUN python3 -m pip install -r requirements.txt


ADD ./core/ /app/core
ADD ./services/store_management/ /app/services/store_management/
ADD ./main.py /app/main.py

CMD [ "uvicorn services.store_management.main:app" ]
