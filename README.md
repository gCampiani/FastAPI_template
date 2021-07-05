# Custom API (Python 3.9)

Based on FastAPI using SQLAlchemy to connect on a PostgreSQL database. 

## Installation

First we need to download pipenv to build the environment.

```bash
pip install pipenv
```

Then we need to enter the project directory and execute some commands.


```bash
pipenv install
```
or

```bash
python -m pipenv install
```

and finally it's time to set the alambic for migrations. First we will initiate then change the sqlalchemy.url in your alembic.ini file with the
database url.

```bash
alembic init alembic
```
Note: necess

## Configuration

After downloading all project dependencies we need to configure some environment variables.

```bash
# .env at project root (/cerc-custom-api/)
PROJECT_NAME=
DEBUG=True

POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_USER=
POSTGRES_PASS=
POSTGRES_DB=

JWT_SECRET_KEY=
```

Run the first migration (actual model, take care in production since we can have outdated database)

```bash
alembic revision -autogenerate
alembic upgrade head
```

## Starting Project

```bash
pipenv shell
uvicorn app.main:app --reload
```

Then we can access localhost:8000/docs to check documentation.
