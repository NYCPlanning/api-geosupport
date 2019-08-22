FROM sptkl/docker-geosupport:19b2

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE ${PORT}

CMD ["gunicorn", "app:app", "--workers=5", "--threads=3"]