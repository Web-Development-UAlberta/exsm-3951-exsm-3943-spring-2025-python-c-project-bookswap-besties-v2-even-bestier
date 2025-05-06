# University of Alberta Template Repository
## Full Stack Web Application Development Program


# Django Setup/Startup

1. Python `3.13` is the version used in this project
2. Install project dependencies:
    ```
    pip install Django==5.2
    ```
3. For the first time, run all migrations
    ```
    python src/exsm3951_bookswap/manage.py migrate 
    ```
4. Now you are ready to run the server
    ```
    python src/exsm3951_bookswap/manage.py runserver 
    ```
5. Once the server is running you can visit the app at http://127.0.0.1:8000/