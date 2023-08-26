const player = document.querySelector('.player');
const tubo = document.querySelector('.tubo');
const nuvem = document.querySelector('.nuvens');

let pulando = false;
let segundos = 0;
let minutos = 0;
let horas = 0;
let running = true;
let intervalId;

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

const loop = setInterval(() => {

    const tuboPosition = tubo.offsetLeft;
    const playerPosition = +window.getComputedStyle(player).bottom.replace('px', '');

    if (tuboPosition <= 110 && tuboPosition > 0 && playerPosition < 50){
        /* CASO BATA FAÇA => */
        tubo.style.animation = 'none';
        tubo.style.right = '75%';

        player.classList.remove('pular');
        player.style.bottom = '${playerPosition}px';
    
        player.src = './imagens/sonicDead.png';
        player.style.width = '125px';
        player.style.marginLeft = '-20px';

        nuvem.style.animation = 'cloud 20s';

        running = false;

        clearInterval(loop);
    }

}, 10);
/* CRONOMETRO */
function atualizarCronometro() {
    const cronometroElemento = document.querySelector('.time');
    let segundos = 0;
    let minutos = 0;

    intervalId = setInterval(() => {
        if (running) {
          segundos++;
            if (segundos == 60) {
                segundos = 0;
                minutos++;
                    if (minutos == 60) {
                        minutos = 0;
                        horas++;
                    }
            }
        }
    
    const segundosFormatados = segundos < 10 ? `0${segundos}` : segundos;
    const minutosFormatados = minutos < 10 ? `0${minutos}` : minutos;

    cronometroElemento.textContent = `${minutosFormatados}:${segundosFormatados}`;
    }, 1000);
  }

  atualizarCronometro();

  // Verificar a condição para mostrar o botão
function checkCondition() {
    // Substitua a condição abaixo pela sua lógica
    return true;
  }
  
  // Mostrar ou esconder o botão com base na condição
  function toggleButton() {
    const reloadButton = document.getElementById("buttonReset");
    if (checkCondition()) {
      reloadButton.classList.remove("btnR");
    } else{
        reloadButton.classList.add("btnR");
    }
  }
  
  // Recarregar a página quando o botão for clicado
  document.getElementById("buttonReset").addEventListener("click", function() {
    location.reload();
  });
  
  // Verificar a condição ao carregar a página e sempre que necessário
  window.addEventListener("load", toggleButton);
  // Chame toggleButton() sempre que a situação mudar que afeta a exibição do botão