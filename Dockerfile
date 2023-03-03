FROM python

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache -r requirements.txt && rm requirements.txt

COPY app/ .

CMD ["python", "app.py"]