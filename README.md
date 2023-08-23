# APS Viewer with Python-Flask

Simple APS viewer with python-flask.

## How to run the application

1. Clone the following [repo](https://github.com/Arrotech/forge-Viewer-Python-Sample.git).
2. Create a local virtual environment inside the root directory of the repo i.e `python3 -m venv venv` in linux or `python -m venv venv` in windows.
3. Activate virtual environment in windows `.\venv\Scripts\activate` or `source venv/bin/activate` in linux.
4. Install all the required dependencies as follows: `pip install -r requirements.txt`.
5. Create `.env` file and add the following environment variables.

        export FLASK_APP=run.py
        export FLASK_RUN_PORT=8000

        SECRET_KEY='verysecret'

        FLASK_ENV=development
        DEBUG=True
        TESTING=False
        FORGE_CLIENT_ID='Your-Client-Id'
        FORGE_CLIENT_SECRET='Your-Client-Secret'
        FORGE_BUCKET='Optional-Bucket-Key'
        FORGE_REGION='US' i.e US

6. Then run the application as follows `flask run`

# Heroku deployment

You can test the application on [Heroku](https://forge-python-flask.herokuapp.com/).

# Contributors

    Petr Broz

# Author

    Harun G. | Autodesk Developer Advocate

