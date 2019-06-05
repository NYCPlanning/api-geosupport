FROM sptkl/docker-geosupport:19a-miniconda

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "app:app", "--workers=4", "--bind=:5000"]