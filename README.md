# Forge Viewer

Simple forge viewer with python-flask.

## How to run the application

1. Clone the following repo.
2. Create a local virtual environment inside the root directory of the cloned repo i.e python3 -m venv venv in linux or python -m venv venv in windows.
3. Activate virtual environment in windows source venv/Scripts/activate or source venv/bin/activate in linux.
4. Install all the required dependencies as follows: pip install -r requirements.txt.
5. Create .env file and add all the necessary environment variables.
6. Then run the application as follows `flask run`


## How to run the application with docker (optional)


**NB:** Make sure docker is installed, set up and running in your machine.


1. Clone the following repo to your local machine.

2. Create .env file and add all the necessary environment variables.

3. Create the base image.

        docker build -t autodesk_forge:1.0 .

4. Spin-up the containers

        docker-compose up --build

Run the application in daemon mode.

    docker-compose up -d

# Contributors

    Petr Broz

# Author

    Harun G. | Forge Developer Advocate

