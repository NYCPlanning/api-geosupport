FROM sptkl/docker-geosupport:19a-api

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "app:app"]