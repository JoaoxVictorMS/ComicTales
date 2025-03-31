from comictales import app, db  
from models import Produto, Personagem  


personagens = [
    {"nome": "Harry Potter"},
    {"nome": "Percy Jackson"},
    {"nome": "The Witcher"},
    {"nome": "Narnia"},
    {"nome": "Duna"},
    {"nome": "Senhor Anéis"},
    {"nome": "Sherlock Holmes"},
    {"nome": "Game Of Thrones"},
    {"nome": "Jogos Vorazes"},
    {"nome": "Crônicas"},

    {"nome": "Dragon Ball"},
    {"nome": "One Piece"},
    {"nome": "Naruto"},
    {"nome": "Bleach"},
    {"nome": "Dandadan"},
    {"nome": "Blue Lock"},
    {"nome": "Kaiju"},
    {"nome": "Berserk"},
    {"nome": "Sword Art Online"},
    {"nome": "Solo Leveling"},
    
    {"nome": "Homem Aranha"},
    {"nome": "Capitão América"},
    {"nome": "Ferro"},
    {"nome": "Hulk"},
    {"nome": "Thor"},
    {"nome": "Wolverine"},
    {"nome": "Feiticeira Escarlate"},
    {"nome": "Venom"},
    {"nome": "Viúva Negra"},
    {"nome": "Pantera Negra"},
    
    {"nome": "Batman"},
    {"nome": "Flash"},
    {"nome": "Superman"},
    {"nome": "Mulher Maravilha"},
    {"nome": "Arqueiro Verde"},
    {"nome": "Lanterna Verde"},
    {"nome": "Arlequina"},
    {"nome": "Aquaman"},
    {"nome": "Asa Noturna"},
    {"nome": "Coringa"}  
]


produtos = [
    
    {
        "titulo": "Dandadan Vol. 01",
        "preco": 29.90,
        "sinopse": "Ken Takakura acredita em fantasmas, mas não em alienígenas. Momo Ayase acredita em alienígenas, mas não em fantasmas. Quando os dois decidem provar quem está certo, acabam se deparando com uma aventura cheia de mistérios sobrenaturais, alienígenas bizarros e espíritos poderosos.",
        "imagem": "dandadancap1.webp",
        "personagem": "Dandadan"
    },
    {
        "titulo": "One Piece Vol. 01",
        "preco": 34.90,
        "sinopse": "Luffy é um garoto que deseja tornar-se um pirata por causa do Shanks. Durante uma discussão com Shanks por causa de alguns bandidos das montanhas, o garoto acaba comendo a Gomu Gomu no Mi. Mais tarde, porém, os bandidos retornam e Luffy decide comprar briga com eles bem quando os piratas não estão lá para protegê-lo. Shanks salva Luffy, mas acaba perdendo seu braço esquerdo por conta disso e logo deixa seu chapéu com o garoto.",
        "imagem": "onepiece1.webp",
        "personagem": "One Piece"
    },

      {
        "titulo" : "Jovens Titãs: Mutano Ama Ravena",
        "preco" : 34.93,
        "sinopse" : "Faz poucos dias que Ravena recobrou suas memórias, mas não há tempo para pensar no passado. ela precisa achar uma forma de se livrar de Trigon, seu pai demônio, de uma vez por todas. Enquanto isso, Garfield Logan está com dificuldade de controlar seus poderes e deseja encontrar respostas. Ravena e ele acabam sentindo uma conexão, apesar dos segredos que ambos guardam. Eles terão a coragem e a confiança para passar por cima das feridas e encontrar, quem sabe, o amor?",
        "imagem" : "MutanoAmaRavena.webp"
    },

    {
        "titulo" : "Jujutsu Kaisen: Batalha De Feiticeiros Vol. 25",
        "preco" : 42.50,
        "sinopse" : "Para ter o controle total do corpo de Fushiguro, Sukuna quer assassinar Tsumiki, dona do corpo em que Yorozu encarnou. Enquanto isso, Itadori e seus amigos tentam trazer Gojou de volta com o poder do Anjo, após Kurusu escapar da morte por um triz. Sukuna, o mais poderoso de todos os tempos, e Gojou, o mais poderoso da atualidade... finalmente teremos o confronto entre essas duas figuras extraordinárias?!",
        "imagem" : "Jujutsu25.webp"
    },

    {
        
        "titulo" : "Kaiju Nº8 Vol. 11",
        "preco" : 40.00,
        "sinopse" : "Os cinco kaijus com identificação criados pelo número 9 se reúnem na área da divisão oriental. O plano do inimigo é erradicar os membros mais poderosos das Forças de Defesa. Para isso, cada um dos comandantes será forçado a passar por uma luta extremamente difícil contra criaturas elaboradas para eliminá-los. Tamanha ameaça chega até mesmo à comandante de pelotão Shinonome… Enquanto isso, Kafka faz uma promessa à Kikoru antes da batalha. O que será…?! Eis aqui o volume 11, sobre como se manter fiel às suas convicções!!",
        "imagem" : "Kaiju11.webp",
        "personagem": "Kaiju"
    
    },

    {
        
        "titulo" : "Sword art Online: Alicization Lasting Vol. 18",
        "preco" : 47.60,
        "sinopse" : "A Guerra do Submundo chega ao seu ápice! Após uma batalha sangrenta com Sinon, Gabriel Miller, o Subtilizer, ainda não desistiu de possuir a alma de Alice, e a segue para o Altar do Fim do Mundo. Já na frente de batalha pelo Reino da Humanidade, os jogadores de China, Coreia e dos EUA são liderados pelo sádico PoH, ex-líder da guilda assassina Laughing Coffin. Asuna, Klein e os demais sobreviventes de SAO, junto dos jogadores de ALO, parecem estar à mercê do maníaco, enquanto Kirito permanece em torpor, preso entre os estilhaços de seu próprio ser…",
        "imagem" : "sao18.webp",
        "personagem": "Sword Art Online"
    
    },

    {
        
        "titulo" : "As Memórias De Vanitas 08",
        "preco" : 35.60,
        "sinopse" : "Este é o caso da “Bête de Gévaudan”, uma melodia da vingança que floresceu para, logo em seguida, desabrochar. Para além deste mundo tomado pela neve, Vanitas e os outros devem encarar uma mudança… Eis que chega o momento decisivo da escolha. Roga-se que ela respeite todos os sentimentos preciosos guardados nos corações.",
        "imagem" : "vanitas8.webp"
    
    },

    {
        
        "titulo" : "Berserk - Edição De Luxo Vol. 32",
        "preco" : 55.90,
        "sinopse" : "Pensando no bem-estar de Caska, Guts sai em uma jornada com destino a Elfhelm, terra natal de Puck. Durante a viagem, ele encontra Isidro, Farnese e Serpico, e então os acolhe por perceber que não daria conta de proteger Caska sozinho. Depois de encontrar a bruxa Flora na floresta dos espíritos das árvores, o novo grupo chega ao distrito-base de Vritanis!",
        "imagem" : "berserk32.webp",
        "personagem": "Berserk"
    
    },

    {
        
        "titulo" : "Flash 01",
        "preco" : 11.90,
        "sinopse" : "Como qualquer supervelocista que se preze pode afirmar, o tempo passa muito devagar para quem é incrivelmente rápido. Então, o que acontece quando um exército inteiro de alienígenas velocistas conquistadores aparece invadindo a Terra? A batalha mais intensa que o planeta já travou no espaço de sessenta segundos tem início!",
        "imagem" : "flash01.webp",
        "personagem": "Flash"
    
    },

    {
        
        "titulo" : "Homem-Aranha: Azul (Marvel Essenciais)",
        "preco" : 86.90,
        "sinopse" : "Acompanhe os primórdios de Peter Parker como o espetacular Homem-Aranha e também o início de seu relacionamento com a bela Gwen Stacy. Reveja as batalhas e os vilões que consagraram o Amigão da Vizinhança como um dos maiores heróis de todos os tempos. Um comovente e emocionante conto trazido pelo roteirista Jeph Loeb (Nova) e pelo artista Tim Sale (Demolidor: Amarelo)!",
        "imagem" : "homemaranhaazul.webp",
        "personagem": "Homem Aranha"
    
    },

    {
        
        "titulo" : "Spider-Man Noir: The Complete Collection",
        "preco" : 225.30,
        "sinopse" : "As aventuras difíceis do webslinger mais corajoso do Aranhaverso! Nos dias sombrios da Grande Depressão, o jovem repórter Peter Parker se vê mudado para sempre pela picada de uma aranha - e resolve enfrentar o crime e a corrupção como o vigilante urbano chamado Homem-Aranha! E não faltam inimigos - desde chefes de gangues, o Goblin e o Mestre do Crime, até reviravoltas da era popular em rostos familiares como Kraven, Camaleão, Doutor Octopus e muito mais! Mas será que a sedutora Felicia Hardy provará ser amiga ou inimiga? Além disso, o Homem-Aranha Noir entra no Aranhaverso através de um encontro com Mysterio – e compartilha uma equipe espetacular com um Aranha de seis braços! E uma nova aventura em quadrinhos em vídeo, impressa pela primeira vez!",
        "imagem" : "spidermannoir.jpg",
        "personagem": "Homem Aranha"
    
    },

    {
        
        "titulo" : "Novíssima Wolverine Vol. 2",
        "preco" : 60.68,

        "sinopse" : "Nesta novíssima versão de Wolverine, Laura tenta seguir em frente com sua vida, mas o passado de Wolverine parece destinado a alcançá-la e causar estragos. Quando o Velho Logan entra em nosso mundo com seu passado cheio de horrores, ele traz muita bagagem e carnificina para Laura, e com uma nova Guerra Civil se aproximando, será que o Velho Logan e a Nova Wolverine vão se unir contra esse pesadelo em comum? Laura teme as perdas da Guerra, seu passado e sua missão. O legado de Logan lançou uma grande sombra, como Laura pode esperar sair dela?",

        "imagem" : "novissimawolverine.webp",
        "personagem": "Wolverine"
    
    },

    {
        
        "titulo" : "Novos Vingadores: Motim!",

        "preco" : 41.92,

        "sinopse" : "Os Vingadores não existem mais. A ausência dos Heróis Mais Poderosos da Terra abre caminho para um insidioso plano de fuga da Balsa, a instalação de segurança rmáxima da penitenciária da Ilha Ryker, onde os supercriminosos mais perigosos do mundo cumprem pena. Mas um grupo de heróis reunidos pelo destino estará lá para impedir que isso aconteça e ressuscitar uma lenda. Testemunhe o nascimento dos... Novos Vingadores!",

        "imagem" : "vingadoresmotim.jpg"
        
    
    },

    {
        
        "titulo" : "Homem-Aranha Superior (2024) Vol. 1",

        "preco" : 34.43,

        "sinopse" : "A teia do Homem-Aranha superior balança novamente! Um acerto de contas superior! O teioso enfrenta um novo vilão de seu passado, e enquanto Nova York sofre com todo o poder de uma estrela viva, o Doutor Octopus faz uma descoberta que muda sua vida. Os pecados do passado do doutor estão cobrando um preço alto no presente, e um dos amigos mais próximos de Peter Parker deve pagar o preço por eles. Com a vida de Anna Maria em jogo, Otto busca uma meta audaciosa, eliminar o Homem-Aranha e tomar seu lugar como o único a usar esse nome!",

        "imagem" : "homemaranhasuperior.webp",
        "personagem": "Homem Aranha"
    
    },


    {
        
        "titulo" : "X-Men: A Saga Da Fênix Negra (Marvel Essenciais)",

        "preco" : 60.00,

        "sinopse" : "Reunidos pelo Professor Xavier, os X-Men dedicaram suas vidas a proteger a humanidade, mesmo sendo temidos e odiados por todos. No entanto, a equipe nunca imaginou que teria de lutar com uma de suas antigas companheiras, quando Jean Grey é corrompida e se torna a Fênix Negra, trazendo morte e destruição para todo o universo. Com roteiro de Chris Claremont (Novos Mutantes) e arte de John Byrne (Quarteto Fantástico), que também colaborou na trama ao lado de Claremont, esta é a maior aventura de todos os tempos dos Filhos do Átomo!",

        "imagem" : "xmenfenix.webp"
    
    },


    {
        
        "titulo" : "Batman: a Piada Mortal",

        "preco" : 35.00,

        "sinopse" : "Encontre neste único volume com 136 páginas duas das histórias que melhor souberam descrever a figura do Coringa e sua relação com o Batman. Em Batman: A Piada Mortal, Alan Moore e Brian Bolland nos levam à mente do Príncipe Palhaço do Crime, mostrando-nos o que poderia ser um vislumbre de seu passado. Em Batman: O Homem Que Ri, Ed Brubaker e Doug Mahnke revisitam as primeiras aparições do Coringa, voltando no tempo aos dias de seu primeiro confronto com o Batman, oferecendo novas perspectivas a histórias clássicas. Uma viagem alucinante ao mundo daquele que é o vilão dos quadrinhos por excelência!",

        "imagem" : "Joker.jpg"
    
    },

    {
        
        "titulo" : "Mulher-Maravilha/Flash 10",

        "preco" : 79.99,

        "sinopse" : "À medida que o domínio do Soberano sobre a psique da Mulher-Maravilha se intensifica, ela se refugia nos braços de Steve Trevor. Mas será que o amor deles triunfará sobre a rede de mentiras trançada no Mundo dos Homens? Ao mesmo tempo, conforme a falha da Força de Aceleração gera mais caos ao redor do mundo, outros poderes misteriosos são despertos e Linda busca a fonte das vozes misteriosas que ecoam na sua cabeça enquanto Barry atinge o ponto de ruptura.",

        "imagem" : "MulherMaravilha.webp"
    
    },


    {
        
        "titulo" : "Força Da Aceleração",

        "preco" : 32.45,

        "sinopse" : "Enquanto Wally West e Avery Ho, que já foram membros dos Novos Titãs, da Liga da Justiça e da Família Flash, se dão conta das misteriosas mudanças ocorrendo com a Força de Aceleração, eles disparam para Keystone City, onde encontram antigos amigos, novas ameaças e uma chance de construírem os próprios caminhos. Acompanhe a entrada da nova geração de velocistas na Aurora da DC!",

        "imagem" : "ForçadaAceleração.webp",

        "personagem": "Flash"
    
    },

    {
        
        "titulo" : "Asa Noturna (2022) Vol. 2",

        "preco" : 34.43,

        "sinopse" : "A premiada equipe composta por Tom Taylor e Bruno Redondo continua sua aclamada fase do Asa Noturna com este segundo volume que se conecta ao evento Batman: Estado de Medo! O sistema de Bárbara Gordon foi hackeado! Mas quem é poderoso o suficiente para invadir a própria rede supersegura da Oráculo? E quais informações pessoais estão agora em risco? Ao investigar quem está por trás disso, os medos mais profundos de Batgirl e Asa Noturna são relevados!",

        "imagem" : "asaNoturna.webp",

        "personagem": "Asa Noturna"
    
    },


    {
        
        "titulo" : "A Saga Da Liga Da Justiça 06/22",

        "preco" : 32.65,

        "sinopse" : "À medida que o domínio do Soberano sobre a psique da Mulher-Maravilha se intensifica, ela se refugia nos braços de Steve Trevor. Mas será que o amor deles triunfará sobre a rede de mentiras trançada no Mundo dos Homens? Ao mesmo tempo, conforme a falha da Força de Aceleração gera mais caos ao redor do mundo, outros poderes misteriosos são despertos e Linda busca a fonte das vozes misteriosas que ecoam na sua cabeça enquanto Barry atinge o ponto de ruptura.",

        "imagem" : "LigadaJustiça.webp"
    
    },

    {
        
        "titulo" : "One Piece Vol. 100",

        "preco" :  30.75,

        "sinopse" : "Com todas as estrelas reunidas no topo da fortaleza, Luffy e os Piratas da Nova Geração desafiam Kaido e Big Mom! Será que há alguma chance de vitória contra essa aliança formada entre os dois mais poderosos piratas dos mares?! O que o futuro reserva para essa batalha extrema que está fazendo toda Onigashima tremer?!",

        "imagem" : "onepiece100.webp"
    
    },


    {
        
        "titulo" : "Dandadan Vol. 02",

        "preco" : 28.90,

        "sinopse" : "Depois de ser amaldiçoado pela Velha Turbo em um túnel assombrado, Okarun, um viciado em fenômenos inexplicáveis, decide junto de Momo Ayase, uma colegial com poderes paranormais, desafiar a própria Velha Turbo para uma partida de pega-pega na intenção de desfazer sua maldição! A dupla vence se conseguir escapar, mas a disputa não será tão fácil, pois a Velha Turbo manda um terrível assassino para os atrapalhar: Um espírito vagante que assume a forma de um caranguejo gigante!! Monstros, paixões e batalhas seguem em polvorosa nesse segundo volume!!",

        "imagem" : "dandadan2.webp",

        "personagem": "Dandadan"
    
    },


    {
        
        "titulo" : "Blue Lock Vol. 27",

        "preco" : 25.95,

        "sinopse" : "A disputa pelo protagonismo se intensifica no seu clímax! A partida contra Ubers chega imponentemente a sua decisão!! A Itália encosta o placar na quinta partida da Liga Neo Egoísta com um gol do Barou. Mas no momento em que os times disputam o último ponto, a última peça que Isagi buscava — Hiori — entra em campo! Será que o Hiori, com quem Isagi quer gerar uma reação química, vai conseguir se livrar de sua “maldição”? A Itália, por outro lado, combina Barou que acabou de se livrar de suas amarras com um novo “desenho” e mostra uma nova explosão evolutiva! Em meio a uma situação extrema onde Kaiser busca uma brecha para dar o bote, Isagi precisa mudar a situação com a ajuda do seu “parça” Hiori e se tornar o rei da partida!! Dá para ficar calado diante do ego de alguém? Não é outra pessoa, sou eu quem vou mudar o mundo!!",

        "imagem" : "bluelock27.webp",
        
        "personagem": "Blue Lock"
    
    },


    {
        
        "titulo" : "Dragon Ball Super Vol. 14",

        "preco" : 26.70,

        "sinopse" : "Vegeta adquire um novo poder e retorna à Terra para uma nova luta. Com uma técnica que força a separação do espírito do adversário, ele começa a desmembrar o poder de Moro. Mas Moro tem uma carta na manga... e não é apenas o suporte do Seven Three... o que será que ele está escondendo?",

        "imagem" : "dragonballsuper14.webp",

        "personagem": "Dragon Ball"
    
    },


{
        
        "titulo" : "Harry Potter e o Prisioneiro de Azkaban: 3",

        "preco" : 50.00,

        "sinopse" : "As aulas estão de volta à Hogwarts e Harry Potter não vê a hora de embarcar no expresso a vapor que o levará de volta à escola de bruxaria. Mais uma vez suas férias na rua dos Alfeneiros foi triste e solitária. Com muita ação, humor e magia, 'Harry Potter e o prisioneiro de Azkaban' traz de volta o gigante atrapalhado Rúbeo Hagrid, o sábio diretor Alvo Dumbledore, a exigente professora de transformação Minerva MacGonagall e o novo mestre Lupin, que guarda grandes surpresas para Harry.",

        "imagem" : "harrypotter3.jpg",
        
        "personagem": "Harry Potter"
    
    },


{
        
        "titulo" : "O último desejo - The Witcher - (capa dura): 1",

        "preco" : 55.90,

        "sinopse" : "Geralt de Rívia é um bruxo sagaz e habilidoso. Um assassino impiedoso e de sangue-frio treinado, desde a infância, para caçar e eliminar monstros. Seu único objetivo: destruir as criaturas do mal que assolam o mundo. Um mundo fantástico criado por Sapkowski com claras influências da mitologia eslava. Um mundo em que nem todos os que parecem monstros são maus e nem todos os que parecem anjos são bons...",

        "imagem" : "thewitcher1.jpg",
        
        "personagem": "The Witcher"
    
    },


{
        
        "titulo" : "As Crônicas de Nárnia. Brochura",

        "preco" : 115.00,

        "sinopse" : "Viagens ao fim do mundo, criaturas fantásticas e batalhas épicas entre o bem e o mal - o que mais um leitor poderia querer de um livro? O livro que tem tudo isso é 'O leão, a feiticeira e o guarda-roupa', escrito em 1949 por Clive Staples Lewis. MasLewis não parou por aí. Seis outros livros vieram depois e, juntos, ficaram conhecidos como 'As crônicas de Nárnia'. Nos últimos cinqüenta anos, 'As crônicas de Nárnia' transcenderam o gênero da fantasia para se tornar parte do cânone da literaturaclássica. Cada um dos sete livros é uma obra-prima, atraindo o leitor para um mundo em que a magia encontra a realidade, e o resultado é um mundo ficcional que tem fascinado gerações. Esta edição apresenta todas as sete crônicas integralmente, num único volume. Os livros são apresentados de acordo com a ordem de preferência de Lewis, cada capítulo com uma ilustração do artista original, Pauline Baynes. Enganosamente simples e direta, 'As crônicas de Nárnia' continuam cativando os leitores com aventuras, personagens e fatos que falam a pessoas de todas as idades.",

        "imagem" : "narniabochura.jpg",
        "personagem": "Narnia"
    
    },

    {
        
        "titulo" : "O cálice dos Deuses: Série Percy Jackson e os olimpianos: 1",

        "preco" : 36.60,

        "sinopse" : "Após quase dez anos de espera, os fãs do semideus mais amado ― e azarado ― da literatura já podem comemorar: Percy Jackson está de volta! No aguardado novo título da série Percy Jackson e os olimpianos , que chega ao Brasil em lançamento simultâneo, o filho de Poseidon se prepara para uma de suas missões mais difíceis até agora: entrar na faculdade. Depois de salvar o mundo inúmeras vezes de monstros, titãs, gigantes e outras criaturas aterrorizantes, tudo que Percy deseja é que seu último ano no ensino médio seja tranquilo. Infelizmente, os deuses têm outros planos para o jovem herói. Se ele quiser mesmo entrar na universidade, terá que cumprir três missões para conquistar três cartas de recomendação vindas diretamente do Monte Olimpo. A primeira missão envolve ajudar o copeiro de Zeus a recuperar seu cálice antes que ele caia nas mãos erradas. Será que Percy, Annabeth e Grover conseguirão achar o cálice dos deuses a tempo? Unindo aventura, ação e mitologia grega a personagens apaixonantes e tramas hilárias, a série Percy Jackson e os olimpianos transformou a literatura jovem nos últimos anos e conquistou fãs no mundo inteiro. A história de Rick Riordan sobre um adolescente com TDAH que descobre ser filho do deus do mar e precisa navegar entre o mundo humano e o divino se tornou um best-seller e formou uma geração de leitores apaixonados que até hoje acompanham a saga de Percy e seus amigos. O sucesso da série chegou também às telas, em uma adaptação da plataforma de streaming Disney+ com estreia prevista para 2024..",

        "imagem" : "percyjackson1.jpg",
        "personagem": "Percy Jackson"
    
    },

    {
        
        "titulo" : "Duna: livro 1",

        "preco" : 62.45,

        "sinopse" : "Em 'Duna Livro 1: Duna', Paul Atreides e sua família são designados para governar o planeta desértico Arrakis, a única fonte da preciosa especiaria melange. Mas, ao chegar, Paul se vê no meio de uma complexa trama política, com traições e disputas pelo controle do planeta. À medida que o destino de Arrakis se entrelaça com o de Paul, ele começa a despertar para um poder misterioso e potencialmente destrutivo.",

        "imagem" : "duna1.jpg",
        "personagem": "Duna"
    
    },


    {
        
        "titulo" : "It: A coisa",

        "preco" : 84.50,

        "sinopse" : "Durante as férias de 1958, em uma pacata cidadezinha chamada Derry, um grupo de sete amigos começa a ver coisas estranhas. Um conta que viu um palhaço, outro que viu uma múmia. Finalmente, acabam descobrindo que estavam todos vendo a mesma coisa: um ser sobrenatural e maligno que pode assumir várias formas. É assim que Bill, Beverly, Eddie, Ben, Richie, Mike e Stan enfrentam a Coisa pela primeira vez. Quase trinta anos depois, o grupo volta a se encontrar. Mike, o único que permaneceu em Derry, dá o sinal ― uma nova onda de terror tomou a pequena cidade. É preciso unir forças novamente. Só eles têm a chave do enigma. Só eles sabem o que se esconde nas entranhas de Derry. Só eles podem vencer a Coisa. “Mesmo depois de tantos anos, o público continua obcecado por IT. Ficamos obcecados porque todos temos medos. Todos temos algo que nos assusta, sejam palhaços e aranhas ou coisas que se escondem em um lugar muito mais profundo de nossa mente. Este livro fala com todo mundo. É o romance mais assustador de King, e duvido que isso vá mudar” ― The Guardian.",

        "imagem" : "ItaCoisa.jpg"
    },

{
        
        "titulo" : "A mulher na janela",

        "preco" : 48.50,

        "sinopse" : "Anna Fox mora sozinha na bela casa que um dia abrigou sua família feliz. Separada do marido e da filha e sofrendo de uma fobia que a mantém reclusa, ela passa os dias bebendo (muito) vinho, assistindo a filmes antigos, conversando com estranhos na internet e... espionando os vizinhos.Quando os Russells – pai, mãe e o filho adolescente – se mudam para a casa do outro lado do parque, Anna fica obcecada por aquela família perfeita. Certa noite, ela vê na casa deles algo que a deixa aterrorizada e faz seu mundo – e seus segredos chocantes – começar a ruir.Mas aquilo aconteceu mesmo? O que é realidade? Existe realmente alguém em perigo? E quem está no controle? Neste thriller diabolicamente viciante, ninguém – e nada – é o que parece.A mulher na janela é um suspense psicológico engenhoso e comovente que remete ao melhor de Hitchcock..",

        "imagem" : "amulhernajanela.jpg"
    },


{
        
        "titulo" : "O Retrato de Dorian Gray",

        "preco" : 32.60,

        "sinopse" : "Em 1891, quando foi publicado em sua versão final, O retrato de Dorian Gray foi recebido com escândalo, e provocou um intenso debate sobre o papel da arte em relação à moralidade. Alguns anos mais tarde, o livro foi inclusive usado contra o próprio autor em processos judiciais, como evidência de que ele possuía “uma certa tendência” - no caso, a homossexualidade, motivo pelo qual acabou condenado a dois anos de prisão por atentado ao pudor. Mais de cem anos depois, porém, o único romance de Oscar Wilde continua sendo lido e debatido no mundo inteiro, e por questões que vão muito além do moralismo do fim do período vitoriano na Inglaterra, definida por um dos personagens do livro como “a terra natal da hipocrisia”. Seu tema central - um personagem que leva uma vida dupla, mantendo uma aparência de virtude enquanto se entrega ao hedonismo mais extremado - tem apelo atemporal e universal, e sua trama se vale de alguns dos traços que notabilizaram a melhor literatura de sua época, como a presença de elementos fantásticos e de grandes reflexões filosóficas, além do senso de humor sagaz e do sarcasmo implacável característicos de Wilde.",

        "imagem" : "oretrato.jpg"
    },


    {
        
        "titulo" : "Romeu e Julieta",

        "preco" : 33.80,

        "sinopse" : "Há muito tempo duas famílias banham em sangue as ruas de Verona. Enquanto isso, na penumbra das madrugadas, ardem as brasas de um amor secreto. Romeu, filho dos Montéquio, e Julieta, herdeira dos Capuleto, desafiam a rixa familiar e sonham com um impossível futuro, longe da violência e da loucura. Romeu e Julieta é a primeira das grandes tragédias de William Shakespeare, e esta nova tradução de José Francisco Botelho recria com maestria o ritmo ao mesmo tempo frenético e melancólico do texto shakespeariano. Contando também com um excelente ensaio introdutório do especialista Adrian Poole, esta edição traz nova vida a uma das mais emocionantes histórias de amor já contadas",

        "imagem" : "RomeueJulieta.jpg"
    },

    
    {
        
        "titulo" : "Vidas Secas",

        "preco" : 70.00,

        "sinopse" : "Graciliano Ramos nasceu em 1892, no interior de Alagoas, e cresceu na fazenda do pai antes de se mudar para a capital do estado e, posteriormente, para o Rio de Janeiro, onde começou a trabalhar na imprensa. Em 1937, foi preso sob vagas acusações de defender ideologias comunistas. Ao deixar a prisão, procurou trabalho como jornalista em um jornal do Rio de Janeiro. O editor então lhe permitiu publicar um texto curto, e Graciliano escreveu um conto chamado “Baleia”, sobre o sofrimento e a morte da cachorrinha de uma família de retirantes sertanejos. O conto fez sucesso e o jornal encomendou outros no mesmo estilo. Graciliano produziu então um conto para cada membro da família: o pai, a mãe e os dois filhos. Nascia assim  Vidas secas , narrado em terceira pessoa, com treze capítulos que, por não terem uma linearidade temporal, podem ser lidos fora de ordem, como contos. Lançado originalmente em 1938,  Vidas secas  retrata a vida miserável de uma família de retirantes sertanejos obrigada a se deslocar de tempos em tempos para áreas menos castigadas pela seca. O pai, Fabiano, caminha pela paisagem árida da caatinga do Nordeste brasileiro com a sua mulher, Sinha Vitória, e os dois filhos, que não têm nome, sendo chamados apenas de “filho mais velho” e “filho mais novo”. São também acompanhados pela cachorrinha da família, Baleia, cujo nome é irônico, pois a falta de comida a fez muito magra. Vidas secas  pertence à segunda fase modernista da literatura brasileira, conhecida como “regionalista” ou “romance de 30”. Denuncia fortemente as mazelas do povo brasileiro, principalmente a situação de miséria do sertão nordestino. É o romance em que Graciliano alcança o máximo da expressão que vinha buscando em sua prosa: o que impulsiona os personagens é a seca, áspera e cruel, e paradoxalmente a ligação telúrica, afetiva, que expõe naqueles seres em retirada, à procura de meios de sobrevivência e um futuro.",

        "imagem" : "vidassecas.jpg"
    },

    {
    "titulo" : "Harry Potter e a Pedra Filosofal: 1",
    "preco" : 46.70,
    "sinopse" : "Harry Potter é um garoto cujos pais, feiticeiros, foram assassinados por um poderosíssimo bruxo quando ele ainda era um bebê. Ele foi levado, então, para a casa dos tios que nada tinham a ver com o sobrenatural. Pelo contrário. Até os 10 anos, Harry foi uma espécie de gata borralheira: maltratado pelos tios, herdava roupas velhas do primo gorducho, tinha óculos remendados e era tratado como um estorvo. No dia de seu aniversário de 11 anos, entretanto, ele parece deslizar por um buraco sem fundo, como o de Alice no país das maravilhas, que o conduz a um mundo mágico. Descobre sua verdadeira história e seu destino: ser um aprendiz de feiticeiro até o dia em que terá que enfrentar a pior força do mal, o homem que assassinou seus pais. O menino de olhos verdes, magricela e desengonçado, tão habituado à rejeição, descobre, também, que é um herói no universo dos magos. Potter fica sabendo que é a única pessoa a ter sobrevivido a um ataque do tal bruxo do mal e essa é a causa da marca em forma de raio que ele carrega na testa. Ele não é um garoto qualquer, ele sequer é um feiticeiro qualquer, ele é Harry Potter, símbolo de poder, resistência e um líder natural entre os sobrenaturais. A fábula, recheada de fantasmas, paredes que falam, caldeirões, sapos, unicórnios, dragões e gigantes, não é, entretanto, apenas um passatempo.",
    "imagem" : "harrypotter1.jpg",
    "personagem": "Harry Potter"
},

{
    "titulo" : "Harry Potter e a Câmara Secreta: 2",
    "preco" : 45.50,
    "sinopse" : "Depois de férias aborrecidas na casa dos tios trouxas, está na hora de Harry Potter voltar a estudar. Coisas acontecem, no entanto, para dificultar o regresso de Harry. Persistente e astuto, o herói não se deixa intimidar pelos obstáculos e, com a ajuda dos fiéis amigos Weasley, começa o ano letivo na Escola de Magia e Bruxaria de Hogwarts. As novidades não são poucas. Novos colegas, novos professores, muitas e boas descobertas e um grande e perigoso desafio. Alguém ou alguma coisa ameaça a segurança e a tranquilidade dos membros de Hogwarts.",
    "imagem" : "harrypotter2.jpg",
    "personagem": "Harry Potter"
},

{
    "titulo" : "Harry Potter e o Cálice de Fogo: 4",
    "preco" : 70.50,
    "sinopse" : "Nesta aventura, o feiticeiro cresceu e está com 14 anos. O início do ano letivo de Harry Potter reserva muitas emoções, mágicas e acontecimentos inesperados, além de um novo torneio em que os alunos de Hogwarts terão de demonstrar todas as habilidades mágicas e não mágicas que vêm adquirindo ao longo de suas vidas. Harry é escolhido pelo Cálice de Fogo para competir como um dos campeões de Hogwarts, tendo ao lado seus fiéis amigos. Muitos desafios, feitiços, poções e confusões estão reservados para Harry. Além disso, ele terá que lidar ainda com os problemas comuns da adolescência: amor, amizade, aceitação e rejeição.",
    "imagem" : "harrypotter4.jpg",
    "personagem": "Harry Potter"
},

{
    "titulo" : "Harry Potter e a Ordem da Fênix: 5",
    "preco" : 89.90,
    "sinopse" : "Harry não é mais um garoto. Aos 15 anos, continua sofrendo a rejeição dos Dursley, sua estranha família no mundo dos 'trouxas'. Também continua contando com Rony Weasley e Hermione Granger, seus melhores amigos em Hogwarts, para levar adiante suas investigações e aventuras. Mas o bruxinho começa a sentir e descobrir coisas novas, como o primeiro amor e a sexualidade. Nos volumes anteriores, J. K. Rowling mostrou como Harry foi transformado em celebridade no mundo da magia por ter derrotado, ainda bebê, Voldemort, o todopoderoso bruxo das trevas que assassinou seus pais. Neste quinto livro da saga, o protagonista, numa crise típica da adolescência, tem ataques de mau humor com a perseguição da imprensa, que o segue por todos os lugares e chega a inventar declarações que nunca deu. Harry vai enfrentar as investidas de Voldemort sem a proteção de Dumbledore, já que o diretor de Hogwarts é afastado da escola. E vai ser sem a ajuda de seu protetor que o jovem herói enfrentará descobertas sobre a personalidade controversa de seu pai, Tiago Potter, e a morte de alguém muito próximo.",
    "imagem" : "harrypotter5.jpg",
    "personagem": "Harry Potter"
},

{
    "titulo" : "O mar de monstros: Série Percy Jackson e os olimpianos: 2",
    "preco" : 45.90,
    "sinopse" : "Unindo mitologia grega, muita aventura e tramas hilárias, a história de Rick Riordan sobre um adolescente com TDAH que descobre ser filho do deus do mar e precisa navegar entre o mundo humano e o divino se tornou um best-seller e formou uma geração de leitores apaixonados que até hoje acompanham a saga de Percy e seus amigos. Agora, a Intrínseca relança os cinco livros da série em uma edição com nova arte de capa, tão pedida pelos leitores. As belas ilustrações da artista Victo Ngai acompanham o design da mais nova aventura de Percy Jackson, O cálice dos deuses , que chega às livrarias em lançamento mundial no dia 26 de setembro. Em O Mar de Monstros , segundo livro da série, o ano de Percy foi surpreendentemente calmo. Nenhum monstro em sua escola, nenhum acidente esquisito, nenhuma briga em sala de aula. Mas, quando um inocente jogo de queimado entre ele e seus colegas torna-se uma disputa mortal contra uma tenebrosa gangue de gigantes canibais, as coisas ficam, digamos, feias. Com a inesperada chegada da amiga Annabeth vêm outras más notícias: as fronteiras mágicas que protegem o Acampamento Meio-Sangue foram envenenadas por um inimigo desconhecido, e, a menos que um antídoto seja encontrado, o único porto seguro dos semideuses será destruído. Nesta aventura vibrante e divertidíssima, Percy e seus amigos partem em uma arriscada e incrível viagem pelo Mar de Monstros para salvar o acampamento. Lá, eles vão enfrentar seres fantásticos, muitos perigos e situações inusitadas. Antes, porém, nosso herói entrará em confronto com um mistério atordoante sobre sua família ― algo que o fará questionar se ser filho de Poseidon é uma honra ou uma terrível maldição.",
    "imagem" : "percyjackson2.jpg",
    "personagem": "Percy Jackson"
},

{
    "titulo" : "A maldição do titã: Série Percy Jackson e os olimpianos: 3",
    "preco" : 44.50,
    "sinopse" : "Unindo mitologia grega, muita aventura e tramas hilárias, a história de Rick Riordan sobre um adolescente com TDAH que descobre ser filho do deus do mar e precisa navegar entre o mundo humano e o divino se tornou um best-seller e formou uma geração de leitores apaixonados, que até hoje acompanham a saga de Percy e seus amigos. Agora, a Intrínseca relança os cinco livros da série em uma edição com nova arte de capa, muito pedida pelos leitores. As belas ilustrações da artista Victo Ngai acompanham o design da mais nova aventura do semideus, O cálice dos deuses , que chega às livrarias em lançamento mundial no dia 26 de setembro. No terceiro livro da série, um chamado do amigo Grover deixa Percy a postos para mais uma missão: dois novos meios-sangues foram encontrados, e sua ascendência ainda é desconhecida. Como sempre, Percy sabe que precisará contar com o poder de seus aliados, com sua leal espada Contracorrente... e com uma caroninha da mãe. Eles só não desconfiam de que os jovens descobertos não são os únicos em perigo: Cronos, o Senhor dos Titãs, arquitetou um de seus planos mais traiçoeiros, e nossos heróis serão presas fáceis. Um monstro ancestral foi despertado ― um ser com poder suficiente para destruir o Olimpo ―, e Ártemis, a única capaz de encontrá-lo, desapareceu. Percy e seus amigos têm apenas uma semana para resgatar a deusa sequestrada e solucionar o mistério que ronda o monstro que ela caçava. Divertidíssimo e repleto de ação, o livro coloca nosso herói e seus aliados frente a frente com o maior desafio de suas vidas: a terrível profecia da maldição do titã.",
    "imagem" : "percyjackson3.jpg",
    "personagem": "Percy Jackson"
},

{
    "titulo" : "A batalha do labirinto: Série Percy Jackson e os olimpianos: 4",
    "preco" : 89.90,
    "sinopse" : "Unindo mitologia grega, muita aventura e tramas hilárias, a história de Rick Riordan sobre um adolescente com TDAH que descobre ser filho do deus do mar e precisa navegar entre o mundo humano e o divino se tornou um best-seller e formou uma geração de leitores apaixonados que até hoje acompanham a saga de Percy e seus amigos. Agora, a Intrínseca relança os cinco livros da série em uma edição imperdível com nova arte de capa, muito pedida pelos leitores. As belas ilustrações da artista Victo Ngai acompanham o design da mais nova aventura do semideus, O cálice dos deuses , que chega às livrarias em lançamento mundial no dia 26 de setembro. Neste quarto volume da série, Percy começou o ano letivo em uma nova escola. Ele já não esperava que a experiência fosse lá muito agradável, mas, ao dar de cara com líderes de torcida monstruosas e mortas de fome, conclui que tudo pode sempre ficar ainda pior. O tempo está se esgotando e a batalha entre os deuses do Olimpo e Cronos, o Senhor dos Titãs, está cada vez mais próxima. Até o Acampamento Meio-Sangue, o porto seguro dos heróis, torna-se vulnerável à medida que os exércitos de Cronos abrem caminho para atacar suas fronteiras, até então impenetráveis. Para detê-los, Percy e seus amigos semideuses partirão em uma jornada pelo Labirinto de Dédalo ― um interminável universo subterrâneo que, a cada curva, revela as mais temíveis surpresas.",
    "imagem" : "percyjackson4.jpg",
    "personagem": "Percy Jackson"
},

{
    "titulo" : "O último olimpiano: Série Percy Jackson e os olimpianos: 5",
    "preco" : 39.45,
    "sinopse" : "Unindo mitologia grega, muita aventura e tramas hilárias, a história de Rick Riordan sobre um adolescente com TDAH que descobre ser filho do deus do mar e precisa navegar entre o mundo humano e o divino se tornou um best-seller e formou uma geração de leitores apaixonados que até hoje acompanham a saga de Percy e seus amigos. Agora, a Intrínseca relança os cinco livros da série em uma edição com nova arte de capa, muito pedida pelos leitores. As belas ilustrações da artista Victo Ngai acompanham o design da mais nova aventura do semideus, O cálice dos deuses , que chega às livrarias em lançamento mundial no dia 26 de setembro. Neste quinto volume da série, os meios-sangues passaram o ano inteiro preparando-se para a batalha contra os titãs, e sabem que as chances de vitória são pequenas. O exército de Cronos está mais poderoso que nunca, e cada deus ou semideus que se une à causa confere mais força ao vingativo titã. Enquanto os olimpianos tentam conter a fúria do monstro Tifão, Cronos avança em direção à cidade de Nova York, onde o Monte Olimpo está precariamente vigiado. E apenas Percy Jackson e seu exército de heróis podem deter o Senhor do Tempo. Em O último olimpiano , o acirrado combate que pode acarretar o fim da civilização ocidental ganha as ruas de Manhattan, e Percy tem a terrível sensação de que sua luta, na verdade, é contra o próprio destino. Revelada a sinistra profecia acerca do décimo sexto aniversário do herói, ele enfim encontra seu verdadeiro caminho.",
    "imagem" : "percyjackson5.jpg",
    "personagem": "Percy Jackson"
},

{
    "titulo" : "A espada do destino - The Witcher - A saga do bruxo Geralt de Rívia 2",
    "preco" : 51.00,
    "sinopse" : "Geralt de Rívia é um bruxo. Um feiticeiro cheio de astúcia. Um matador impiedoso. Um assassino de sangue-frio, treinado desde a infância para caçar e eliminar monstros. Seu único objetivo: destruir as criaturas do mal que assolam o mundo. Um mundo fantástico criado por Sapkowski com claras influências da mitologia eslava. Um mundo em que nem todos os que parecem monstros são maus e nem todos os que parecem anjos são bons. A espada do destino é o segundo livro da saga do bruxo Geralt de Rívia e terá continuidade com O sangue dos elfos.",
    "imagem" : "thewitcher2.jpg",
    "personagem": "The Witcher"
},

{
    "titulo" : "O sangue dos elfos - The Witcher - A saga do bruxo Geralt de Rívia: 3",
    "preco" : 52.00,
    "sinopse" : "Geralt de Rívia é um bruxo sagaz e habilidoso. Um assassino impiedoso e de sangue-frio treinado, desde a infância, para caçar e eliminar monstros. Seu único objetivo: destruir as criaturas do mal que assolam o mundo. Um mundo fantástico criado por Sapkowski com claras influências da mitologia eslava. Um mundo em que nem todos os que parecem monstros são maus e nem todos os que parecem anjos são bons...",
    "imagem" : "thewitcher3.jpg",
    "personagem": "The Witcher"
},

{
    "titulo" : "Tempo do desprezo - The Witcher - A saga do bruxo Geralt de Rívia: 4",
    "preco" : 59.00,
    "sinopse" : "Tempo do desprezo é o quarto livro da saga do bruxo Geralt de Rívia. Geralt lutou contra monstros e demônios por todo o país, mas até ele pode não estar preparado para o que está acontecendo com seu mundo. Há intrigas, divergências e rebeliões por todo lado. Os Elfos e outros seres não humanos vivem sob repressão há décadas. Os Magos brigam uns com os outros, alguns a soldo dos reis, outros simpatizantes dos elfos. E, nesse cenário de medo e desprezo, Geralt e sua amante Yennefer precisam proteger Ciri, herdeira órfã e procurada por todos os lados. Ela tem o poder de salvar o mundo ou, talvez, acabar com ele.",
    "imagem" : "thewitcher4.jpg",
    "personagem": "The Witcher"
},

{
    "titulo" : "Batismo de fogo - The Witcher - A saga do bruxo Geralt de Rívia: 5",
    "preco" : 60.50,
    "sinopse" : "Batismo de fogo é o quinto livro da saga do bruxo Geralt de Rívia. A Irmandade dos Magos foi esfacelada por um golpe e Geralt ficou seriamente ferido. E agora, que tempos sombrios pairam sobre o mundo, ele não poderá defender os homens contra os monstros perigosos que os aterrorizam. Guerras devastam todos os territórios e o futuro da magia está ameaçado. Mas as feiticeiras que sobreviveram estão determinadas a protegê-lo. É um momento conturbado, e ainda é preciso encontrar a garota Ciri, herdeira do trono de Cintra, que desapareceu. Até que surge o rumor de que ela está na corte de Nilfgaard e vai se casar com o imperador. Ferido ou não, Geralt tem uma missão em suas mãos. Fenômeno literário que inspirou a criação do game The Witcher.",
    "imagem" : "thewitcher5.jpg",
    "personagem": "The Witcher"
},

{
    "titulo" : "As Crônicas de Nárnia: O Leão, a Feiticeira e o Guarda-roupa",
    "preco" : 34.50,
    "sinopse" : "O Leão, a Feiticeira e o Guarda-roupa conta a história dos irmãos Pedro, Susana, Edmundo e Lúcia Pevensie. Em meio a brincadeiras na casa de um velho professor, eles descobrem um misterioso guarda-roupa que os leva a Nárnia, um reino mágico que sofre de um inverno sem fim desde que Jadis, a temida Feiticeira Branca, tomou o poder. Mas uma antiga profecia ― que envolve justamente quatro crianças, além de um fantástico leão chamado Aslan ― afirma que há esperança para o reino, contanto que se tenha coragem. Escrito pelo gênio C.S. Lewis, O Leão, a Feiticeira e o Guarda-roupa foi o primeiro livro lançado de As Crônicas de Nárnia, em 1950. Esta obra encanta crianças e adultos há mais de 70 anos, o que faz dela um dos maiores clássicos do gênero infantojuvenil e fantástico. Há muito aguardada pelos fãs, esta é a versão definitiva para os amantes de Sr. Tumnus e dos seus amigos da floresta. Com nova tradução de Ronald Kyrmse, o livro possui capa dura com acabamento soft touch e pintura trilateral, além de ter ilustrações coloridas de Pauline Baynes, a artista favorita de C.S. Lewis e de seu melhor amigo, J.R.R. Tolkien, autor de O Hobbit e O Senhor dos Anéis.",
    "imagem" : "narnia1.jpg",
    "personagem": "Narnia"
},

{
    "titulo" : "As Crônicas de Nárnia: Príncipe Caspian",
    "preco" : 35.50,
    "sinopse" : "Príncipe Caspian conta a história de um período em que Nárnia era dominada pelo Rei Miraz, quando toda a magia e encanto de Nárnia foram abafados por seu reinado. Seu sobrinho, Caspian X, é o rei legítimo de Nárnia e contará com a ajuda de Pedro, Susana, Edmundo e Lúcia para retomar o trono e restabelecer a paz. Escrito pelo gênio C.S. Lewis, este é o quarto livro de As Crônicas de Nárnia, um dos maiores clássicos da literatura infantojuvenil. Promovendo valores como a lealdade, honestidade, justiça e bondade, essas histórias envolventes marcaram gerações de leitores no mundo todo. Há muito aguardada pelos fãs e com nova tradução de Ronald Kyrmse, esta edição possui capa dura com acabamento soft touch e pintura trilateral, além de ter ilustrações coloridas de Pauline Baynes, a artista favorita de C.S. Lewis e de seu melhor amigo, J.R.R. Tolkien, autor de O Hobbit e O Senhor dos Anéis.",
    "imagem" : "narnia2.jpg",
    "personagem": "Narnia"
},

{
    "titulo" : "As Crônicas de Nárnia: A Viagem do Peregrino da Alvorada",
    "preco" : 36.50,
    "sinopse" : "Em A Viagem do Peregrino da Alvorada, os corajosos Edmundo e Lúcia ― e seu rabugento primo Eustáquio ― juntam-se ao Rei Caspian X, a fim de encontrar sete lordes que foram exilados após o malvado Miraz usurpar o trono de Nárnia. Conforme navegam por mares desconhecidos e se deparam com criaturas fantásticas e ilhas encantadas, as crianças descobrem que sua jornada é maior e mais perigosa do que imaginavam ― e que o fim do mundo é apenas o começo. Este é o terceiro livro da série de C.S. Lewis, um dos maiores clássicos da literatura infantojuvenil. Promovendo valores como a lealdade, honestidade, justiça e bondade, as histórias envolventes de As Crônicas de Nárnia marcaram gerações de leitores no mundo todo.",
    "imagem" : "narnia3.jpg",
     "personagem": "Narnia"
},

{
    "titulo" : "As Crônicas de Nárnia: A Cadeira de Prata",
    "preco" : 60.50,
    "sinopse" : "Em A Cadeira de Prata, anos se passaram em Nárnia. O Rei Caspian X já está bem velho, e o Príncipe Rilian, seu único filho e herdeiro, está desaparecido. Para desvendar esse mistério, Aslan convoca Eustáquio, o primo dos irmãos Pevensie, e Giu, a amiga de escola que já o escutou falar muito a respeito desse mundo mágico. Guiados por Poçaflito, um narniano extremamente pessimista e preocupado, eles vão embarcar em uma jornada muito perigosa que os levará até o fundo do mundo. Há muito aguardada pelos fãs e com nova tradução de Ronald Kyrmse, esta edição possui capa dura com acabamento soft touch e pintura trilateral, além de ter ilustrações coloridas de Pauline Baynes, a artista favorita de C.S. Lewis e de seu melhor amigo, J.R.R. Tolkien, autor de O Hobbit e O Senhor dos Anéis.",
    "imagem" : "narnia4.jpg",
    "personagem": "Narnia"
},

{
    "titulo" : "As Crônicas de Nárnia: O cavalo e seu Menino",
    "preco" : 43.50,
    "sinopse" : "Em O Cavalo e seu Menino acompanhamos a história de Shasta ― filho adotivo de um pai nada afetivo ― nas terras ao sul de Nárnia. Após descobrir que seria vendido como escravo, ele foge rumo ao destino de seus sonhos ― para o Norte e em direção a Nárnia! Ao lado do cavalo falante Bri, Shasta viverá uma aventura que terminará por colocá-lo no centro de uma batalha que decidirá não apenas seu destino, mas também o de toda Nárnia. Há muito aguardada pelos fãs e com nova tradução de Ronald Kyrmse, esta edição possui capa dura com acabamento soft touch e pintura trilateral, além de ter ilustrações coloridas de Pauline Baynes, a artista favorita de C.S. Lewis e de seu melhor amigo, J.R.R. Tolkien, autor de O Hobbit e O Senhor dos Anéis.",
    "imagem" : "narnia5.jpg",
    "personagem": "Narnia"
},

{
    "titulo" : "Duna Livro 2: O Messias de Duna",
    "preco" : 79.90,
    "sinopse" : "Em 'Duna Livro 2: O Messias de Duna', Paul Atreides agora é o imperador de um vasto império, mas o peso do poder e as consequências de suas ações começam a se manifestar. A especiaria melange e a profecia de Paul como o messias reverberam por todo o universo, enquanto ele enfrenta novas ameaças e conspirações que podem destruir tudo o que ele construiu.",
    "imagem" : "duna2.jpg",
    "personagem": "Duna"
},

{
    "titulo" : "Duna Livro 3: Filhos de Duna",
    "preco" : 79.90,
    "sinopse" : "Em 'Duna Livro 3: Filhos de Duna', os filhos de Paul, Leto II e Ghanima, se veem no centro da luta pelo futuro de Arrakis e do império. Enquanto o passado de seu pai e a presciência de Paul pairam sobre eles, eles enfrentam perigos tanto externos quanto internos, enquanto lutam contra a ameaça de uma nova ordem que pode alterar o destino da galáxia.",
    "imagem" : "duna3.jpg",
    "personagem": "Duna"
},

{
    "titulo" : "Duna Livro 4: O Imperador-Deus de Duna",
    "preco" : 79.90,
    "sinopse" : "Em 'Duna Livro 4: O Imperador-Deus de Duna', Leto II, o filho de Paul Atreides, tornou-se uma figura quase divina, governando o império com mão de ferro. Ao se transformar em uma criatura híbrida entre humano e verme das areias, Leto II busca um caminho para a sobrevivência da humanidade, mas sua tirania e os sacrifícios necessários para manter sua visão de futuro geram grandes conflitos.",
    "imagem" : "duna4.jpg",
    "personagem": "Duna"
},

{
    "titulo" : "Duna Livro 5: Heréticos de Duna",
    "preco" : 79.90,
    "sinopse" : "Em 'Duna Livro 5: Heréticos de Duna', a galáxia está em um momento de transição após a queda do império de Leto II. A nova luta pelo poder envolve grupos poderosos como as Bene Gesserit, os Tleilaxu e os navegadores da Guilda Espacial. Enquanto novos mistérios surgem, o planeta Arrakis continua a ser o centro de disputas e intrigas que podem mudar o futuro da humanidade.",
    "imagem" : "duna5.jpg",
    "personagem": "Duna"
},

{
    "titulo": "O Senhor dos Anéis Livro 1: A Sociedade do Anel",
    "preco": 69.90,
    "sinopse": "Em 'O Senhor dos Anéis Livro 1: A Sociedade do Anel', o jovem hobbit Frodo Bolseiro é incumbido de uma missão perigosa para destruir o Um Anel e impedir que o sombrio Sauron domine a Terra-média. Com a ajuda de seus amigos e aliados, ele inicia uma jornada épica através de terras traiçoeiras e perigosas.",
    "imagem": "senhordosaneis1.jpg",
    "personagem": "Senhor Anéis"
},


{
    "titulo" : "O Senhor dos Anéis Livro 2: As Duas Torres",
    "preco" : 69.90,
    "sinopse" : "Em 'O Senhor dos Anéis Livro 2: As Duas Torres', Frodo e Sam continuam sua jornada para destruir o Um Anel, enquanto Aragorn, Legolas e Gimli lutam contra as forças de Saruman e Sauron. A batalha pela Terra-média ganha intensidade, e as alianças entre os povos livres da Terra-média são testadas.",
    "imagem" : "senhordosaneis2.jpg",
    "personagem": "Senhor Anéis"
},

{
    "titulo" : "O Senhor dos Anéis Livro 3: O Retorno do Rei",
    "preco" : 69.90,
    "sinopse" : "No último livro da trilogia, 'O Senhor dos Anéis Livro 3: O Retorno do Rei', a guerra contra as forças de Sauron chega ao seu clímax. Frodo enfrenta o maior desafio de sua vida enquanto tenta destruir o Um Anel, enquanto Aragorn reivindica seu destino como rei e líder das forças da liberdade.",
    "imagem" : "senhordosaneis3.jpg",
    "personagem": "Senhor Anéis"
},

{
    "titulo" : "Sherlock Holmes - Um estudo em vermelho",
    "preco" : 10.00,
    "sinopse" : "Holmes é chamado para solucionar o caso de um homem que foi encontrado morto, com uma expressão de terror, mas que não apresenta ferimentos, apenas manchas de sangue pelo corpo.",
    "imagem" : "sherlockholmes1.jpg",
    "personagem": "Sherlock Holmes"
},

{
    "titulo" : "Sherlock Holmes - O signo dos quatro",
    "preco" : 12.50,
    "sinopse" : "Holmes é procurado por Mary Morstan para descobrir o que aconteceu com seu pai que morreu há dez anos. Começa uma investigação, e, acompanhado do dr. Watson, Holmes se depara com curiosas pistas.",
    "imagem" : "sherlockholmes2.jpg",
    "personagem": "Sherlock Holmes"
},

{
    "titulo" : "As aventuras de Sherlock Holmes",
    "preco" : 10.00,
    "sinopse" : "Sherlock Holmes é um detetive britânico enigmático e pedante do final do século XIX e início do século XX. Ele utiliza a metodologia científica e a lógica dedutiva para solucionar seus casos e conta com a ajuda de seu fiel amigo e parceiro dr. Watson. Observação, perspicácia e um pouco de intuição são alguns dos instrumentos usados por Sherlock Holmes para desvendar os seis curiosos casos reunidos nesta obra e narrados pelo atento doutor Watson.",
    "imagem" : "sherlockholmes3.jpg",
    "personagem": "Sherlock Holmes"
},

{
    "titulo" : "Memórias de Sherlock Holmes",
    "preco" : 15.00,
    "sinopse" : "Sherlock Holmes é um detetive britânico enigmático e pedante do final do século XIX e início do século XX. Ele utiliza a metodologia científica e a lógica dedutiva para solucionar seus casos e conta com a ajuda de seu fiel amigo e parceiro dr. Watson. Memórias de Sherlock Holmes é o último livro em que o doutor Watson narra os misteriosos casos solucionados pelo famoso detetive. O livro conta com onze histórias envolventes e enigmáticas em que vemos Holmes e Watson em ação.",
    "imagem" : "sherlockholmes4.jpg",
    "personagem": "Sherlock Holmes"
},

{
    "titulo" : "Sherlock Holmes - O cão dos Baskerville",
    "preco" : 12.00,
    "sinopse" : "Holmes investiga a morte do milionário Sir Charles Baskerville, que foi encontrado em um pântano próximo a sua casa. Uma lenda local dizia que ele foi assassinado por um cão que assombrava a região. Será isso mesmo?",
    "imagem" : "sherlockholmes5.jpg",
    "personagem": "Sherlock Holmes"
},

{
    "titulo" : "Game of Thrones Livro 1: A Guerra dos Tronos",
    "preco" : 89.90,
    "sinopse" : "Em 'Game of Thrones Livro 1: A Guerra dos Tronos', o reino dos Sete Reinos é abalado pela luta pelo Trono de Ferro. Eddard Stark, patriarca da Casa Stark, é chamado a ser o Mão do Rei, enquanto conspirações e intrigas ameaçam a paz, enquanto os Targaryen planejam retornar ao poder.",
    "imagem" : "gameofthrones1.jpg",
    "personagem": "Game Of Thrones"
},

{
    "titulo" : "Game of Thrones Livro 2: A Fúria dos Reis",
    "preco" : 89.90,
    "sinopse" : "Em 'Game of Thrones Livro 2: A Fúria dos Reis', a guerra pelo Trono de Ferro se intensifica. Novos reinos se levantam, e as famílias poderosas se enfrentam por poder, honra e sobrevivência. Enquanto isso, em terras distantes, as ameaças além do Muro se tornam mais perigosas.",
    "imagem" : "gameofthrones2.jpg",
    "personagem": "Game Of Thrones"
},

{
    "titulo" : "Game of Thrones Livro 3: A Tormenta de Espadas",
    "preco" : 89.90,
    "sinopse" : "Em 'Game of Thrones Livro 3: A Tormenta de Espadas', os destinos dos grandes personagens se entrelaçam enquanto as batalhas por Westeros atingem proporções épicas. Os filhos das casas poderosas enfrentam seus próprios demônios, e a guerra pelo Trono de Ferro se aproxima de seu clímax.",
    "imagem" : "gameofthrones5.jpg",
    "personagem": "Game Of Thrones"
},

{
    "titulo" : "Game of Thrones Livro 4: O Festim dos Corvos",
    "preco" : 89.90,
    "sinopse" : "No 'Game of Thrones Livro 4: O Torneio dos Reis', a guerra entre os pretendentes ao Trono de Ferro chega ao seu ponto de ruptura. Alianças são formadas e desfeitas, enquanto a luta pelo poder se espalha por toda Westeros. Ao mesmo tempo, a ameaça de criaturas misteriosas cresce no norte.",
    "imagem" : "gameofthrones3.jpg",
    "personagem": "Game Of Thrones"
},

{
    "titulo" : "Game of Thrones Livro 5: A Dança dos Dragões",
    "preco" : 89.90,
    "sinopse" : "Em 'Game of Thrones Livro 5: A Dança dos Dragões', o jogo político e a luta pelo poder continuam a dominar os Sete Reinos. Novas figuras surgem e antigas casas caem, enquanto os dragões de Daenerys começam a reacender a chama do império Targaryen.",
    "imagem" : "gameofthrones4.jpg",
    "personagem": "Game Of Thrones"
},



{
    "titulo": "A cantiga dos pássaros e das serpentes",
    "preco": 53.00,
    "sinopse": "UMA HISTÓRIA DA SÉRIE JOGOS VORAZES. AMBIÇÃO O ALIMENTARÁ. COMPETIÇÃO O CONDUZIRÁ. MAS O PODER TEM O SEU PREÇO. É a manhã do dia da colheita que iniciará a décima edição dos Jogos Vorazes. Na Capital, o jovem de dezoito anos Coriolanus Snow se prepara para sua oportunidade de glória como um mentor dos Jogos. A outrora importante casa Snow passa por tempos difíceis e o destino dela depende da pequena chance de Coriolanus ser capaz de encantar, enganar e manipular seus colegas estudantes para conseguir mentorar o tributo vencedor. A sorte não está a favor dele. A ele foi dada a tarefa humilhante de mentorar a garota tributo do Distrito 12, o pior dos piores. Os destinos dos dois estão agora interligados – toda escolha que Coriolanus fizer pode significar sucesso ou fracasso, triunfo ou ruína. Na arena, a batalha será mortal. Fora da arena, Coriolanus começa a se apegar a já condenada garota tributo... e deverá pesar a necessidade de seguir as regras e o desejo de sobreviver custe o que custar.",
    "imagem": "jogosvorazes1.jpg",
    "personagem": "Jogos Vorazes"
},

{
    "titulo": "Jogos Vorazes",
    "preco": 44.00,
    "sinopse": "Na abertura dos Jogos Vorazes, a organização não recolhe os corpos dos combatentes caídos e dá tiros de canhão até o final. Cada tiro, um morto. Onze tiros no primeiro dia. Treze jovens restaram, entre eles, Katniss. Para quem os tiros de canhão serão no dia seguinte?...\nApós o fim da América do Norte, uma nova nação chamada Panem surge. Formada por doze distritos, é comandada com mão de ferro pela Capital. Uma das formas com que demonstra seu poder sobre o resto do carente país é com Jogos Vorazes, uma competição anual transmitida ao vivo pela televisão, em que um garoto e uma garota de doze a dezoito anos de cada distrito são selecionados e obrigados a lutar até a morte!\nPara evitar que sua irmã seja a mais nova vítima do programa, Katniss se oferece para participar em seu lugar. Vinda do empobrecido Distrito 12, ela sabe como sobreviver em um ambiente hostil. Peeta, um garoto que ajudou sua família no passado, também foi selecionado. Caso vença, terá fama e fortuna. Se perder, morre. Mas para ganhar a competição, será preciso muito mais do que habilidade. Até onde Katniss estará disposta a ir para ser vitoriosa nos Jogos Vorazes?\nBest-seller da Veja, a trilogia Jogos Vorazes foi adaptada para o cinema e estrelada por Jennifer Lawrence.",
    "imagem": "jogosvorazes2.jpg",
    "personagem": "Jogos Vorazes"
},

{
    "titulo": "Jogos Vorazes: Em Chamas",
    "preco": 41.00,
    "sinopse": "Depois da improvável e inusitada vitória de Katniss Everdeen e Peeta Mellark nos últimos Jogos Vorazes, algo parece ter mudado para sempre em Panem. Aqui e ali, distúrbios e agitações nos distritos dão sinais de que uma revolta é iminente. Katniss e Peeta, representantes do paupérrimo Distrito 12, não apenas venceram os Jogos, mas ridicularizaram o governo e conseguiram fazer todos – incluindo o próprio Peeta – acreditarem que são um casal apaixonado. A confusão na cabeça de Katniss não é menor do que a das ruas. Em meio ao turbilhão, ela pensa cada vez mais em seu melhor amigo, o jovem caçador Gale, mas é obrigada a fingir que o romance com Peeta é real. Já o governo parece especialmente preocupado com a influência que os dois adolescente vitoriosos – transformados em verdadeiros ídolos nacionais – podem ter na população. Por isso, existem planos especiais para mantê-los sob controle, mesmo que isso signifique forçá-los a lutar novamente. Apenas um sobrevive. Best-seller da Veja, a trilogia Jogos Vorazes foi adaptada para o cinema e estrelada por Jennifer Lawrence.",
    "imagem": "jogosvorazes3.jpg",
    "personagem": "Jogos Vorazes"
},

{
    "titulo": "Jogos Vorazes: A Esperança: 3",
    "preco": 46.00,
    "sinopse": "Depois de sobreviver duas vezes à crueldade de uma arena projetada para destruí-la, Katniss acreditava que não precisaria mais lutar. Mas as regras do jogo mudaram: com a chegada dos rebeldes do lendário Distrito 13, enfim é possível organizar uma resistência. Começou a revolução.\nA coragem de Katniss nos jogos fez nascer a esperança em um país disposto a fazer de tudo para se livrar da opressão. E agora, contra a própria vontade, ela precisa assumir seu lugar como símbolo da causa rebelde. Ela precisa virar o Tordo.\nO sucesso da revolução dependerá de Katniss aceitar ou não essa responsabilidade. Será que vale a pena colocar sua família em risco novamente? Será que as vidas de Peeta e Gale serão os tributos exigidos nessa nova guerra?\nAcompanhe Katniss até o fim deste thriller, numa jornada ao lado mais obscuro da alma humana, em uma luta contra a opressão e a favor da esperança.",
    "imagem": "jogosvorazes4.jpg",
    "personagem": "Jogos Vorazes"
},

{
    "titulo": "A Guerra dos Tronos: As Crônicas de Gelo e Fogo, volume 1",
    "preco": 70.00,
    "sinopse": "A guerra dos tronos é o primeiro livro da série best-seller internacional As Crônicas de Gelo e Fogo, que deu origem à adaptação de sucesso da HBO, Game of Thrones.\nO verão pode durar décadas. O inverno, toda uma vida. E a guerra dos tronos começou. Como Guardião do Norte, lorde Eddard Stark não fica feliz quando o rei Robert o proclama a nova Mão do Rei. Sua honra o obriga a aceitar o cargo e deixar seu posto em Winterfell para rumar para a corte, onde os homens fazem o que lhes convém, não o que devem... e onde um inimigo morto é algo a ser admirado.\nLonge de casa e com a família dividida, Eddard se vê cada vez mais enredado nas intrigas mortais de Porto Real, sem saber que perigos ainda maiores espreitam a distância.\nNas florestas ao norte de Winterfell, forças sobrenaturais se espalham por trás da Muralha que protege a região. E, nas Cidades Livres, o jovem Rei Dragão exilado na Rebelião de Robert planeja sua vingança e deseja recuperar sua herança de família: o Trono de Ferro de Westeros.\n“A guerra dos tronos é a maior obra de fantasia desde que Bilbo encontrou o Anel.” — SF Reviews.",
    "imagem": "cronicasgeloefogo1.jpg",
    "personagem": "Crônicas"
},

{
    "titulo": "A Fúria dos Reis: As Crônicas de Gelo e Fogo, volume 2",
    "preco": 68.00,
    "sinopse": "Um cometa da cor de fogo e sangue corta os céus. E, da antiga cidadela de Pedra do Dragão às costas áridas de Winterfell, reina o caos.\nEm A fúria dos reis, seis facções disputam o controle de uma terra dividida e o direito de ocupar o Trono de Ferro de Westeros – e estão dispostos a encarar tempestades, levantes e guerras para isso.\nNesta história, irmão trama contra irmão e os mortos se levantam para caminhar pela noite. Aqui, uma princesa se disfarça de menino órfão, um cavaleiro se prepara para encarar uma pérfida feiticeira e bárbaros descem das Montanhas da Lua para saquear os campos.\nEm um contexto de incesto e fratricídio, alquimia e assassinato, a vitória será dos homens e mulheres que possuírem o mais frio aço... e o mais frio coração. Pois, quando se desperta a fúria dos reis, a terra inteira treme.",
    "imagem": "cronicasgeloefogo2.jpg",
    "personagem": "Crônicas"
},

{
    "titulo": "A Tormenta de Espadas: As Crônicas de Gelo e Fogo, volume 3",
    "preco": 80.00,
    "sinopse": "O futuro de Westeros está em jogo, e ninguém descansará até que os Sete Reinos tenham explodido em uma verdadeira tormenta de espadas.\nDos cinco pretendentes ao trono, um está morto e outro caiu em desgraça, e ainda assim a guerra continua em toda sua fúria, enquanto alianças são feitas e desfeitas. Joffrey, da Casa Lannister, ocupa o Trono de Ferro, como o instável governante dos Sete Reinos, ao passo que seu rival mais amargo, lorde Stannis, jaz derrotado e enfeitiçado pelas promessas da Mulher Vermelha.\nO jovem Robb, da Casa Stark, ainda comanda o Norte, contudo, e planeja sua batalha contra os Lannister, mesmo que sua irmã seja refém deles em Porto Real. Enquanto isso, Daenerys Targaryen atravessa um continente deixando um rastro de sangue a caminho de Westeros, levando consigo os três únicos dragões existentes em todo o mundo.\nEnquanto forças opostas avançam para uma gigantesca batalha final, um exército de selvagens chega dos confins da civilização. Em seu rastro vem uma horda de terríveis criaturas místicas – os Outros: um batalhão de mortos-vivos cujos corpos são imparáveis.",
    "imagem": "cronicasgeloefogo3.jpg",
    "personagem": "Crônicas"
},

{
    "titulo": "O Festim dos Corvos: As Crônicas de Gelo e Fogo, volume 4",
    "preco": 68.00,
    "sinopse": "Há séculos os sete grandes reinos de Westeros se enfrentam em amargas disputas, batalhas e traições. Agora, com Joffrey Baratheon e Robb Stark fora da jogada e lordes insignificantes competindo pelas Ilhas de Ferro, a guerra que devorou o continente parece ter finalmente chegado ao fim.\nNo entanto, como após todo grande conflito, não demora para que os sobreviventes, os bandidos, os renegados e os carniceiros avancem para disputar o espólio dos mortos. Por toda Westeros os lordes se agitam, formando alianças e fazendo planos, enquanto nomes conhecidos e desconhecidos se apresentam para tomar parte das danças políticas.\nTodos precisam lançar mão de suas habilidades e poderes para encarar os tempos de terror que se aproximam. Nobres e plebeus, soldados e feiticeiros, assassinos e saqueadores devem arriscar suas fortunas... e suas vidas, pois em um festim de corvos, muitos são os convidados ― e poucos os sobreviventes.",
    "imagem": "cronicasgeloefogo4.jpg",
    "personagem": "Crônicas"
},

{
    "titulo": "A Dança dos Dragões: As Crônicas de Gelo e Fogo, volume 5",
    "preco": 80.00,
    "sinopse": "As Crônicas de Gelo e Fogo. Jon Snow, Daenerys Targaryen, Tyrion Lannister e outros personagens estão presentes no quinto volume da série, A dança dos dragões, envolvendo as duas linhas cronológicas da saga e, novamente, muitas emoções e reviravoltas aguardam os leitores. O futuro dos Sete Reinos ainda é incerto – novas ameaças e novos inimigos surgem a cada momento. Além do Mar Estreito, Daenerys Targaryen, a última herdeira da Casa Targaryen, governa uma cidade construída sobre o pó e a morte. Mas seus inimigos são cada vez mais numerosos e farão de tudo para destruí-la. Enquanto isso, dois jovens embarcam em missões distintas, mas que podem mudar o destino da Mãe dos Dragões. No Norte, Jon Snow – 998º Senhor Comandante da Patrulha da Noite – fará de tudo para garantir a segurança da Muralha. Para isso, não hesitará em transformar amigos em inimigos e vice-versa. Traições, revelações e um fantasma do passado que volta para assombrar quando menos se espera: em todos os cantos de Westeros e de Essos, mercadores, foras da lei, meistres, reis, nobres, escravos, soldados e troca-peles estão prestes a encarar fatos inesperados. Alguns fracassarão, outros se aproveitarão das forças sombrias que crescem cada vez mais. Mas, neste momento de inquietude crescente, as marés da política e do destino levarão inevitavelmente à maior dança de todas.",
    "imagem": "cronicasgeloefogo5.jpg",
    "personagem": "Crônicas"
},

{
    "titulo": "The Witcher - Box capa dura",
    "preco": 386.18,
    "sinopse": "Box contendo os 8 volumes da série The Witcher (capa dura) • O Último Desejo - Livro 1 • A Espada do Destino - Livro 2 • O Sangue dos Elfos - Livro 3 • Tempo do Desprezo - Livro 4 • Batismo de Fogo - Livro 5 • A Torre da Andorinha - Livro 6 • A Senhora do Lago - Livro 7 • Tempo de Tempestade - Prelúdio",
    "imagem": "boxthewitcher.jpg",
    "personagem": "The Witcher"
},

{
    "titulo": "Box Harry Potter - Edição Pottermore: 7 livros",
    "preco": 339.93,
    "sinopse": "A vida do menino Harry Potter não tem um pingo de magia. Ele vive com os tios e o primo, que não gostam nem um pouco dele. O quarto de Harry é, na verdade, um armário sob a escada, e ele nunca comemorou um aniversário sequer em onze anos. Até que, um dia, Harry recebe uma carta misteriosa, entregue por uma coruja: um convite para estudar num lugar incrível chamado Escola de Magia e Bruxaria Hogwarts. Lá ele vai encontrar não só amigos, esportes praticados em vassouras voadoras e magia para todo lado, como também seu destino: ser um aprendiz de feiticeiro até o dia em que terá que enfrentar a pior força do mal, o bruxo que assassinou seus pais. Mas, para isso, Harry precisará passar por uma série de desafios e enfrentar inúmeros perigos. Em sete livros que se tornaram o maior fenômeno editorial de todos os tempos, com mais de 450 milhões de exemplares vendidos e traduções em 78 idiomas, Harry Potter não é exposto apenas a batalhas e feitiços. Ele precisa superar traições, surpresas e, sobretudo, aprender a lidar com os próprios sentimentos. O amor, a amizade e claro, uma boa dose de magia e imaginação, são os elementos-chave para da maior saga bruxa de todos os tempos. Harry Potter é a série juvenil mais vendida de todos os tempos e uma nova série para o streaming da MAX está entrando em produção para ser lançada em nos próximos anos. Essa caixa traz os sete livros com texto integral, em acabamento brochura, com orelhas. Acompanha folha de adesivos destacáveis com mais de 20 ilustrações.",
    "imagem": "boxharrypotter.jpg",
    "personagem": "Harry Potter"
},

{
    "titulo": "Box As Crônicas de Nárnia - Edição de Luxo",
    "preco": 263.50,
    "sinopse": "Guarda-roupas mágicos, anéis que levam para outros mundos, cavalos falantes e, o mais impressionante, um leão muito poderoso! As Crônicas de Nárnia são a aclamada série de livros, escritos por C. S. Lewis, que narram as aventuras de crianças corajosas no nosso mundo e em outros universos mágicos e desconhecidos. Ao adquirir o box As Crônicas de Nárnia – Coleção de Luxo você garante a saga completa, em edição de luxo, na sua estante. São sete livros capa dura, com pintura trilateral, páginas amareladas, fitilho e detalhes dourados. As edições contam ainda com a nova tradução do professor Ronald Kyrmse – que também é um tolkienista de respeito – e com as ilustrações coloridas de Pauline Baynes. Tudo isso em um box rígido colorido, com soft-touch e detalhes em dourado. Este box inclui os seguintes livros: · O Sobrinho do Mago – Coleção de Luxo · O Leão, a Feiticeira e o Guarda-Roupa – Coleção de Luxo · O Cavalo e seu Menino – Coleção de Luxo · Príncipe Caspian – Coleção de Luxo · A Viagem do Peregrino da Alvorada – Coleção de Luxo · A Cadeira de Prata – Coleção de Luxo · A Última Batalha – Coleção de Luxo.",
    "imagem": "boxnarnia.jpg"
},

{
    "titulo": "Box Duna: Primeira Trilogia",
    "preco": 221.90,
    "sinopse": "Uma estonteante mistura de aventura e misticismo, ecologia e política, este romance ganhador dos prêmios Hugo e Nebula deu início a uma das mais épicas histórias de toda a ficção científica; Duna é um triunfo da imaginação, que influenciará a literatura para sempre, com introdução de Neil Gaiman, apresentando o universo fantástico criado por Herbert, que será adaptado ao cinema por Denis Villeneuve; doze anos após Paul Atreides ascender ao trono como imperador e messias, Arrakis se torna o centro do Imperium, e os conflitos gerados pela expansão de sua filosofia de governo fazem facções contrárias reunirem forças para detê-lo, enquanto Paul enfrenta desafios e sua irmã Alia assume o poder como regente, com seus filhos gêmeos carregando o legado Atreides, e a hegemonia da dinastia ameaçada.",
    "imagem": "boxduna.jpg",
    "personagem": "Duna"
},

{

    "titulo": "Box Game of Thrones",
    "preco":  500.00,
    "sinopse": "Uma experiência de entretenimento envolvente e única, As Crônicas de Gelo e Fogo de George R. R. Martin, apelidado de 'o Tolkien americano' pela revista Time, conquistou aclamação internacional e milhões de leitores, e agora recebe o tratamento real com cada livro em capas de couro e tecido, embalados em uma elegante caixa de exposição, incluindo os volumes A Guerra dos Tronos, A Confusão dos Reis, A Tempestade de Espadas, A Festa dos Corvos e A Dança com Dragões, onde o inverno chega e a luta pelo poder se intensifica entre as Casas Stark e Lannister, enquanto uma ameaça sobrenatural espreita ao norte e conspirações surgem ao sul.",
    "imagem": "boxgot.jpg",
    "personagem": "Game Of Thrones"

},
    

   {
        "titulo": "Dragon Ball Vol. 1",
        "preco": 45.90,
        "sinopse": "Acompanhe as aventuras de Goku e seus amigos em sua jornada para encontrar as esferas do dragão, enfrentando poderosos inimigos e se tornando cada vez mais forte.",
        "imagem": "dragonball1.webp",
        "personagem": "Dragon Ball"
    },
    {
        "titulo": "Dragon Ball Vol. 2",
        "preco": 22.90,
        "sinopse": "O segundo volume da série continua a emocionante busca por poder e amizade, com novos desafios e personagens, enquanto Goku e seus amigos enfrentam novas ameaças.",
        "imagem": "dragonball2.webp",
        "personagem": "Dragon Ball"
    },
    {
        "titulo": "Dragon Ball Vol. 3",
        "preco": 37.90,
        "sinopse": "As aventuras de Goku continuam neste volume, com batalhas intensas e o surgimento de novos inimigos, enquanto ele treina para enfrentar desafios ainda maiores.",
        "imagem": "dragonball3.webp",
        "personagem": "Dragon Ball"
    },
    {
        "titulo": "Dragon Ball Vol. 4",
        "preco": 37.90,
        "sinopse": "Goku e seus amigos enfrentam desafios ainda maiores, com mais batalhas épicas e a introdução de personagens marcantes que transformam o rumo da história.",
        "imagem": "dragonball4.webp",
        "personagem": "Dragon Ball"
    },
    {
        "titulo": "Dragon Ball Vol. 5",
        "preco": 37.90,
        "sinopse": "No quinto volume da saga Dragon Ball, novas aventuras e inimigos se apresentam, enquanto Goku e seus amigos continuam sua jornada de crescimento e descoberta.",
        "imagem": "dragonball5.webp",
        "personagem": "Dragon Ball"
    },


   
    {
        "titulo": "One Piece Vol. 02",
        "preco": 34.90,
        "sinopse": "Luffy Chapéu de Palha não está mais sozinho em sua jornada, depois de admitir em sua tripulação o famoso espadachim Roronoa Zoro, o Caça-Piratas! Mas um imprevisto os separa, colocando Luffy no caminho do Bando do Pirata Buggy, o Palhaço, que está aterrorizando uma pequena cidade portuária! E ele também conhece uma misteriosa ladra, que promete muita confusão e trapaças por onde passa!",
        "imagem": "onepiece2.webp",
        "personagem": "One Piece"
    },
    {
        "titulo": "One Piece Vol. 03",
        "preco": 34.90,
        "sinopse": "Luffy e Coby navegam em direção a uma ilha que é base da Marinha onde está aprisionado o espadachim e caçador de piratas, Roronoa Zoro. Por ter feito um acordo com Helmeppo, filho do oficial da base, Tenente Morgan, Zoro permanece preso, e Luffy decide tentar recrutá-lo para seu bando.",
        "imagem": "onepiece3.webp",
        "personagem": "One Piece"
    },
    {
        "titulo": "One Piece Vol. 04",
        "preco": 34.90,
        "sinopse": "Helmeppo ameaça matar Luffy por atacá-lo e vai falar com seu pai. Luffy tenta convencer Zoro a ser seu companheiro e promete recuperar suas espadas. E o Chapéu de Palha destrói a estatua do Morgan.",
        "imagem": "onepiece4.webp",
        "personagem": "One Piece"
    },
    {
        "titulo": "One Piece Vol. 05",
        "preco": 34.90,
        "sinopse": "Usopp decide defender sozinho sua vila e sua amiga Kaya contra o ataque do Capitão Kuro e sua antiga tripulação! Luffy, Zoro e Nami não vão perder essa briga por nada!",
        "imagem": "onepiece5.webp",
        "personagem": "One Piece"
    },

    
    {
        "titulo": "Naruto Vol. 01",
        "preco": 29.90,
        "sinopse": "Naruto Uzumaki é um garoto ninja da Vila Oculta da Folha que sonha em se tornar Hokage, o líder da vila. Mas ele carrega dentro de si a Raposa de Nove Caudas, uma fera que atacou a vila no passado. Enquanto luta para ganhar o respeito de todos, Naruto faz amigos e enfrenta desafios, incluindo seu rival Sasuke e a misteriosa organização ninja.",
        "imagem": "naruto1.webp",
        "personagem": "Naruto"
    },
    {
        "titulo": "Naruto Vol. 02",
        "preco": 29.90,
        "sinopse": "Naruto, Sasuke e Sakura formam o Time 7 sob a liderança do enigmático Kakashi Hatake. Juntos, eles enfrentam sua primeira grande missão: proteger o construtor de pontes Tazuna contra o temível Zabuza e sua fiel aliada, Haku. Será que o Time 7 está preparado para uma batalha tão intensa?",
        "imagem": "naruto2.webp",
        "personagem": "Naruto"
    },
    {
        "titulo": "Naruto Vol. 03",
        "preco": 29.90,
        "sinopse": "O Time 7 continua enfrentando Zabuza e Haku em uma batalha intensa. Naruto começa a descobrir o verdadeiro poder do chakra da Raposa de Nove Caudas, enquanto Sasuke demonstra suas habilidades. A conclusão desta missão moldará os laços entre os membros da equipe.",
        "imagem": "naruto3.webp",
        "personagem": "Naruto"
    },
    {
        "titulo": "Naruto Vol. 04",
        "preco": 29.90,
        "sinopse": "Com sua missão em Tazuna concluída, o Time 7 retorna à Vila da Folha. Eles participam dos exames Chunin, um torneio ninja repleto de desafios perigosos. Novos personagens, como Rock Lee e Gaara, aparecem para mostrar o quão árduo será o caminho para se tornarem verdadeiros ninjas.",
        "imagem": "naruto4.webp",
        "personagem": "Naruto"
    },
    {
        "titulo": "Naruto Vol. 05",
        "preco": 29.90,
        "sinopse": "Os exames Chunin continuam com lutas emocionantes. Naruto enfrenta novos adversários e tenta provar sua força. Enquanto isso, Sasuke revela um novo poder, mas os perigos por trás da organização sombria começam a aparecer.",
        "imagem": "naruto5.webp",
        "personagem": "Naruto"
    },

    {
    "titulo": "Bleach Vol. 01",
    "preco": 34.90,
    "sinopse": "Ichigo Kurosaki é um adolescente que, após um encontro inesperado com a shinigami Rukia Kuchiki, ganha poderes para enfrentar os Hollows, espíritos malignos que ameaçam os vivos. Agora, Ichigo deve equilibrar sua vida normal com suas novas responsabilidades como um substituto de shinigami.",
    "imagem": "bleach1.webp",
    "personagem": "Bleach"
},
{
    "titulo": "Bleach Vol. 02",
    "preco": 34.90,
    "sinopse": "Ichigo continua a lutar contra Hollows enquanto se adapta à sua nova vida. Ele descobre mais sobre o mundo dos shinigamis e a verdadeira extensão de seus poderes. Porém, sua conexão com Rukia o coloca em perigos inesperados.",
    "imagem": "bleach2.webp",
    "personagem": "Bleach"
},
{
    "titulo": "Bleach Vol. 03",
    "preco": 34.90,
    "sinopse": "A Soul Society envia shinigamis para recuperar Rukia, acusando-a de ter transferido seus poderes para Ichigo. Para protegê-la, Ichigo precisa treinar intensamente e se preparar para enfrentar inimigos muito mais poderosos.",
    "imagem": "bleach3.webp",
    "personagem": "Bleach"
},
{
    "titulo": "Bleach Vol. 04",
    "preco": 34.90,
    "sinopse": "Ichigo e seus aliados embarcam em uma missão para invadir a Soul Society e resgatar Rukia. Eles enfrentam desafios mortais e descobrem mais sobre os segredos e a hierarquia desse misterioso mundo espiritual.",
    "imagem": "bleach4.webp",
    "personagem": "Bleach"
},
{
    "titulo": "Bleach Vol. 05",
    "preco": 34.90,
    "sinopse": "Ichigo enfrenta seu primeiro confronto real contra um capitão da Soul Society. As apostas nunca foram tão altas, e Ichigo começa a perceber a extensão dos sacrifícios necessários para salvar Rukia.",
    "imagem": "bleach5.webp",
    "personagem": "Bleach"
},
 

{
    "titulo": "Dandadan Vol. 03",
    "preco": 29.90,
    "sinopse": "Ken e Momo encontram novos aliados em sua luta contra alienígenas e espíritos sobrenaturais. A ameaça aumenta quando um poderoso espírito se junta à caçada, forçando os dois a unirem forças de maneira nunca antes vista.",
    "imagem": "dandadan3.webp",
    "personagem": "Dandadan"
},
{
    "titulo": "Dandadan Vol. 04",
    "preco": 29.90,
    "sinopse": "As forças sobrenaturais e alienígenas ficam ainda mais perigosas. Ken descobre um poder latente dentro de si, enquanto Momo enfrenta uma entidade que ameaça destruir tudo o que ela ama.",
    "imagem": "dandadan4.webp",
    "personagem": "Dandadan"
},
{
    "titulo": "Dandadan Vol. 05",
    "preco": 29.90,
    "sinopse": "Os mistérios por trás dos eventos sobrenaturais começam a ser revelados. Ken e Momo enfrentam uma batalha épica contra um inimigo que pode ser o responsável por tudo o que está acontecendo.",
    "imagem": "dandadan5.webp",
    "personagem": "Dandadan"
},

{
    "titulo": "Blue Lock Vol. 01",
    "preco": 34.90,
    "sinopse": "Após uma derrota humilhante da seleção japonesa na Copa do Mundo, a União de Futebol do Japão decide reformar o futebol no país. Yoichi Isagi, um jovem atacante, é convidado para o Blue Lock, um projeto brutal que busca criar o melhor atacante egoísta do mundo. Apenas um jogador sairá vitorioso, enquanto o resto verá seus sonhos destruídos.",
    "imagem": "bluelock1.webp",
    "personagem": "Blue Lock"
},
{
    "titulo": "Blue Lock Vol. 02",
    "preco": 34.90,
    "sinopse": "O torneio no Blue Lock continua feroz. Yoichi Isagi começa a descobrir seu estilo de jogo, enquanto enfrenta novos desafios e rivais cada vez mais habilidosos. Para avançar, ele deve superar não apenas os adversários, mas também suas próprias dúvidas.",
    "imagem": "bluelock2.webp",
    "personagem": "Blue Lock"
},
{
    "titulo": "Blue Lock Vol. 03",
    "preco": 34.90,
    "sinopse": "Yoichi e seus companheiros enfrentam times ainda mais habilidosos no torneio de sobrevivência. Estratégias ousadas, rivalidades acirradas e momentos de pura tensão colocam todos à prova. Isagi começa a entender o verdadeiro significado de ser egoísta em campo.",
    "imagem": "bluelock3.webp",
    "personagem": "Blue Lock"
},
{
    "titulo": "Blue Lock Vol. 04",
    "preco": 34.90,
    "sinopse": "O time de Yoichi enfrenta o jogo mais difícil até agora, com um adversário que combina velocidade e técnica impecáveis. Yoichi precisa despertar sua verdadeira habilidade para virar o jogo e continuar no Blue Lock.",
    "imagem": "bluelock4.webp",
    "personagem": "Blue Lock"
},
{
    "titulo": "Blue Lock Vol. 05",
    "preco": 34.90,
    "sinopse": "A competição esquenta ainda mais quando os jogadores enfrentam novos desafios individuais. Yoichi e seus aliados começam a mostrar um verdadeiro crescimento, mas a pressão por resultados ameaça derrubar alguns.",
    "imagem": "bluelock5.webp",
    "personagem": "Blue Lock"
},

{
    "titulo": "Kaiju No. 8 Vol. 01",
    "preco": 34.90,
    "sinopse": "Kafka Hibino é um limpador de monstros que sempre sonhou em se tornar um grande combatente contra os Kaiju. Após um incidente inesperado, ele ganha a habilidade de se transformar em um Kaiju, mas isso o coloca em uma posição delicada. Agora, Kafka precisa esconder sua nova identidade enquanto busca realizar seu sonho.",
    "imagem": "kaiju1.webp",
    "personagem": "Kaiju"
},
{
    "titulo": "Kaiju No. 8 Vol. 02",
    "preco": 34.90,
    "sinopse": "Kafka continua a esconder sua transformação em Kaiju enquanto tenta entrar para a Força de Defesa. Ao lado de sua amiga de infância, Mina, ele enfrenta os desafios das provas de admissão, mas a presença de um Kaiju ainda mais poderoso ameaça revelar seu segredo.",
    "imagem": "kaiju2.webp",
    "personagem": "Kaiju"
},
{
    "titulo": "Kaiju No. 8 Vol. 03",
    "preco": 34.90,
    "sinopse": "Kafka passa nos testes de admissão para a Força de Defesa, mas precisa manter seu segredo mais escondido do que nunca. Enquanto enfrenta novos ataques Kaiju, ele luta para equilibrar sua nova vida com o fardo de ser um 'monstro' escondido entre humanos.",
    "imagem": "kaiju3.webp",
    "personagem": "Kaiju"
},
{
    "titulo": "Kaiju No. 8 Vol. 04",
    "preco": 34.90,
    "sinopse": "Kafka e seus companheiros enfrentam uma ameaça ainda maior quando um Kaiju de classe superior ataca. Seu segredo fica à beira de ser revelado, e ele começa a questionar se pode continuar escondendo sua transformação.",
    "imagem": "kaiju4.webp",
    "personagem": "Kaiju"
},
{
    "titulo": "Kaiju No. 8 Vol. 05",
    "preco": 34.90,
    "sinopse": "O passado de Kafka começa a ser explorado enquanto ele enfrenta seu maior desafio até agora. Ele precisa fazer escolhas difíceis entre proteger seus amigos e aceitar sua verdadeira natureza como Kaiju.",
    "imagem": "kaiju5.webp",
    "personagem": "Kaiju"
},

{
    "titulo": "Berserk Vol. 01",
    "preco": 49.90,
    "sinopse": "Guts é um mercenário solitário que carrega uma gigantesca espada e uma terrível maldição. Ele vive para lutar, enfrentando monstros aterrorizantes e as forças do destino. Em sua jornada, ele encontra Griffith, o carismático líder do Bando do Falcão, e sua vida muda para sempre.",
    "imagem": "berserk1.webp",
    "personagem": "Berserk"
},
{
    "titulo": "Berserk Vol. 02",
    "preco": 49.90,
    "sinopse": "Após se juntar ao Bando do Falcão, Guts começa a forjar laços com Griffith e seus companheiros. Eles enfrentam batalhas brutais no campo de guerra, enquanto o sonho de Griffith de alcançar o poder absoluto começa a tomar forma. Mas a escuridão espreita, e o destino do grupo é cada vez mais sombrio.",
    "imagem": "berserk2.webp",
    "personagem": "Berserk"
},
{
    "titulo": "Berserk Vol. 03",
    "preco": 49.90,
    "sinopse": "Guts e o Bando do Falcão continuam a vencer batalhas, ganhando fama e poder. No entanto, o relacionamento de Guts com Griffith começa a ficar mais complexo, especialmente quando os segredos e ambições de Griffith vêm à tona.",
    "imagem": "berserk3.webp",
    "personagem": "Berserk"
},
{
    "titulo": "Berserk Vol. 04",
    "preco": 49.90,
    "sinopse": "Griffith e o Bando do Falcão enfrentam um dos maiores desafios de suas vidas. Uma batalha contra um demônio terrível coloca Guts em uma posição de vida ou morte, enquanto ele questiona seu papel no grupo.",
    "imagem": "berserk4.webp",
    "personagem": "Berserk"
},
{
    "titulo": "Berserk Vol. 05",
    "preco": 49.90,
    "sinopse": "O eclipse se aproxima, trazendo uma escuridão avassaladora para Guts e seus companheiros. Griffith toma uma decisão que mudará tudo, levando o Bando do Falcão ao seu momento mais sombrio.",
    "imagem": "berserk5.webp",
    "personagem": "Berserk"
},

{
    "titulo": "Sword art Online: Aincrad Vol. 1",
    "preco": 39.90,
    "sinopse": "O cientista prodígio Akihiko Kayaba criou Sword Art Online, o primeiro game de realidade virtual on-line para multijogadores. Mas o que os jogadores não sabem é que, uma vez que se entra, não se pode sair até a conclusão desse jogo implacável. E se você morrer dentro do game, morrerá também no mundo real. Kirito está logado no SAO e já sabe que a sua vida está em jogo. Este jogador solo tentará chegar ao último andar do Castelo Aincrad, em meio a tantos usuários que disputam os mesmos recursos. Mas ao conhecer Asuna, vice-comandante da guilda Knights of the Blood, sua trajetória mudará de forma radical. Será que Kirito conseguirá escapar deste mundo virtual? Afinal, apesar de ser um jogo, SAO não pode ser encarado como uma simples brincadeira.",
    "imagem": "sao1.webp",
    "personagem": "Sword Art Online"
},
{
    "titulo": "Sword art Online: Aincrad Vol. 2",
    "preco": 39.90,
    "sinopse": "Todos que logaram no Sword Art Online – um MMORPG em realidade virtual – não conseguem mais escapar. O revolucionário game que prometia a imersão em um mundo fantástico prendeu milhares de jogadores e só vai lhes devolver a liberdade quando alguém zerá-lo. Kirito é um jogador solo que, entre tantos outros das mais variadas profissões e ideais, tem um único objetivo: chegar ao último andar do castelo. Silica é uma Beast Tamer; Lisbeth, proprietária de uma loja de armas; Yui, uma menina cheia de mistérios; e Sachi não consegue tirar o Cavaleiro Negro de seu coração. Mesmo numa situação extrema como essa, elas vivem plenamente, dão risada, divertem-se e às vezes choram. Acima de tudo, curtem as suas vidas que agora fazem parte deste universo. Está é a adaptação em mangá de Sword Art Online – Aincrad, um fenômeno mundial da literatura e dos animes. A adaptação para mangá é de Tamako Makamura, baseada na obra de Reki Kawahara e com design de personagens de abec.",
    "imagem": "sao2.webp",
    "personagem": "Sword Art Online"
},
{
    "titulo": "Sword art Online: Fairy Dance Vol. 3",
    "preco": 30.00,
    "sinopse": "Kirito finalmente regressou ao mundo real após finalizar o MMORPG mortal Sword Art Online. Porém, sua companheira, Asuna, ainda não despertou. Quando Kirito vê uma misteriosa imagem dela no jogo Alfheim Online, ele embarca em uma nova e perigosa aventura virtual. Kirito mergulha no jogo em que os jogadores-fadas se emaranham: ALO! É o início do arco Fairy Dance, também de grande sucesso na internet!",
    "imagem": "sao3.webp",
    "personagem": "Sword Art Online"
},
{
    "titulo": "Sword art Online Vol. 4 - Fairy Dance",
    "preco": 31.00,
    "sinopse": "Após passar por diversos desafios em Alfheim Online, o VRMMORPG herdeiro de SAO, Kirito chega até a base da Árvore do Mundo, onde sua amada Asuna permanece cativa do odioso Oberon, o Rei das Fadas. Além de ter de enfrentar monstros poderosos e a própria regra do jogo, Kirito também terá de lidar com sua aliada, Leafa, quando segredos de ambos são revelados...",
    "imagem": "sao4.webp",
    "personagem": "Sword Art Online"
},
{
    "titulo": "Sword art Online: Phantom Bullet Vol. 5",
    "preco": 22.90,
    "sinopse": "O incidente de Sword Art Online deixou milhares de vítimas, mas o mundo virtual não parou de se desenvolver: a nova febre entre os VRMMOs é Gun Gale Online, um jogo de tiro. Quando ele começa a ter consequências mortais no mundo real, quem precisa vestir o visor e mergulhar mais uma vez é Kirito.",
    "imagem": "sao5.webp",
    "personagem": "Sword Art Online"
},

{
    "titulo": "Solo Leveling Vol. 01",
    "preco": 39.90,
    "sinopse": "Sung Jin-Woo é conhecido como o 'caçador mais fraco de todos os tempos'. Durante uma missão que dá terrivelmente errado, ele é deixado para morrer, mas acorda com uma habilidade única: um sistema que permite que ele 'suba de nível'. Agora, ele está determinado a se tornar o caçador mais forte do mundo.",
    "imagem": "sololeveling1.webp",
    "personagem": "Solo Leveling"
},
{
    "titulo": "Solo Leveling Vol. 02",
    "preco": 39.90,
    "sinopse": "Com seu novo sistema de habilidades, Sung Jin-Woo começa a enfrentar desafios cada vez maiores. Ele treina e explora masmorras perigosas, enquanto seu poder cresce exponencialmente. No entanto, ele também começa a atrair atenção indesejada de outros caçadores.",
    "imagem": "sololeveling2.webp",
    "personagem": "Solo Leveling"
},
{
    "titulo": "Solo Leveling Vol. 03",
    "preco": 39.90,
    "sinopse": "Sung Jin-Woo enfrenta sua primeira masmorra de alto nível sozinho, testando os limites de seu novo poder. Ele começa a perceber que o sistema que o transformou tem segredos ainda mais profundos.",
    "imagem": "sololeveling3.webp",
    "personagem": "Solo Leveling"
},
{
    "titulo": "Solo Leveling Vol. 04",
    "preco": 39.90,
    "sinopse": "A fama de Sung Jin-Woo como um caçador solo poderoso começa a se espalhar. Ele enfrenta novos inimigos, incluindo outros caçadores que o veem como uma ameaça. Enquanto isso, novas masmorras misteriosas começam a surgir pelo mundo.",
    "imagem": "sololeveling4.webp",
    "personagem": "Solo Leveling"
},
{
    "titulo": "Solo Leveling Vol. 05",
    "preco": 39.90,
    "sinopse": "Sung Jin-Woo descobre mais sobre o sistema que o transformou, enquanto enfrenta um dos chefes de masmorra mais aterrorizantes que já encontrou. A batalha é brutal, mas Jin-Woo começa a se aproximar do verdadeiro potencial de seus poderes.",
    "imagem": "sololeveling5.webp",
    "personagem": "Solo Leveling"
},

{
    "titulo": "Spy x Family Vol. 1",
    "preco": 28.80,
    "sinopse": "O habilidoso espião 'Twilight' é instruído a construir uma 'família' para se infiltrar em uma tradicional instituição de ensino. Mas a 'filha' que ele encontra é uma paranormal que lê mentes! E a 'esposa' é uma assassina?! Ocultando um do outro suas identidades, essa família temporária terá de enfrentar os perigos dos exames de admissão e do mundo em uma espirituosa comédia doméstica!",
    "imagem": "spyxfamily1.webp"
},

{
    "titulo": "Black Clover Vol. 1",
    "preco": 30.00,
    "sinopse": "Em um mundo onde magia é tudo, Asta é um garoto que, mesmo incapaz de utilizá-la, almeja o posto de 'Rei Mago', o maior entre os magos, a fim de provar sua força e cumprir a promessa que fez com seu amigo! Abrem-se as cortinas dessa fantástica e mágica aventura!",
    "imagem": "blackClover.webp"
},

{
    "titulo": "Demon Slayer - Kimetsu No Yaiba Vol. 1",
    "preco": 34.90,
    "sinopse": "Estamos na Era Taishou. O dia-a-dia pacato de Tanjiro, um gentil garoto que vende carvão, se transforma radicalmente quando sua família é assassinada por um demônio. A única sobrevivente é Nezuko, sua irmã mais nova. Porém, agora, ela se transformou em um Oni. Diante dessa tragédia, os dois irmãos partem em uma jornada para derrotar o Oni que matou sua mãe e irmãozinhos. E assim tem início uma aventura sanguinolenta de espadachins!",
    "imagem": "kimetsuvol1.webp"
},

{
    "titulo": "Oshi No Ko Vol. 1",
    "preco": 33.90,
    "sinopse": "\"Nesta indústria, a mentira é uma arma.\"\n\nGoro é um obstetra trabalhando em uma cidade do interior e sem qualquer ligação com a indústria do entretenimento. Por outro lado, Ai Hoshino, sua idol favorita, começava a subir no estrelato. Mas, por um acaso do destino, a vida de ambos será mudada radicalmente...?",
    "imagem": "oshinoKo.webp"
},

{
    "titulo": "Vagabond Vol. 1",
    "preco": 41.90,
    "sinopse": "Em 1600 d.C., o Japão passa por um dos períodos mais turbulentos de sua história. O jovem Takezo, ao lado de seu amigo Matahachi, deixa a vila Miyamoto para lutar na Batalha de Sekigahara. Embora sonhem com fama e glória, eles somente encontram a derrota e um caminho repleto de incertezas. Acompanhe a jornada de combates sanguinolentos e desafios espirituais desse destemido espadachim, que ficou conhecido pela posteridade como o grande samurai Miyamoto Musashi! Baseado no romance épico de Eiji Yoshikawa com a sublime arte de Takehiko Inoue, este clássico dos quadrinhos é uma das obras mais premiadas e fiéis à lenda do maior herói do Japão!",
    "imagem": "Vagabond.webp"
},

{
    "titulo": "Jujutsu Kaisen: Batalha De Feiticeiros 0",
    "preco": 35.50,
    "sinopse": "O estudante colegial Yuuta Okkotsu deseja ser executado porque sofre com as ações de Rika Orimoto, espírito rancoroso que o possuiu. Enquanto isso, Satoru Gojou, professor que ensina a exorcizar ´maldições´, transfere Yuuta para a Escola Técnica Superior de Jujutsu de Tokyo. Tem início a pré-sequência da série Jujutsu Kaisen!.",
    "imagem": "jujutsukaisen0.webp"
},

{
    "titulo": "Wind Breaker 01",
    "preco": 24.60,
    "sinopse": "Haruka Sakura só quer saber de enfrentar os mais fortes. Tendo acabado de ser transferido para o instituto Fuurin, escola de jovens problemáticos prestes a desistir dos estudos, o garoto tem um único objetivo: chegar ao topo da hierarquia dos delinquentes.",
    "imagem": "WindBreaker.webp"
},

{
    "titulo": "The Elusive Samurai 01",
    "preco": 25.50,
    "sinopse": "O ano é 1333, Japão. Tokiyuki Hojo, garoto que deveria viver como herdeiro do Xogunato Kamakura, perde tudo em uma revolta repentina: sua terra natal e sua família. Mas ele tinha um talento insuperável: sobreviver. Convidado por Yorishige Suwa, sacerdote xintoísta de Shinano, Tokiyuki foge para começar a trilhar o caminho do herói!.",
    "imagem": "theelusivesamurai.webp"
},

{
    "titulo": "Banana Fish Vol. 1",
    "preco": 54.90,
    "sinopse": "Vietnã, 1973. Um soldado americano sofreu um repentino distúrbio mental e proferiu apenas as seguintes palavras: 'bananafish'. Nova York, 1985. Ash tenta descobrir o significado desse misterioso termo enquanto a sombra sinistra de Papa Dino, o chefe do submundo, se aproxima dele.",
    "imagem": "bananafish1.webp"
},

{
    "titulo": "Tokyo Ghoul Vol. 1",
    "preco": 34.70,
    "sinopse": "Em Tokyo, criaturas conhecidas como 'Ghouls' vivem entre os humanos e os devoram para sobreviver. Alheio a eles, o jovem universitário Ken Kaneki leva uma vida pacata entre livros, até que um trágico encontro o coloca diante desses seres e o obriga a lutar por sua humanidade.",
    "imagem": "tokyoghoul1.webp"
},

{
    "titulo": "Kaguya Sama - Love Is War Vol. 7",
    "preco": 22.90,
    "sinopse": "Neste 7º volume, começamos um 'novo episódio'!! O 67º Conselho Estudantil chegou ao fim, e Kaguya e Shirogane perderam o contato que tinham. Ele até decidiu concorrer à presidência de novo como sua única oportunidade na vida de mostrar quem é. No entanto, querendo pedir para que Kaguya se responsabilizasse pelo discurso de sua campanha, o ar criado foi de uma declaração de amor! Enquanto essas costumeiras guerras intelectuais vão se desenrolando à sua frente, o gênio do 1º ano, Miko Iino, aparece para confrontá-lo!! Acompanhe a corrida pela presidência do 68º Conselho Estudantil!",
    "imagem": "kaguyasama.webp"
},

{
    "titulo": "As Memórias De Vanitas 07",
    "preco": 37.90,
    "sinopse": "Nesse volume, a cadeia de acontecimentos atinge o clímax na gélida floresta argêntea de Gévaudan. Qual seria o projeto secreto dos D’Apchier, no qual Chloe vem há longos anos trabalhando? As revelações desconcertantes sobre a identidade da bête, a tenebrosa atuação da 'Igreja', o passado intrincado de personagens-chave, como lorde Ruthven e Jeanne, e a bruxa do fogo infernal: é chegado o momento em que todos os atos convergem para um cenário maior e, em meio a tantas emoções, Noé e Vanitas estão em sintonia cada vez mais apurada. Juntos, conseguirão eles impedir que Jeanne cumpra a trágica tarefa que lhe foi incumbida enquanto bourreau...?!",
    "imagem": "vanitas7.webp"
},

{
    "titulo": "Tougen Anki Vol. 1",
    "preco": 48.90,
    "sinopse": "O sangue de Shiki Ichinose é Oni, e o de seu pai é Momotarou. Normalmente, aqueles com sangue Momotarou caçam os Oni — mas o pai de Shiki se recusou a matá-lo quando criança. Em vez disso, ele adotou Shiki e o criou apesar da atitude rebelde e do temperamento perigoso que vem com o sangue Oni. Quando um membro da Agência Momotarou mata o pai de Shiki, ele jura vingá-lo. Mas conforme Shiki aprimora suas habilidades e aprende a controlar seu sangue Oni, ele será forte o suficiente para sobreviver aos perigos que o aguardam...?",
    "imagem": "tougenanki.webp"
},

{
    "titulo": "O Espetacular Homem-Aranha Vol. 01",
    "preco": 39.90,
    "sinopse": "Peter Parker é um estudante brilhante, mas com dificuldades em sua vida social. Após ser picado por uma aranha radioativa, ele ganha habilidades incríveis. Neste volume, Peter descobre o verdadeiro custo de ter poderes quando perde seu tio Ben, aprendendo que 'com grandes poderes, vêm grandes responsabilidades.'",
    "imagem": "oespetacularhomemaranha1.webp",
    "personagem": "Homem Aranha"
},

{
    "titulo": "O Espetacular Homem-Aranha Vol. 02",
    "preco": 39.90,
    "sinopse": "Enquanto o Homem-Aranha tenta se estabelecer como herói em Nova York, ele enfrenta seu primeiro grande vilão: o Abutre, que usa uma tecnologia avançada para cometer crimes. Peter deve encontrar uma forma de derrotá-lo, enquanto tenta conciliar sua vida de herói com os desafios da escola e do trabalho.",
    "imagem": "oespetacularhomemaranha2.webp",
    "personagem": "Homem Aranha"
},

{
    "titulo": "O Espetacular Homem-Aranha Vol. 03",
    "preco": 39.90,
    "sinopse": "O Homem-Aranha enfrenta novos inimigos, incluindo o ameaçador Electro, que possui poderes elétricos devastadores. Ao mesmo tempo, Peter luta para proteger sua identidade secreta, enquanto tenta manter sua tia May segura e sua vida pessoal intacta.",
    "imagem": "oespetacularhomemaranha3.webp",
    "personagem": "Homem Aranha"
},

{
    "titulo": "O Espetacular Homem-Aranha Vol. 04",
    "preco": 39.90,
    "sinopse": "O Lagarto faz sua estreia como o novo inimigo de Peter Parker. Curt Connors, um cientista brilhante, se transforma em um monstro reptiliano após uma experiência fracassada. Peter deve descobrir como derrotar o Lagarto sem machucar seu mentor e amigo.",
    "imagem": "oespetacularhomemaranha4.webp",
    "personagem": "Homem Aranha"
},

{
    "titulo": "O Espetacular Homem-Aranha Vol. 05",
    "preco": 39.90,
    "sinopse": "Neste volume, Peter Parker precisa enfrentar o Doutor Octopus, um cientista com braços mecânicos que se volta contra a sociedade. Em meio a essa batalha, Peter também se vê em um dilema moral, questionando até onde vai o seu dever como herói e como ele pode equilibrar sua vida pessoal com suas responsabilidades. A luta entre o Homem-Aranha e o Doutor Octopus se intensifica, trazendo novas revelações sobre os limites dos poderes de Peter e o custo de ser um herói.",
    "imagem": "oespetacularhomemaranha5.webp",
    "personagem": "Homem Aranha"
},

{
    "titulo": "Capitão América Vol. 1",
    "preco": 24.43,
    "sinopse": "Em 'Quando retornou às revistas em quadrinhos no início da década de 1960, após anos desaparecido, o Capitão América ainda era inegavelmente um ícone. Não à toa, suas novas histórias logo chamaram atenção e - escritas por Stan Lee e desenhadas por Jack Kirby - em pouco tempo conquistaram os leitores da época! Descubra o porquê desse apelo irresistível nessas aventuras ´iniciais´ da Sentinela da Liberdade em Tales of Suspense, que mostram a repaginada origem do personagem e jogam Steve Rogers contra assassinos e criminosos de todos os tipos e, claro, contra seu maior adversário, o Caveira Vermelha!",
    "imagem": "capitao1.webp",
    "personagem": "Capitão América"
},


{
    "titulo": "Capitão América Vol. 2",
    "preco": 36.90,
    "sinopse": "O segundo volume da Coleção Clássica Marvel dedicado ao Capitão América traz mais algumas aventuras seminais de Steve Rogers! Testemunho a Sentinela da Liberdade (e seu parceiro Bucky) em um castelo mal-assombrado enfrentando perigosos nazistas em uma aventura na 2ª Guerra Mundial. Depois, confira as consequências nefastas dessa missão no futuro… e, claro, muito mais!",
    "imagem": "capitao2.webp",
    "personagem": "Capitão América"
},

{
    "titulo": "Capitão América Vol. 3",
    "preco": 36.90,
    "sinopse": "Neste terceiro volume dedicado ao Capitão América, veremos o tão aguardado (e temido!) retorno do Caveira Vermelha, o maior inimigo da Sentinela da Liberdade! Mas a volta desse maquiavélico vilão está intimamente ligada ao cobiçado Cubo Cósmico, o objeto que confere poderes ilimitados a quem o possuir! Mas o líder dos Vingadores também terá de enfrentar uma verdadeira legião de perigosíssimos adversários, como Batroc, Poderoso, Espadachim e o Superadaptoide! Em histórias cheias de ação e reviravoltas, Steve Rogers terá de provar uma vez mais por que é chamado de “A Lenda Viva da Segunda Guerra Mundial”!",
    "imagem": "capitao3.webp",
    "personagem": "Capitão América"
},

{
    "titulo": "Capitão América Vol. 4",
    "preco": 36.90,
    "sinopse": "Neste quarto volume da COLEÇÃO CLÁSSICA MARVEL dedicado ao Capitão América, para salvar Manhattan da destruição, nosso patriótico herói se rende ao Caveira Vermelha e jura servi-lo! Depois, a lenda viva da Segunda Guerra Mundial testemunha seu amigo Nick Fury ser morto por um assassino mecânico. Será que o intempestivo diretor da SHIELD morreu mesmo?! O horrendo e impiedoso M.O.D.O.C. e a I.M.A. podem estar por trás dessa trama... Então, cansado das batalhas sem fim e do perigo sempre rondando sua vida, o Capitão decide abandonar sua carreira e anuncia ao mundo sua identidade secreta! Outra ameaça que ressurge das cinzas é Zemo, mas a Sentinela da Liberdade contará com a ajuda inesperada do Pantera Negra para enfrentar este vilão do passado! Participações especialíssimas da Agente 13 e dos Vingadores!",
    "imagem": "capitao4.webp",
    "personagem": "Capitão América"
},

{
    "titulo": "Capitão América Por Mark Waid E Chris Samnee",
    "preco": 109.90,
    "sinopse": "Mark Waid e Chris Samnee, a equipe espetacular que transformou o mundo do Demolidor e já produziu um thriller inesquecível estrelando a Viúva Negra, se reúnem para dar a vez ao maior herói de todos – o Capitão América! Steve Rogers está de volta à ação, e com escudo em mãos ele sai numa jornada através dos Estados Unidos para restaurar a sua reputação. Mas os perigos com os quais o herói vai se deparar são diferentes de tudo que ele já viu, e vão demandar muita coragem! E quando ele encontrar o mais novo Espadachim, vai se ver diante de um duelo inacreditável!",
    "imagem": "capitao5.webp",
    "personagem": "Capitão América"
},

{
    "titulo": "Homem de Ferro Vol. 01",
    "preco": 39.90,
    "sinopse": "Tony Stark é um gênio, bilionário, filantropo e inventor que cria armas para proteger o mundo. Após ser sequestrado por terroristas e gravemente ferido, ele desenvolve uma armadura tecnológica para escapar. Esse evento marca o nascimento do Homem de Ferro, um herói movido por sua inteligência e inovação.",
    "imagem": "homemdeferro1.jpg",
    "personagem": "Ferro"
},
{
    "titulo": "Homem de Ferro Vol. 02",
    "preco": 39.90,
    "sinopse": "Tony Stark continua aprimorando sua armadura enquanto enfrenta novos desafios, incluindo inimigos corporativos que desejam roubar sua tecnologia. Além disso, ele começa a questionar o impacto de suas invenções no mundo, iniciando sua luta para encontrar um equilíbrio entre poder e responsabilidade.",
    "imagem": "homemdeferro2.webp",
    "personagem": "Ferro"
},
{
    "titulo": "Homem de Ferro Vol. 03",
    "preco": 39.90,
    "sinopse": "Quando o misterioso Mandarim surge como uma nova ameaça, Tony Stark precisa confrontar não apenas um inimigo poderoso, mas também os próprios demônios de seu passado. Com sua tecnologia sendo usada contra ele, Stark precisa encontrar uma solução criativa para derrotar seu adversário.",
    "imagem": "homemdeferro3.webp",
    "personagem": "Ferro"
},
{
    "titulo": "Homem de Ferro Vol. 04",
    "preco": 39.90,
    "sinopse": "A pressão sobre Tony Stark aumenta quando a sociedade começa a questionar suas ações como o Homem de Ferro. Ele enfrenta novos desafios tecnológicos e a chegada de uma poderosa figura que ameaça revelar os segredos por trás de sua armadura.",
    "imagem": "homemdeferro4.webp",
    "personagem": "Ferro"
},
{
    "titulo": "Homem de Ferro Vol. 05",
    "preco": 39.90,
    "sinopse": "Uma conspiração global coloca Stark Industries no centro de um conflito que pode destruir o mundo. Tony precisa usar toda sua inteligência e coragem para enfrentar uma ameaça que desafia os limites de sua armadura e sua determinação como herói.",
    "imagem": "homemdeferro5.webp",
    "personagem": "Ferro"
},

{
    "titulo": "A Saga do Hulk Vol. 01",
    "preco": 39.90,
    "sinopse": "Bruce Banner é um brilhante cientista que, após ser exposto a raios gama durante um experimento, se transforma no poderoso e incontrolável Hulk toda vez que perde o controle emocional. Neste volume, acompanhamos sua luta para controlar sua fúria e evitar que o exército, liderado pelo General Ross, o capture.",
    "imagem": "sagadomhulk1.webp",
    "personagem": "Hulk"
    
},
{
    "titulo": "A Saga do Hulk Vol. 02",
    "preco": 39.90,
    "sinopse": "Hulk enfrenta Abominável, um adversário com força semelhante à sua, mas movido por um ódio implacável contra Bruce Banner. Enquanto isso, Banner busca uma cura para sua condição, mas descobre que o preço pode ser mais alto do que ele imaginava.",
    "imagem": "sagadomhulk2.webp",
    "personagem": "Hulk"
},
{
    "titulo": "A Saga do Hulk Vol. 03",
    "preco": 39.90,
    "sinopse": "Neste volume, Bruce Banner é capturado por uma organização secreta que busca explorar o poder do Hulk. Ao ser submetido a experimentos cruéis, o monstro dentro dele se torna ainda mais incontrolável, levando a destruição em massa e questionamentos sobre o verdadeiro inimigo.",
    "imagem": "sagadomhulk3.webp",
    "personagem": "Hulk"
},
{
    "titulo": "A Saga do Hulk Vol. 04",
    "preco": 39.90,
    "sinopse": "Hulk é enviado ao espaço e aterrissa no distante planeta Sakaar, onde é forçado a lutar como gladiador em uma arena brutal. Este volume explora a força inigualável do Hulk e sua luta por liberdade, enquanto ele se torna um herói improvável para os oprimidos do planeta.",
    "imagem": "sagadomhulk4.webp",
    "personagem": "Hulk"
},
{
    "titulo": "A Saga do Hulk Vol. 05",
    "preco": 39.90,
    "sinopse": "Após conquistar Sakaar, Hulk retorna à Terra em busca de vingança contra aqueles que o exilaram, em uma saga épica chamada 'Hulk Contra o Mundo.' Este volume coloca o monstro contra os heróis mais poderosos da Terra, enquanto Bruce Banner luta para evitar uma destruição total.",
    "imagem": "sagadomhulk5.webp",
    "personagem": "Hulk"
},

{
    "titulo": "A Saga de Thor Vol. 01",
    "preco": 39.90,
    "sinopse": "Thor, o poderoso deus do trovão de Asgard, é banido para a Terra por seu pai, Odin, para aprender humildade. Neste volume, Thor descobre sua conexão com o mortal Dr. Donald Blake e enfrenta seu primeiro grande desafio contra os Gigantes de Gelo, enquanto aprende o verdadeiro significado de ser um herói.",
    "imagem": "sagadethor1.webp",
    "personagem": "Thor"
},
{
    "titulo": "A Saga de Thor Vol. 02",
    "preco": 39.90,
    "sinopse": "Thor enfrenta Loki, seu meio-irmão e o Deus da Trapaça, que conspira para tomar o trono de Asgard. Enquanto protege a Terra de seus esquemas, Thor precisa equilibrar sua vida como um deus e sua crescente afeição pelos humanos.",
    "imagem": "sagadethor2.webp",
    "personagem": "Thor"
},
{
    "titulo": "A Saga de Thor Vol. 03",
    "preco": 39.90,
    "sinopse": "Neste volume, Thor enfrenta a poderosa Encantor e o Executioner, que foram enviados por Loki para destruí-lo. Enquanto batalha contra essas forças mágicas, Thor questiona se conseguirá viver como um herói em dois mundos tão diferentes.",
    "imagem": "sagadethor3.webp",
    "personagem": "Thor"
},
{
    "titulo": "A Saga de Thor Vol. 04",
    "preco": 39.90,
    "sinopse": "Thor retorna a Asgard para enfrentar Surtur, o demônio do fogo que ameaça consumir os Nove Reinos. Com sua força e Mjölnir, Thor lidera os guerreiros asgardianos em uma batalha épica para salvar sua terra natal.",
    "imagem": "sagadethor4.webp",
    "personagem": "Thor"
},
{
    "titulo": "A Saga de Thor Vol. 05",
    "preco": 39.90,
    "sinopse": "Thor enfrenta um dos maiores desafios de sua vida ao lutar contra o Destruidor, uma arma mística criada para ser imparável. Neste volume, ele precisará provar sua dignidade como o portador do Mjölnir e como o protetor de Asgard e da Terra.",
    "imagem": "sagadethor5.webp",
    "personagem": "Thor"
},

{
    "titulo": "A Saga do Wolverine Vol. 01",
    "preco": 39.90,
    "sinopse": "Logan, conhecido como Wolverine, é um mutante com garras retráteis, sentidos aguçados e um fator de cura que o torna praticamente indestrutível. Neste volume, ele luta para se lembrar de seu passado enquanto enfrenta inimigos brutais em uma jornada que define sua identidade como um guerreiro solitário.",
    "imagem": "sagadawolverine1.webp",
    "personagem": "Wolverine"
},
{
    "titulo": "A Saga do Wolverine Vol. 02",
    "preco": 39.90,
    "sinopse": "Wolverine se encontra no Japão, onde enfrenta a Yakuza e um poderoso samurai mutante. Este volume explora seu lado mais humano, com Logan lutando não apenas contra inimigos físicos, mas também contra suas emoções ao se apaixonar por Mariko Yashida.",
    "imagem": "sagadawolverine2.webp",
    "personagem": "Wolverine"
},
{
    "titulo": "A Saga do Wolverine Vol. 03",
    "preco": 39.90,
    "sinopse": "Logan descobre mais sobre o programa Arma X, responsável por transformar seu corpo com adamantium. Ao buscar vingança contra aqueles que o torturaram, ele é confrontado por fantasmas do passado e segredos obscuros que ameaçam destruir seu senso de identidade.",
    "imagem": "sagadawolverine3.webp",
    "personagem": "Wolverine"
},
{
    "titulo": "A Saga do Wolverine Vol. 04",
    "preco": 39.90,
    "sinopse": "O passado de Wolverine volta para assombrá-lo quando ele cruza caminhos com Dentes-de-Sabre, um inimigo implacável que compartilha uma conexão misteriosa com ele. A batalha entre os dois é feroz e revela mais sobre a brutalidade que moldou Logan.",
    "imagem": "sagadawolverine4.webp",
    "personagem": "Wolverine"
},
{
    "titulo": "A Saga do Wolverine Vol. 05",
    "preco": 39.90,
    "sinopse": "Wolverine junta forças com os X-Men para enfrentar uma nova ameaça global, mas sua natureza selvagem coloca o grupo em perigo. Este volume revela como Logan luta para equilibrar sua ferocidade com sua lealdade aos amigos e seu desejo de redenção.",
    "imagem": "sagadawolverine5.webp",
    "personagem": "Wolverine"
},

{
    "titulo": "Feiticeira Escarlate Vol. 01: O Poder da Realidade",
    "preco": 39.90,
    "sinopse": "Em 'Feiticeira Escarlate Vol. 01: O Poder da Realidade', Wanda Maximoff começa a explorar os limites de seus poderes, enquanto lida com a perda de entes queridos e a responsabilidade de controlar suas habilidades extraordinárias. Com a capacidade de alterar a realidade, Wanda enfrenta dilemas morais sobre até onde pode ir para proteger os outros.",
    "imagem": "feiticeiraescarlate1.webp",
    "personagem": "Feiticeira Escarlate"
},
{
    "titulo": "Feiticeira Escarlate Vol. 02: O Caos Interior",
    "preco": 39.90,
    "sinopse": "Em 'Feiticeira Escarlate Vol. 02: O Caos Interior', Wanda se vê em uma jornada para restaurar a normalidade após suas ações no passado gerarem caos no mundo. No entanto, seus poderes começam a descontrolar novamente, trazendo novas ameaças e colocando seus amigos e aliados em perigo.",
    "imagem": "feiticeiraescarlate2.webp",
    "personagem": "Feiticeira Escarlate"
},
{
    "titulo": "Feiticeira Escarlate Vol. 03: O Coração da Bruxa",
    "preco": 39.90,
    "sinopse": "Neste volume, Wanda enfrenta uma nova ameaça mística que coloca em risco o equilíbrio do universo. Enquanto ela tenta controlar o caos que criou, uma antiga figura de seu passado ressurge, forçando Wanda a questionar sua própria identidade e a natureza de seus poderes.",
    "imagem": "feiticeiraescarlate3.webp",
     "personagem": "Feiticeira Escarlate"
},
{
    "titulo": "Feiticeira Escarlate Vol. 04: O Preço do Poder",
    "preco": 39.90,
    "sinopse": "Em 'Feiticeira Escarlate Vol. 04: O Preço do Poder', Wanda precisa lidar com as consequências de suas ações passadas enquanto enfrenta uma nova ameaça global. Ao tentar salvar o mundo, ela descobre o verdadeiro custo de seus poderes e o impacto que eles têm sobre sua vida e seus relacionamentos.",
    "imagem": "feiticeiraescarlate4.webp",
     "personagem": "Feiticeira Escarlate"
},
{
    "titulo": "Feiticeira Escarlate Vol. 05: O Último Feitiço",
    "preco": 39.90,
    "sinopse": "No volume final, 'Feiticeira Escarlate Vol. 05: O Último Feitiço', Wanda enfrenta a maior batalha de sua vida, ao tentar conter um cataclismo cósmico. Ela terá que fazer escolhas difíceis sobre sua própria humanidade e sobre o destino do universo, sabendo que o preço de seu poder pode ser mais alto do que ela pode suportar.",
    "imagem": "feiticeiraescarlate5.webp",
     "personagem": "Feiticeira Escarlate"
},


    {
        "titulo": "Venom Vol. 01: Origens",
        "preco": 39.90,
        "sinopse": "Em 'Venom Vol. 01: Origens', o jornalista Eddie Brock se une ao simbiótico alienígena Venom, criando uma das duplas mais perigosas do universo Marvel. Juntos, eles lutam contra ameaças sobrenaturais, enquanto Eddie tenta controlar a natureza impiedosa de Venom e sua própria moralidade.",
        "imagem": "venomorigens1.webp",
         "personagem": "Venom"
    },
    {
        "titulo": "Venom Vol. 02: Caçada Letal",
        "preco": 39.90,
        "sinopse": "Em 'Venom Vol. 02: Caçada Letal', Venom se vê em uma batalha contra outros simbióticos que buscam dominar a Terra. Eddie Brock deve enfrentar inimigos poderosos e questionar sua própria relação com o simbiótico, enquanto lida com a pressão de ser um herói em um mundo que o teme.",
        "imagem": "venomcaçadaletal2.webp",
        "personagem": "Venom"
    },
    {
        "titulo": "Venom Vol. 03: Entre Dois Mundos",
        "preco": 39.90,
        "sinopse": "Neste volume, Eddie Brock e Venom são forçados a atravessar a barreira entre os mundos humanos e alienígenas para derrotar uma ameaça cósmica. Mas com cada viagem, o vínculo entre Eddie e o simbiótico fica mais instável, e a luta pelo controle de sua própria identidade se intensifica.",
        "imagem": "venomentredoismundos3.webp",
        "personagem": "Venom"
    },
    {
        "titulo": "Venom Vol. 04: O Último Combate",
        "preco": 39.90,
        "sinopse": "Em 'Venom Vol. 04: O Último Combate', Venom se encontra diante de uma escolha impossível: proteger a Terra ou seu próprio futuro. Com forças externas tentando destruir a conexão entre Eddie e o simbiótico, Venom deve enfrentar seus piores inimigos para proteger aqueles que ama.",
        "imagem": "venomultimocombate4.webp",
        "personagem": "Venom"
    },
    {
        "titulo": "Venom Vol. 05: O Renascimento",
        "preco": 39.90,
        "sinopse": "Venom enfrenta sua batalha mais pessoal em 'Venom Vol. 05: O Renascimento'. Após uma derrota devastadora, Eddie Brock e o simbiótico precisam reinventar seu vínculo, enquanto enfrentam uma ameaça que pode destruir não apenas a Terra, mas toda a realidade. Este é o ponto culminante de uma jornada épica.",
        "imagem": "venomrenascimento5.webp",
        "personagem": "Venom"
    },

  
    {
        "titulo": "Viúva Negra Vol. 01: O Passado Sombrio",
        "preco": 39.90,
        "sinopse": "Em 'Viúva Negra Vol. 01: O Passado Sombrio', Natasha Romanoff, a Viúva Negra, encara seu passado como espiã e agente da KGB. Neste volume, ela é forçada a confrontar velhos inimigos e segredos de sua infância enquanto lida com as consequências de sua traição à Rússia e sua aliança com os Vingadores.",
        "imagem": "viuvanegra1.webp",
        "personagem": "Viúva Negra"
    },
    {
        "titulo": "Viúva Negra Vol. 02: Fim dos Segredos",
        "preco": 39.90,
        "sinopse": "Em 'Viúva Negra Vol. 02: Missão Impossível', Natasha é recrutada para uma missão arriscada que a leva ao coração do crime organizado mundial. Com seu treinamento impecável e habilidades de espionagem, ela deve derrubar uma rede criminosa poderosa, enquanto lida com a culpa e as sombras de seu passado.",
        "imagem": "viuvanegra2.jpg",
        "personagem": "Viúva Negra"
    },
    {
        "titulo": "Viúva Negra Vol. 03: A Teia de Intrigas",
        "preco": 39.90,
        "sinopse": "Neste volume, a Viúva Negra se vê em uma batalha mortal contra ex-colegas da KGB e um novo inimigo com intenções sombrias. Natasha deve usar todas as suas habilidades de espionagem e combate para proteger seus aliados e evitar que uma ameaça global se concretize.",
        "imagem": "viuvanegra4.webp",
        "personagem": "Viúva Negra"
    },
    {
        "titulo": "Viúva Negra Vol. 04: Morrer pela espada",
        "preco": 39.90,
        "sinopse": "Em 'Viúva Negra Vol. 04: Perigo Imminente', Natasha enfrenta uma ameaça terrorista que coloca em risco a segurança de todo o planeta. À medida que novas alianças são formadas e antigos inimigos surgem, Natasha precisa decidir até onde está disposta a ir para salvar o mundo.",
        "imagem": "viuvanegra3.jpg",
        "personagem": "Viúva Negra"
    },
    {
        "titulo": "Viúva Negra Vol. 05: O Último Sacrifício",
        "preco": 39.90,
        "sinopse": "No emocionante final da saga, 'Viúva Negra Vol. 05: O Último Sacrifício', Natasha se vê diante de uma escolha impossível que pode mudar sua vida para sempre. Com sua lealdade e habilidades sendo testadas ao máximo, Natasha terá que fazer sacrifícios que afetarão não só sua vida, mas a dos seus entes queridos e aliados.",
        "imagem": "viuvanegra5.webp",
        "personagem": "Viúva Negra"
    },


    {
        "titulo": "Pantera Negra Vol. 01: O Despertar de Wakanda",
        "preco": 39.90,
        "sinopse": "Em 'Pantera Negra Vol. 01: O Despertar de Wakanda', T'Challa assume o trono de Wakanda após a morte de seu pai, mas logo descobre que ser rei é mais complexo do que ele imaginava. Enquanto defende seu país, ele também enfrenta desafios de fora e dentro, incluindo uma ameaça inesperada que pode mudar o destino de Wakanda.",
        "imagem": "panteranegra1.webp",
        "personagem": "Pantera Negra"
    },
    {
        "titulo": "Pantera Negra Vol. 02: O Rei e o Guerreiro",
        "preco": 39.90,
        "sinopse": "Em 'Pantera Negra Vol. 02: O Rei e o Guerreiro', T'Challa lida com uma crise política interna em Wakanda, enquanto enfrenta antigos inimigos que buscam derrubar seu governo. Ao mesmo tempo, ele se vê confrontado com o dilema de manter o segredo de Wakanda ou abrir as portas do reino para o mundo.",
        "imagem": "panteranegra2.webp",
        "personagem": "Pantera Negra"
    },
    {
        "titulo": "Pantera Negra Vol. 03: Herança Perdida",
        "preco": 39.90,
        "sinopse": "Neste volume, T'Challa descobre segredos ocultos sobre seu pai e a história de Wakanda. Ele deve enfrentar um novo inimigo que busca desestabilizar o reino com conhecimentos ancestrais e perigosos, ao mesmo tempo em que tenta reconciliar sua identidade como Pantera Negra e como rei.",
        "imagem": "panteranegra3.webp",
        "personagem": "Pantera Negra"
    },
    {
        "titulo": "Pantera Negra Vol. 04: O Império do Sol",
        "preco": 39.90,
        "sinopse": "Em 'Pantera Negra Vol. 04: O Império do Sol', Wakanda se encontra ameaçada por um império militarista que quer dominar todo o continente africano. T'Challa, com a ajuda de aliados, deve reunir forças para proteger seu povo e seu reino, ao mesmo tempo em que lida com traições internas.",
        "imagem": "panteranegra4.webp",
        "personagem": "Pantera Negra"
    },
    {
        "titulo": "Pantera Negra Vol. 05: A Última Batalha",
        "preco": 39.90,
        "sinopse": "No volume final, 'Pantera Negra Vol. 05: A Última Batalha', T'Challa enfrenta uma guerra total contra seus inimigos mais poderosos, enquanto lida com questões de legado e o futuro de Wakanda. Em uma batalha épica, ele deve decidir até onde está disposto a ir para salvar seu reino e proteger seus entes queridos.",
        "imagem": "panteranegra5.webp",
        "personagem": "Pantera Negra"
    },

 
    {
        "titulo": "A Saga Do Batman Vol. 1",
        "preco": 34.90,
        "sinopse": "O final da década de 1980 viu alguns dos mais aclamados criadores assumirem as rédeas dos títulos do Batman, e o início dessa tão celebrada fase é o que você verá neste volume. Acompanhe o herói em diversas tramas investigativas escritas por Mike W. Barr e outros roteiristas de peso. Edição perfeita para quem pretende conhecer ou revisitar um dos melhores momentos do Cavaleiro das Trevas. Destaque para uma das raras histórias do Cruzado Encapuzado escritas pelo premiado roteirista Alan Moore (Watchmen, V de Vingança).",
        "imagem": "batman1.webp",
        "personagem": "Batman"
    },
    {
        "titulo": "A Saga Do Batman Vol. 2",
        "preco": 34.90,
        "sinopse": "Graves ferimentos sofridos pelo Menino-Prodígio após um combate da Dupla Dinâmica com o Chapeleiro Louco levam Batman a refletir sobre o passado e o futuro de sua parceria com Jason Todd, o segundo garoto a usar a identidade de Robin. As dúvidas do Homem-Morcego aumentarão ainda mais conforme ele se aprofunda em outros elementos da vida pregressa do jovem, como a relação dele com o Duas-Caras e um estranho orfanato de Gotham.",
        "imagem": "batman2.webp",
        "personagem": "Batman"
    },
    {
        "titulo": "A Saga Do Batman Vol. 3",
        "preco": 22.90,
        "sinopse": "Alguns dos crimes mais macabros de Gotham são investigados por Batman nessa edição, como um assassino serial que deixa suas vítimas em lixeiras, uma mímica macabra que ameaça a cidade e um cirurgião que realiza operações ilícitas a fim de enriquecer com o mercado negro. Em meio a tudo isso, Batman e seu novo Robin, Jason Todd, precisam lidar com a ameaça do Duas-Caras, que compartilha elos com o passado do Menino-Prodígio.",
        "imagem": "batman3.webp",
        "personagem": "Batman"
    },
    {
        "titulo": "A Saga Do Batman Vol. 4",
        "preco": 34.90,
        "sinopse": "O Comissário Gordon parte de Gotham City para Louisiana para resolver um caso, mas é imediatamente substituído por um androide que destrói todas as evidências da ausência do verdadeiro Gordon. Cabe a Batman e Robin destruírem o dublê antes que problemas aconteçam. Em Louisiana, Batman parte em busca de respostas, não apenas para encontrar Gordon, mas para rastrear Mark Shaw, o ex-caçador cósmico que ele havia falhado em localizar por lá. Enquanto isso, um assassino conhecido como KGBesta surge nas ruas de Gotham City, e seu plano é atacar diretamente os serviços de segurança dos Estados Unidos da América, em um ataque de proporções catastróficas. Caberá ao Batman defender seu papel como protetor da cidade e interromper esse atentado! E, após se envolver nessa contenda pelo futuro de sua nação, o Cavaleiro das Trevas deverá resolver um misterioso assassinato antes que mais vítimas surjam, em uma desesperada corrida contra o tempo!",
        "imagem": "batman4.webp",
        "personagem": "Batman"
    },
    {
        "titulo": "A Saga Do Batman Vol. 5",
        "preco": 34.90,
        "sinopse": "Graves ferimentos sofridos pelo Menino-Prodígio após um combate da Dupla Dinâmica com o Chapeleiro Louco levam Batman a refletir sobre o passado e o futuro de sua parceria com Jason Todd, o segundo garoto a usar a identidade de Robin. As dúvidas do Homem-Morcego aumentarão ainda mais conforme ele se aprofunda em outros elementos da vida pregressa do jovem, como a relação dele com o Duas-Caras e um estranho orfanato de Gotham.",
        "imagem": "batman5.webp",
        "personagem": "Batman"
    },



{
    "titulo": "Flash Por Geoff Johns Vol. 1",
    "preco": 299.90,
    "sinopse": "Duas décadas atrás, Geoff Johns assumiu os roteiros de The Flash e redefiniu o ícone dos quadrinhos para toda uma geração. Durante seus inesquecíveis cinco anos no comando da série, Johns enriqueceu o mundo de Keystone City e tornou mais humanos tanto Wally West quanto seus inimigos, de um modo que nenhum outro roteirista jamais conseguiu. Agora, reviva ou leia pela primeira vez as incríveis aventuras do Flash desde o início, com arte de gigantes da indústria, como Scott Kolins, Angel Unzueta, Ethan Van Sciver e muitos outros!",
    "imagem": "flash1.webp",
    "personagem": "Flash"
},
{
    "titulo": "Flash Por Geoff Johns Vol. 2",
    "preco": 349.90,
    "sinopse": "Geoff Johns deu uma nova vida ao Flash e seus vilões no seu arco do Velocista Escarlate, e este omnibus coleta a segunda metade de sua passagem na série, destacada pelo ataque do novo inimigo Hunter Zolomon - também conhecido como Zoom! Esta coleção também inclui uma viagem a Gorilla City, tumulto entre os vilões e um encontro com a Mulher-Maravilha, enquanto Mulher Leopardo e Zoom se unem contra nossos heróis! Tudo isso levará à 'Rogue War', enquanto os maiores inimigos do Flash lutam entre si, e o ataque final – e muito pessoal – de Zoom contra Wally!",
    "imagem": "flash2.webp",
    "personagem": "Flash"
},
{
    "titulo": "Flash Por Geoff Johns Vol. 3",
    "preco": 359.90,
    "sinopse": "Quase 20 anos atrás, o roteirista Geoff Johns (Batman: Terra Um, Shazam!), assumiu o título do Flash e redefiniu o ícone para uma nova geração. Neste terceiro e último volume, ele traz de volta o maior de todos os velocistas a carregar o manto do Flash: Barry Allen… e tudo vai pro inferno quando mortos voltam à vida em tudo o mundo e duas crises seguidas se abatem sobre o Universo DC, uma delas com consequências que duram até hoje!",
    "imagem": "flash3.webp",
    "personagem": "Flash"
},
{
    "titulo": "Flash Por Joshua Williamson E Carmine Di Giandomenico Vol. 01",
    "preco": 109.90,
    "sinopse": "Seu nome é Barry Allen, o Homem Mais Rápido do Mundo. Mas ele é muito mais do que isso. Enquanto aprende mais sobre a Força de Aceleração que lhe confere incríveis poderes, também começa a descobrir segredos sobre seu passado que nunca sequer imaginou, como ter sido responsável pelo Ponto de Ignição, que mudou toda a história e ajudou a criar um novo mundo, assistido por forças misteriosas. E quando essa Força de Aceleração que o energiza é liberada por toda Central City, atingindo policiais, criminosos e também civis, cabe ao Flash treinar esses novos velocistas para utilizar seus vastos poderes de maneira inteligente. Mas enquanto alguns concordam em se aliar ao herói na batalha contra o crime – formando literalmente uma Força de Aceleração –, outros utilizarão esse incrível potencial para atos sinistros. E o Velocista Escarlate vai descobrir da pior maneira que alguns males se espalham mais rápido do que ele pode correr.",
    "imagem": "flash4.webp",
    "personagem": "Flash"
},
{
    "titulo": "Flash Por Joshua Williamson E Carmine Di Giandomenico Vol. 02",
    "preco": 104.90,
    "sinopse": "Barry Allen está definitivamente de volta. Depois de inúmeras crises e batalhas, sua cidade está novamente em (aparente) paz e seu relacionamento com a corajosa repórter Íris West parece afinal ter alguma chance. Infelizmente, a Galeria de Vilões não pretende deixar o herói aproveitar esse momento… A doentia relação entre o Velocista Escarlate e seu mais perigoso inimigo, o Flash Reverso, finalmente é esclarecida no retorno do vilão. Mais obcecado do que nunca, Eobard Thawne explica como sua admiração pelo herói se transformou em ódio, mas é claro que seu plano vai muito além de apenas revelar sua origem. Determinado a arruinar completamente a vida de Barry Allen, o vilão pretende matar a amada do herói, Íris West, obrigando o homem mais rápido do mundo a segui-lo até o século 25 para salvá-la. Revelações polêmicas, decisões delicadas e uma corrida frenética aguardam por Barry neste volume.",
    "imagem": "flash5.webp",
    "personagem": "Flash"
},

{
    "titulo": "A Saga Do Superman Vol. 1",
    "preco": 34.90,
    "sinopse": "A história que redefiniu o Homem de Aço para toda uma nova geração de leitores retorna aos fãs nesta edição comemorativa. Escrita e desenhada pelo icônico John Byrne, essa HQ revisita a origem e primeiros anos do Superman e mostra como o pacato Clark Kent se tornou o maior herói de todos os tempos. Edição perfeita tanto para novos leitores que desejam conhecer o herói quanto para os fãs das antigas que desejam relembrar um clássico absoluto.",
    "imagem": "superman1.webp",
    "personagem": "Superman"
},
{
    "titulo": "A Saga Do Superman Vol. 2",
    "preco": 34.90,
    "sinopse": "Após ser surpreendido com a chegada do Homem de Aço a Metrópolis, o ganancioso empresário Lex Luthor usa todos os seus recursos para descobrir tudo o que puder sobre o novo herói. principalmente sua identidade secreta. Luthor, contudo, não será o único adversário que Superman precisará enfrentar no início de sua trajetória heroica, que é marcada ainda pela ameaça de Metallo e Darkseid.",
    "imagem": "superman2.webp",
    "personagem": "Superman"
},
{
    "titulo": "A Saga Do Superman Vol. 3",
    "preco": 34.90,
    "sinopse": "Na arte de Jerry Ordway e John Byrne, dois dos mais aclamados ilustradores dos anos 1980, o Homem de Aço continua sua luta para ajudar pessoas da Terra e de Apokolips, planeta em que lidera um levante contra o tirano Darkseid. Já em nosso mundo, o herói envolve-se em uma intriga internacional e também ajuda seu amigo Perry White. Continue acompanhando uma das melhores fases do Superman pelas mãos de uma talentosa equipe criativa.",
    "imagem": "superman3.webp",
    "personagem": "Superman"
},
{
    "titulo": "A Saga Do Superman Vol. 4",
    "preco": 34.90,
    "sinopse": "Superman é um dos heróis mais poderosos do universo! E entre todos os anos enfrentando perigos e superando vilões poderosos, ele já teve a ajuda de diversos grandes heróis como em seu encontro com o Gavião Negro e a Mulher-Gavião para interromperem uma frota de Thanagarianos, ou ao unir-se a Tropa dos Lanternas Verdes para deter um poderoso inimigo. Mas será que seus grandes poderes podem ser comparados às habilidades de 500 alienígenas ancestrais e derrota-los sem ferir seus amigos, cujas mentes foram usurpadas pelos alienígenas? Ou será que Clark Kent vê seu pior inimigo ao cair em um tanque de produtos químicos e dar origem ao Químio? Nessa edição, vemos também um experimento científico que deu terrivelmente errado e que pode transformar Lois Lane em uma selvagem enorme com força sobre-humana e um enorme problema para controlar sua raiva!",
    "imagem": "superman4.webp",
    "personagem": "Superman"
},
{
    "titulo": "A Saga Do Superman Vol. 5",
    "preco": 34.90,
    "sinopse": "Após enfrentar a Fúria pela primeira vez e ter uma revanche com o Mamute, acompanhado do Quinteto Mortal, o Superman agora precisa encarar a surpreendente aparição de um adolescente vestindo seu uniforme e exibindo habilidades parecidas com as suas! A resposta para quem é o Superboy está espalhada pelo tempo e o Superman se verá preso em um jogo mortal comandado pelo sinistro Senhor do Tempo. Nem mesmo a Legião dos Super-Heróis poderá ser capaz de salvar o Homem de Aço desta vez.",
    "imagem": "superman5.webp",
    "personagem": "Superman"
}, 

{
    "titulo": "Mulher Maravilha: Terra Um - Volume 1",
    "preco": 49.00,
    "sinopse": "Das brilhantes mentes de Grant Morrison (Crise Final, Multiverso DC) e Yanick Paquette (Monstro do Pântano, Corporação Batman), chega a mais provocativa das origens da Mulher-Maravilha já vista – uma releitura sem igual que honra a rica história da personagem! Por milênios, as amazonas da Ilha Paraíso construíram uma próspera sociedade longe da influência maligna dos homens. Uma delas, no entanto, não está satisfeita com sua vida reclusa: Diana, a filha da rainha, sabe que há mais no mundo e quer explorá-lo, mesmo que Hipólita, sua superprotetora mãe, não concorde nada com seus planos. A jovem consegue escapar quando o piloto da Força Aérea Norte-Americana, Steve Trevor (o primeiro homem que ela viu na vida), cai nas praias de sua ilha. Com a vida do militar por um fio, Diana se aventura no há muito proibido mundo do patriarcado. As amazonas a perseguem e a trazem de volta para encarar um julgamento, acusada de violar a lei mais antiga das guerreiras: nunca entrar em contato com o mundo que as prejudicou. Provocadora, mas ainda assim reverente… Moderna, mas ainda assim atemporal… A força e a coragem da maior campeã da Ilha Paraíso – a Mulher-Maravilha – ganha uma nova apresentação nessa graphic novel original!",
    "imagem": "mulhermaravilha1.jpg",
    "personagem": "Mulher Maravilha"
},
{
    "titulo": "Mulher Maravilha: Terra um: Volume 2",
    "preco": 125.00,
    "sinopse": "Durante anos, Diana da Ilha Paraíso ansiou por deixar o único lar que conheceu para trás em busca de aventuras. Agora, depois de um fatídico encontro com o piloto da Força Aérea Steve Trevor, a guerreira amazona se encontra no Mundo dos Homens. E ela está pronta para qualquer coisa que possa aparecer. Mas será que o mundo está pronto para a Mulher-Maravilha? O governo americano, cheio de discórdia e conflitos estranhos para Diana a considerou uma ameaça à sociedade. Como ela poderá levar adiante sua missão de paz e amor para um mundo que não consegue sair do seu modus operandi? Quer dizer, ao menos se houver mais forças malignas em jogo. Confira neste volume 2, da aclamada dupla Grant Morrison e Yanick Paquette! (Wonder Woman Earth One vol. 2).",
    "imagem": "mulhermaravilha2.jpg",
    "personagem": "Mulher Maravilha"
},
{
    "titulo": "Mulher Maravilha: Terra um: Volume 3",
    "preco": 60.90,
    "sinopse": "Confira a épica conclusão da graphic novel mais vendida do The New York Times do aclamado roteirista Grant Morrison e do artista Yanick Paquette! Diana, a nova rainha das Amazonas, deverá reunir as tribos amazonas distantes pela primeira vez em mil anos, pois o ataque de Maxwell Lord à Ilha Paraíso está se aproximando, e, para lidar com a guerra iminente, a Mulher-Maravilha precisará de todas as suas irmãs ao seu lado!",
    "imagem": "mulhermaravilha3.jpg",
    "personagem": "Mulher Maravilha"
},
{
    "titulo": "A Saga Da Mulher-Maravilha Vol. 1",
    "preco": 39.90,
    "sinopse": "Chegou a hora de a maior super-heroína da Editora das Lendas ganhar espaço na coleção mais amada da DC no Brasil dos últimos tempos! A Saga da Mulher-Maravilha se inicia a partir do começo da fase do aclamado roteirista e ilustrador John Byrne. Aqui, o artista se encarrega da arte e da história, entregando uma das fases mais icônicas da Princesa Amazona.",
    "imagem": "mulhermaravilha4.jpg",
    "personagem": "Mulher Maravilha"
},
{
    "titulo": "A Saga Da Mulher-Maravilha Vol. 2",
    "preco": 39.90,
    "sinopse": "Controlado por Morgana Le Fey, cujo objetivo é a vida eterna, Etrigan vai a Gateway City visando capturar a Mulher-Maravilha para sua mestra feiticeira! Além do Demônio, o Vingador Fantasma e Atrion, o imortal, unem-se a essa trama mágica, e a batalha é levada para um plano místico. E mais: a cidade da Princesa Amazona é atingida pela ameaça… do Flash?! E, como se não bastasse um de seus amigos atacá-la, os vilões Sinestro e Apocalypse também tentarão acabar com Diana!",
    "imagem": "mulhermaravilha5.jpg",
    "personagem": "Mulher Maravilha"
},

{
    "titulo": "Arqueiro Verde (2024) Vol. 1",
    "preco": 39.90,
    "sinopse": "O Arqueiro Verde sumiu. E onde é que ele está? É isso que Roy Harper e a Canário Negro querem saber – e a busca os leva até os recônditos da Belle Reve. Será necessário que a família toda de Oliver Queen se junte para encontrá-lo… só que forças perigosas estão determinadas a mantê-los separados a qualquer custo. E é bom se apressarem, pois Oliver e outro membro da família estão sendo perseguidos por uma vilã que eles ainda não conhecem!",
    "imagem": "ArqueiroVerde1.jpeg",
    "personagem": "Arqueiro Verde"
},
{
    "titulo": "Arqueiro Verde Por Mike Grell Vol. 01 (Omnibus)",
    "preco": 314.90,
    "sinopse": "Como seria o Arqueiro Verde sem seus truques, bugigangas e flechas especiais? É a pergunta que Mike Grell tentou responder para o mundo dos quadrinhos ao apresentar um Oliver Queen mais velho e atormentado pela vida e pelos arrependimentos. Patrulhando os becos e telhados de Seattle – acompanhado de sua parceira no combatente do crime e no amor – ele é um caçador urbano na selva de pedra, buscando um propósito no que faz.",
    "imagem": "ArqueiroVerde2.jpeg",
    "personagem": "Arqueiro Verde"
    
},
{
    "titulo": "Arqueiro Verde - Especial Aniversário De 80 Anos",
    "preco": 20.90,
    "sinopse": "Comemorando o 80º aniversário do Arqueiro Verde! Nas últimas oito décadas, ele tem sido um dos personagens principais (e mais barulhentos) do Universo DC, sempre na vanguarda do gênero super-herói. Esta edição de aniversário segue esses passos, com uma grande seleção de talentos que se unem para prestar homenagem ao Arqueiro. Veja o que o passado, o presente e o futuro reservam para Oliver Queen, Canário Negro, Connor Hawke, Arsenal, Arqueiro Vermelho, Ricardito e muito mais neste épico especial!",
    "imagem": "ArqueiroVerde3.jpeg",
    "personagem": "Arqueiro Verde"
},
{
    "titulo": "Lanterna Verde E Arqueiro Verde – Edição Absoluta",
    "preco": 339.90,
    "sinopse": "As histórias clássicas – assinadas pela dupla O’Neil-Adams – que revolucionaram o Universo DC no início da década de 1970! Enquanto o Lanterna Verde Hal Jordan combate ameaças cósmicas no setor 2814 do espaço com o auxílio de seu incrível Anel de Poder, o Arqueiro Verde Oliver Queen se defronta com problemas diferentes na Terra: racismo, pobreza, drogas e outras questões sociais igual.",
    "imagem": "ArqueiroVerde4.jpeg",
    "personagem": "Arqueiro Verde"
},
{
    "titulo": "Arqueiro Verde: a Guerra dos Renegados",
    "preco": 39.90,
    "sinopse": "A Lança. A Espada. O Punho. O Machado. A Máscara. O Escudo. A Flecha. Seis anos atrás, Oliver Queen ficou isolado em uma ilha misteriosa, onde o homem que ele era morreu… e sua nova vida como Arqueiro Verde começou. No entanto, ele não foi parar naquele local por acaso. O destino de Oliver era encontrar o totem da Flecha, escondido na ilha, e se unir aos Renegados – uma agremiação de clãs guerreiros que guiam a humanidade há milênios. Em vez disso, Komodo – o homem que roubou a irmã de Oliver e matou seu pai – tomou a liderança da Flecha e está usando os Renegados para ajudá-lo a conquistar o mundo. E cabe ao Arqueiro detê-lo! Porém, antes disso, o herói terá que descobrir o mais chocante segredo sobre o tempo que passou na fatídica ilha… e sobre a pessoa que o levou até lá.",
    "imagem": "ArqueiroVerde5.jpeg",
    "personagem": "Arqueiro Verde"
},

{
    "titulo": "Lanterna Verde (2024) 01",
    "preco": 24.90,
    "sinopse": "Direto dos eventos da Crise Sombria, os Guardiões de OA, no coração da Tropa dos Lanternas Verdes, puseram em quarentena o setor 2814 – lar do planeta Terra e de seu campeão! Uma derrota retumbante enviou Hal cambaleando de volta para casa, em busca de redescobrir suas raízes… e encontrar o homem responsável por destruir sua vida: Sinestro!",
    "imagem": "LanternaVerde1.webp",
    "personagem": "Lanterna Verde"
},
{
    "titulo": "Lanterna Verde (2024) 02",
    "preco": 24.90,
    "sinopse": "Tem algo errado no setor 2814. Hal Jordan, Kilowog e alguns outros Lanternas devem encontrar a perturbação misteriosa, apesar de haver uma proibição de qualquer Lanterna Verde da Terra deixar o planeta. Eles acabam descobrindo um planeta controlado pelo maior medo de Jordan! E mais: Sinestro se vê jogado numa nova realidade que o empurra para os recônditos mais profundos de seu passado… e talvez de seu futuro.",
    "imagem": "LanternaVerde2.webp",
    "personagem": "Lanterna Verde"
},
{
    "titulo": "Lanterna Verde (2024) 03",
    "preco": 19.90,
    "sinopse": "Hal Jordan descobre mais sobre seu misterioso anel energético, ao passo que Sinestro faz um acordo com a misteriosa 'Guilda' para detonar um ataque em larga escala contra a empresa de Carol Ferris – o que levou o Lanterna Verde a se dar conta de que seu maior inimigo está de volta à Terra e empenhado em fazer o mal! E ainda: John Stewart retorna à sua casa e se reencontra com sua mãe… Mas lembranças de outros tempos ainda o assombram.",
    "imagem": "LanternaVerde3.webp",
    "personagem": "Lanterna Verde"
},
{
    "titulo": "Lanterna Verde (2024) 04",
    "preco": 24.90,
    "sinopse": "O tempo de John Stewart servir como Lanterna Verde chegou ao fim… ou assim ele pensava. Uma tragédia familiar o chama de volta para casa, e, à medida que John começa a recuperar a carreira que deixou para trás, ele tenta abraçar uma vida pacífica. Mas, quando uma força terrível e contagiosa com uma misteriosa conexão com Oa surge na Terra, o último Lanterna Verde de outro universo vem em busca do único guerreiro que pode enfrentar esta ameaça e vencer: o próprio John Stewart!",
    "imagem": "LanternaVerde4.webp",
    "personagem": "Lanterna Verde"
},
{
    "titulo": "Lanterna Verde (2024) 05",
    "preco": 24.90,
    "sinopse": "Sinestro assumiu o controle da empresa de Carol Ferris! E a fúria do inimigo mais perverso de Hal Jordan sai completamente do controle com o poder do anel de Lanterna Vermelho, atingindo níveis planetários. A única esperança de Hal é passar por cima da lei dos Planetas Unidos e levar o vilão à fronteira final! E ainda: confira a continuação da jornada de John Stewart no combate aos Mortos Radiantes! Sem seu anel, como ele conseguirá sobrepujar a Rainha Renascida?",
    "imagem": "LanternaVerde5.webp",
    "personagem": "Lanterna Verde"
},

{
    "titulo": "Arlequina Harleen Vol. 1",
    "preco": 95.00,
    "sinopse": "'A estrada para o inferno está pavimentada de boas intenções. Andando por ela, vi um homem pálido. E ele sorriu para mim.' A dra. Harleen Quinzel - uma jovem e brilhante psiquiatra que tem a cura para a insanidade de Gotham - toma medidas drásticas para salvar a cidade de si mesma. Seja uma testemunha do nascimento da lendária vilã Arlequina nessa pervertida e trágica história de amor produzida pelo aclamado contador de histórias Stjepan Sejic!",
    "imagem": "Arlequina1.webp",
    "personagem": "Arlequina"
},
{
    "titulo": "Arlequina: Edição Especial De 30 Anos",
    "preco": 30.90,
    "sinopse": "Vocês estão cordialmente convidados para uma festança celebrando o 30º aniversário da Princesa Palhaça do Crime nesta fantástica edição especial! É isso mesmo, a Arlequina fez 30 anos em grande estilo e convidou um batalhão de suas antigas equipes criativas para se juntar a ela nesta coletânea matadora de histórias imperdíveis destas três décadas! Incluindo obras com histórias e arte de grandes nomes dos quadrinhos, como: Paul Dini, Amanda Conner, Rafael Albuquerque, Terry e Rachel Dodson, e muito mais!",
    "imagem": "Arlequina2.webp",
    "personagem": "Arlequina"
},
{
    "titulo": "Arlequina E As Aves De Rapina: Todos Contra A Arlequina",
    "preco": 24.90,
    "sinopse": "Desde que seu relacionamento com o Coringa terminou, a Arlequina evitou Gotham City (e seu ex) e encontrou um lar em Coney Island. Mas quando ela recebe uma oferta irrecusável e acaba voltando para a cidade, ela desperta o interesse do Coringa, que coloca todos os supervilões de Gotham contra nossa adorável anti-heroína. Agora, as únicas pessoas corajosas o suficiente para vir em sua defesa são Canário Negro, a Caçadora, Renee Montoya e Cassandra Cain: as Aves de Rapina! Amanda Conner e Jimmy Palmiotti, a dupla que redefiniu a Arlequina para a era moderna, volta para colocar um ponto de exclamação em sua fase lendária!",
    "imagem": "Arlequina3.webp",
    "personagem": "Arlequina"
},
{
    "titulo": "Arlequina (2019) Vol. 5",
    "preco": 24.90,
    "sinopse": "A Arlequina vive suas aventuras em Los Angeles entrando... em uma equipe de luta livre?! A Rainha do Ringue se dá bem com seus novos amigos, mas quando um deles é encontrado morto, a heroína terá de rastrear o assassino antes que ataquem de novo! Com participação especial do inusitado super-herói do futuro, o Gladiador Dourado! A vida da Arlequina em Los Angeles será repleta de boas experiências, ou acontecimentos trágicos...? Última e explosiva edição da Palhacinha do Crime!",
    "imagem": "Arlequina4.webp",
    "personagem": "Arlequina"
},
{
    "titulo": "Arlequina: Beijinho Beijinho Tiro e Facada",
    "preco": 58.00,
    "sinopse": "A melhor amiga da Arlequina está em perigo e nada vai ficar entre a Piradinha e a sua tão querida Hera Venenosa! E mais, quando a vida é atribulada demais para se conciliar o combate ao crime, o trabalho no hospital, as responsabilidades de senhoria e o Clube do Patim, uma solução um tanto quanto não ortodoxa pode ser a única alternativa possível... Acompanhe esse novo momento da Arlequina pelas talentosas mão de Amanda Conner e Jimmy Palmiotti, em aventuras temáticas e especiais. (Harley Quinn 14-16, Harley Quinn Annual 1, Harley Quinn Valentines Day Special, Harley Quinn Holiday Special)",
    "imagem": "arlequina5.jpg",
    "personagem": "Arlequina"
},

{
    "titulo": "Aquaman Por Peter David Vol. 1",
    "preco": 156.90,
    "sinopse": "A clássica fase de Peter David em Aquaman começa neste volume! Desde seu abandono em um recife até sua criação por um golfinho e seu primeiro encontro com os habitantes da superfície, essas histórias narram a origem e a ascensão da figura mítica conhecida como Aquaman.",
    "imagem": "aquaman1.webp",
    "personagem": "Aquaman"
},
{
    "titulo": "Aquaman & Flash: Canção Do Vazio",
    "preco": 40.00,
    "sinopse": "Barry Allen é o Homem Mais Rápido do Mundo. Arthur Curry é filho da terra e Rei dos Mares. E tanto Flash quanto Aquaman, estão tentando conciliar suas relações pessoais com suas vidas profissionais como super-heróis. O Velocista Escarlate está tendo dificuldades em equilibrar desde os recados esquecidos para a sua família até à luta com sua galeria de vilões e a atenção de Barry está sendo atraída para todas as direções. Ele compartilha esta sensação com Arthur Curry, que está tendo as mesmas dificuldades porém em larga escala. Como se isso tudo não bastasse, uma raça alienígena conhecida apenas como Vazios está se aproximando para uma invasão à Terra que ameaça destruir tudo o que eles mais amam. Quem são estes misteriosos extraterrestres e o que eles querem em nosso planeta? O Homem Mais Rápido do Mundo e o Rei dos Mares têm de embarcar em uma missão juntos para descobrir estas e outras respostas e ainda tentar salvar o mundo!",
    "imagem": "aquaman2.webp",
    "personagem": "Aquaman",
    "personagem": "Flash"
},
{
    "titulo": "Aquaman: Andrômeda",
    "preco": 53.83,
    "sinopse": "No fundo do Oceano Pacífico, na distância mais longe possível de qualquer terra firme, está o Ponto Nemo: o cemitério de naves espaciais. Desde o começo da corrida espacial, as nações do mundo enviavam suas naves para amerissar lá e afundarem no silencioso oceano. Mas há no Ponto Nemo uma estrutura que não foi feita por mãos humanas. E ela parece estar... despertando. A tripulação do submarino experimental Andrômeda, movido por um motor quântico secreto, foi escolhida para investigar esse mistério. Mas qualquer coisa de valor no fundo do mar atrai o pirata Arraia Negra. E tudo o que atrai o Arraia Negra atrai seu inimigo, Arthur Curry, o Aquaman! Mas que os céus os ajudem quando as portas do mistério em Ponto Nemo se abrirem para deixá-los entrar. Ram V (Venom, Monstro do Pântano) e Christian Ward (Thor, Invisible Kingdom) se unem a Arthur Curry neste terror psicológico que pode quebrar até mesmo a vontade de um rei!",
    "imagem": "aquaman3.webp",
    "personagem": "Aquaman"
},
{
    "titulo": "Aquaman: A Busca Por Mera",
    "preco": 104.90,
    "sinopse": "Mera, a rainha da Atlântida, desaparece misteriosamente. Enquanto Aquaman inicia sua busca desesperada em todos os lugares, seu reino está nas garras de um novo inimigo chamado Narkran, um ardiloso político com planos para usurpar o trono e governar com mão de ferro! Por fim, como se a situação não fosse ruim o suficiente, o Arraia Negra aparece para tirar vantagem do apuro do Aquaman! Um clássico escrito por Steve Skeates e desenhado pelo lendário Jim Aparo!",
    "imagem": "aquaman4.webp",
    "personagem": "Aquaman"
},
{
    "titulo": "Aquaman Por Geoff Johns (Omnibus)",
    "preco": 304.90,
    "sinopse": "Arthur Curry é um homem de dois mundos. Seis anos atrás, era um habitante da superfície, criado como filho do zelador de um farol. Até que uma tragédia aconteceu. O destino se revelou. E o jovem Arthur Curry acaba reclamando o que era seu por direito: o trono da Atlântida. Mas seu reino é breve. Quando a escuridão ameaça o mundo da superfície, ele se levanta do trono para encarar o desafio. Como Aquaman, ele entra para a equipe de heróis chamada Liga da Justiça, deixando para trás o governo de seu reino. Mas o passado não fica enterrado por muito tempo. Se ele não reclamar seu direito sobre o trono novamente, talvez o trono reclame o direito sobre sua vida…",
    "imagem": "aquaman5.webp",
    "personagem": "Aquaman"
},

{
    "titulo": "Asa Noturna (2022) Vol. 1",
    "preco": 44.90,
    "sinopse": "Asa Noturna está de volta, e sua vontade de manter Blüdhaven segura nunca foi tão forte! Mas sua cidade adotiva elegeu um novo prefeito com o sobrenome Zucco, o nome do assassino de seus pais. Ao investigar o passado do político com a Batgirl, ele desenterra detalhes que irão chocar e alterar para sempre o futuro do herói. Começa aqui a nova fase escrita pelo aclamado roteirista Tom Taylor (DComposição, Injustiça)!",
    "imagem": "asanoturna1.webp",
    "personagem": "Asa Noturna"
},

{
    "titulo": "Asa Noturna (2022) Vol. 3",
    "preco": 44.90,
    "sinopse": "Dick Grayson retorna a Blüdhaven após os eventos de Estado de Medo, apenas para descobrir que uma recompensa de US$ 10.000.000 foi colocada por sua cabeça devido a seus planos de mudar a cidade. E ainda: o encontro de Asa Noturna e Superman! Anos atrás, quando Robin deu seus primeiros passos incertos para longe de Batman como herói solo, Superman interveio e ofereceu apoio e conselhos a Dick Grayson, além de tê-lo nomeado como Asa Noturna. Agora chegou a hora do Asa Noturna retribuir o favor… com o filho de Kal-El, Jon Kent.",
    "imagem": "asanoturna3.webp",
    "personagem": "Asa Noturna"
},
{
    "titulo": "Asa Noturna (2022) Vol. 4",
    "preco": 44.90,
    "sinopse": "A prefeita de Blüdhaven, Melinda Zucco, está com problemas - fingindo trabalhar para o Arrasa-Quarteirão enquanto secretamente tenta derrubar ele e sua gangue de criminosos. Ela também opera ao lado de Dick Grayson para salvar a cidade. Com o Arrasa-Quarteirão controlando mais do submundo do crime do que Asa Noturna jamais imaginou ser possível, Dick será capaz de ajudar a detê-lo antes de as coisas irem longe demais? Enquanto isso, Asa Noturna e Oráculo decidem finalmente definir seu relacionamento.",
    "imagem": "asanoturna4.webp",
    "personagem": "Asa Noturna"
},
{
    "titulo": "Asa Noturna (2022) Vol. 5",
    "preco": 49.90,
    "sinopse": "Descubra quem é o vilão Sem Coração, escondido por trás da máscara de platina, e por que ele só coleta os corações de algumas vítimas e não de outras… e por que ele mesmo não tem coração. Em outra aventura: dez anos atrás, o Vaga-Lume incendiou a casa de infância de Dick Grayson. Agora, ele deve enfrentar a ira de Asa Noturna! E ainda: Asa Peluda - Ano Um! Siga Haley em seu primeiro ano com seus humanos Asa Noturna e Batgirl e veja como ela combate o crime em seu primeiro ano se tornando Asa Peluda!",
    "imagem": "asanoturna5.webp",
    "personagem": "Asa Noturna"
},

{
    "titulo": "Coringa: Operação Babá 01",
    "preco": 24.43,
    "sinopse": "Batman, o símbolo da justiça, e o Coringa, seu eterno arqui-inimigo... A luta entre os dois se desenrolava por toda Gotham City. Porém, certo dia, um acidente inesperado acaba transformando o Batman em um bebê...! Coringa, que precisa derrotar a justiça para provar sua maldade, decide que vai criar e educar o bebê até que ele se torne o super-herói justiceiro, Batman...! Uma atroz comédia parental oficial da DC Comics começa agora...!",
    "imagem": "coringa1.webp",
    "personagem": "Coringa"
},
{
    "titulo": "Coringa: Operação Babá 02",
    "preco": 34.90,
    "sinopse": "Batman, o símbolo da justiça, e o Coringa, seu eterno arqui-inimigo... A luta entre os dois se desenrolava por toda Gotham City. Porém, certo dia, um acidente inesperado acaba transformando o Batman em um bebê...! Quais serão os inúmeros problemas típicos da criação de um filho que o Coringa, que decidiu criar e educar o bebê até que ele se torne o Batman, enfrentará…?! A atroz comédia parental oficial da DC Comics, que atrai a total simpatia da geração que cuida de seus filhos, chega ao segundo volume...!",
    "imagem": "coringa2.webp",
    "personagem": "Coringa"
},
{
    "titulo": "Coringa: Operação Babá 03",
    "preco": 34.90,
    "sinopse": "Batman, o símbolo da justiça, e o Coringa, seu eterno arqui-inimigo… A luta entre os dois se desenrolava por toda Gotham City. Porém, certo dia, um acidente inesperado acaba transformando o Batman em um bebê…! Com a adição da Arlequina, o Coringa e o Batzinho vivem seu dia a dia como uma família de verdade. Quando eles percebem, a formatura do jardim de infância se aproxima. Será que, do jeito que as coisas estão, o Batzinho conseguirá crescer até se tornar o grandioso Batman?! A geração que cuida de seus filhos certamente chorará de emoção! A atroz comédia parental oficial da DC Comics chega a seu último volume…!",

    "imagem": "coringa3.webp",
    "personagem": "Coringa"
},
{
    "titulo": "Coringa: Quebra-Cabeça",
    "preco": 104.90,
    "sinopse": "A Polícia de Gotham tem um cadáver misterioso, uma caixa mágica e uma cela cheia com os vilões mais perigosos da cidade. Agora, tudo o que eles precisam descobrir é o que aconteceu exatamente. Felizmente, um suspeito está disposto a falar. Infelizmente, esse suspeito é o Coringa. Veja se consegue identificar as pistas e resolver o quebra-cabeça!",
    "imagem": "coringa4.webp",
    "personagem": "Coringa"
},
{
    "titulo": "Coringa: O Mundo",
    "preco": 89.90,
    "sinopse": "Em uma iniciativa global que começou com a antologia Batman: O Mundo, autores de todo o planeta apresentam sua visão única do Príncipe Palhaço do Crime… que está prestes a dominar muito mais do que apenas Gotham City. Existe todo um mundo para aterrorizar, e o vilão viajará ao redor do globo, dos Estados Unidos até o Brasil, passando por Argentina, diversos países da Europa e muitos outros locais, fazendo o que sabe de melhor: criando o caos!",
    "imagem": "coringa5.webp",
    "personagem": "Coringa"
},

{
    "titulo": "Era do X-man Vol. 1",
    "preco": 22.90,
    "sinopse": "Os X-Men ajudaram a transformar o planeta numa utopia, na qual viver sendo temido e odiado é algo do passado. Todas as pessoas estão unidas sob a bandeira mutante e todos idolatram a equipe. E, quando um perigo ameaça o mundo, os Maravilhosos X-Men agem pelo bem de todos. Mas, quando Apocalipse e os X-Traídos semeiam a rebelião nesse estranho paraíso, poderão eles reprimir a insurreição em nome da paz?.",
    "imagem": "xmanera.webp"
},

{
    "titulo": "Vingadores Por Geoff Johns Vol 1",
    "preco": 139.90,
    "sinopse": "O celebrado roteirista Geoff Johns assume um arco dos Vingadores! Eles podem derrotar qualquer supervilão, mas serão os Heróis Mais Poderosos da Terra capazes de governar o mundo? Quando as capitais de cada país da Terra desaparecem, as nações através do globo podem socorro aos únicos capazes de ajudá-los: OS VINGADORES! Em seguida, com suas memórias roubadas, Visão procura a ajuda da neta relutante de seu criador para enfrentar um terror tecnológico herdado da Segunda Guerra! Por fim, Thor ascende até o trono asgardiano, e decide que é hora de atender os pedidos de ajuda de seus adoradores.",
    "imagem": "vingadoresgeoff.webp"
},

{
    "titulo": "Zumbis Marvel (Marvel Essenciais)",
    "preco": 66.90,
    "sinopse": "Em uma Terra assustadoramente semelhante à do Universo Marvel, um vírus alienígena transformou todos os maiores super-heróis do mundo em monstros devoradores de carne humana! Por causa de seus incríveis poderes e habilidades, eles levaram apenas algumas horas para destruir toda a vida como a conhecemos... mas o que acontece quando eles ficam sem seres humanos para comer?! Esses incrivelmente poderosos zumbis precisam encontrar uma nova fonte de alimento. Por sorte, a chegada do Surfista Prateado oferecerá a oportunidade que tanto almejavam! Bem-vindo ao mundo chocante de Zumbis Marvel! Escrito por Robert Kirkman, o criador da bem-sucedida série de TV The Walking Dead, e ilustrada por Sean Phillips (Hellblazer, Criminal), este volume mostra uma realidade alternativa do Universo Marvel como jamais imaginamos.",
    "imagem": "zumbismarvel.webp"
},

{
    "titulo": "O Espetacular Homem-Aranha Edição Definitiva Vol. 3",
    "preco": 221.90,
    "sinopse": "A fase mais icônica das aventuras do Amigão da Vizinhança continua! A dupla lendária Stan Lee e John Romita segue criando os maiores clássicos do Aranha, histórias para sempre lembradas como aquelas que criaram o cânone de um dos maiores heróis de todos os tempos! Nesse volume: testemunhe a vingança do Duende Verde, o arqui-inimigo do Homem-Aranha! A estreia de vários dos maiores vilões de Aranha e da Marvel, como o Rino, Shocker e o Rei do Crime! E em meio a grandes mudanças e enormes problemas em sua vida pessoal, a chegada do furacão chamado Mary Jane Watson e a ameaça à vida de sua querida Tia May, Peter Parker toma sua mais drástica decisão... Homem-Aranha, nunca mais!.",
    "imagem": "espetacularhomemaranha1.webp"
},

{
    "titulo": "Demolidor: A Queda De Murdock",
    "preco": 100.90,
    "sinopse": "Em 1986, um já consagrado Frank Miller retornou ao título que o havia lançado ao estrelato para mais uma vez mudar o jogo: ao lado do genial ilustrador David Mazzucchelli, Miller contou uma história que levou o Demolidor ao inferno... e o trouxe de volta transformado - e pronto para uma nova era dos comics! Sem dúvida o clássico dos clássicos estrelado pelo Homem Sem Medo da Marvel, agora com o tratamento diferenciado da coleção Marvel Essenciais!",
    "imagem": "demolidormurdock.webp"
},

{
    "titulo": "Ms. Marvel Vol. 1: Kamala Khan",
    "preco": 34.90,
    "sinopse": "Kamala Khan é uma garota comum de New Jersey - até que subitamente ganha dons extraordinários. Mas quem é realmente a nova Miss Marvel? Adolescente? Muçulmana? Inumana? Saiba as respostas conforme ela toma de assalto o Universo Marvel! Ao descobrir os perigos associados a seus recém-descobertos poderes, Kamala precisa lidar também com o segredo que existe por trás deles. Estará a mais nova heroína do pedaço pronta para utilizar seus imensos dons? Ou o peso do legado que tem a carregar será mais do que ela pode suportar? Nem a própria Kamala sabe ao certo, mas New Jersey que se prepare, pois a Miss Marvel chegou para ficar!.",
    "imagem": "msmarvel.webp"
},

{
    "titulo": "Caçada Sangrenta: Filhos Da Meia-Noite",
    "preco": 36.90,
    "sinopse": "A instável aliança de aventureiros sobrenaturais, antes conhecidos como Filhos da Meia-Noite, deve se unir mais uma vez para lidar com a ameaça vampírica desencadeada em Caçada Sangrenta! Eles têm dois Motoqueiros Fantasmas entre suas fileiras, mas mesmo assim terão dificuldade quando tentarem enfrentar um dos seus! Além disso: enquanto a invasão vampira destrói vidas e causa estragos incalculáveis ​​em todo o Universo Marvel, um dos afetados de uma forma mais inesperada será Jake Gomez, o Lobisomem da Noite! Imbuído de novas habilidades, um novo visual e uma nova direção perigosa, este Lobisomem da Noite é diferente de tudo que você já viu ou conheceu antes!.",
    "imagem": "acaçadasangrenta.webp"
},

{
    "titulo": "Pequenos Heróis Marvel 01",
    "preco": 9.90,
    "sinopse": "Diversão para todas as idades com as contrapartes infantis selvagens e malucas dos maiores heróis da Marvel - ilustradas pelo brilhante cartunista Chris Giarrusso! O Aranha fica triste quando arrisca sua vida tentando fazer entregas na casa do Duende Verde, luta para fazer com que seus colegas heróis paguem suas contas e enfrenta a perda de sua rota para seu temido rival, Eddie Brock! E ainda: Será que Wolverine vai conseguir concluir uma missão angustiante para… comprar uma nova caixa de cereal?.",
    "imagem": "pequenosherois.webp",
    "personagem": "Wolverine"
},

{
    "titulo": "Surfista Prateado Renascimento: Legado (Marvel Lendas)",
    "preco": 31.90,
    "sinopse": "Os amados criadores Ron Marz e Ron Lim retornam para uma história célebre do Surfista Prateado e eles não são os únicos a viajar no tempo… O Sentinela das Estrelas colocou o filho do Capitão Mar-Vell, Genis, sob sua proteção, mas mesmo o Poder Cósmico não pode substituir o amor de um pai! A missão do Surfista para acalmar o coração partido do Kree logo sofre uma reviravolta quando Genis-Vell se perde no tempo, e o Surfista é incriminado por sua aparente morte! Agora, o único que pode salvar o jovem herói é… THANOS?! Encontros com figuras importantes do seu passado, e até mesmo com o próprio diabo.",
    "imagem": "osurfista.webp"
},

{
    "titulo": "A Vingança Do Cavaleiro Da Lua 01",
    "preco": 29.90,
    "sinopse": "Na esteira da morte de Marc Spector, quem será o novo responsável pela Missão da Meia-Noite?  E como ela foi afetada pelas ações do Espectro Negro? Conforme os membros da congregação procuram se recuperar e seguir em frente, eles são confrontados por um misterioso inimigo em vestimentas sombriamente familiares! Um confronto entre Punhos de Khonshu é iminente quando um surpreendente novo Cavaleiro da Lua coloca um alvo na cabeça de Lua do Caçador, mas o que poderia levar os irmãos à guerra?",
    "imagem": "ocavaleiro.webp"
},


{
    "titulo": "Poderosa Vol. 2",
    "preco": 51.90,
    "sinopse": "Depois dos eventos do Cavaleiro dos Pesadelos, uma ameaça kryptoniana há muito adormecida retornou para derrubar Superman e sua família. Quem poderia impedi-la? Bem, de acordo com o Homem de Aço, é a Poderosa! Testemunhe uma corrida contra o tempo, enquanto Paige se reconecta com suas raízes para salvar o mundo de seu passado mortal. E mais: o que acontecerá com o vírus kryptoniano que está se espalhando rapidamente pela costa de Metrópolis?.",
    "imagem": "poderosa.webp"
},

{
    "titulo": "Mulher-Gato (2023) 05",
    "preco": 39.90,
    "sinopse": "Nesta conclusão do arco “Nove Vidas”, acompanhe Selina em uma aventura espacial com heróis e vilões interplanetários, seguida de uma luta contra criminosos canibais nos confins da Terra e de um conflito contra o Esquadrão Suicida que a deixa mais perto da morte. No entanto, caso termine todos as suas provações, ela precisará retornar a Gotham e enfrentar um novo vilão. O que será que a espera lá?.",
    "imagem": "MulherGATO.webp"
},

{
    "titulo": "Mulher-Maravilha/Flash 11",
    "preco": 22.90,
    "sinopse": "Mulher-Leopardo entra na briga enquanto o Soberano recruta o maior inimigo de Diana para um golpe mortal. Como será que a Amazona sairá dessa? Enquanto isso, as Moças-Maravilha haviam prometido à mentora que ficariam de fora da luta, mas Diana precisa de ajuda! Será que elas chegarão a tempo? Enquanto isso, Wally West precisa enfrentar vilões antigos ao mesmo tempo que Amanda Waller coloca parte do seu plano em ação.",
    "imagem": "mulhermaravilhaflash11.webp",
    "personagem": "Mulher Maravilha"
},

{
    "titulo": "A Saga Da Liga Da Justiça 07/23",
    "preco": 57.70,
    "sinopse": "Na conclusão desse incrível arco escrito por Dwayne McDuffie, vemos como a Divisão das Sombras roubou os restos mortais de Doutor Luz, com os poderes prestes a serem restaurados. Mas tudo isso fica em segundo plano quando o Destruidor Cósmico se mostra muito próximo de consumir o Sol. Talvez, nem todo o poder combinado da Divisão das Sombras e da Liga da Justiça possa derrotá-lo. Será que este é o fim do universo como conhecemos? Se a Liga da Justiça não consegue proteger o mundo, então qual o seu propósito?",
    "imagem": "LigadaJustiça.webp"
},

{
    "titulo": "Liga Da Justiça Vs Godzilla Vs Kong",
    "preco": 91.90,
    "sinopse": "Como destruir a Liga da Justiça? Essa é a pergunta que atormenta Lex Luthor e sua Legião do Mal desde os primeiros confrontos entre os dois grupos titânicos. Agora, ao se deparar com as colossais entidades da Ilha da Caveira, Lex acredita ter encontrado a resposta para essa questão eterna. É Superman contra Godzilla, Mulher-Maravilha contra Behemoth, Lanterna Verde contra Scylla, Batman contra Camazotz e Supergirl contra Kong, em uma batalha épica pelo destino do Universo DC.",
    "imagem": "godzillavskong.webp"
},

{
    "titulo": "Supergirl: Mulher Do Amanhã",
    "preco": 159.90,
    "sinopse": "Kara Zor-El, a Supergirl, já vivenciou muitas aventuras épicas ao longo dos anos. Porém, nos últimos tempos, ela está passando por uma crise em relação ao seu propósito no mundo. Ela é uma jovem que, depois de ter visto seu planeta ser destruído, foi enviada à Terra para proteger e ajudar o seu primo bebê; contudo, no fim das contas, ele acabou nem precisando dela. Na verdade, aonde quer que ela vá em seu mundo adotivo, as pessoas a veem só como a prima do Superman. Mas a rotina de Kara está prestes a virar de cabeça para baixo. Ao se deparar com uma garota alienígena que busca vingança pelo assassinato de seu pai, a Supergirl se verá obrigada a repensar as suas convicções para ajudar a menina. É então que uma kryptoniana e uma criança furiosa embarcam numa jornada perigosa no melhor estilo espada e feitiçaria espacial que irá mudar a vida de ambas para sempre! Escrita pelo aclamado roteirista Tom King, com arte da brilhante artista brasileira Bilquis Evely e com cores do talentoso colorista brasileiro Mat Lopes, a obra foi indicada ao Prêmio Eisner de melhor minissérie. Esta Edição de Luxo reúne a minissérie completa em oito edições e traz um texto de introdução inédito de Tom King, uma arte de capa nova de Bilquis Evely, um roteiro alternativo nunca antes publicado da edição 6 e uma galeria de arte de Evely.",
    "imagem": "supergirlamanha.webp"
},

{
    "titulo": "Shazam! (2024) Vol. 1",
    "preco": 49.90,
    "sinopse": "O lendário roteirista Mark Waid se junta mais uma vez ao talentoso ilustrador Dan Mora para, desta vez, trazer a nova série estrelada pelo garoto que, ao dizer duas sílabas, se transforma no Mortal Mais Poderoso da Terra! Agora, devido aos acontecimentos ocorridos no evento Planeta de Lázaro, Billy Batson não divide mais suas habilidades místicas ancestrais cedidas pelo Mago Shazam com seus irmãos. Apesar disso, ele não estará sozinho! Confira as aventuras do herói de coração puro e de sua carismática galeria de aliados e terríveis inimigos num volume que, além de estar recheado de elementos clássicos, é um ponto de início perfeito para novos leitores!.",
    "imagem": "Shazam.webp"
},

{
    "titulo": "Titãs: Viagem Pelo Mundo Das Feras",
    "preco": 84.90,
    "sinopse": "O que está acontecendo com Mutano e por que todos estão se transformando em animais? As consequências da batalha dos Titãs com Starro reverberam em todo o mundo, e, à medida que a infecção se espalha, os esporos que mudam de forma começam a criar raízes. Das ruas escuras de Gotham a Metrópolis, Central City, Blüdhaven e até Atlântida, siga os contos selvagens de seus heróis e vilões favoritos enquanto eles se perdem em sua natureza mais bestial!.",
    "imagem": "titasferas.webp"
},

{
    "titulo": "Jovens Titãs: Ravena (DC Teens)",
    "preco": 49.90,
    "sinopse": "Testemunhe a jornada de Ravena para descobrir quem ela é, a vida que ela quer ter e a pessoa que ela será em jovens titãs ravena. Quando um acidente trágico tira a vida da mãe adotiva de Ravena Roth, aos 17 anos - e a memória de Ravena - ela se muda para Nova Orleans para morar com a família de sua mãe adotiva e terminar o último ano do ensino médio. Começar de novo não é fácil. Ravena lembra como resolver equações matemáticas e fazer macarrão, mas não consegue se lembrar de sua música favorita ou de quem era antes do acidente. Quando coisas estranhas começam a acontecer - coisas que a maioria das pessoas consideraria impossíveis - Ravena começa a pensar que seria melhor não saber quem ela era em sua vida anterior. Da coautora best-seller número 1 do New York Times, de Beautiful Creatures, Kami Garcia e o artista brasileiro Gabriel Picolo, vem este primeiro romance gráfico da série Jovens Titãs.",
    "imagem": "ravenatitans.webp"
},

{
    "titulo": "Gavião Negro Por Geoff Johns Vol. 2",
    "preco": 149.90,
    "sinopse": "Após os acontecimentos ocorridos no volume 1, o Gavião Negro pensou que teria alguns momentos de paz na cidade de St. Roch. No entanto, o passado atribulado dele volta à tona quando um outro Gavião Negro e uma outra Mulher-Gavião aparecem na jogada. No meio do caos, uma boa notícia: o herói assume a liderança da Sociedade da Justiça da América, tendo ao seu lado como companheiros de equipe seus amigos Kendra Saunders, a Moça-Gavião, e o Átomo. Não perca a continuação da aclamada fase do roteirista Geoff Johns à frente de um dos heróis mais interessantes do Universo DC!",
    "imagem": "gaviaonegro1.webp"
},


]


with app.app_context():
    try:
        
        for produto_data in produtos:
            produto = Produto(
                titulo=produto_data["titulo"],
                preco=produto_data["preco"],
                sinopse=produto_data["sinopse"],
                imagem=produto_data["imagem"]
            )
            
           
            if "personagem" in produto_data:
                
                personagem_nome = produto_data["personagem"]
                personagem = Personagem.query.filter_by(nome=personagem_nome).first()
                
                
                if not personagem:
                    personagem = Personagem(nome=personagem_nome)
                    db.session.add(personagem)
                
               
                produto.personagens.append(personagem)
            
            db.session.add(produto)
        
       
        db.session.commit()
        print(f'{len(produtos)} produtos cadastrados com sucesso!')
    except Exception as e:
        db.session.rollback()  
        print(f'Erro ao cadastrar os produtos: {e}')


