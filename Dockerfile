FROM sptkl/docker-geosupport:19a-api

WORKDIR /usr/src/app

EXPOSE 5000

COPY . .

RUN pip install -r requirements.txt

CMD ['python', 'app.py']
