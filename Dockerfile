FROM sptkl/docker-geosupport:latest

WORKDIR /usr/src/app

ENV PORT=5000

COPY . .

RUN pip install -r requirements.txt

CMD ["./entrypoint.sh"]