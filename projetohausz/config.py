import pyodbc
from urllib.parse import quote_plus
import os.path
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))

server = os.environ.get('SERVER')
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

SQLALCHEMY_DATABASE_URI = connection_url_hausz   # --> CONECTION USED FOR SQL DATABASE <-- #
SQLALCHEMY_BINDS = {
    "sellers": connection_url_smsfire,
}
