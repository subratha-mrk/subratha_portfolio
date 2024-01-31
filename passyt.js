const len_range = document.getElementById('len_range')
const len_num = document.getElementById('len_num')
const CapsElement = document.getElementById('Caps')
const numElement = document.getElementById('num')
const spl_charElement = document.getElementById('spl_char')
const form = document.getElementById('formGen')
const passwordDisplay = document.getElementById('passwordDisplay')

const capitalChar = arrayFromLowToHigh(65, 90)
const lowerChar = arrayFromLowToHigh(97, 122)
const numberCodes = arrayFromLowToHigh(48, 57)
const specialChar = arrayFromLowToHigh(32, 47).concat(arrayFromLowToHigh(58, 64)).concat(arrayFromLowToHigh(91, 96)).concat(arrayFromLowToHigh(123, 126))

len_range.addEventListener('input', syncLength)
len_num.addEventListener('input', syncLength)

form.addEventListener('submit', e => {
    e.preventDefault()
    const Length = len_num.value
    const Caps = CapsElement.checked
    const num = numElement.checked
    const spl_char = spl_charElement.checked
    const password = generatePassword(Length, Caps, num, spl_char)
    passwordDisplay.innerText = password
})


function generatePassword(Length, Caps, num, spl_char){
    let charCodes = lowerChar
    if(Caps) charCodes = charCodes.concat(capitalChar)
    if(spl_char) charCodes = charCodes.concat(specialChar)
    if(num) charCodes = charCodes.concat(numberCodes)

    const passwordChar = []
    for(let i=0; i < Length; i++) {
        const character = charCodes[Math.floor(Math.random()*charCodes.length)]
        passwordChar.push(String.fromCharCode(character))
    }
    return passwordChar.join('')
}


function arrayFromLowToHigh(low, high){
    const array = []
    for(let i = low; i <= high; i++){
        array.push(i)
    }
    return array
}


function syncLength(e){
    const value = e.target.value
    len_range.value = value
    len_num.value = value
}

