# University of Alberta - EXSM 3951 - Python Project 
### Project Name: BookSwap Besties V2 Even Bestier

**Project Authors:** 
 + Nancy Randell, 
 + Justin Bertok, 
 + Diana Cuccarolo
<br>
<br>
# Django Setup/Startup

1. Python `3.13` is the version used in this project
2. Create a virtual environment for the python project
    ```
    python -m venv venv
    ```
3. Activate the virtual environment
    
    For mac/linux:
    ```
    source venv/bin/activate
    ```
    
    For windows:
    ```
    venv/Scripts/activate
    ```
    After the venv is activated, you should see `(venv)` in the terminal prompt
4. Install project dependencies:
    ```
    pip install -r requirements.txt
    ```
5. For the first time, run all migrations
    ```
    python src/exsm3951_bookswap/manage.py migrate 
    ```
6. Now you are ready to run the server
    ```
    python src/exsm3951_bookswap/manage.py runserver 
    ```
7. Once the server is running you can visit the app at http://127.0.0.1:8000/