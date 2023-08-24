FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

RUN python3 -m pip install -r requirements.txt

COPY ./src ./app

ENTRYPOINT ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "9000"]

