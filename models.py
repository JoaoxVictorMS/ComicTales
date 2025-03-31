from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from comictales import db
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    cpf = db.Column(db.String(11), primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    sobrenome = db.Column(db.String(50), nullable=False)
    pais = db.Column(db.String(50), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.Enum('Masculino', 'Feminino', 'Outros'), nullable=False)
    enderecos = db.relationship('Endereco', back_populates='usuario', lazy=True)

    def __repr__(self):
        return f'<Usuario {self.nome}>'


class Endereco(db.Model):
    __tablename__ = 'enderecos'

    id = db.Column(db.Integer, primary_key=True)
    cpf_usuario = db.Column(db.String(11), db.ForeignKey('usuarios.cpf'), nullable=False) 
    nome = db.Column(db.String(100), nullable=False)  
    celular = db.Column(db.String(15), nullable=False)
    empresa = db.Column(db.String(100), nullable=True)  
    cep = db.Column(db.String(10), nullable=False)
    bairro = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(2), nullable=False)  
    cidade = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)  
    pais = db.Column(db.String(2), nullable=False)  
    numero = db.Column(db.String(10), nullable=False)
    complemento = db.Column(db.String(100), nullable=True)  

    usuario = db.relationship('Usuario', back_populates='enderecos')  

    def __repr__(self):
        return f'<Endereco {self.id} - {self.nome}>'
    


produtos_personagens = db.Table(
    'produtos_personagens',
    db.Column('personagem_id', db.Integer, db.ForeignKey('personagens.id'), primary_key=True),
    db.Column('produto_id', db.Integer, db.ForeignKey('produtos.id'), primary_key=True)
)

class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    sinopse = db.Column(db.Text, nullable=False)
    imagem = db.Column(db.String(150), nullable=False)  

   
    personagens = db.relationship('Personagem', secondary=produtos_personagens, backref='produtos')

    def __repr__(self):
        return f'<Produto {self.titulo}>'

class Personagem(db.Model):
    __tablename__ = 'personagens'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)

    
    def __repr__(self):
        return f'<Personagem {self.nome}>'


class ListaDesejos(db.Model):
    __tablename__ = 'lista_desejos'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.String(11), db.ForeignKey('usuarios.cpf'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)

    usuario = db.relationship('Usuario', back_populates='desejos')
    produto = db.relationship('Produto')

    def __repr__(self):
        return f'<ListaDesejos Usuario {self.usuario_id} Produto {self.produto_id}>'

Usuario.desejos = db.relationship('ListaDesejos', back_populates='usuario', lazy=True)


class Carrinho(db.Model):
    __tablename__ = 'carrinho'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.String(11), db.ForeignKey('usuarios.cpf'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    quantidade = db.Column(db.Integer, default=1, nullable=False)

    usuario = db.relationship('Usuario', back_populates='carrinho')
    produto = db.relationship('Produto')

    def __repr__(self):
        return f'<Carrinho Usuario {self.usuario_id} Produto {self.produto_id} Quantidade {self.quantidade}>'

Usuario.carrinho = db.relationship('Carrinho', back_populates='usuario', lazy=True)


class Pedido(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.String(11), db.ForeignKey('usuarios.cpf'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=1)
    data = db.Column(db.Date, nullable=False)

    usuario = db.relationship('Usuario', back_populates='pedidos')
    produto = db.relationship('Produto')

    @property
    def valor_total(self):
        if self.produto:
            return self.quantidade * self.produto.preco
        return 0

    def __repr__(self):
        return f'<Pedido {self.id} Usuario {self.usuario_id} Produto {self.produto_id}>'
    

Usuario.pedidos = db.relationship('Pedido', back_populates='usuario', lazy=True)



class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)

    def set_password(self, senha):
        self.senha = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.senha, senha)

    def __repr__(self):
        return f'<Admin {self.email}>'
    






