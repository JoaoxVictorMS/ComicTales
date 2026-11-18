<h1 align="center" style="font-weight: bold;">ComicTales</h1>

<p align="center">
    <img src="static/ComicTales-Photoroom.png" alt="ComicTales Logo" width="300px">
</p>

[PYTHON__BADGE]: https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white
[FLASK__BADGE]: https://img.shields.io/badge/Flask-%23000000.svg?style=for-the-badge&logo=flask&logoColor=white
[MYSQL__BADGE]: https://img.shields.io/badge/MySQL-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white
[BOOTSTRAP__BADGE]: https://img.shields.io/badge/Bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white

<p align="center">
  <a href="#technologies">Tecnologias</a> •
  <a href="#started">Iniciando</a> •
  <a href="#layout">Layout/Preview</a> •
  <a href="#routes">Rotas Principais</a> •
  <a href="#colab">Colaboradores</a> •
  <a href="#contribute">Contribua</a>
</p>

<p align="center">
    <b>Plataforma de e-commerce e vitrine digital especializada em quadrinhos, mangás e colecionáveis.</b>
</p>

<h2 id="layout">🎨 Layout/Preview</h2>

<p align="center">
    <img src="m_project/CT_index.gif" alt="Vitrine Inicial" width="500px">
    <br />
    <img src="m_project/CT_user.gif" alt="Área do Cliente" width="500px">
    <br />
    <img src="m_project/CT_admin.gif" alt="Painel Administrativo" width="500px">
</p>

<h2 id="technologies">💻 Tecnologias</h2>

<div>

![Python][PYTHON__BADGE]
![Flask][FLASK__BADGE]
![MySQL][MYSQL__BADGE]
![Bootstrap][BOOTSTRAP__BADGE]

</div>

<h2 id="started">🚀 Iniciando</h2>

Siga as instruções abaixo para configurar e rodar o projeto localmente na sua máquina.

<h3>Pré-requisitos</h3>

Lista dos pré-requisitos necessários:

- [Python 3.10+](https://www.python.org/)
- [MySQL Server / XAMPP](https://www.mysql.com/)
- [Git](https://git-scm.com/)

<h3>Clonando</h3>

```bash
git clone https://github.com/JoaoxVictorMS/ComicTales.git
cd ComicTales
```

<h3>Configurando o Ambiente Virtual e Dependências</h3>

Crie e ative o seu ambiente virtual Python, e em seguida instale os pacotes necessários:

```bash
# Criar o ambiente virtual
python -m venv .venv

# Ativar no Windows (PowerShell)
.venv\Scripts\Activate

# Ativar no Linux/macOS
source .venv/bin/activate

# Instalar as dependências
pip install -r requirements.txt
```

<h3>Configurando o Banco de Dados e Inicialização</h3>

Certifique-se de que o seu servidor MySQL local está ativo. Verifique as credenciais de conexão (usuário e senha) nos arquivos `config.py` e `prepara_banco.py`, e execute o script de preparação para criar o banco de dados `comictales`, todas as tabelas relacionais e o administrador padrão:

```bash
python prepara_banco.py
```

- **Credenciais de Administrador (geradas automaticamente):**
  - **E-mail:** `admin@comictales.com`
  - **Senha:** `12341234`

> **Nota sobre o catálogo inicial:** O banco de dados é criado com as tabelas vazias. Para testar a loja (como adicionar itens à lista de desejos ou ao carrinho sem erros de chave estrangeira), acesse o painel administrativo (`/admin/login`) e cadastre pelo menos um produto no catálogo.

<h3>Criando um Cliente de Teste (Opcional)</h3>

Caso queira testar o fluxo de compras, carrinho e lista de desejos sem precisar preencher o formulário de cadastro na interface, execute o script utilitário (que já gera a senha criptografada no padrão exigido pelo `Flask-Bcrypt`):

```bash
python criar_usuario_teste.py
```

- **Credenciais de Cliente de Teste:**
  - **E-mail:** `cliente@comictales.com`
  - **Senha:** `12341234`

<h3>Executando</h3>

Com o banco de dados preparado, inicie o servidor Flask localmente:

```bash
python comictales.py
```

Acesse a aplicação no seu navegador através de: `http://127.0.0.1:5000`

<h2 id="routes">📍 Rotas e Endpoints da Aplicação</h2>

Abaixo estão listadas todas as rotas mapeadas na aplicação **ComicTales**, divididas por módulos funcionais:

### 🌐 Páginas Públicas, Catálogo e Busca
| Rota | Método | Descrição |
| :--- | :---: | :--- |
| `GET /` | GET | Página inicial / Vitrine principal do e-commerce. |
| `GET /produto/<int:produto_id>` | GET | Página de exibição e detalhes de um quadrinho ou item específico. |
| `GET /search` | GET | Processa a barra de busca e redireciona para os resultados. |
| `GET /search_results` | GET | Exibe a página estruturada com os resultados da pesquisa. |
| `GET /dc` | GET | Vitrine filtrada com produtos do universo DC Comics. |
| `GET /marvel` | GET | Vitrine filtrada com produtos do universo Marvel. |
| `GET /livros` | GET | Vitrine filtrada de livros e publicações especiais. |
| `GET /world_mangas` | GET | Vitrine dedicada ao mundo dos mangás. |
| `GET /personagem/<personagem_url>` | GET | Filtro dinâmico de produtos por personagem específico. |
| `GET /template_lancamentos` | GET | Seção especial de novos lançamentos da loja. |
| `GET /perguntas_frequentes` | GET | Página institucional de FAQ (Dúvidas frequentes). |
| `GET /politica_cookie` | GET | Termos e política de cookies. |
| `GET /politica_privacidade` | GET | Política de privacidade do e-commerce. |
| `GET /termos_condicoes` | GET | Termos e condições gerais de uso. |

### 👤 Autenticação e Gestão de Clientes
| Rota | Método | Descrição |
| :--- | :---: | :--- |
| `GET /login` | GET | Exibe a tela de login de clientes. |
| `POST /autenticar` | POST | Processa as credenciais de login do usuário (com verificação de senha via Bcrypt). |
| `GET /criar_conta.html` | GET / POST | Exibe o formulário e processa o cadastro de uma nova conta de cliente. |
| `GET /logout` | GET | Encerra a sessão ativa do usuário cliente. |
| `GET /minha_conta` | GET | Painel do cliente logado (exibe dados cadastrais). |
| `GET /meus_enderecos` | GET / POST | Gerenciamento e listagem dos endereços cadastrados do usuário. |
| `GET /adicionar_endereco` | GET / POST | Formulário para cadastro de um novo endereço de entrega. |
| `GET /editar_endereco/<int:id>` | GET / POST | Edição de um endereço já cadastrado. |
| `POST /remover_endereco/<int:id>` | POST | Exclusão de um endereço do usuário. |
| `GET /meus_pedidos` | GET | Histórico de compras e pedidos realizados pelo cliente. |

### 🛒 Carrinho, Lista de Desejos e Checkout
| Rota | Método | Descrição |
| :--- | :---: | :--- |
| `GET /carrinho` | GET | Exibe os itens adicionados no carrinho de compras e o valor total. |
| `POST /adicionar_ao_carrinho/<id>` | POST | Adiciona uma quantidade específica de um produto ao carrinho. |
| `POST /remover_do_carrinho/<id>` | POST | Remova um item do carrinho de compras. |
| `GET /lista_de_desejos` | GET | Exibe a lista de produtos salvos como favoritos pelo cliente. |
| `POST /adicionar_a_lista_de_desejos/<id>` | POST | Adiciona um item à lista de desejos (requer autenticação). |
| `POST /remover_da_lista_de_desejos/<id>` | POST | Remove um item da lista de desejos. |
| `GET /checkout` | GET / POST | Página de revisão de endereço e pagamento para fechamento do pedido. |
| `POST /processar_checkout` | POST | Converte o carrinho em pedidos definitivos e limpa o carrinho. |

### ⚙️ Painel Administrativo (Restrito)
> *Nota: Todas as rotas abaixo são protegidas pelo decorador personalizado `@admin_required`, exigindo sessão de administrador ativa.*

| Rota | Método | Descrição |
| :--- | :---: | :--- |
| `GET /admin/login` | GET / POST | Tela de autenticação exclusiva para administradores. |
| `GET /admin/logout` | GET | Encerra a sessão administrativa. |
| `GET /produtos` | GET | Painel principal de listagem e gerenciamento de produtos. |
| `POST /produtos/adicionar` | POST | Processa o cadastro de novo produto e upload de imagem. |
| `GET /produtos/editar/<id>` | GET / POST | Formulário e processamento da edição de um produto. |
| `POST /produtos/excluir/<id>` | POST | Remove permanentemente um produto da base de dados. |

<h2 id="colab">🤝 Colaboradores</h2>

Um agradecimento especial a todas as pessoas que contribuíram para este projeto.

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/JoaoxVictorMS">
        <img src="https://avatars.githubusercontent.com/u/98715957?v=4" width="100px;" alt="Foto de perfil do João Victor"/><br>
        <sub>
          <b>João Victor</b>
        </sub>
      </a>
    </td>
      <td align="center">
      <a href="https://github.com/FernandessFelipe">
        <img src="https://avatars.githubusercontent.com/u/181539218?v=4" width="100px;" alt="Foto de perfil do João Victor"/><br>
        <sub>
          <b>João Victor</b>
        </sub>
      </a>
    </td>
      <td align="center">
      <a href="https://github.com/guumendess">
        <img src="https://avatars.githubusercontent.com/u/133999103?v=4" width="100px;" alt="Foto de perfil do João Victor"/><br>
        <sub>
          <b>João Victor</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<h2 id="contribute">📫 Contribua</h2>

Contribuições são sempre bem-vindas! Siga os passos abaixo para colaborar com o projeto:

1. Faça um fork ou clone o repositório: `git clone https://github.com/JoaoxVictorMS/ComicTales.git`
2. Crie uma branch para a sua funcionalidade: `git checkout -b feature/NOME_DA_FEATURE`
3. Faça o commit das suas alterações seguindo os padrões convencionais
4. Envie para o repositório remoto: `git push origin feature/NOME_DA_FEATURE`
5. Abra um Pull Request explicando o problema resolvido ou a funcionalidade criada e, se houver modificações visuais, anexe screenshots!

<h3>Documentações que podem ajudar</h3>

[📝 Como criar um Pull Request](https://www.atlassian.com/br/git/tutorials/making-a-pull-request)

[💾 Padrão de commit](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)
