<<<<<<< HEAD
const validateFormLogin = () => {
    
    const username = document.getElementById('name').value;
    const password = document.getElementById('password').value;

    const error = document.getElementById('error_login');
    const error_span = document.getElementById('span_error');

    if (username === '') {
        
        error_span.textContent = 'Username é obrigatório'
        error.classList.remove('hidden')
        timeError(error)
        
        return false
    }

    if (password === '') {
        
        error_span.textContent = 'Os campos de senha não coincidem'
        error.classList.remove('hidden')
        timeError(error)
        
        return false
    }
    return true
}

const timeError = (error) => {
    setTimeout(() => {
       error.classList.add('hidden') 
    }, 3000);
    return error
=======
const validateLogin = (event) => {
    event.preventDefault();

    const username = document.getElementById('name').value;
    const password = document.getElementById('password').value;

    const error = document.getElementById('error_login');
    const error_span = document.getElementById('span_error');

    if (username === '') {
        
        error_span.textContent = 'Username é obrigatório'
        error.classList.remove('hidden')
        timeError(error)
        
        return false
    }

    if (password === '') {
        
        error_span.textContent = 'Os campos de senha não coincidem'
        error.classList.remove('hidden')
        timeError(error)
        
        return false
    }
    
}

const timeError = (error) => {
    setTimeout(() => {
       error.classList.add('hidden') 
    }, 3000);
    return error
>>>>>>> 3ad139db12e98e697f75a8aa63cf1ff4d2b82fa8
}