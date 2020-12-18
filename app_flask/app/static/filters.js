
const rootElement = document.querySelector('#filter_form')
const container = document.querySelector('.filtros')
let tbody = document.createElement('tbody')
tbody.className = 'w-100'
container.appendChild(tbody)

export function addFiltro(ev){
    console.log('admin')
    let attr = ev.target.name
    let module = document.createElement('tr')
    
    let three = [1,2,3]
    three.forEach(element => {
        
        let parte = document.createElement('td')
        switch (element){
            case 1:
//                parte.classList = ['col-2']
                let a = document.createElement('a')
                a.href = '#'
                let myspan = document.createElement('span')
                myspan.classList = 'close-filter searchBy'
                myspan.textContent = '× ' + attr
                a.appendChild(myspan)
                parte.appendChild(a)
                module.appendChild(parte)
                break;
            case 2:
  //              parte.classList = ['col-2']
                let sel = document.createElement('select')
                sel.className = 'searchCond'
                let two = [0,1,2]
                two.forEach(optionN => {
                    
                    let option = document.createElement('option')
                    switch (optionN){
                        case 0:
                            option.value = 'equal'
                            option.text = 'Equal'
                            break;
                        case 1:
                            option.value = 'notequal'
                            option.text = 'Not equal'
                            break;
                        case 2:
                            option.value = 'contains'
                            option.text = 'Contains'
                            break;
                    }
                    sel.appendChild(option)
                })
                parte.appendChild(sel)
                module.appendChild(parte)
                break;
            case 3:
                let input = document.createElement('input')
                input.placeholder = attr
                input.classList = ['flex-fill form-control searchTxt']
                parte.appendChild(input)
                module.appendChild(parte)
                break;
        }
    });
    tbody.appendChild(module)
}


export async function filtralo(){
    let filterBy = document.querySelectorAll('.searchBy')
    let filterConditions = document.querySelectorAll('.searchCond')
    let filterText = document.querySelectorAll('.searchTxt')
    
    let objReq = {}
    for (let i = 0; i < filterBy.length; i++) {
        let condicionIndex = filterConditions[i].selectedIndex
        let condicionOption = filterConditions[i].options

        let busqueda = {
            'attr': filterBy[i].textContent.slice(2),
            'simil': condicionOption[condicionIndex].value,
            'text':filterText[i].value
        }        
        objReq['filter_'+i] = busqueda
    }
    console.log(objReq)
    let url= location.pathname+'/filtered'
    
    
    let envio = await fetch(url,{
        method:'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body:JSON.stringify(objReq)
    }).then(e => {
        return e.json()
    })
    console.log(await envio)
    return await envio
}
