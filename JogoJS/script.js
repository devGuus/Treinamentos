const player = document.querySelector('.player');
let pulando = false;

document.addEventListener('keydown', (event) => {
    const key = event.key.toLowerCase();

    if (key === ' ' && !pulando){
        pulando = true;
        player.classList.add('pular');
        setTimeout(() => {
            player.classList.remove('pular');
            pulando = false;
        }, 500);
    }
});