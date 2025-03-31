// Ativando menu-toggle no modo responsivo
const menuToggle = document.getElementById("mobile-menu");
const searchBtnMobile = document.getElementById("search-btn-mobile")
const navLinks = document.querySelector(".nav-links");
const searchBarMobile = document.getElementById("search-bar-mobile")

const prevMarvel = document.getElementById('prevMarvel');
const nextMarvel = document.getElementById('nextMarvel');
const trackMarvel = document.querySelector('.carrossel-marvel-itens');


    const prevLancamentoMarvel = document.getElementById('prev-lancamento-marvel');
    const nextLancamentoMarvel = document.getElementById('next-lancamento-marvel');
    const trackMarvelLancamento = document.querySelector('.carrossel-lancamento-marvel-items');


  let lancamentoMarvelIndex = 0; 
  let marvelIndex = 0;
  let currentIndex = 0;

menuToggle.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});


 //Responsividade search bar

  searchBtnMobile.addEventListener("click", () => {
    searchBarMobile.classList.toggle("search-disable-mobile");
    
  })

   // Carrossel - Personagens - Marvel
   
  function updatecarrosselMarvel(){
    trackMarvel.style.transform = `translateX(-${marvelIndex * 100}%)`;
    console.log (marvelIndex);
  }

  prevMarvel.addEventListener('click', () => {
    marvelIndex = (marvelIndex > 0) ? marvelIndex - 1 : 2 - 1;
    updatecarrosselMarvel();
  });

  nextMarvel.addEventListener('click', () => {
    marvelIndex = (marvelIndex < 2 - 1) ? marvelIndex + 1 : 0;
    updatecarrosselMarvel();
  });

 
  // Carrossel- Marvel - Lançamentos

    function  updatecarrosselLancamentoMarvel(){
      trackMarvelLancamento.style.transform = `translateX(-${lancamentoMarvelIndex * 100}%)`;
    console.log (lancamentoMarvelIndex);
  }

  prevLancamentoMarvel.addEventListener('click', () => {
    lancamentoMarvelIndex = (lancamentoMarvelIndex > 0) ? lancamentoMarvelIndex - 1 : 2 - 1;
    updatecarrosselLancamentoMarvel();
  });

  nextLancamentoMarvel.addEventListener('click', () => {
    lancamentoMarvelIndex = (lancamentoMarvelIndex < 2 - 1) ? lancamentoMarvelIndex + 1 : 0;
    updatecarrosselLancamentoMarvel();
  });

