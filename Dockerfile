FROM sptkl/docker-geosupport:19a-api

RUN python app.py

EXPOSE 5000
