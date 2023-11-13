$("#navbar a, .btn").on("click", function(event){
    if(this.hash != ""){
        event.preventDefault();

        const hash = this.hash;

        $("html, body").animate(
            {
                scrollTop: $(hash).offset().top - 100
            },800
        );
    }
});

window.addEventListener("scoll", function(){
    if(window.scrolly > 150) {
        document.querySelector("#navbar").computedStyleMap.opacity = 0.9;
    }else{
        document.querySelector("#navbar").computedStyleMap.opacity = 1;
    }
});

let select = document.querySelector('.interacao'),
selectedValue = document.getElementById('selecione'),
optionsViewButton = document.getElementById('estados'),
inputsOptions = document.querySelectorAll('.opcao input')

inputsOptions.forEach(input => {
    input.addEventListener('click', event => {
        selectedValue.textContent = input.dataset.label

        const isMouseOrTouch =
        event.pointerType == "mouse" ||
        event.pointerType == "touch"

        isMouseOrTouch && optionsViewButton.click()
    })
})

window.addEventListener('keydown', e => {
    if(!select.classList.contains('open')) return

    if(e.key == "Escape" || e.key == " "){
        optionsViewButton.click()
    }
})

optionsViewButton.addEventListener('input', () => {
    select.classList.toggle('open')

    if(!select.classList.contains('open')) return

    const input =
        document.querySelector('.opcao input:checked') ||
        document.querySelector('.opcao input')

        input.focus()
})