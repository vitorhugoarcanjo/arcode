/**
 * Theme toggle — claro/escuro
 * Persiste escolha do usuário no localStorage.
 */

document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    if (!themeToggle) return;

    const html = document.documentElement;
    const icon = themeToggle.querySelector('i');

    // 1. Recupera preferência salva OU detecta sistema
    const savedTheme = localStorage.getItem('theme') ||
        (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');

    // 2. Aplica tema inicial
    html.setAttribute('data-theme', savedTheme);
    atualizarIcone(savedTheme);

    // 3. Listener de clique
    themeToggle.addEventListener('click', () => {
        const atual = html.getAttribute('data-theme');
        const novo = atual === 'dark' ? 'light' : 'dark';

        html.setAttribute('data-theme', novo);
        localStorage.setItem('theme', novo);
        atualizarIcone(novo);
    });

    function atualizarIcone(theme) {
        if (theme === 'dark') {
            icon.className = 'fas fa-sun';
            themeToggle.setAttribute('aria-label', 'Ativar modo claro');
        } else {
            icon.className = 'fas fa-moon';
            themeToggle.setAttribute('aria-label', 'Ativar modo escuro');
        }
    }
});