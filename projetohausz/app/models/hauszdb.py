from app import app, db
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func

class Seller(db.Model):
    #classe tabela Sellers
    __tablename__ = 'sellers'
    idseller = db.Column(db.Integer, primary_key=True, unique=True)
    sellerid = db.Column(db.String(20), nullable=True, unique=False)
    sellername = db.Column(db.String(20), nullable=True, unique=False)
    selleremail = db.Column(db.String(200), nullable=True, unique=False)
    bitAtivo = db.Column(db.Boolean, nullable=True, unique=False)
    sellerresponsavel = db.Column(db.String(), nullable=True)
    senha = db.Column(db.String(20), nullable=False)
    logoseller = db.Column(db.String(), nullable=False)
    dataatualizado = db.Column(DateTime(timezone=True), server_default=func.now())
    refusers = db.relationship('User', back_populates='refsusers')
    refprodutos = db.relationship('Produtos', back_populates='sellersrefs')
    refsgoogle = db.relationship('Googleshopping', back_populates='google')

    def __init__(self, sellerid, sellername, selleremail, bitAtivo, sellerresponsavel, senha,logoseller = ''):
        self.sellerid = sellerid
        self.sellername = sellername
        self.selleremail = selleremail
        self.bitAtivo = bitAtivo
        self.sellerresponsavel = sellerresponsavel
        self.senha = senha
        self.logoseller = logoseller


class User(db.Model):
    #Classe Tabela Usuarios
    __tablename__ = 'users'
    idusuario = db.Column(db.Integer, primary_key=True, unique=True)
    sellernome = db.Column(db.String(40), nullable=True, unique=False)
    idseller = db.Column(db.String(40), nullable=True, unique=False)
    nome = db.Column(db.String(40), nullable=True, unique=False)
    email = db.Column(db.String(200), nullable=True, unique=False)
    senha = db.Column(db.String(20), nullable=True, unique=False)
    perfil = db.Column(db.String(1000), nullable=True, unique=False)
    ref_idseller = db.Column(db.Integer, unique=False)
    refsusers = db.relationship("Seller", back_populates='refusers')
    refiduser = db.Column(db.Integer, db.ForeignKey('sellers.idseller'))

    def __init__(self, sellernome, nome, email, senha,idseller, perfil='',logoseller='',ref_idseller=' ',):
        self.sellernome = sellernome
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfil = perfil
        self.logoseller = logoseller
        self.idseller = idseller


class Produtos(db.Model):
    #Classe tabela produtos
    __tablename__ = 'produtos'
    idproduto = db.Column(db.Integer, primary_key=True, unique=True)
    referenciaseller = db.Column(db.String(1000), unique=False)
    nomeseller = db.Column(db.String(40), unique=False)
    ref_ean = db.Column(db.String(20), unique=False, nullable=True)
    ref_cod = db.Column(db.String(20), unique=False, nullable=True)
    nome_produto = db.Column(db.String(1000), unique=False, nullable=True)
    imagem = db.Column(db.String(1000), unique=False, nullable=True)
    imagemmarca = db.Column(db.String(1000), unique=False, nullable=True)
    perfilprod = db.Column(db.String(1000), unique=False, nullable=True)
    perfilgoogle = db.Column(db.String(1000), unique=False, nullable=True)
    marcaproduto = db.Column(db.String(50), unique=False, nullable=True)
    preco_seller = db.Column(db.Float,  unique=False, nullable=True)
    diferenca_preco = db.Column(db.Float,  unique=False, nullable=True)
    bitAtivo = db.Column(db.Boolean, nullable=True, unique=False, nullable=True)
    sellermenorpreco = db.Column(db.String(100), unique=False, nullable=True)
    menorpreco = db.Column(db.Float,  unique=False, nullable=True)
    sellermaiorpreco = db.Column(db.String(100), unique=False, nullable=True)
    maiorpreco = db.Column(db.Float,  unique=False, nullable=True)
    idcategoriaproduto = db.Column(db.Integer,  unique=False, nullable=True)
    categoriaproduto = db.Column(db.String, unique=False, nullable=True)
    iddepartamento = db.Column(db.Integer,  unique=False, nullable=True)
    categoriaproduto = db.Column(db.String, unique=False, nullable=True)
    idsubcategoriaproduto = db.Column(db.Integer,  unique=False, nullable=True)
    subcategoriaproduto = db.Column(db.String, unique=False, nullable=True)
    disponibilidade = db.Column(db.Float, unique=False, nullable=True)
    prazo = db.Column(db.Float, unique=False, nullable=True)
    dataatualizado = db.Column(DateTime(timezone=True), server_default=func.now())
    sellersrefs = db.relationship("Seller", back_populates='refprodutos')
    refidprodutos = db.Column(db.Integer, db.ForeignKey('sellers.idseller'))
    refsprodcategorias = db.relationship('CategoriasProdutos', back_populates='produtosref')

    def __init__(self,referenciaseller,nomeseller, ref_ean,ref_cod,nome_produto,imagem, imagemmarca,
        perfilprod,perfilgoogle,marcaproduto,preco_seller,diferenca_preco,bitAtivo,sellermenorpreco,menorpreco,
        sellermaiorpreco,maiorpreco,idcategoriaproduto,categoriaproduto,idsubcategoriaproduto,subcategoriaproduto):

        self.referenciaseller = referenciaseller
        self.nomeseller = nomeseller
        self.ref_ean = ref_ean
        self.ref_cod = ref_cod
        self.nome_produto = nome_produto
        self.imagem = imagem
        self.imagemmarca = imagemmarca
        self.perfilprod = perfilprod
        self.perfilgoogle = perfilgoogle
        self.marcaproduto = marcaproduto
        self.preco_seller = preco_seller
        self.diferenca_preco = diferenca_preco
        self.bitAtivo = bitAtivo
        self.sellermenorpreco = sellermenorpreco
        self.menorpreco = menorpreco
        self.sellermaiorpreco = sellermaiorpreco
        self.maiorpreco = maiorpreco
        self.idcategoriaproduto = idcategoriaproduto
        self.categoriaproduto = categoriaproduto
        self.idsubcategoriaproduto = idsubcategoriaproduto
        self.subcategoriaproduto = subcategoriaproduto


class CategoriasProdutos(db.Model):
    #Classe Categorias MercoStore
    id = db.Column(db.Integer, primary_key=True, unique=True)
    iddepartamento = db.Column(db.Integer, unique=False, nullable=True)
    nomedepartamento = db.Column(db.String(100), unique=False, nullable=True)
    idcategoria = db.Column(db.Integer, unique=False, nullable=True)
    nomecategoria = db.Column(db.String(100), unique=False, nullable=True)
    idsubcategoria = db.Column(db.Integer, unique=False, nullable=True)
    nomesubcategoria = db.Column(db.String(100), unique=False, nullable=True)
    refsprods = db.Column(db.Integer, db.ForeignKey('produtos.idproduto'))
    produtosref  = db.relationship("Produtos", back_populates='refsprodcategorias')
    def __init__(self,iddepartamento,nomedepartamento,idcategoria,nomecategoria,idsubcategoria,nomesubcategoria):
        self.iddepartamento = iddepartamento
        self.nomedepartamento = nomedepartamento
        self.idcategoria = idcategoria
        self.nomecategoria = nomecategoria
        self.idsubcategoria = idsubcategoria
        self.nomesubcategoria = nomesubcategoria


class Googleshopping(db.Model):
    #Classe Google Shopping
    googleid = db.Column(db.Integer, primary_key=True, unique=True, nullable=True)
    eangoogle = db.Column(db.String(20), unique=False, nullable=True)
    marcaproduto = db.Column(db.String(100), unique=False, nullable=True)
    urlgoogle = db.Column(db.String(1000), unique=False, nullable=True)
    sellermen = db.Column(db.String(100), unique=False, nullable=True)
    menorpreco = db.Column(db.Float,  unique=False, nullable=True)
    sellermai = db.Column(db.String(100), unique=False, nullable=True)
    maiorpreco = db.Column(db.String(100), unique=False, nullable=True)
    bitAtivo = db.Column(db.Boolean, nullable=True, unique=False, nullable=True)
    dataatualizado = db.Column(DateTime(timezone=True), server_default=func.now())
    google = db.relationship("Seller",back_populates="refsgoogle")
    refgoogle = db.Column(db.Integer, db.ForeignKey('sellers.idseller'))


    def __init__(self,eangoogle,marcaproduto, urlgoogle,sellermen, menorpreco,sellermai,maiorpreco, bitAtivo):
        self.eangoogle = eangoogle
        self.marcaproduto = marcaproduto
        self.urlgoogle = urlgoogle
        self.sellermen = sellermen
        self.menorpreco = menorpreco
        self.sellermai = sellermai
        self.maiorpreco = maiorpreco
        self.bitAtivo = bitAtivo


class ProdutosEspecificacoes(db.Model):
    #classe caracteristicas produtos
    especificacaoid = db.Column(db.Integer, primary_key=True, unique=True)
    produtodescricao = db.Column(db.String(1000), unique=False)
    produtovoltagem = db.Column(db.String(1000), unique=False)
    produtoun = db.Column(db.String(1000), unique=False)
    produtocor = db.Column(db.String(1000), unique=False)
    produtomaterial = db.Column(db.String(1000), unique=False)
    linkmanual = db.Column(db.String(1000), unique=False)
    linksitefabricante = db.Column(db.String(1000), unique=False)
    produtopeso = db.Column(db.String(1000), unique=False)
    produtoaltura = db.Column(db.String(1000), unique=False)
    produtolargura = db.Column(db.String(1000), unique=False)
    produtoimagens = db.Column(db.String(1000), unique=False)
    produtocaracteristicasgerais = db.Column(db.String(1000), unique=False)
    produtomarca = db.Column(db.String(1000), unique=False)
    produtocategoria = db.Column(db.String(1000), unique=False)
    produtosubcategoria = db.Column(db.String(1000), unique=False)
    produtodepartamento = db.Column(db.String(1000), unique=False)
    dataatualizado = db.Column(DateTime(timezone=True), server_default=func.now())
    
    def __init__(self,produtodescricao, produtovoltagem,produtoun,
                produtocor,produtomaterial, linkmanual,linksitefabricante,produtopeso,produtoaltura,
                produtolargura,produtoimagens,produtocaracteristicasgerais,produtomarca,produtocategoria,produtodepartamento):
        self.produtodescricao =produtodescricao
        self.produtovoltagem = produtovoltagem
        self.produtoun = produtoun
        self.produtocor = produtocor
        self.produtomaterial = produtomaterial
        self.linkmanual = linkmanual
        self.linksitefabricante = linksitefabricante
        self.produtopeso = produtopeso
        self.produtoaltura = produtoaltura
        self.produtolargura =produtolargura
        self.produtoimagens = produtoimagens
        self.produtocaracteristicasgerais = produtocaracteristicasgerais
        self.produtomarca = produtomarca
        self.produtocategoria = produtocategoria
        self.produtodepartamento = produtodepartamento


class Saldoprodutos(db.Model):
    idsaldoproduto = db.Column(db.Integer, primary_key=True, unique=True)
    disponivel = db.Column(db.Float,  unique=False, nullable=True)
    reservado = db.Column(db.Float,  unique=False, nullable=True)
    total = db.Column(db.Float,  unique=False, nullable=True)
    datadisponibilidade = db.Column(db.DateTime,unique=False, nullable=True)

    def __init__(self,disponivel, reservado,total):
        self.disponivel = disponivel
        self.reservado = reservado
        self.total = total

class Precosprodutos(db.Model):
    idprecoproduto = db.Column(db.Integer, primary_key=True, unique=True)
    precocusto = db.Column(db.Integer, primary_key=True, unique=False, nullable=True)
    precovenda = db.Column(db.Integer, primary_key=True, unique=False, nullable=True)
    margem = db.Column(db.String(30), unique=False, nullable=True)

    def __init__(self,precocusto,precovenda, margem):
        self.precocusto = precocusto
        self.precovenda = precovenda
        self.margem = margem


