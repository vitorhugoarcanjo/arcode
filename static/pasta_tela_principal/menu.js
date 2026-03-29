// ==================== MENU.JS COMPLETO ====================
document.addEventListener('DOMContentLoaded', function() {
    
    // ==================== MENU HAMBURGER ====================
    const menuHamburger = document.getElementById('menu-hamburger');
    const menuLinks = document.getElementById('menu-links');
    const body = document.body;
    
    if (menuHamburger && menuLinks) {
        // Abrir/fechar menu
        menuHamburger.addEventListener('click', function(e) {
            e.stopPropagation();
            menuLinks.classList.toggle('active');
            body.classList.toggle('menu-open');
        });
        
        // Fechar menu ao clicar em um link
        const links = menuLinks.querySelectorAll('a');
        links.forEach(link => {
            link.addEventListener('click', function() {
                menuLinks.classList.remove('active');
                body.classList.remove('menu-open');
            });
        });
        
        // Fechar menu ao clicar fora
        document.addEventListener('click', function(e) {
            if (!menuHamburger.contains(e.target) && !menuLinks.contains(e.target)) {
                menuLinks.classList.remove('active');
                body.classList.remove('menu-open');
            }
        });
    }
    
    // ==================== TEMA CLARO/ESCURO COM ÍCONES ====================
    const themeToggle = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;
    
    // Função para atualizar o ícone do botão de tema
    function updateThemeIcon(theme) {
        if (themeToggle) {
            if (theme === 'dark') {
                themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
            } else {
                themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
            }
        }
    }
    
    // Verifica tema salvo no localStorage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        htmlElement.setAttribute('data-theme', 'dark');
        updateThemeIcon('dark');
    } else {
        htmlElement.removeAttribute('data-theme');
        updateThemeIcon('light');
    }
    
    // Alternar tema ao clicar
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            if (htmlElement.getAttribute('data-theme') === 'dark') {
                htmlElement.removeAttribute('data-theme');
                localStorage.setItem('theme', 'light');
                updateThemeIcon('light');
            } else {
                htmlElement.setAttribute('data-theme', 'dark');
                localStorage.setItem('theme', 'dark');
                updateThemeIcon('dark');
            }
        });
    }
    
    // ==================== FIX: Ajuste do padding-top para o menu fixo ====================
    function adjustBodyPadding() {
        const menu = document.querySelector('.bloco-menu');
        if (menu) {
            const menuHeight = menu.offsetHeight;
            document.body.style.paddingTop = menuHeight + 'px';
        }
    }
    
    adjustBodyPadding();
    window.addEventListener('resize', adjustBodyPadding);
    
    // ==================== VERIFICA SE OS ÍCONES ESTÃO CARREGANDO ====================
    console.log('Menu.js carregado!');
    console.log('Botão tema:', themeToggle);
    console.log('Menu hamburger:', menuHamburger);
});








// ==================== CARROSSEL DE PROJETOS ====================
function initCarrossel() {
    const slides = document.getElementById('carrosselSlides');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const indicators = document.getElementById('indicators');
    
    if (!slides || !prevBtn || !nextBtn) return;
    
    const slidesCount = slides.children.length;
    let currentIndex = 0;
    let autoPlayInterval;
    const AUTO_PLAY_DELAY = 5000; // 5 segundos
    
    // Cria os indicadores (bolinhas)
    if (indicators) {
        for (let i = 0; i < slidesCount; i++) {
            const indicator = document.createElement('div');
            indicator.classList.add('indicator');
            if (i === 0) indicator.classList.add('active');
            indicator.addEventListener('click', () => goToSlide(i));
            indicators.appendChild(indicator);
        }
    }
    
    // Função para ir para um slide específico
    function goToSlide(index) {
        if (index < 0) index = slidesCount - 1;
        if (index >= slidesCount) index = 0;
        
        currentIndex = index;
        const offset = -currentIndex * 100;
        slides.style.transform = `translateX(${offset}%)`;
        
        // Atualiza indicadores
        if (indicators) {
            const allIndicators = indicators.querySelectorAll('.indicator');
            allIndicators.forEach((ind, i) => {
                if (i === currentIndex) {
                    ind.classList.add('active');
                } else {
                    ind.classList.remove('active');
                }
            });
        }
    }
    
    // Próximo slide
    function nextSlide() {
        goToSlide(currentIndex + 1);
    }
    
    // Slide anterior
    function prevSlide() {
        goToSlide(currentIndex - 1);
    }
    
    // Inicia autoplay
    function startAutoPlay() {
        if (autoPlayInterval) clearInterval(autoPlayInterval);
        autoPlayInterval = setInterval(nextSlide, AUTO_PLAY_DELAY);
    }
    
    // Para autoplay
    function stopAutoPlay() {
        if (autoPlayInterval) {
            clearInterval(autoPlayInterval);
            autoPlayInterval = null;
        }
    }
    
    // Eventos dos botões
    prevBtn.addEventListener('click', () => {
        prevSlide();
        stopAutoPlay();
        startAutoPlay();
    });
    
    nextBtn.addEventListener('click', () => {
        nextSlide();
        stopAutoPlay();
        startAutoPlay();
    });
    
    // Pausa autoplay quando mouse está sobre o carrossel
    const carrosselContainer = document.querySelector('.carrossel-container');
    if (carrosselContainer) {
        carrosselContainer.addEventListener('mouseenter', stopAutoPlay);
        carrosselContainer.addEventListener('mouseleave', startAutoPlay);
        
        // Para touch devices
        carrosselContainer.addEventListener('touchstart', stopAutoPlay);
        carrosselContainer.addEventListener('touchend', startAutoPlay);
    }
    
    // Inicia autoplay
    startAutoPlay();
    
    // Suporte a swipe no mobile
    let touchStartX = 0;
    let touchEndX = 0;
    
    slides.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
    });
    
    slides.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        const swipeThreshold = 50;
        
        if (touchEndX < touchStartX - swipeThreshold) {
            nextSlide();
            stopAutoPlay();
            startAutoPlay();
        }
        
        if (touchEndX > touchStartX + swipeThreshold) {
            prevSlide();
            stopAutoPlay();
            startAutoPlay();
        }
    });
}

// Inicializa o carrossel quando a página carregar
document.addEventListener('DOMContentLoaded', function() {
    initCarrossel();
});