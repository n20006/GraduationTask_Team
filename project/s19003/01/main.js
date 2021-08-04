let p = document.querySelector('p')
let fontSize = document.querySelector('.fontSize')
let slider = document.querySelector('.slider')

slider.addEventListener('input', e => {
  setFontSize(e.target.value)
})

const setFontSize = val => {
  p.style.fontSize = `${val}px`
  fontSize.innerHTML = `${val}px`
}

window.onload = () => {
  setFontSize(10)
}