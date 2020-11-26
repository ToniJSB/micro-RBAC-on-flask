if (sessionStorage.getItem('styleElement') != null) {
    let form = document.querySelector('#move');
    let lsstyle = JSON.parse(sessionStorage.getItem('styleElement'))

    form.style.top = lsstyle.top
    form.style.left = lsstyle.left
    form.style.position = lsstyle.position
}
function allowDrop(ev) {
    ev.preventDefault();
}
function drag(ev) {

    ev.dataTransfer.setData('text', ev.target.id);
    let initialRC = JSON.stringify({'x':ev.offsetX,'y':ev.offsetY})
    ev.dataTransfer.setData('initialRC', initialRC);
    
}

function drop(ev) {
    ev.preventDefault();
    let data = ev.dataTransfer.getData('text')
    let initialRC = JSON.parse(ev.dataTransfer.getData('initialRC'))
    let elementoGetted = document.getElementById(data)
    console.log(elementoGetted.children[0].clientHeight)
    console.log(ev)

    let locationY =  ev.offsetY - initialRC.y
    let locationX =  ev.offsetX - initialRC.x

    console.log(locationY)
    console.log(locationX)
    let heightEl = elementoGetted.children[0].clientHeight
    let widthEl = elementoGetted.getBoundingClientRect().width


    elementoGetted.style.setProperty('position', 'relative')
    if(locationY<0){
        locationY=0
    }
    if(locationY+heightEl>ev.target.clientHeight){
        console.log('confirm')
        locationY = ev.target.clientHeight - heightEl
    }
    if(locationX<0){
        locationX=0
    }
    if(locationX+widthEl>ev.target.clientWidth){
        locationX = ev.target.clientWidth - widthEl
    }
    elementoGetted.style.setProperty('top', locationY + 'px')
    elementoGetted.style.setProperty('left', locationX + 'px')

    let stEl = window.getComputedStyle(elementoGetted)
    sessionStorage.setItem('element', elementoGetted.innerHTML)
    sessionStorage.setItem('styleElement', JSON.stringify(elementoGetted.style))

    ev.target.appendChild(elementoGetted)
}
