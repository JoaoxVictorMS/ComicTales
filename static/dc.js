// Ativando menu-toggle no modo responsivo
const menuToggle = document.getElementById("mobile-menu");
const searchBtnMobile = document.getElementById("search-btn-mobile")
const navLinks = document.querySelector(".nav-links");
const searchBarMobile = document.getElementById("search-bar-mobile")

const prevDC = document.getElementById('prevDC');
const nextDC = document.getElementById('nextDC');
const trackDC = document.querySelector('.carrossel-dc-itens');


    const prevLancamentoDC = document.getElementById('prev-lancamento-dc');
    const nextLancamentoDC = document.getElementById('next-lancamento-dc');
    const trackDCLancamento = document.querySelector('.carrossel-lancamento-dc-items');


  let lancamentoDCIndex = 0; 
  let DCIndex = 0;
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
    trackDC.style.transform = `translateX(-${DCIndex * 100}%)`;
    console.log (DCIndex);
  }

  prevDC.addEventListener('click', () => {
    DCIndex = (DCIndex > 0) ? DCIndex - 1 : 2 - 1;
    updatecarrosselMarvel();
  });

  nextDC.addEventListener('click', () => {
    DCIndex = (DCIndex < 2 - 1) ? DCIndex + 1 : 0;
    updatecarrosselMarvel();
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

