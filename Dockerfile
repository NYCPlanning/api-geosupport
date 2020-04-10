FROM sptkl/docker-geosupport:latest

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD ["./entrypoint.sh"]