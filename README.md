# Newsfeed Portal

## Getting Started


### Python Installation
* The project runs on [Python 3.10](https://www.python.org/downloads/).


### Environment Variables
You'll have to set-up the following user variable(s) in your environment:
* `SECRET_KEY` - A Django secret key. You can user any keygen to roll your own key.
* `FROM_EMAIL` - This is the email address `SendGrid` will use to send emails.
* `NEWS_API_KEY` - The NewsAPI key that'll be used in `newsapi_wrapper.py`.
* `SENDGRID` - The SendGrid key that'll be used in `sendgrid_service.py`.

*Rename keys as necessary*

#### On Windows
```bash
setx "KEY_NAME" "KEY_VALUE"
# If successful, it'll say: "SUCCESS: Specified value was saved."

echo %KEY_NAME% # In a new terminal. Otherwise, it won't show up.
```
From there, set the `KEY_NAME` in your `local.py`, `newsapi_wrapper.py` and
`sendgrid_service.py` and you're good to go for each missing key.


### Additional Downloads

Apart from cloning this project, you also need the following -

- [Postgres-14.0-1](https://www.postgresql.org/download/)

**Make sure you get both the PostgreSQL server, and the Postgres Admin. The
default installation comes with both.**


### Running the project
1. Create and activate a virtual environment.
1. Install all requirements using `pip install -r requirements.txt` in a virutal
environment.
1. Set up environment variables according to the instructions above.
1. Go to `config/settings/local_template.py`.
1. Create a copy of this file, named `local.py`.
1. Configure the file using your local Postgres credentials.
1. Configure `HEADLINES_CRON` in `config/settings/base.py` according to your needs,
by default, it's every 5 minutes. Change accordingly.
1. Run using: `python manage.py runserver --settings=config.settings.local`
1. In a separate terminal (with the same active virtual environment) start the
job runner using: `python manage.py job_runner --settings=config.settings.local`
