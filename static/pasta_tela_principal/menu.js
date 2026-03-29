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
        
        // Fechar menu ao clicar fora (opcional)
        document.addEventListener('click', function(e) {
            if (!menuHamburger.contains(e.target) && !menuLinks.contains(e.target)) {
                menuLinks.classList.remove('active');
                body.classList.remove('menu-open');
            }
        });
    }
    
    // ==================== TEMA CLARO/ESCURO ====================
    const themeToggle = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;
    
    // Verifica tema salvo no localStorage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        htmlElement.setAttribute('data-theme', 'dark');
        if (themeToggle) {
            themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
        }
    } else {
        if (themeToggle) {
            themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
        }
    }
    
    // Alternar tema ao clicar
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            if (htmlElement.getAttribute('data-theme') === 'dark') {
                htmlElement.removeAttribute('data-theme');
                localStorage.setItem('theme', 'light');
                themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
            } else {
                htmlElement.setAttribute('data-theme', 'dark');
                localStorage.setItem('theme', 'dark');
                themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
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
});