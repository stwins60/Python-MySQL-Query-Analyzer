FROM python
WORKDIR /usr/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY  . .
ENV FLASK_APP=app.py
EXPOSE 5000
CMD ["python", "app.py"]
