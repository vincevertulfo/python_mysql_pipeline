FROM python:3.7-slim
WORKDIR /app
ADD . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "load_data.py"]
