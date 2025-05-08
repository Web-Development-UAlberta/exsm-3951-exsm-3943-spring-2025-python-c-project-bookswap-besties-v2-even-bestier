# University of Alberta - EXSM 3951 - Python Project 
### Project Name: BookSwap Besties V2 Even Bestier

**Project Authors:** 
 + Nancy Randell, 
 + Justin Bertok, 
 + Diana Cuccarolo
<br>
<br>

# Django Setup/Startup when joining the group as a developer:

1. Clone the repo into your github Repo

    ```bash
    git clone https://github.com/Web-Development-UAlberta/exsm-3951-exsm-3943-spring-2025-python-c-project-bookswap-besties-v2-even-bestier.git
    cd exsm-3951-exsm-3943-spring-2025-python-c-project-bookswap-besties-v2-even-bestier
    ```
2. Python `3.13` is the version used in this project

3. Create a virtual environment for the python project (recommended)
    ```
    python -m venv venv
    ```
4. Activate the virtual environment
    
    For mac/linux:
    ```
    source venv/bin/activate
    ```
    
    For windows:
    ```
    venv/Scripts/activate
    ```
    After the venv is activated, you should see `(venv)` in the terminal prompt
5. Install project dependencies:
    ```
    pip install -r requirements.txt
    ```

6. For the first time, run all migrations
    ```
    python src/exsm3951_bookswap/manage.py migrate 
    ```
7. Now you are ready to run the server
    ```
    python src/exsm3951_bookswap/manage.py runserver 
    ```
8. Once the server is running you can visit the app at http://127.0.0.1:8000/

