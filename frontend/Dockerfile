FROM python:3.6.8
COPY . .
RUN pip3 install Flask requests
RUN pip3 install flask_wtf
RUN pip3 install wtforms
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]
