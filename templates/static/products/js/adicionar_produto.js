const csrfToken =  document.getElementsByName('csrfmiddlewaretoken')[0].value;
class FetchDados {

    constructor(token,data) {
        this.token = token
        this.data = data
    }

    fetchCategoria() {
        
        console.log(this.data)
        var response =  fetch('/adicionar_categoria/', {
            headers: {
                'X-CSRFToken': this.token,
                'Content-Type': "application/json"
            },
            method: 'POST',
            mode: 'same-origin',
            body: JSON.stringify({categoria:this.data}),
        }).then(
            res => res.json()
        ).then((data) => {
            let categoria = document.getElementById('categoria_produto')
            categoria.options[categoria.options.length] = new Option(data.categoria.nome, data.categoria.id)
            categoria.value = data.categoria.id;
        }).catch(
            error => {
                let message = document.getElementById('msgs')
                console.log(message);
                message.innerHTML = `Erro ao enviar os dados! ${error}`
                message.classList.remove('hidden')

                setTimeout(() => {
                    message.classList.add('hidden')
                }, 5000)
            }
        ).finally(
            closeModalCategoria()
        );
    }

    fetchFabricante() {
        
        var response =  fetch('/adicionar_fabricante/', {
            headers: {
                'X-CSRFToken': this.token,
                'Content-Type': "application/json"
            },
            method: 'POST',
            mode: 'same-origin',
            body: JSON.stringify({fabricante:this.data}),
        }).then(
            res => res.json()
        ).then((data) => {
            let fabricante = document.getElementById('fabricante_produto')
            fabricante.options[fabricante.options.length] = new Option(data.fabricante.nome, data.fabricante.id)
            fabricante.value = data.fabricante.id;
        }).catch(
            error => {
                let message = document.getElementById('msgs')
                console.log(message);
                message.innerHTML = `Erro ao enviar os dados! ${error}`
                message.classList.remove('hidden')

                setTimeout(() => {
                    message.classList.add('hidden')
                }, 5000)
            }
        ).finally(
            closeModalFabricante()
        );
    }
}
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

document.getElementById("form-cat").addEventListener("submit", (e) => {
    e.preventDefault()
    
    const categoria = document.getElementById('categoria').value
    const fetching = new FetchDados(csrfToken,categoria)
    return fetching.fetchCategoria()
    
});   



document.getElementById("form-fab").addEventListener("submit",(e) => {
    e.preventDefault() 

    const fabricante = document.getElementById('fabricante').value
    const fetching = new FetchDados(csrfToken,fabricante)
    return fetching.fetchFabricante()
    
})


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


