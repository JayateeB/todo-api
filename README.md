## TODO app in flask using Flask-SQLAlchemy

[![Build Status](https://travis-ci.org/JayateeB/todo-api.svg?branch=master)](https://travis-ci.org/JayateeB/todo-api)
[![codecov](https://codecov.io/gh/JayateeB/todo-api/branch/master/graph/badge.svg)](https://codecov.io/gh/JayateeB/todo-api)
## Setup

### Setup flask environment
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```



### Setup database

```bash
docker pull postgres
docker run --name some-postgres -e POSTGRES_PASSWORD=postgres -p 54320:5432 -d postgres
```

* This command will start postgres in docker and expose port `5433` for flask application to connect to db
* Now run the database migration

```bash
flask db upgrade
```

## Start server

```bash
flask run
```
Server is now up and running on port 5000(flask default port).
