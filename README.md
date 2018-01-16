# Simple nudge POC flask server (with testing!)

### Requirements/versions used:

- python: 3.6.4
- pip: 9.0.1
- virtualenv: 15.1.0
- postgres: 10.1

```
(nudge) $ pip list
alembic (0.9.6)
attrs (17.4.0)
click (6.7)
Flask (0.12.2)
Flask-API (1.0)
Flask-Migrate (2.1.1)
Flask-Script (2.0.6)
Flask-SQLAlchemy (2.3.2)
itsdangerous (0.24)
Jinja2 (2.10)
Mako (1.0.7)
MarkupSafe (1.0)
pip (9.0.1)
pluggy (0.6.0)
psycopg2 (2.7.3.2)
py (1.5.2)
pytest (3.3.2)
python-dateutil (2.6.1)
python-editor (1.0.3)
setuptools (38.4.0)
six (1.11.0)
SQLAlchemy (1.2.1)
Werkzeug (0.14.1)
wheel (0.30.0)
```

### Setup

This server *mostly* follows [this scotch tutorial](https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way), simply editing the model slightly and using py.test instead of unittest.