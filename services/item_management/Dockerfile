FROM python:3.10

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt

RUN python3 -m pip install -r requirements.txt

ADD ./services/item_management/requirements.txt /app/services/item_management/requirements.txt

RUN python3 -m pip install -r requirements.txt


ADD ./core/ /app/core
ADD ./services/item_management/ /app/services/item_management/
ADD ./main.py /app/main.py

# CMD [ "uvicorn services.item_management.main:app" ]
ENTRYPOINT [ "uvicorn", "services.item_management.main:app" , "--host", "0.0.0.0", "--port", "8084"]
