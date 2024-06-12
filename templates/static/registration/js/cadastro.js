const form = document.getElementById('form_register')

function validateFormRegister(event){
    event.preventDefault();

    const username = document.getElementById('name').value;
    const email  = document.getElementById('email').value;
    const password1 = document.getElementById('password').value;
    const password2 = document.getElementById('repeat_password').value;    

    
    if (username.trim() === '') {
        //window.alert('Username é obrigatório')

        document.getElementById('erro').innerText = 'Username é obrigatório'
        document.getElementById('erro').classList.remove('hidden')    
        return false
    
    }

    if (email.trim() === ''){
        //window.alert('Email é orbigatório')
        
        document.getElementById('erro').innerText = 'Email é obrigatório'
        document.getElementById('erro').classList.remove('hidden')
        return false 
    
    }

    if (password1.trim() !== password2.trim()) {
        window.alert('Campos de senha não são iguais')

        
        document.getElementById('erro').innerText = 'Os campos de senha não coincidem'
        document.getElementById('erro').classList.remove('hidden')
        return false
    
    }  else if (password1.trim() === '' || password2.trim()=== '') {

        document.getElementById('erro').innerText = 'Os campos de senha são obrigatórios'
        document.getElementById('erro').classList.remove('hidden')
        return false
    
    }
    return true
}

const handlePhone = (event) => {
    let celular = event.target
    celular.value = maskphone(celular.value)
}

const maskphone = (value) => {
    if (!value) return ''
    value = value.replace(/\D/g, '')
    value = value.replace(/(\d{2})(\d)/, '($1) $2')
    value = value.replace(/(\d)(\d{4})$/, '$1-$2')
    return value
}