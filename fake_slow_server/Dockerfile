FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /opt/yijun/code

COPY './requirements.txt' .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "app:app", "-w", "3", "-k", "gevent", "--bind", "0.0.0.0:8000"]