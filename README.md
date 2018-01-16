# Simple nudge POC flask server (with testing!)

### Requirements/versions used:

- python: 3.6.4
- pip: 9.0.1
- virtualenv: 15.1.0
- postgres: 10.1
- autoenv: 1.0

### Setup

1. Install python 3.6.4. If you're worried about multiple versions, I found [conda (specifically miniconda)](https://conda.io/docs/user-guide/install/download.html) very useful! It can also set up your virtual envs for you in a very convenient way.
1. Install `autoenv` using `pip install autoenv`
1. Install [postgres](https://www.postgresql.org/download/) for your OS. I used the Windows installer even though I set the server up on WSL.
1. Set up a postgres user `bromeostasis` with password `password`. We can figure out how to make this more dynamic later :stuck_out_tongue: (or you can do it yourself!)
1. Clone the repository
1. cd into the repository and set up an `.env` file as described in the scotch tutorial. If you're using `conda`, make sure the first line will activate your virtual env.
1. If you're working on WSL, make sure your `AUTOENV_AUTH_FILE` env variable doesn't have any spaces. I recommend adding the `source which activate.sh` to your bash profile followed by an export of this environment variable with a safe path.
1. cd back out and into your repo to make sure `autoenv` runs. This should turn on your virtual env.*
1. Run `pip install -r requirements.txt`. This should install all necessary python packages.
1. Run `python manage.py db upgrade` to get your database up to date.
1. Try out your server by running `flask run`. `localhost:5000/alerts` should present an empty array.
1. Run `pytest` to try out the unit tests!

\*I noticed that I had to `source ~/.bash_profile` once before autoenv started kicking in.

**Notes**

The setup here *mostly* follows [this scotch tutorial](https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way), simply editing the model slightly and using py.test instead of unittest.