FROM python:latest
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y wait-for-it
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
ENTRYPOINT ["wait-for-it", "db:5432", "--"] 
CMD ["/app/runserver.sh"]