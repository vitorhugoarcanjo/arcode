document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelector('.carrossel-slides');
    const prevBtn = document.querySelector('.prev');
    const nextBtn = document.querySelector('.next');
    const indicatorsEl = document.querySelector('.carrossel-indicators');
    
    const totalSlides = slides.children.length;
    let currentSlide = 0;
    
    function updateCarousel() {
        slides.style.transform = `translateX(-${currentSlide * 100}%)`;
        
        // Update indicators
        document.querySelectorAll('.indicator').forEach((dot, index) => {
            dot.classList.toggle('active', index === currentSlide);
        });
    }
    
    // Next
    nextBtn.onclick = () => {
        currentSlide = (currentSlide + 1) % totalSlides;
        updateCarousel();
    };
    
    // Prev
    prevBtn.onclick = () => {
        currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
        updateCarousel();
    };
    
    // Indicators
    indicatorsEl.innerHTML = '';
    for(let i = 0; i < totalSlides; i++) {
        const dot = document.createElement('div');
        dot.className = 'indicator';
        dot.onclick = () => {
            currentSlide = i;
            updateCarousel();
        };
        indicatorsEl.appendChild(dot);
    }
    
    // Primeira ativa
    document.querySelector('.indicator')?.classList.add('active');
});