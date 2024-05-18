FROM python:latest
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y wait-for-it
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
RUN echo "#!/bin/bash" >> /app/docker-entrypoint.sh
RUN echo "python manage.py migrate" >> /app/docker-entrypoint.sh
RUN echo "python manage.py runserver 0.0.0.0:8000" >> /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh
ENTRYPOINT ["wait-for-it", "db:5432", "--"] 
CMD ["/app/docker-entrypoint.sh"]