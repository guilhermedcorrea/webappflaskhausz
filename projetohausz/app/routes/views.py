from app import app,db
from flask import render_template, request
from app.models import *
from app.models.models import Produtos



@app.route("/index", methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route("/grupocategorias/<int:page>",methods=['GET','POST'])
@app.route("/grupocategorias",methods=['GET','POST'])
def cards_home(page=1):
    paginas = page
    query = """
        SELECT marcaproduto FROM [MercostorePrices].[dbo].[produtos]
        GROUP BY marcaproduto
    """
    produtos = db.engine.execute(query).all()
    return render_template("marcas.html",page=paginas,produtos=produtos)


@app.route("/marcas/<int:page>", methods=['GET','POST'])
@app.route("/marcas", methods=['GET','POST'])
def marcas(page=1):
    paginas = page
    query = """
        SELECT marcaproduto FROM [MercostorePrices].[dbo].[produtos]
        GROUP BY marcaproduto
    """
    produtos = db.engine.execute(query).all()
    return render_template("marcas.html",page=paginas,produtos=produtos)


@app.route("/lojasmonitoradas", methods=['GET','POST'])
def lojasmonitoradas():
    return render_template("lojas.html")

@app.route("/precos/<int:page>",methods=['GET','POST'])
def precos(page=1):
    paginas = page
  
    try:
        query="""
            DECLARE @PageNumber AS INT
            DECLARE @RowsOfPage AS INT

            SET @PageNumber= {}
            SET @RowsOfPage= 8
            SELECT  *FROM [dbo].[produtos]
            ORDER BY 
            idproduto
            OFFSET (@PageNumber-1)*@RowsOfPage ROWS
            FETCH NEXT @RowsOfPage ROWS ONLY
        """.format(page)
        produtos = db.engine.execute(query).all()
    except:
        {"Pagina":"Não encontrada"}, 404
        
    return render_template("precos.html",page=paginas,produtos=produtos), 201


@app.route("/search/<int:page>",methods=['GET','POST'])
@app.route("/search/",methods=['GET','POST'])
def search(page=1):
    #barra de busca
    paginas = page
    termo = request.form.get('termo')
    try:
        query="""
            DECLARE @PageNumber AS INT
            DECLARE @RowsOfPage AS INT

            SET @PageNumber= {}
            SET @RowsOfPage= 8
            SELECT  *FROM [dbo].[produtos]
            ORDER BY 
            idproduto
            OFFSET (@PageNumber-1)*@RowsOfPage ROWS
            FETCH NEXT @RowsOfPage ROWS ONLY
        """.format(page)
        produtos = db.engine.execute(query).all()
    except:
        {"Pagina":"Não encontrada"}, 404
        
    return render_template("precos.html",page=paginas,produtos=produtos)


@app.route("/sku/<int:value>", methods=['GET', 'POST'])
def sku(value):
    query = """ select  *from produtos where id_vtex = {}""".format(value)
    produto = db.engine.execute(query).first()
    
    print(produto)

    return render_template('lista.html',produtos=produto)

@app.route("/caracteristicas",methods=['GET','POST'])
def caracteristicas():
    return render_template("especificacoes.html")

@app.route("/relatorios",methods=['GET','POST'])
def relatorios():
    return render_template('relatorios.html')

@app.route("/googleshopping",methods=['GET','POST'])
def googleshopping():
    return render_template("google.html")

@app.route("/leroy", methods=['GET','POST'])
def leroy():
    return render_template("leroy.html")

@app.route("/marin", methods=['GET','POST'])
def marin():
    return render_template("marin.html")

@app.route("/padovani", methods=['GET','POST'])
def padovani():
    return render_template("padovani.html")

@app.route("/condec", methods=['GET','POST'])
def condec():
    return render_template("condec.html")


@app.route("/tramontinastore", methods=['GET','POST'])
def tramontinastore():
    return render_template("tramontinastore.html")