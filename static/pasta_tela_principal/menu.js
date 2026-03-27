// Aguarda o DOM carregar completamente
document.addEventListener('DOMContentLoaded', function() {
    
    // ==================== TEMA ESCURO/CLARO ====================
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = themeToggle?.querySelector('i');

    const getPreferredTheme = () => {
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) return savedTheme;
        if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return 'dark';
        }
        return 'light';
    };

    const setTheme = (theme) => {
        if (theme === 'dark') {
            document.documentElement.setAttribute('data-theme', 'dark');
            themeIcon?.classList.remove('fa-moon');
            themeIcon?.classList.add('fa-sun');
        } else {
            document.documentElement.removeAttribute('data-theme');
            themeIcon?.classList.remove('fa-sun');
            themeIcon?.classList.add('fa-moon');
        }
        localStorage.setItem('theme', theme);
    };

    const toggleTheme = () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
    };

    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
        const savedTheme = getPreferredTheme();
        setTheme(savedTheme);
    }

    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem('theme')) {
            setTheme(e.matches ? 'dark' : 'light');
        }
    });

    // ==================== MENU HAMBURGER ====================
    const menuHamburger = document.getElementById('menu-hamburger');
    const menuLinks = document.getElementById('menu-links');

    if (menuHamburger && menuLinks) {
        menuHamburger.addEventListener('click', () => {
            menuLinks.classList.toggle('active');
        });

        document.querySelectorAll('.menu-links a').forEach(link => {
            link.addEventListener('click', () => {
                menuLinks.classList.remove('active');
            });
        });
    }

    // ==================== SCROLL SUAVE ====================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // ==================== SCROLL INDICATOR ====================
    const scrollIndicator = document.querySelector('.scroll-indicator');
    if (scrollIndicator) {
        scrollIndicator.addEventListener('click', () => {
            const projetosSection = document.querySelector('#projetos');
            if (projetosSection) {
                projetosSection.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    }

    // ==================== CARROSSEL ====================
    const slides = document.querySelectorAll('.carrossel-slide');
    const total = slides.length;
    
    if (total > 0) {
        let slide = 0;
        const slidesContainer = document.querySelector('.carrossel-slides');
        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');
        let autoPlayInterval;

        function mudarSlide(direcao) {
            slide = (slide + direcao + total) % total;
            slidesContainer.style.transform = `translateX(-${slide * 100}%)`;
        }

        function startAutoPlay() {
            if (autoPlayInterval) clearInterval(autoPlayInterval);
            autoPlayInterval = setInterval(() => mudarSlide(1), 4000);
        }

        if (prevBtn) prevBtn.addEventListener('click', () => mudarSlide(-1));
        if (nextBtn) nextBtn.addEventListener('click', () => mudarSlide(1));

        startAutoPlay();

        const carrosselContainer = document.querySelector('.carrossel-container');
        if (carrosselContainer) {
            carrosselContainer.addEventListener('mouseenter', () => {
                if (autoPlayInterval) clearInterval(autoPlayInterval);
            });
            carrosselContainer.addEventListener('mouseleave', startAutoPlay);
        }
    }
    
    console.log("✅ Site carregado com sucesso!");
});