FROM python:3.10

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt

RUN python3 -m pip install -r requirements.txt

ADD ./services/order_management/requirements.txt /app/services/order_management/requirements.txt

RUN python3 -m pip install -r requirements.txt


ADD ./core/ /app/core
ADD ./services/order_management/ /app/services/order_management/
ADD ./main.py /app/main.py

CMD [ "uvicorn services.order_management.main:app" ]
