const closeModalCategoria = () => {
    
    document.getElementById('modal_categoria').classList.add('hidden')
}

const closeModalFabricante = () => {
    document.getElementById('modal_fabricante').classList.add('hidden')
}

const openModalCategoria = () => {
    document.getElementById('modal_categoria').classList.remove('hidden')
}

const openModalFabricante = () => {
    document.getElementById('modal_fabricante').classList.remove('hidden')
}

async function formCategoria() {
    
    const csrftoken = document.getElementsByName('csrfmiddlewaretoken')
    const formData = {
        categoria: document.getElementById('categoria').value
    }
    try{
        const response = await fetch(
            'http://127.0.0.1:8000/adicionar_categoria/',
            {
                method:'POST',
                headers :{
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json',
                },
                body:JSON.stringify(formData)
                
            }
        )
        if (!response) throw new Error('HTTP error')

        const data = await response.json()
        console.log(data)
        
    } catch(error) {
        console.error(`Erro ao enviar os dados! ${error}`);    
    }    
    closeModalCategoria()
}

async function formFabricante() {
    

    const csrftoken = document.getElementsByName('csrfmiddlewaretoken')
    const formData = {
        fabricante:document.getElementById('fabricante').value
    }
    try {
        const response = await fetch(
            'http://127.0.0.1:8000/adicionar_fabricante/',
            {
                method: 'POST',
                headers :{
                    'X-CSRFToken': csrftoken,
                    'Content-Type': 'application/json',
                },
                body:JSON.stringify(formData)
            }
        )
        if (!response) throw new Error('HTTP error')

        const data = await response.json()
        console.log(data)
    } catch(error) {
        console.error(`Erro ao enviar os dados! ${error}`)
    }
    closeModalFabricante()
}

const maskpreco = (event) => {
    const digitos = event.target.value
    .split()
    .filter(s => /\d/.test(s))
    .join()
    .padStart(3,'0')
    const digitosFloat = digitos.slice(0, -2) + '.' + digitos.slice(-2)
    event.target.value = moedamask(digitosFloat)
}

const moedamask = (valor, locale = 'pt-BR', currency = 'BRL') => {
    return new Intl.NumberFormat(locale, {
        style:'currency',
        currency
    }).format(valor)
}

function getCookie(name) {
    let cookie = {};
    
    document.cookie.split(';').forEach(function(el) {
      let [k,v] = el.split('=');
      cookie[k.trim()] = v;
    })
    
    return cookie[name];
    
  }
