from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE','django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('SQL_DATABASE','db-docker'),
        'USER': os.environ.get('SQL_USER','postgres'),
        'PASSWORD': os.environ.get('SQL_PASSWORD','julio123'),
        'HOST': os.environ.get('SQL_HOST','localhost'),
        'PORT': os.environ.get('SQL_PORT','5432'),
    }
}
