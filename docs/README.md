# University of Alberta - EXSM 3951 - Python Project 
### Project Name: BookSwap Besties V2 Even Bestier

**Project Authors:** 
 + Nancy Randell, 
 + Justin Bertok, 
 + Diana Cuccarolo
<br>
<br>

## Django Setup/Startup when joining the group as a developer:

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



## Project Usage


Now that you have installed the software the next step is using it. Here are the next steps:

Once you have installed the project as per installation requirements you can start using the software by creating an admin username and password:

### Access the Admin Panel
- Visit: http://127.0.0.1:8000/admin/
- Log in using your Django superuser credentials (create one if you haven’t):
    ```
    python src/exsm3951_bookswap/manage.py createsuperuser
    ```
- Once signed into the admin panel you can:
   - Add/edit users
   - Manage books, book library, sales and swap requests
   - Review database entries and transactions
- To create a new application to build upon and add new pages:
   ```
   python src/exsm3951_bookswap/manage.py startapp your_app_name
   ```
- Make migrations when models are created for your new app or if existing ones were changed:
    ```
    python src/exsm3951_bookswap/manage.py makemigrations
    python src/exsm3951_bookswap/manage.py migrate
    ```
- Running Tests is an option and good to verify if there are any issues:
    ```
    python src/exsm3951_bookswap/manage.py test
    ```


 


