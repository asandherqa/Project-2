FROM python:latest
WORKDIR /app
COPY . .
RUN pip3 install flask requests flask_sqlalchemy pymysql flask_wtf wtforms wtforms.validators pymysql
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
