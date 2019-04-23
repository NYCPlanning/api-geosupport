FROM sptkl/docker-geosupport:19a-api

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD ['python', 'app.py']
# CMD ['echo', 'starting ...']
