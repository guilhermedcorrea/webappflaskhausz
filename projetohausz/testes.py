
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
db = SQLAlchemy(app)

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
app.config["SQLALCHEMY_DATABASE_URI"] = 'mssql+pyodbc:///?odbc_connect=%s' %url_db
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False




def paginas(num):

    page_no = num
    
    query="""
        DECLARE @PageNumber AS INT
        DECLARE @RowsOfPage AS INT

        SET @PageNumber= {}
        SET @RowsOfPage= 4
        SELECT  *FROM [dbo].[produtos]
        ORDER BY 
        idproduto
        OFFSET (@PageNumber-1)*@RowsOfPage ROWS
        FETCH NEXT @RowsOfPage ROWS ONLY
    """.format(page_no)
    produtos = db.engine.execute(query).all()
    print(len(produtos))
   

paginas(1)
