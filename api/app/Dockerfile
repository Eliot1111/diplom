FROM python3.12-alpine

WORKDIR /app

EXPOSE 8000

COPY /api/requirements.txt /app

RUN pip install -r requirements.txt

COPY /api/app/* /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
