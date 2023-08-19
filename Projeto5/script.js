function valideLuhn(code) {
    let x = 0;
    let aux = false;

    for (let i = code.length - 1; i >= 0; i--) {
        let digito = parseInt(code[i]);

        if (aux) {
            digito *= 2;
            if (digito > 9) {
                digito -= 9;
            }
        }

        x += digito;
        aux = !aux;
    }

    return x % 10 === 0;
}
function validarCartao(){

    event.preventDefault();

    let codigoCartao = document.getElementById("resp").value;
    let validando = valideLuhn(codigoCartao);

    let resultadoElement = document.getElementById("resultado");
    if (validando) {
        resultadoElement.textContent = "Código do cartão VERDADEIRO";
    } else {
        resultadoElement.textContent = "Código do cartão FALSO";
    }
}