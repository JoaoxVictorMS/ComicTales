// Ativando menu-toggle no modo responsivo
const menuToggle = document.getElementById("mobile-menu");
const searchBtnMobile = document.getElementById("search-btn-mobile")
const navLinks = document.querySelector(".nav-links");
const searchBarMobile = document.getElementById("search-bar-mobile")

const antManga = document.getElementById('ant-Manga');
const depManga = document.getElementById('dep-Manga');
const trackManga = document.querySelector('.carrossel-manga-itens');


    const prevLancamento = document.getElementById('prev-lancamento');
    const nextLancamento = document.getElementById('next-lancamento');
    const trackLancamento = document.querySelector('.carrossel-lancamento-items');

    const images = document.querySelector('.carrossel-tres-itens .images');
    const antTresItens = document.querySelector('.carrossel-tres-itens .prevTresItens');
    const depTresItens = document.querySelector('.carrossel-tres-itens .nextTresItens');

    const carrossel3ItensManga = document.querySelector('.carrossel-3itens-manga-inner');
    const prevManga = document.getElementById('prev-manga');
    const nextManga = document.getElementById('next-manga');

  let lancamentoIndex = 0; 
  let mangaIndex = 0;
  let currentIndex = 0;

menuToggle.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});


 //Responsividade search bar

  searchBtnMobile.addEventListener("click", () => {
    searchBarMobile.classList.toggle("search-disable-mobile");
    
  })

   // Carrossel - Personagens
  function updatecarrosselManga(){
    trackManga.style.transform = `translateX(-${mangaIndex * 100}%)`;
    console.log (mangaIndex);
  }

  antManga.addEventListener('click', () => {
    mangaIndex = (mangaIndex > 0) ? mangaIndex - 1 : 2 - 1;
    updatecarrosselManga();
  });

  depManga.addEventListener('click', () => {
    mangaIndex = (mangaIndex < 2 - 1) ? mangaIndex + 1 : 0;
    updatecarrosselManga();
  });

 
  // Carrossel- Mangás - Lançamentos

    function updatecarrosselLancamento(){
    trackLancamento.style.transform = `translateX(-${lancamentoIndex * 100}%)`;
    console.log (lancamentoIndex);
  }

  prevLancamento.addEventListener('click', () => {
    lancamentoIndex = (lancamentoIndex > 0) ? lancamentoIndex - 1 : 2 - 1;
    updatecarrosselLancamento();
  });

  nextLancamento.addEventListener('click', () => {
    lancamentoIndex = (lancamentoIndex < 2 - 1) ? lancamentoIndex + 1 : 0;
    updatecarrosselLancamento();
  });


  // Carrossel - 3 itens com id 
  
  let array3ItensManga = [
    {
      id: 140, 
      title: "Kaguya Sama - Love Is War Vol. 7",
      text: "Neste 7º volume, começamos um ´novo episódio´!! O 67º Conselho Estudantil chegou ao fim, e Kaguya e Shirogane perderam o contato que tinham. Ele até decidiu concorrer à presidência de novo como sua única oportunidade na vida de mostrar quem é. No entanto. Querendo pedir para que Kaguya se responsabilizasse pelo discurso de sua campanha, o ar criado foi de uma declaração de amor! Enquanto essas costumeiras guerras intelectuais vão se desenrolando à sua frente, o gênio do 1º ano, Miko Iino, aparece para confrontá-lo!! Acompanhe a corrida pela presidência do 68º Conselho Estudantil!",
      price: "R$ 22,90",
      imgurl: './static/kaguyasama.webp'
    },
    {
      id: 141, 
      title: "As Memórias De Vanitas 07",
      text: "Nesse volume, a cadeia de acontecimentos atinge o clímax na gélida floresta argêntea de Gévaudan. Qual seria o projeto secreto dos D’Apchier, no qual Chloe vem há longos anos trabalhando? As revelações desconcertantes sobre a identidade da bête, a tenebrosa atuação da “Igreja”, o passado intrincado de personagens-chave, como lorde Ruthven e Jeanne, e a bruxa do fogo infernal: é chegado o momento em que todos os atos convergem para um cenário maior e, em meio a tantas emoções, Noé e Vanitas estão em sintonia cada vez mais apurada. Juntos, conseguirão eles impedir que Jeanne cumpra a trágica tarefa que lhe foi incumbida enquanto bourreau...?!",
      price: "R$ 37,90",
      imgurl: './static/vanitas7.webp'
    },
    {
      id: 142,  
      title: "Tougen Anki Vol. 1",
      text: "O sangue de Shiki Ichinose é Oni, e o de seu pai é Momotarou. Normalmente, aqueles com sangue Momotarou caçam os Oni — mas o pai de Shiki se recusou a matá-lo quando criança. Em vez disso, ele adotou Shiki e o criou apesar da atitude rebelde e do temperamento perigoso que vem com o sangue Oni. Quando um membro da Agência Momotarou mata o pai de Shiki, ele jura vingá-lo. Mas conforme Shiki aprimora suas habilidades e aprende a controlar seu sangue Oni, ele será forte o suficiente para sobreviver aos perigos que o aguardam...?",
      price: "R$ 48,90",
      imgurl: './static/tougenanki.webp'
    },
  ];
  

  function renderItensManga() {
    const itensMapped = array3ItensManga.map((item, index) => {

      const productId = item.id; 
  
      return `
        <div class="carrossel-3itens-manga-item">
          <!-- Link para a página do produto -->
          <a href="/produto/${productId}" style="text-decoration: none; color: inherit;">
            <img src="${item.imgurl}" alt="${item.title}">
          </a>
        </div>`;
    });
  
    carrossel3ItensManga.innerHTML = itensMapped.join('');
  }
  

  function updateCarousel(direction) {
    if (direction === 'prev') {
      carrossel3ItensManga.style.transition = 'transform 0.3s ease-in-out';
      carrossel3ItensManga.style.transform = `translateX(${220}px)`;


      let newManga = [...array3ItensManga].pop();
      array3ItensManga.unshift(newManga);
  

      renderItensManga();
      array3ItensManga.pop();
  
      setTimeout(() => {
        carrossel3ItensManga.style.transition = 'none';
        renderItensManga();
        updateMangaInfo();
        carrossel3ItensManga.style.transform = 'translateX(0)';
      }, 450);
    } else if (direction === 'next') {
      carrossel3ItensManga.style.transition = 'transform 0.3s ease-in-out';
      carrossel3ItensManga.style.transform = `translateX(-${220}px)`;
  

      let newManga = [...array3ItensManga].shift();
      array3ItensManga.push(newManga);
  

      renderItensManga();
      array3ItensManga.shift();
  
      setTimeout(() => {
        carrossel3ItensManga.style.transition = 'none';
        renderItensManga();
        updateMangaInfo();
        carrossel3ItensManga.style.transform = 'translateX(0)';
      }, 450);
    }
  }
  

  function updateMangaInfo() {
    let finalItem = array3ItensManga[1]; 
    if (!finalItem) return;
  
    document.getElementById('title').innerText = finalItem.title;
    document.getElementById('text').innerText = finalItem.text;
    document.getElementById('price').innerText = finalItem.price;
  }
  

  prevManga.addEventListener('click', () => {
    updateCarousel('prev');
    updateMangaInfo();
  });
  
  nextManga.addEventListener('click', () => {
    updateCarousel('next');
    updateMangaInfo();
  });
  

  renderItensManga();
  updateMangaInfo();
  
  