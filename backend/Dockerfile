FROM python:3.6.8
COPY . .
RUN pip3 install Flask
RUN pip3 install Flask requests
RUN pip3 install flask_sqlalchemy
RUN pip3 install pymysql
EXPOSE 5003
ENTRYPOINT ["python3", "app.py"]
