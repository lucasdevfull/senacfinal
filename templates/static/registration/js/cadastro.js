const validateFormRegister = () => {
    
    const username = document.getElementById('name').value;
    const email  = document.getElementById('email').value;
    const password1 = document.getElementById('password').value;
    const password2 = document.getElementById('repeat_password').value;    
    const phone = document.getElementById('telefone').value;
    
    const error = document.getElementById('error_cadastro');
    const error_span = document.getElementById('span_error');

    if (username.trim() === '') {

        error_span.textContent = 'Username é obrigatório!'
        error.classList.remove('hidden')
        timeError(error) 

        return false
    
    }

    if (email.trim() === ''){
        
        error_span.textContent = 'Email é obrigatório!'
        error_span.classList.remove('hidden')
        timeError(error)

        return false 
    
    }

    if (!isEmailValid(email)) {
        error_span.textContent = 'Insira um email válido'
        error_span.classList.remove('hidden')
        timeError(error)

        
    }

    if (password1.trim()<8) {
        error_span.textContent = 'A senha deve conter pelo menos 8 caracteres!'
        error.classList.remove('hidden')
        timeError(error)
    }
    if (password1.trim() !== password2.trim()) { 
        
        error_span.textContent = 'Os campos de senha não coincidem!'
        error.classList.remove('hidden')
        timeError(error)

        return false
    
    }  else if (password1.trim() === '' || password2.trim()=== '') {

        error_span.textContent = 'Os campos de senha são obrigatórios!'
        error.classList.remove('hidden')
        timeError(error)

        return false
    
    }

    if (phone.trim() === '') {

        error_span.textContent = 'Insira seu número de contato'
        error.classList.remove('hidden')
        timeError(error)

        return false
    }

    return true
    
}
// validação de email
const isEmailValid = (email) => {
    
    // cria um regex para validar o email
    const emailRegex = new RegExp(
        //usuario12@host.com
        /^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}$/
    )
    if(emailRegex.test(email)) {
        return true
    }
    return false
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

const timeError = (error) => {
    setTimeout(() => {
       error.classList.add('hidden') 
    }, 3000);
}
