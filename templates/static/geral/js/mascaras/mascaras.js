const maskphone = (value) => {
    if (!value) return ''
    value = value.replace(/\D/g, '')
    value = value.replace(/(\d{2})(\d)/, '($1) $2')
    value = value.replace(/(\d)(\d{4})$/, '$1-$2')
    return value
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

