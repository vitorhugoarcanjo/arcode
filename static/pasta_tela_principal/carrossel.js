// carrossel.js - VERSÃO SIMPLIFICADA
document.addEventListener('DOMContentLoaded', function() {
    const slides = document.getElementById('carrosselSlides');
    const prev = document.getElementById('prevBtn');
    const next = document.getElementById('nextBtn');
    const indicators = document.getElementById('indicators');
    
    if (!slides) {
        console.log('Carrossel não encontrado');
        return;
    }
    
    const total = slides.children.length;
    let current = 0;
    
    function update() {
        slides.style.transform = `translateX(-${current * 100}%)`;
        
        if (indicators) {
            const dots = indicators.querySelectorAll('.indicator');
            dots.forEach((dot, i) => {
                dot.classList.toggle('active', i === current);
            });
        }
    }
    
    function nextSlide() {
        current = (current + 1) % total;
        update();
    }
    
    function prevSlide() {
        current = (current - 1 + total) % total;
        update();
    }
    
    if (prev) prev.onclick = prevSlide;
    if (next) next.onclick = nextSlide;
    
    // Criar indicadores
    if (indicators) {
        indicators.innerHTML = '';
        for (let i = 0; i < total; i++) {
            const dot = document.createElement('div');
            dot.className = 'indicator';
            if (i === 0) dot.classList.add('active');
            dot.onclick = () => {
                current = i;
                update();
            };
            indicators.appendChild(dot);
        }
    }
    
    console.log('Carrossel iniciado com', total, 'slides');
});