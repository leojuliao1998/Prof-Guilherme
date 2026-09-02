// Pegando as tags pelo id
let texto = document.getElementById("texto");
let status = document.getElementById("status");
let card = document.querySelector(".card");
let titulo = document.querySelector(".card h1");

// Regra: guardar o tamanho atual em uma variável numérica
let tamanho = 18;

// Controla se o modo noturno está ativo ou não
let noturnoAtivo = false;

function aumentar() {
  tamanho = tamanho + 2;
  texto.style.fontSize = tamanho + "px";
  status.textContent = "Ação usada: Aumentar fonte (agora " + tamanho + "px)";
}

function diminuir() {
  tamanho = tamanho - 2;
  texto.style.fontSize = tamanho + "px";
  status.textContent = "Ação usada: Diminuir fonte (agora " + tamanho + "px)";
}

function modoNoturno() {
  noturnoAtivo = !noturnoAtivo;

  if (noturnoAtivo) {
    document.body.style.backgroundColor = "#111111";
    card.style.backgroundColor = "#1e1e1e";
    titulo.style.color = "#ffffff";
    texto.style.color = "#ffffff";
    status.style.color = "#cccccc";
    status.textContent = "Ação usada: Modo noturno ativado";
  } else {
    document.body.style.backgroundColor = "#ffffff";
    card.style.backgroundColor = "#f4f4f4";
    titulo.style.color = "#000000";
    texto.style.color = "#000000";
    status.style.color = "#555555";
    status.textContent = "Ação usada: Modo noturno desativado";
  }
}