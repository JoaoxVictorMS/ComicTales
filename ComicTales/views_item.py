from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from comictales import app
from models import Produto, Personagem

@app.route('/')
def index():
    produtos = Produto.query.all()
    return render_template('index.html', produtos=produtos)

@app.route('/search', methods=['GET'])
def buscar():
    query = request.args.get('query', '').strip()
    produtos = []
    mensagem = None

    try:
        if query:
            produtos = buscar_produtos(query)
            if not produtos:
                mensagem = f"Nenhum produto encontrado para '{query}'."
        else:
            mensagem = "Digite algo para buscar."
    except Exception as e:
        print(f"Erro ao buscar produtos: {e}")
        mensagem = "Ocorreu um erro interno ao realizar a busca. Tente novamente."

    return render_template('index.html', produtos=produtos, query=query, mensagem=mensagem)

@app.route('/search_results')
def search_results():
    query = request.args.get('query', '').strip()
    produtos = buscar_produtos(query)
    mensagem = None

    if not produtos:
        mensagem = f"Nenhum produto encontrado para '{query}'."
    
    return render_template(
        'search_results.html',
        query=query,
        produtos=produtos,
        mensagem=mensagem,
        personagem=None  
    )

def buscar_produtos(query):
    return Produto.query.filter(Produto.titulo.ilike(f'%{query}%')).all()

@app.route('/produto/<int:produto_id>')
def exibir_produto(produto_id):
    produto = Produto.query.get(produto_id)
    if not produto:
        flash('Produto não encontrado!', 'danger')
        return redirect(url_for('index'))  
    
    return render_template('template_compra.html', produto=produto)

@app.route('/dc')
def dc():
    produtos = Produto.query.all()
    return render_template('dc.html', produtos=produtos)

@app.route('/marvel')
def marvel():
    produtos = Produto.query.all()
    return render_template('marvel.html', produtos=produtos)

@app.route('/livros')
def livros():
    produtos = Produto.query.all()
    return render_template('livros.html', produtos=produtos)

@app.route('/world_mangas')
def world_mangas():
    produtos = Produto.query.all()
    return render_template('WorldManga.html', produtos=produtos)

@app.route('/personagem/<personagem_url>')
def exibir_personagem(personagem_url):
    personagem_nome = personagem_url.replace('-', ' ').title()
    personagem = Personagem.query.filter_by(nome=personagem_nome).first()

    if personagem:
        
        produtos = Produto.query.filter(Produto.personagens.any(id=personagem.id)).all()

        return render_template(
            'Template_Personagens.html',
            personagem=personagem,
            produtos=produtos
        )
    else:
        
        return render_template('404.html', mensagem="Personagem não encontrado")
