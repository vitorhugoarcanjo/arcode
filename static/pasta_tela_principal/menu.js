document.addEventListener('DOMContentLoaded', function () {
    const hamburger = document.getElementById('menu-hamburger');
    const menuLinks = document.getElementById('menu-links');

    hamburger.addEventListener('click', function () {
        menuLinks.classList.toggle('active');

        const expanded = menuLinks.classList.contains('active');
        hamburger.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    });

    menuLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function () {
            menuLinks.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const themeToggle = document.getElementById('theme-toggle');
    const html = document.documentElement;
    const icon = themeToggle.querySelector('i');

    let currentTheme = 'light';

    if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        currentTheme = 'dark';
    }

    html.setAttribute('data-theme', currentTheme);
    updateThemeIcon(currentTheme);

    themeToggle.addEventListener('click', function () {
        currentTheme = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        html.setAttribute('data-theme', currentTheme);
        updateThemeIcon(currentTheme);
    });

    function updateThemeIcon(theme) {
        if (theme === 'dark') {
            icon.className = 'fas fa-sun';
            themeToggle.setAttribute('aria-label', 'Ativar modo claro');
        } else {
            icon.className = 'fas fa-moon';
            themeToggle.setAttribute('aria-label', 'Ativar modo escuro');
        }
    }
});