// variavel
let optionLanguage = document.querySelector('#language')
let optionMonth = document.querySelector('#month')

// fetch
function definirOutput() {
  // condicao: checa se lang e month estao selecionados
  if (optionLanguage.value != 'blank' && optionMonth.value != 'blank'){
  // acessa arquivo estatico
  let url = `./data/${optionLanguage.value}-${optionMonth.value}-content.json`;
      // esperar carregar para o console.log
  fetch(url).then(
    function(resposta){
      // retorna json
      return resposta.json()
    }
  ).then(
    function(data) {
      let html = '';
      // insere dados em cada linha com o respectivo link
      // adiciona cada linha ao html
      for (let key of Object.keys(data)){
        let int_key = parseInt(key) // por conta do formato do json
        let row = data[int_key] // idem
        let efemeride = '<li><a href="' + row.url + '" target="_blank">' + row.date + '</a> - ' + row.event + '</li>';
        html += efemeride // para cada item add no html
      }
      // insere dentro da ul no html
      document.querySelector('ul').innerHTML = html
    }
  )
  }else{
    console.log('falta selecionar!')
  }
}

// funcao para limpar resultado
function limparResultado() {
  // condicao: se um dos select tiver valor 'blank'
  if (optionLanguage.value == 'blank' || optionMonth.value == 'blank'){
    html = '' // limpa html
    document.querySelector('ul').innerHTML = html // adiciona dentro de ul
  }else{
    console.log('nao foi blank!')
 }
}

// executa funcao considerando variavel
optionLanguage.addEventListener('change', definirOutput)
optionMonth.addEventListener('change', definirOutput)

optionLanguage.addEventListener('change', limparResultado)
optionMonth.addEventListener('change', limparResultado)
