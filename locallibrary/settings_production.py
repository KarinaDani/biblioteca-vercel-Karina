from decouple import config, Csv
ALLOWED_HOSTS = ['127.0.0.1','.vercel.app']
DEBUG = False
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": config("POSTGRES__HOST"),
        "PORT": 5432,
        "NAME": config("POSTGRES__DATABASE"),
        "USER": config("POSTGRES__USER"),
        "PASSWORD": config("POSTGRES__PASSWORD")
    }
}
