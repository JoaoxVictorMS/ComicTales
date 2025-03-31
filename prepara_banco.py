import mysql.connector
from mysql.connector import errorcode
from werkzeug.security import generate_password_hash

try:
    print("Conectando...")
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='4100.143'
    )

    cursor = conn.cursor()

    
    cursor.execute("DROP DATABASE IF EXISTS `comictales`;")
    cursor.execute("CREATE DATABASE `comictales`;")
    cursor.execute("USE `comictales`;")

    
    TABLES = {}

    
    TABLES['Usuarios'] = ('''
        CREATE TABLE `usuarios` (
        `cpf` VARCHAR(11) NOT NULL,
        `email` VARCHAR(255) NOT NULL,
        `senha` VARCHAR(100) NOT NULL,
        `nome` VARCHAR(50) NOT NULL,
        `sobrenome` VARCHAR(50) NOT NULL,
        `pais` VARCHAR(50) NOT NULL,
        `data_nascimento` DATE NOT NULL,
        `sexo` ENUM('Masculino', 'Feminino', 'Outros') NOT NULL,
        PRIMARY KEY (`cpf`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    ''')

    
    TABLES['Personagens'] = ('''
        CREATE TABLE `personagens` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `nome` VARCHAR(100) NOT NULL UNIQUE,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    ''')

    
    TABLES['Enderecos'] = ('''
        CREATE TABLE `enderecos` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `cpf_usuario` VARCHAR(11) NOT NULL,
        `nome` VARCHAR(100) NOT NULL,
        `celular` VARCHAR(15) NOT NULL,
        `empresa` VARCHAR(100) NULL,
        `cep` VARCHAR(10) NOT NULL,
        `bairro` VARCHAR(100) NOT NULL,
        `estado` VARCHAR(2) NOT NULL,
        `cidade` VARCHAR(100) NOT NULL,
        `endereco` VARCHAR(200) NOT NULL,
        `pais` VARCHAR(2) NOT NULL,
        `numero` VARCHAR(10) NOT NULL,
        `complemento` VARCHAR(100) NULL,
        PRIMARY KEY (`id`),
        FOREIGN KEY (`cpf_usuario`) REFERENCES `usuarios`(`cpf`)
        ON DELETE CASCADE ON UPDATE CASCADE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    ''')

   
    TABLES['Produtos'] = ('''
        CREATE TABLE `produtos` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `titulo` VARCHAR(150) NOT NULL,
        `preco` FLOAT NOT NULL,
        `sinopse` TEXT NOT NULL,
        `imagem` VARCHAR(150) NOT NULL,
        `personagem_id` INT NULL,
        PRIMARY KEY (`id`),
        FOREIGN KEY (`personagem_id`) REFERENCES `personagens`(`id`) ON DELETE SET NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    ''')

    
    TABLES['ProdutosPersonagens'] = ('''
        CREATE TABLE `produtos_personagens` (
        `personagem_id` INT,
        `produto_id` INT,
        PRIMARY KEY (`personagem_id`, `produto_id`),
        FOREIGN KEY (`personagem_id`) REFERENCES `personagens`(`id`) ON DELETE CASCADE,
        FOREIGN KEY (`produto_id`) REFERENCES `produtos`(`id`) ON DELETE CASCADE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    ''')

    
    TABLES['ListaDesejos'] = ('''
        CREATE TABLE `lista_desejos` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `usuario_id` VARCHAR(11) NOT NULL,
        `produto_id` INT NOT NULL,
        PRIMARY KEY (`id`),
        FOREIGN KEY (`usuario_id`) REFERENCES `usuarios`(`cpf`)
        ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (`produto_id`) REFERENCES `produtos`(`id`)
        ON DELETE CASCADE ON UPDATE CASCADE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    ''')

   
    TABLES['Carrinho'] = ('''
        CREATE TABLE `carrinho` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `usuario_id` VARCHAR(11) NOT NULL,
        `produto_id` INT NOT NULL,
        `quantidade` INT DEFAULT 1 NOT NULL,
        PRIMARY KEY (`id`),
        FOREIGN KEY (`usuario_id`) REFERENCES `usuarios`(`cpf`)
        ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (`produto_id`) REFERENCES `produtos`(`id`)
        ON DELETE CASCADE ON UPDATE CASCADE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    ''')

 
    TABLES['Pedidos'] = ('''
        CREATE TABLE `pedidos` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `usuario_id` VARCHAR(11) NOT NULL,
        `produto_id` INT NOT NULL,
        `quantidade` INT NOT NULL DEFAULT 1,
        `data` DATE NOT NULL,
        PRIMARY KEY (`id`),
        FOREIGN KEY (`usuario_id`) REFERENCES `usuarios`(`cpf`)
        ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (`produto_id`) REFERENCES `produtos`(`id`)
        ON DELETE CASCADE ON UPDATE CASCADE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    ''')

    
    TABLES['Admins'] = ('''
        CREATE TABLE `admins` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `email` VARCHAR(255) NOT NULL UNIQUE,
        `senha` VARCHAR(256) NOT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    ''')



    
    for tabela_nome, tabela_sql in TABLES.items():
        try:
            print(f'Criando tabela {tabela_nome}:', end=' ')
            cursor.execute(tabela_sql)
            print('OK')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('Já existe')
            else:
                print(err.msg)

    
    print("Inserindo admin inicial...")
    email_admin = "admin@comictales.com"
    senha_admin = "12341234"
    senha_hash = generate_password_hash(senha_admin)

    cursor.execute(
        "INSERT INTO admins (email, senha) VALUES (%s, %s)",
        (email_admin, senha_hash)
    )
    print("Admin inicial criado com sucesso!")

except mysql.connector.Error as err:
    print(f"Erro ao conectar ao MySQL: {err}")

finally:
   
    if 'conn' in locals() and conn.is_connected():
        conn.commit()
        cursor.close()
        conn.close()
        print("Conexão encerrada.")
