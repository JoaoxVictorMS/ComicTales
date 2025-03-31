from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, BooleanField, validators, DecimalField, FileField, TextAreaField
from email_validator import validate_email, EmailNotValidError 
from wtforms.validators import DataRequired, Length, NumberRange

class FormularioUsuario(FlaskForm):
    cpf = StringField('CPF', [
        validators.DataRequired(message='O CPF é obrigatório.'),
        validators.Length(min=11, max=11, message='O CPF deve ter 11 dígitos.')
    ])

    email = StringField('E-mail', [
        validators.DataRequired(message='O e-mail é obrigatório.'),
        validators.Length(max=255, message='O e-mail pode ter no máximo 255 caracteres.'),
        validators.InputRequired(message="E-mail é obrigatório."),
        validators.Email(message="E-mail inválido.")
    ])

    def validate_email(form, field):
        try:
            valid = validate_email(field.data)
            field.data = valid.email
        except EmailNotValidError as e:
            raise validators.ValidationError(str(e))

    senha = PasswordField('Senha', [
        validators.DataRequired(message='A senha é obrigatória.'),
        validators.Length(min=8, max=100, message='A senha deve ter entre 8 e 100 caracteres.')
    ])

    nome = StringField('Nome', [
        validators.DataRequired(message='O nome é obrigatório.'),
        validators.Length(max=50, message='O nome pode ter no máximo 50 caracteres.')
    ])

    sobrenome = StringField('Sobrenome', [
        validators.DataRequired(message='O sobrenome é obrigatório.'),
        validators.Length(max=50, message='O sobrenome pode ter no máximo 50 caracteres.')
    ])

    pais = SelectField('País', [validators.DataRequired(message='O país é obrigatório.')],
        choices=[('Brasil', 'Brasil'), ('Portugal', 'Portugal')]
    )

    mes_nascimento = SelectField('Mês de Nascimento', [validators.DataRequired(message='O mês de nascimento é obrigatório.')],
        choices=[
            ('1', 'Janeiro'), ('2', 'Fevereiro'), ('3', 'Março'), ('4', 'Abril'),
            ('5', 'Maio'), ('6', 'Junho'), ('7', 'Julho'), ('8', 'Agosto'),
            ('9', 'Setembro'), ('10', 'Outubro'), ('11', 'Novembro'), ('12', 'Dezembro')
        ]
    )

    ano_nascimento = SelectField('Ano de Nascimento', [validators.DataRequired(message='O ano de nascimento é obrigatório.')],
        choices=[str(ano) for ano in range(1900, 2024)]
    )

    sexo = SelectField('Sexo', [validators.DataRequired(message='O sexo é obrigatório.')],
        choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outros', 'Outros')]
    )

    remember = BooleanField('Lembrar-me')  
    cadastrar = SubmitField('Cadastrar')


class FormularioEndereco(FlaskForm):
    nome = StringField('Nome', [
        validators.DataRequired(message='O nome é obrigatório.'),
        validators.Length(max=100, message='O nome pode ter no máximo 100 caracteres.')
    ])
    celular = StringField('Celular', [
        validators.DataRequired(message='O celular é obrigatório.'),
        validators.Length(max=15, message='O celular pode ter no máximo 15 caracteres.')
    ])
    empresa = StringField('Empresa', [
        validators.Optional(),
        validators.Length(max=100, message='A empresa pode ter no máximo 100 caracteres.')
    ])
    cep = StringField('CEP', [
        validators.DataRequired(message='O CEP é obrigatório.'),
        validators.Length(min=8, max=10, message='O CEP deve ter entre 8 e 10 caracteres.')
    ])
    bairro = StringField('Bairro', [
        validators.DataRequired(message='O bairro é obrigatório.'),
        validators.Length(max=100, message='O bairro pode ter no máximo 100 caracteres.')
    ])
    estado = SelectField('Estado', [
        validators.DataRequired(message='O estado é obrigatório.')
    ], choices=[
        ('SP', 'São Paulo'), 
        ('RJ', 'Rio de Janeiro')
    ])
    cidade = StringField('Cidade', [
        validators.DataRequired(message='A cidade é obrigatória.'),
        validators.Length(max=100, message='A cidade pode ter no máximo 100 caracteres.')
    ])
    endereco = StringField('Endereço', [
        validators.DataRequired(message='O endereço é obrigatório.'),
        validators.Length(max=200, message='O endereço pode ter no máximo 200 caracteres.')
    ])
    pais = SelectField('País', [
        validators.DataRequired(message='O país é obrigatório.')
    ], choices=[
        ('BR', 'Brasil'), 
        ('PT', 'Portugal')
    ])
    numero = StringField('Número', [
        validators.DataRequired(message='O número é obrigatório.'),
        validators.Length(max=10, message='O número pode ter no máximo 10 caracteres.')
    ])
    complemento = StringField('Complemento', [
        validators.Optional(),
        validators.Length(max=100, message='O complemento pode ter no máximo 100 caracteres.')
    ])
    submit = SubmitField('Atualizar')


class FormularioAdmin(FlaskForm):
    email = StringField('E-mail', [
        validators.DataRequired(message='O e-mail é obrigatório.'),
        validators.Email(message="E-mail inválido."),
    ])
    senha = PasswordField('Senha', [
        validators.DataRequired(message='A senha é obrigatória.')
    ])
    remember = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')
    

class FormularioEditarProduto(FlaskForm):
    titulo = StringField('Título', [
        DataRequired(message='O título é obrigatório.'),
        Length(max=100, message='O título pode ter no máximo 100 caracteres.')
    ])
    
    sinopse = TextAreaField('Sinopse', [
        DataRequired(message='A sinopse é obrigatória.'),
        Length(max=500, message='A sinopse pode ter no máximo 500 caracteres.')
    ])
    
    preco = DecimalField('Preço', [
        DataRequired(message='O preço é obrigatório.'),
        NumberRange(min=0.01, message='O preço deve ser maior que 0.')
    ], places=2)
    
    imagem = FileField('Imagem (opcional)', [
        
    ])
    
    submit = SubmitField('Salvar Alterações')

