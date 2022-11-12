const diasEl = document.getElementById("dias");
const horasEl = document.getElementById("horas");
const minsEl = document.getElementById("mins");
const segEl = document.getElementById("sec");

const newAno = "1 jan 2023"

function contarTempo(){

    const newRifaTempo = new Date(newAno);
    const dataAtual = new Date();

    const totalSeconds = (newRifaTempo - dataAtual) / 1000;

    const dias = Math.floor(totalSeconds / 3600 / 24);
    const horas= Math.floor(totalSeconds / 3600) % 24;
    const mins = Math.floor(totalSeconds / 60) % 60;
    const sec = Math.floor(totalSeconds) % 60;

    diasEl.innerHTML = dias;
    horasEl.innerHTML = formatTime(horas);
    minsEl.innerHTML = formatTime(mins);
    segEl.innerHTML = formatTime(sec);

}

function formatTime(time){
    return time < 10 ? '0${time}' : time;
}

contarTempo();

setInterval(contarTempo, 1000);