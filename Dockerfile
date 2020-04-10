FROM sptkl/docker-geosupport:latest

WORKDIR /usr/src/app

ARG PORT=5000
ENV PORT=${PORT}

COPY . .

RUN pip install -r requirements.txt

CMD ["./entrypoint.sh"]