FROM sptkl/docker-geosupport:19b-miniconda

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "app:app", "--workers=5", "--threads=3", "--bind=:5000"]