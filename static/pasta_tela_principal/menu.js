document.addEventListener('DOMContentLoaded', function () {
    const menuHamburger = document.getElementById('menu-hamburger');
    const menuLinks = document.getElementById('menu-links');
    const body = document.body;

    if (menuHamburger && menuLinks) {
        menuHamburger.addEventListener('click', function (e) {
            e.stopPropagation();
            menuLinks.classList.toggle('active');
            body.classList.toggle('menu-open');
        });

        menuLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function () {
                menuLinks.classList.remove('active');
                body.classList.remove('menu-open');
            });
        });

        document.addEventListener('click', function (e) {
            if (!menuHamburger.contains(e.target) && !menuLinks.contains(e.target)) {
                menuLinks.classList.remove('active');
                body.classList.remove('menu-open');
            }
        });
    }
});




document.addEventListener('DOMContentLoaded', function () {
    const themeToggle = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;

    function updateThemeIcon(theme) {
        if (theme === 'dark') {
            themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
        } else {
            themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
        }
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            const currentTheme = htmlElement.getAttribute('data-theme');

            if (currentTheme === 'dark') {
                htmlElement.removeAttribute('data-theme');
                updateThemeIcon('light');
            } else {
                htmlElement.setAttribute('data-theme', 'dark');
                updateThemeIcon('dark');
            }
        });
    }
});