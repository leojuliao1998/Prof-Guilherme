// todo const => mais usado do que "let" para variáveis de TAG
const select = document.getElementById("linguagem")
const selecionar = document.getElementById("selecionar")

selecionar.addEventListener("click", () => {
    let linguagemSelecionada = select.value
    if (linguagemSelecionada == "javascript") {
        alert("Ai sim meu chapa!")
    }
})