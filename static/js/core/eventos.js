/**
 * Eventos globais — Padrão 2099
 * Utilidades e listeners reutilizáveis.
 */

// Helper: querySelector encurtado
window.$ = (selector, context = document) => context.querySelector(selector);
window.$$ = (selector, context = document) => context.querySelectorAll(selector);

// Delegação de eventos (evita inline onclick)
window.delegar = (elemento, evento, seletor, callback) => {
    elemento.addEventListener(evento, (e) => {
        const alvo = e.target.closest(seletor);
        if (alvo) callback(e, alvo);
    });
};