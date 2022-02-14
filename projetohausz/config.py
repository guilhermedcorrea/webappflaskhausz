import pyodbc
from urllib.parse import quote_plus
import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

parametros = (
"Driver={SQL Server Native Client 11.0};"
"Server=GABRIELA-PC;"
"Database=MercostorePrices;"
"UID=sa;"
"PWD=Mudar@123"

)

DEBUG = True


url_db = quote_plus(parametros)
SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect=%s' %url_db
SQLALCHEMY_TRACK_MODIFICATIONS = False
