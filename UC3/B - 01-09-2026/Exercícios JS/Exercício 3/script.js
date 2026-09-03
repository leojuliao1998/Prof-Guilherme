let pontos = document.getElementById("pontos")
let resultado = document.getElementById("resultado")
let body = document.querySelector("body")

pontuacao = 0

function verdadeiro(correta){
    if (correta) {
        pontuacao++
        pontos.innerText = pontuacao
        resultado.innerText = "Acertou!"
        body.style.backgroundColor = "#2e7d32"
    }
    else {
        pontuacao--
        pontos.innerText = pontuacao
        resultado.innerText = "Errou!"
        body.style.backgroundColor = "#c62828"
    }
}

function reiniciar() {
    pontuacao = 0
    pontos.innerText = pontuacao
    resultado.innerText = ""
    body.style.backgroundColor = "transparent"
}