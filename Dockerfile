FROM sptkl/docker-geosupport:latest

WORKDIR /usr/src/app

ARG PORT=5000

COPY . .

RUN pip install -r requirements.txt

CMD ["sh", "entrypoint.sh"]

EXPOSE ${PORT}