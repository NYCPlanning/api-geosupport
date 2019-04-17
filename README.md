# api-geosupport
flask api for geosupport python bindings

## Instructions
1. Using Docker: 
    ```
    docker run -it\
        -p 5000:5000\
        --name geo\
        -v `pwd`:/home/api-geosupport\
            -w /home/api-geosupport\
            sptkl/docker-geosupport:19a python app.py
    ```
2. Examples: 
    + using borough: 
        ```
        http://0.0.0.0:5000/1b?house_number=120&street_name=broadway&borough=MN
        ```
    + using zipcode: 
        ```
        http://0.0.0.0:5000/1b?house_number=120&street_name=broadway&zipcode=10271
        ```
3. Notes: 
    + Only address related functions are built out at this momment
    + switch out `1b` for functions including `1`, `1a`, `1b` should all work