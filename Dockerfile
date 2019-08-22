FROM sptkl/docker-geosupport:19b2

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "app:app", "--workers=5", "--threads=3"]