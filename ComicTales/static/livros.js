// Ativando menu-toggle no modo responsivo
const menuToggle = document.getElementById("mobile-menu");
const searchBtnMobile = document.getElementById("search-btn-mobile")
const navLinks = document.querySelector(".nav-links");
const searchBarMobile = document.getElementById("search-bar-mobile")

const prevLivros = document.getElementById('prevLivros');
const nextLivros = document.getElementById('nextLivros');
const trackLivros = document.querySelector('.carrossel-livros-itens');


    const prevLancamentoDC = document.getElementById('prev-lancamento-dc');
    const nextLancamentoDC = document.getElementById('next-lancamento-dc');
    const trackDCLancamento = document.querySelector('.carrossel-lancamento-dc-items');


    const carrossel3ItensLivros = document.querySelector('.carrossel-3itens-manga-inner');
    const prevManga = document.getElementById('prev-manga');
    const nextManga = document.getElementById('next-manga');

  let lancamentoDCIndex = 0; 
  let LivrosIndex = 0;
  let currentIndex = 0;

menuToggle.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});


 //Responsividade search bar

  searchBtnMobile.addEventListener("click", () => {
    searchBarMobile.classList.toggle("search-disable-mobile");
    
  })

   // Carrossel - Personagens - Marvel
  function updatecarrosselLIVROS(){
    trackLivros.style.transform = `translateX(-${LivrosIndex * 100}%)`;
    console.log (LivrosIndex);
  }

  prevLivros.addEventListener('click', () => {
    LivrosIndex = (LivrosIndex > 0) ? LivrosIndex - 1 : 2 - 1;
    updatecarrosselLIVROS();
  });

  nextLivros.addEventListener('click', () => {
    LivrosIndex = (LivrosIndex < 2 - 1) ? LivrosIndex + 1 : 0;
    updatecarrosselLIVROS();
  });

 
  // Carrossel- Marvel - Lançamentos

    function  updatecarrosselLancamentoDC(){
      trackDCLancamento.style.transform = `translateX(-${lancamentoDCIndex * 100}%)`;
    console.log (lancamentoDCIndex);
  }

  prevLancamentoDC.addEventListener('click', () => {
    lancamentoDCIndex = (lancamentoDCIndex > 0) ?    - 1 : 2 - 1;
    updatecarrosselLancamentoDC();
  });

  nextLancamentoDC.addEventListener('click', () => {
    lancamentoDCIndex = (lancamentoDCIndex < 2 - 1) ? lancamentoDCIndex + 1 : 0;
    updatecarrosselLancamentoDC();
  });



     