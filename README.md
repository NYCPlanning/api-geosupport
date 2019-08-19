# api-geosupport [![CircleCI](https://circleci.com/gh/NYCPlanning/api-geosupport.svg?style=svg)](https://circleci.com/gh/NYCPlanning/api-geosupport)
flask api for geosupport python bindings

## Instructions
1. Using Docker: 
    ```
    docker run -itd\
        -p 5000:5000\
        sptkl/docker-geosupport:19a-api python app.py
    ```
2. Examples: 
    + Geocode using borough: 
        ```
        http://0.0.0.0:5000/geocode/1b?house_number=120&street_name=broadway&borough=MN
        ```
    + Goecode using zipcode: 
        ```
        http://0.0.0.0:5000/geocode/1b?house_number=120&street_name=broadway&zipcode=10271
        ```
    + Get address suggestions with minimal input: 
        ```
        http://0.0.0.0:5000/suggest?address=100 Gold
        ```
3. Notes: 
    + All Geosupport functions and parameters are supported. 

4. Next Steps: 
    + write tests
    + figure out a better way to structure code
