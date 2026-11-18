from comictales import app, db
from models import Usuario
from flask_bcrypt import generate_password_hash  # <-- Import correto do Flask-Bcrypt
from datetime import date

with app.app_context():
    email_teste = "cliente@comictales.com"
    
    # Remove o usuário antigo se ele já existir (para limpar o hash errado)
    usuario_antigo = Usuario.query.filter_by(email=email_teste).first()
    if usuario_antigo:
        db.session.delete(usuario_antigo)
        db.session.commit()

    # Cria o novo usuário com o hash compatível com o Bcrypt
    novo_usuario = Usuario(
        cpf="12345678901",
        email=email_teste,
        senha=generate_password_hash("12341234").decode('utf-8'),  # <-- Gerado via Bcrypt
        nome="João",
        sobrenome="Silva",
        pais="Brasil",
        data_nascimento=date(2000, 1, 1),
        sexo="Masculino"
    )
    
    db.session.add(novo_usuario)
    db.session.commit()
    print("Usuário de teste criado com sucesso!")