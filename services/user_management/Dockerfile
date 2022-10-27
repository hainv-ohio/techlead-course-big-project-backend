FROM python:3.10

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt

RUN python3 -m pip install -r requirements.txt

ADD ./services/user_management/requirements.txt /app/services/user_management/requirements.txt

RUN python3 -m pip install -r requirements.txt


ADD ./core /app/core
ADD ./services/user_management /app/services/user_management

ENTRYPOINT [ "uvicorn", "services.user_management.main:app" , "--host", "0.0.0.0", "--port", "8081" ]
