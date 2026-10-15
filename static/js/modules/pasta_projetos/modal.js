/**
 * Modal de Imagem — Projetos
 * Abre imagem em tela cheia com navegação.
 */

document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('proj-modal');
    const modalImg = document.getElementById('proj-modal-img');
    const modalCaption = document.getElementById('proj-modal-caption');
    const btnClose = document.getElementById('proj-modal-close');
    const btnPrev = document.getElementById('proj-modal-prev');
    const btnNext = document.getElementById('proj-modal-next');

    if (!modal) return;

    let carrosselAtual = null;
    let imagensAtuais = [];
    let indexAtual = 0;

    function abrir(carrossel, index) {
        carrosselAtual = carrossel;
        imagensAtuais = Array.from(carrossel.querySelectorAll('.proj-carrossel-img'));
        indexAtual = index;

        renderizar();
        modal.classList.add('active');
        modal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
    }

    function fechar() {
        modal.classList.remove('active');
        modal.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
        carrosselAtual = null;
    }

    function renderizar() {
        const img = imagensAtuais[indexAtual];
        if (!img) return;

        modalImg.src = img.dataset.srcFull || img.src;
        modalImg.alt = img.dataset.altFull || img.alt;
        modalCaption.textContent = img.dataset.altFull || img.alt || '';

        // Esconde botões de navegação se só tem 1 imagem
        const temNav = imagensAtuais.length > 1;
        btnPrev.style.display = temNav ? '' : 'none';
        btnNext.style.display = temNav ? '' : 'none';
    }

    function irPara(index) {
        if (!imagensAtuais.length) return;
        if (index < 0) index = imagensAtuais.length - 1;
        if (index >= imagensAtuais.length) index = 0;
        indexAtual = index;
        renderizar();
    }

    // Expõe globalmente pro carrossel chamar
    window.abrirModalImagem = abrir;

    // Fecha
    btnClose?.addEventListener('click', fechar);

    // Navega
    btnPrev?.addEventListener('click', (e) => {
        e.stopPropagation();
        irPara(indexAtual - 1);
    });

    btnNext?.addEventListener('click', (e) => {
        e.stopPropagation();
        irPara(indexAtual + 1);
    });

    // Clica fora da imagem fecha
    modal.addEventListener('click', (e) => {
        if (e.target === modal) fechar();
    });

    // ESC fecha, setas navegam
    document.addEventListener('keydown', (e) => {
        if (!modal.classList.contains('active')) return;

        if (e.key === 'Escape') fechar();
        if (e.key === 'ArrowLeft') irPara(indexAtual - 1);
        if (e.key === 'ArrowRight') irPara(indexAtual + 1);
    });
});