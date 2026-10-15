/**
 * Carrossel — Projetos
 * Controla navegação de imagens em cada card.
 */

document.addEventListener('DOMContentLoaded', () => {
    const carrosseis = document.querySelectorAll('[data-carrossel]');

    carrosseis.forEach((carrossel) => {
        const imgs = carrossel.querySelectorAll('.proj-carrossel-img');
        const dots = carrossel.querySelectorAll('[data-carrossel-dot]');
        const btnPrev = carrossel.querySelector('[data-carrossel-prev]');
        const btnNext = carrossel.querySelector('[data-carrossel-next]');

        if (imgs.length <= 1) return;

        let atual = 0;

        function irPara(index) {
            if (index < 0) index = imgs.length - 1;
            if (index >= imgs.length) index = 0;

            imgs[atual].classList.remove('active');
            dots[atual]?.classList.remove('active');

            atual = index;

            imgs[atual].classList.add('active');
            dots[atual]?.classList.add('active');
        }

        btnPrev?.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            irPara(atual - 1);
        });

        btnNext?.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            irPara(atual + 1);
        });

        dots.forEach((dot) => {
            dot.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                irPara(parseInt(dot.dataset.carrosselDot, 10));
            });
        });

        // Teclado
        carrossel.setAttribute('tabindex', '0');
        carrossel.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft') irPara(atual - 1);
            if (e.key === 'ArrowRight') irPara(atual + 1);
        });

        // Clique na imagem ativa → abre modal
        // (O modal captura o evento globalmente pelo data-src-full)
        imgs.forEach((img) => {
            img.addEventListener('click', () => {
                if (!img.classList.contains('active')) return;

                const srcFull = img.dataset.srcFull;
                const altFull = img.dataset.altFull;

                if (window.abrirModalImagem) {
                    window.abrirModalImagem(carrossel, atual);
                }
            });
        });
    });
});