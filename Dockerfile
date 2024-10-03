FROM python:3.10.12

WORKDIR /app

COPY model.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "save_model.py"]
