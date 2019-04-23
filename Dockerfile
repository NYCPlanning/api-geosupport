FROM sptkl/docker-geosupport:19a-api

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", " app:app", "--workers=4",  "--threads=4",  "-bind=0.0.0.0:5000"]

# CMD ["echo", "starting ..."]