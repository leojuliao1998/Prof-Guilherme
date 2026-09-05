/*
~ Primeiro, selecionamos TODAS AS TAGS COM A CLASSE .slide
^ Eles serão colocados em um "vetor"/lista
* getElementsByClassName = Pega várias tags de uma vez só
*/

const slides = document.getElementsByClassName("slide")
// ^ Slides é um vetor e lembrando: vetor se conta do 0!
/*
todo Slide 1 = Posição 0
todo Slide 2 = Posição 1
todo Slide 3 = Posição 2
todo Slide 4 = Posição 3
*/

// ^ A variável abaixo é um contador para sabermos e controlarmos qual é o slide atual (E trocar para os próximos)
let slideAtual = 0

// ^ Função recebe como parâmetro qual é o slide que ela vai mostrar
function mostrarSlide(posicao){
    // ^ Esaconde todos os slides
    
    /*
    todo let i = 0 => Cria a variável de contador do loop
    todo i < slides.length => Condição de repetir
    todo i++ => De quanto em quanto sobe o contador
    todo length => Comprimento (Tamanho do slide)
    */

    for (let i = 0; i < slides.length; i++){
        // ^ slides[i] = Acessando o slide da vez
        // ^ classList.remove = Remove uma classe daquela TAG
        slides[i].classList.remove("ativo")
    }

    // ^ Após limpar todos, ele só ativa o atual (posicao)
    slides[posicao].classList.add("ativo")
}

function avancarSlide(){
    // ^ Aumentamos o contador
    slideAtual++

    // ~ Porém existe um problema. Não são slides infinitos.
    // ~ Dessa forma, se o número chegar no slide final, ele deve resetar para o slide 0. (Chegou no slide 3 ele volta para o 0)
    // ^ slides.length - conta do 1 (Então ele terá o número 4)
    if (slideAtual >= slides.length){
        slideAtual = 0
    }

    // todo Após aumentar o contador, mostramos ele
    mostrarSlide(slideAtual)
}

function voltarSlide(){
    slideAtual--
    // ^ Chacar limite
    if (slideAtual < 0){
        slideAtual = slides.length - 1
    }
    mostrarSlide(slideAtual)
}

// ^ Chama a função sozinha em um intervalo em milissegundos
// ~ 3000ms = 3 segundos
setInterval(avancarSlide, 3000)