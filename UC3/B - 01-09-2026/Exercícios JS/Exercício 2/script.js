let tagFeliz = document.getElementById("feliz")
let tagCansado = document.getElementById("cansado")
let tagBravo = document.getElementById("bravo")
let tagNome = document.getElementById("nome")
let tagSentimento = document.getElementById("sentimento")
let tagBody = document.querySelector("body")

function humorFeliz(){
    if (tagFeliz){
        let nome = (tagNome.value)
        tagSentimento.innerHTML = ("O " + nome + " está se sentindo FELIZ")
        tagBody.style.backgroundColor = "#3d8d0fa8"
    }
}

function humorCansado(){
    if(tagCansado){
        let nome = (tagNome.value)
        tagSentimento.innerHTML = ("O " + nome + " está se sentindo CANSADO")
        tagBody.style.backgroundColor = "#3d0f8da8"
        
    }
}

function humorBravo(){
    if(tagBravo){
        let nome = (tagNome.value)
        tagSentimento.innerHTML = ("O " + nome + " está se sentindo BRAVO")
        tagBody.style.backgroundColor = "#8d0f0fa8"

    }
}