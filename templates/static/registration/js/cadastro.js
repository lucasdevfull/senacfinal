function validateFormRegister(event){
    event.preventDefault();

    const username = document.getElementById('name').value;
    const email  = document.getElementById('email').value;
    const password1 = document.getElementById('password').value;
    const password2 = document.getElementById('repeat_password').value;    

    const error = document.getElementById('error');
    const error_span = document.getElementById('spanerror')

    if (username.trim() === '') {
        //window.alert('Username é obrigatório')

        error_span.innerText = 'Username é obrigatório'
        error.classList.remove('hidden')
        timeError()    
        return false
    
    }

    if (email.trim() === ''){
        //window.alert('Email é orbigatório')
        
        error_span.innerText = 'Email é obrigatório'
        error_span.classList.remove('hidden')
        timeError()
        return false 
    
    }

    if (password1.trim() !== password2.trim()) {
        //window.alert('Campos de senha não são iguais')

        
        error_span.innerText = 'Os campos de senha não coincidem'
        error.classList.remove('hidden')
        timeError()
        return false
    
    }  else if (password1.trim() === '' || password2.trim()=== '') {

        error_span.innerText = 'Os campos de senha são obrigatórios'
        error.classList.remove('hidden')
        timeError()
        return false
    
    }
    return true
    
}
function timeError() {

    const error = document.getElementById('erro') 
    setTimeout(() => {
       error.classList.add('hidden') 
    }, 3000);
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