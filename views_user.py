from flask import render_template, request, redirect, session, flash, url_for
from comictales import app, db  
from models import Usuario, Endereco, Admin, Carrinho, ListaDesejos, Pedido, Produto
from helpers import FormularioUsuario, FormularioEndereco, FormularioAdmin
from flask_bcrypt import generate_password_hash, check_password_hash
from datetime import date
from flask_wtf import FlaskForm
import os
from werkzeug.utils import secure_filename
from functools import wraps


@app.route('/', endpoint='index_home')
def index():
    produtos = Produto.query.all() 
    return render_template('index.html', produtos=produtos)


@app.route('/login')
def login():
    proxima = request.args.get('proxima') or url_for('index')
    form = FormularioUsuario(request.form)
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/perguntas_frequentes')
def perguntas_frequentes():
    return render_template('perguntas_frequentes.html')

@app.route('/politica_cookie')
def politica_cookie():
    return render_template('politica_cookie.html')

@app.route('/politica_privacidade')
def politica_privacidade():
    return render_template('politica_privacidade.html')

@app.route('/termos_condicoes')
def termos_condicoes():
    return render_template('termos_condicoes.html')

@app.route('/template_lancamentos')
def template_lancamentos():
    
    produtos_novos = Produto.query.filter(Produto.imagem.like('uploads/%')).all()
    return render_template('template_lancamentos.html', produtos=produtos_novos)


@app.route('/criar_conta.html', methods=['GET', 'POST'])
def criar_conta():
    form = FormularioUsuario(request.form)
    if request.method == 'POST' and form.validate():
       
        usuario_existente = Usuario.query.filter_by(cpf=form.cpf.data).first()
        if usuario_existente:
            flash('Usuário com este CPF já existe.')
            return redirect(url_for('criar_conta'))

       
        data_nascimento = date(int(form.ano_nascimento.data), int(form.mes_nascimento.data), 1)

        novo_usuario = Usuario(
            cpf=form.cpf.data,
            email=form.email.data,
            senha=generate_password_hash(form.senha.data).decode('utf-8'),  
            nome=form.nome.data,
            sobrenome=form.sobrenome.data,
            pais=form.pais.data,
            data_nascimento=data_nascimento,
            sexo=form.sexo.data
        )

       
        db.session.add(novo_usuario)
        db.session.commit()

        flash('Conta criada com sucesso!')
        return redirect(url_for('login'))
    return render_template('criar_conta.html', form=form)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioUsuario(request.form)

    
    usuario = Usuario.query.filter_by(email=form.email.data).first()

    
    if not usuario:
        flash('E-mail não encontrado.')
    elif not check_password_hash(usuario.senha, form.senha.data):
        flash('Senha inválida.')
    else:
        
        session['usuario_logado'] = usuario.email
        flash(f'{usuario.nome} logado com sucesso!')

        
        proxima_pagina = request.form.get('proxima') or url_for('index')
        return redirect(proxima_pagina)

    
    return redirect(url_for('login'))



@app.route('/logout')
def logout():
    if 'usuario_logado' in session:
        session.pop('usuario_logado', None)
        flash('Logout efetuado com sucesso.')
    else:
        flash('Você já está deslogado.')
    return redirect(url_for('index_home'))



@app.route('/minha_conta')
def minha_conta():
    if 'usuario_logado' not in session:
        flash('Faça login para acessar sua conta.')
        return redirect(url_for('login'))
    usuario = Usuario.query.filter_by(email=session['usuario_logado']).first()
    return render_template('minha_conta.html', usuario=usuario)


class DummyForm(FlaskForm):
    pass

@app.route('/meus_enderecos', methods=['GET', 'POST'])
def meus_enderecos():
    if 'usuario_logado' not in session:
        flash('Faça login para acessar seus endereços.')
        return redirect(url_for('login'))
    
    usuario = Usuario.query.filter_by(email=session['usuario_logado']).first()

    
    if request.method == 'POST':
        novo_endereco = Endereco(
            cpf_usuario=usuario.cpf,
            nome=request.form.get('nome'),
            rua=request.form.get('rua'),
            cidade=request.form.get('cidade'),
            estado=request.form.get('estado'),
            cep=request.form.get('cep')
        )
        db.session.add(novo_endereco)
        db.session.commit()
        flash('Endereço adicionado com sucesso!')
        return redirect(url_for('meus_enderecos'))
    
    
    enderecos = usuario.enderecos

    
    form = DummyForm()

    return render_template('meus_enderecos.html', usuario=usuario, enderecos=enderecos, form=form)


@app.route('/meus_pedidos')
def meus_pedidos():
    if 'usuario_logado' not in session:
        flash('Faça login para acessar seus pedidos.')
        return redirect(url_for('login'))
    
    usuario = Usuario.query.filter_by(email=session['usuario_logado']).first()
    if not usuario:
        flash('Usuário não encontrado. Faça login novamente.')
        return redirect(url_for('login'))
    
    pedidos = Pedido.query.filter_by(usuario_id=usuario.cpf).all()
    
    if not pedidos:
        flash('Você ainda não realizou nenhum pedido.')
    
    return render_template('meus_pedidos.html', usuario=usuario, pedidos=pedidos)




@app.route('/adicionar_endereco', methods=['GET', 'POST'])
def adicionar_endereco():
    if 'usuario_logado' not in session:
        flash('Faça login para adicionar um endereço.')
        return redirect(url_for('login'))
    
    usuario = Usuario.query.filter_by(email=session['usuario_logado']).first()
    form = FormularioEndereco()

    if form.validate_on_submit():
        novo_endereco = Endereco(
            cpf_usuario=usuario.cpf,
            nome=form.nome.data,
            celular=form.celular.data,
            empresa=form.empresa.data,
            cep=form.cep.data,
            bairro=form.bairro.data,
            estado=form.estado.data,
            cidade=form.cidade.data,
            endereco=form.endereco.data,
            pais=form.pais.data,
            numero=form.numero.data,
            complemento=form.complemento.data
        )
        db.session.add(novo_endereco)
        db.session.commit()
        flash('Endereço adicionado com sucesso!')
        return redirect(url_for('meus_enderecos'))
    
    return render_template('adicionar_endereco.html', form=form)

@app.route('/remover_endereco/<int:endereco_id>', methods=['POST'])
def remover_endereco(endereco_id):
    if 'usuario_logado' not in session:
        flash('Faça login para remover um endereço.')
        return redirect(url_for('login'))
    
    endereco = Endereco.query.get_or_404(endereco_id)

    
    usuario = Usuario.query.filter_by(email=session['usuario_logado']).first()
    if endereco.cpf_usuario != usuario.cpf:
        flash('Você não tem permissão para remover este endereço.')
        return redirect(url_for('meus_enderecos'))
    
    
    db.session.delete(endereco)
    db.session.commit()
    flash('Endereço removido com sucesso!')
    return redirect(url_for('meus_enderecos'))



@app.route('/editar_endereco/<int:endereco_id>', methods=['GET', 'POST'])
def editar_endereco(endereco_id):
    if 'usuario_logado' not in session:
        flash('Faça login para editar um endereço.')
        return redirect(url_for('login'))

    endereco = Endereco.query.get_or_404(endereco_id)
    usuario = Usuario.query.filter_by(email=session['usuario_logado']).first()

    if endereco.cpf_usuario != usuario.cpf:
        flash('Você não tem permissão para editar este endereço.')
        return redirect(url_for('meus_enderecos'))

    form = FormularioEndereco(obj=endereco)

    if form.validate_on_submit():
        form.populate_obj(endereco)
        db.session.commit()
        flash('Endereço atualizado com sucesso!')
        return redirect(url_for('meus_enderecos'))

    return render_template('editar_endereco.html', form=form, endereco=endereco)



@app.route('/lista_de_desejos')
def lista_de_desejos():
    if 'usuario_logado' not in session:
        flash('Faça login para acessar a lista de desejos.')
        return redirect(url_for('login'))

    
    usuario = Usuario.query.filter_by(email=session['usuario_logado']).first()

    if not usuario:
        flash('Usuário não encontrado.')
        return redirect(url_for('login'))

   
    desejos = ListaDesejos.query.filter_by(usuario_id=usuario.cpf).all()

    if not desejos:
        flash('Sua lista de desejos está vazia.')
        return render_template('lista_de_desejos.html', produtos=[])

   
    produtos_desejados = [desejo.produto for desejo in desejos if desejo.produto]

    
    return render_template('lista_de_desejos.html', produtos=produtos_desejados)


@app.route('/adicionar_a_lista_de_desejos/<int:produto_id>', methods=['POST'])
def adicionar_a_lista_de_desejos(produto_id):
    if 'usuario_logado' not in session:
        flash('Faça login para adicionar itens à lista de desejos.')
        return redirect(url_for('login'))

    usuario = Usuario.query.filter_by(email=session['usuario_logado']).first()
    desejo_existente = ListaDesejos.query.filter_by(usuario_id=usuario.cpf, produto_id=produto_id).first()

    if desejo_existente:
        flash('O item já está na sua lista de desejos.')
    else:
        novo_desejo = ListaDesejos(usuario_id=usuario.cpf, produto_id=produto_id)
        db.session.add(novo_desejo)
        db.session.commit()
        flash('Item adicionado à lista de desejos com sucesso!')

    return redirect(url_for('exibir_produto', produto_id=produto_id))


@app.route('/remover_da_lista_de_desejos/<int:produto_id>', methods=['POST'])
def remover_da_lista_de_desejos(produto_id):
    if 'usuario_logado' not in session:
        flash('Faça login para remover itens da lista de desejos.')
        return redirect(url_for('login'))

    usuario = Usuario.query.filter_by(email=session['usuario_logado']).first()
    desejo = ListaDesejos.query.filter_by(usuario_id=usuario.cpf, produto_id=produto_id).first()

    if desejo:
        db.session.delete(desejo)
        db.session.commit()
        flash('Item removido da lista de desejos com sucesso!')
    else:
        flash('O item não estava na sua lista de desejos.')

    return redirect(url_for('lista_de_desejos'))



@app.route('/carrinho')
def carrinho():
    if 'usuario_logado' not in session:
        flash('Faça login para acessar o carrinho.')
        return redirect(url_for('login'))

    usuario = Usuario.query.filter_by(email=session['usuario_logado']).first()
    itens_carrinho = Carrinho.query.filter_by(usuario_id=usuario.cpf).all()

    produtos_carrinho = [
        {
            'produto': item.produto if item.produto else None,
            'quantidade': item.quantidade,
            'subtotal': item.produto.preco * item.quantidade if item.produto else 0
        }
        for item in itens_carrinho
    ]

    
    total_itens = sum(item['quantidade'] for item in produtos_carrinho)
    
    
    total = sum(item['subtotal'] for item in produtos_carrinho)

    return render_template('carrinho_de_compras.html', cart_items=produtos_carrinho, total=total, total_itens=total_itens)



@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'usuario_logado' not in session:
        flash('Faça login para finalizar a compra.', 'danger')
        return redirect(url_for('login'))

    usuario = Usuario.query.filter_by(email=session['usuario_logado']).first()

    if not usuario:
        flash('Usuário não encontrado. Faça login novamente.', 'danger')
        return redirect(url_for('login'))

    enderecos = usuario.enderecos  
    itens_carrinho = Carrinho.query.filter_by(usuario_id=usuario.cpf).all()

    if not itens_carrinho:
        flash('Seu carrinho está vazio!', 'warning')
        return redirect(url_for('carrinho'))

   
    total_cost = sum(item.produto.preco * item.quantidade for item in itens_carrinho)

    return render_template(
        'checkout.html',
        usuario=usuario,
        enderecos=enderecos,
        itens_carrinho=itens_carrinho,
        total_cost=total_cost
    )



@app.route('/processar_checkout', methods=['POST'])
def processar_checkout():
    if 'usuario_logado' not in session:
        flash('Faça login para finalizar a compra.', 'danger')
        return redirect(url_for('login'))

    usuario = Usuario.query.filter_by(email=session['usuario_logado']).first()
    if not usuario:
        flash('Usuário não encontrado.', 'danger')
        return redirect(url_for('login'))

    itens_carrinho = Carrinho.query.filter_by(usuario_id=usuario.cpf).all()

    if not itens_carrinho:
        flash('Seu carrinho está vazio!', 'warning')
        return redirect(url_for('carrinho'))

    
    for item in itens_carrinho:
        novo_pedido = Pedido(
            usuario_id=usuario.cpf,
            produto_id=item.produto_id,
            quantidade=item.quantidade,
            data=date.today()
        )
        db.session.add(novo_pedido)

    
    Carrinho.query.filter_by(usuario_id=usuario.cpf).delete()
    db.session.commit()

    flash('Compra realizada com sucesso!', 'success')
    return redirect(url_for('index_home'))  



@app.route('/adicionar_ao_carrinho/<int:produto_id>', methods=['POST'])
def adicionar_ao_carrinho(produto_id):
    if 'usuario_logado' not in session:
        flash("Faça login para adicionar itens ao carrinho.", "danger")
        return redirect(url_for('login'))  # Redireciona para a página de login

    usuario = Usuario.query.filter_by(email=session['usuario_logado']).first()
    if not usuario:
        flash("Usuário não encontrado. Faça login novamente.", "danger")
        return redirect(url_for('login'))

    quantidade = request.form.get('quantidade', type=int, default=1)

    # Verifica se o item já está no carrinho
    item_carrinho = Carrinho.query.filter_by(usuario_id=usuario.cpf, produto_id=produto_id).first()

    if item_carrinho:
        item_carrinho.quantidade += quantidade
    else:
        novo_item = Carrinho(usuario_id=usuario.cpf, produto_id=produto_id, quantidade=quantidade)
        db.session.add(novo_item)

    db.session.commit()
    flash("Produto adicionado ao carrinho com sucesso!", "success")
    return redirect(url_for('exibir_produto', produto_id=produto_id))




@app.route('/remover_do_carrinho/<int:produto_id>', methods=['POST'])
def remover_do_carrinho(produto_id):
    if 'usuario_logado' not in session:
        flash('Faça login para remover itens do carrinho.')
        return redirect(url_for('login'))

    usuario = Usuario.query.filter_by(email=session['usuario_logado']).first()
    item_carrinho = Carrinho.query.filter_by(usuario_id=usuario.cpf, produto_id=produto_id).first()

    if item_carrinho:
        db.session.delete(item_carrinho)
        db.session.commit()
        flash('Item removido do carrinho com sucesso!')
    else:
        flash('O item não estava no carrinho.')

    return redirect(url_for('carrinho'))


app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logado' not in session:
            flash('Você precisa estar logado como administrador para acessar esta página.', 'error')
            return redirect(url_for('login_admin'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/admin/login', methods=['GET', 'POST'])
def login_admin():
    form = FormularioAdmin()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()
        if admin and admin.check_password(form.senha.data):
            session['admin_logado'] = admin.id
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('gerenciar_produtos'))
        else:
            flash('Credenciais inválidas.', 'error')
    return render_template('login_admin.html', form=form)


@app.route('/admin/logout')
def logout_admin():
    session.pop('admin_logado', None)
    flash('Logout realizado com sucesso.', 'success')
    return redirect(url_for('login_admin'))


@app.route('/produtos')
@admin_required
def gerenciar_produtos():
    produtos = Produto.query.all()
    return render_template('gerenciar_produtos.html', produtos=produtos)

@app.route('/produtos/adicionar', methods=['POST'])
@admin_required
def adicionar_produto():
    titulo = request.form['nome']
    sinopse = request.form['descricao']
    preco = request.form['preco']
    imagem = request.files['imagem']

    if imagem and titulo and sinopse and preco:
        filename = secure_filename(imagem.filename)

        
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        imagem.save(image_path)

        
        novo_produto = Produto(titulo=titulo, sinopse=sinopse, preco=float(preco), imagem='uploads/' + filename)
        db.session.add(novo_produto)
        db.session.commit()
        flash('Produto adicionado com sucesso!', 'success')
    else:
        flash('Preencha todos os campos corretamente.', 'error')

    return redirect(url_for('gerenciar_produtos'))

@app.route('/produtos/editar/<int:id>', methods=['POST', 'GET'])
@admin_required
def editar_produto(id):
    produto = Produto.query.get_or_404(id)

    if request.method == 'POST':
        print(request.form)  

        try:
            titulo = request.form['titulo']
            sinopse = request.form['sinopse']
            preco = request.form['preco']
            imagem = request.files['imagem']
        except KeyError as e:
            print(f"KeyError: {e}")  
            flash(f"Campo {str(e)} não encontrado.", 'error')
            return redirect(url_for('editar_produto', id=id))

        if titulo and sinopse and preco:
            produto.titulo = titulo
            produto.sinopse = sinopse
            produto.preco = float(preco)

            
            if imagem:
                filename = secure_filename(imagem.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                imagem.save(image_path)
                produto.imagem = 'uploads/' + filename

            db.session.commit()
            flash('Produto editado com sucesso!', 'success')
            return redirect(url_for('gerenciar_produtos'))
        else:
            flash('Preencha todos os campos corretamente.', 'error')

    return render_template('editar_produtos.html', produto=produto)



@app.route('/produtos/excluir/<int:id>', methods=['POST'])
@admin_required
def excluir_produto(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    flash('Produto excluído com sucesso!', 'success')
    return redirect(url_for('gerenciar_produtos'))

if __name__ == '__main__':
    app.run(debug=True)


