const timeError = (error) => {
    setTimeout(() => {
       error.classList.add('hidden') 
    }, 3000);
}