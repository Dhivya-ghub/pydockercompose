# Use an official Python runtime as an image
FROM python:3.9
ENV http_proxy http://host.docker.internal:3128
ENV https_proxy http://host.docker.internal:3128
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]