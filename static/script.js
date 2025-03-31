// Ativando menu-toggle no modo responsivo
const menuToggle = document.getElementById("mobile-menu");
const searchBtnMobile = document.getElementById("search-btn-mobile")
const navLinks = document.querySelector(".nav-links");
const searchBarMobile = document.getElementById("search-bar-mobile")

/* carrossel dos banners */

const container = document.querySelector('.carousel-container');
const images = document.querySelectorAll('.carousel img');
const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');

/* segundo carrossel */
const arrowPrev = document.getElementById('prev-items');
const arrowNext = document.getElementById('next-items');
const containerItems = document.querySelector('.carousel-items');

/*carrossel final */
const Anterior = document.getElementById('ant-items');
const Depois = document.getElementById('dep-items');
const itens = document.querySelector('.itens-carrossel');

const categories = {
  marvel: {
    banner: '/static/MarvelHQs.webp',
    cards: [
      {
        title: 'Spider-Man Noir: The Complete Collection',
        price: 'R$ 225,30',
        image: '/static/spidermannoir.jpg',
      },
      {
        title: 'Novíssima Wolverine Vol. 2',
        price: 'R$ 60,68',
        image: '/static/novissimaWolverine.webp',
      },
      {
        title: 'Novos Vingadores: Motim!',
        price: 'R$ 41,92',
        image: '/static/vingadoresmotim.jpg',
      },
      {
        title: 'Homem-Aranha Superior (2024) Vol. 1',
        price: 'R$ 34,43',
        image: '/static/Spider-ManSuperior.webp',
      },
      {
        title: 'X-Men: A Saga Da Fênix Negra (Marvel Essenciais)',
        price: 'R$ 60,00',
        image: '/static/FenixNegra.webp',
      },
    ],
  },
  dc: {
    banner: '/static/DCbanner.webp',
    cards: [
      {
        title: 'Batman: a Piada Mortal',
        price: 'R$ 35,00',
        image: '/static/Joker.jpg',
      },
      {
        title: 'Mulher-Maravilha/Flash 10',
        price: 'R$ 79,99',
        image: '/static/MulherMaravilha.webp',
      },
      {
        title: 'Força Da Aceleração',
        price: 'R$ 32,45',
        image: '/static/ForçadaAceleração.webp',
      },
      {
        title: 'Asa Noturna (2022) Vol. 2',
        price: 'R$ 34,43',
        image: '/static/asaNoturna.webp',
      },
      {
        title: 'A Saga Da Liga Da Justiça 06/22',
        price: 'R$ 32,65',
        image: '/static/LigadaJustiça.webp',
      },
    ],
  },
  mangas: {
    banner: '/static/mangásBanner.png',
    cards: [
      {
        title: 'One Piece Vol. 100',
        price: 'R$ 30,75',
        image: '/static/OnePiecev.webp',
      },
      {
        title: 'Dandadan Vol. 02',
        price: 'R$ 28,90',
        image: '/static/Dandadan.webp',
      },
      {
        title: 'Blue Lock Vol. 27',
        price: 'R$ 25,95',
        image: '/static/BlueLock.webp',
      },
      {
        title: 'Dragon Ball Super Vol. 14',
        price: 'R$ 26,70',
        image: '/static/dragonball.webp',
      },
    ],
  },
};
let itemsIndex = 0;
let bookindex = 0;
let index = 0;

menuToggle.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});


//Responsividade search bar

searchBtnMobile.addEventListener("click", () => {
  searchBarMobile.classList.toggle("search-disable-mobile");

})

function updateCarousel() {
  container.style.transform = `translateX(-${index * 100}%)`;
}

prevButton.addEventListener('click', () => {
  index = (index > 0) ? index - 1 : images.length - 1;
  updateCarousel();
});

nextButton.addEventListener('click', () => {
  index = (index < images.length - 1) ? index + 1 : 0;
  updateCarousel();
});


/* segundo carrossel */

function updatecarrossel() {
  containerItems.style.transform = `translateX(-${bookindex * 100}%)`;
  console.log(bookindex);
}

arrowNext.addEventListener('click', () => {
  bookindex = (bookindex > 0) ? bookindex - 1 : 2 - 1;
  updatecarrossel();
});

arrowPrev.addEventListener('click', () => {
  bookindex = (bookindex < 2 - 1) ? bookindex + 1 : 0;
  updatecarrossel();
});





function changeCategory(category) {
  const banner = document.getElementById('banner');
  const cardsContainer = document.getElementById('cards');

  if (categories[category]) {

    // Atualizar o banner
    
    banner.innerHTML = `<img src="${categories[category].banner}" alt="${category} Banner">`;
    banner.style.display = 'flex';

    // Atualizar os cards
    cardsContainer.innerHTML = categories[category].cards
      .map(
        (card, index) => {
          let productId;

          if (category === 'marvel') {
            productId = index + 11;  // IDs 11 a 15 para Marvel
          } else if (category === 'dc') {
            productId = index + 16;  // IDs 16 a 20 para DC
          } else if (category === 'mangas') {
            if (index < 4) {
              productId = index + 21;  // IDs 21 a 24 para Mangás
            }
          }

          if (productId) {
            return `
              <div class="card">
                <div class="top-card">
                  <a href="/produto/${productId}" style="text-decoration: none; color: inherit;">
                    <img src="${card.image}" alt="${card.title}">
                    <p>${card.title}</p>
                  </a>
                </div>
                <div class="bottom-card">
                  <h2>${card.price}</h2>
                  <button>Adicionar ao Carrinho</button>
                </div>
              </div>
            `;
          } else {
            return ''; // Não retorna nada caso o índice seja maior que 3 para Mangás
          }
        }
      )
      .join('');
  }
}

// Carregar uma categoria inicial 
changeCategory('marvel');




/* carrossel final */

function updateCarroussel() {
  itens.style.transform = `translateX(-${itemsIndex * 100}%)`;
  console.log(itemsIndex);
}

Anterior.addEventListener('click', () => {
  itemsIndex = (itemsIndex > 0) ? itemsIndex - 1 : 2 - 1;
  updateCarroussel();
});

Depois.addEventListener('click', () => {
  itemsIndex = (itemsIndex < 2 - 1) ? itemsIndex + 1 : 0;
  updateCarroussel();
});