/**
 * Menu hamburger — mobile
 * Abre/fecha menu com ARIA correto.
 */

document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.getElementById('menu-hamburger');
    const menuLinks = document.getElementById('menu-links');
    if (!hamburger || !menuLinks) return;

    hamburger.addEventListener('click', () => {
        const ativo = menuLinks.classList.toggle('active');
        hamburger.setAttribute('aria-expanded', ativo ? 'true' : 'false');
    });

    // Fecha menu ao clicar num link (mobile)
    menuLinks.querySelectorAll('a').forEach((link) => {
        link.addEventListener('click', () => {
            menuLinks.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
        });
    });
});