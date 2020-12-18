
export async function draw_view(listItems,links, title){
    let tablaView = document.querySelector('#tabla')
    tablaView.innerHTML = ''
    let headTable = document.createElement('tr')
    listItems.attr.forEach(atributo => {
        let colTable = document.createElement('th')
        if (atributo == 'buttons'){
            let a = document.createElement('a')
            a.href = links.create;
            let boton = document.createElement('button')
            boton.classList = 'btn btn-light '
            boton.textContent = 'Create a new '+ title
            a.appendChild(boton)
            colTable.appendChild(a)
        }else{
            colTable.textContent = atributo
        }
        headTable.appendChild(colTable)
    });
    tablaView.appendChild(headTable)
    listItems.lista.forEach(object => {
        let colTable = document.createElement('tr')
        listItems.attr.forEach(elemento => {
            let field
            if(elemento == 'buttons'){
                field = document.createElement('th')
                field.classList = 'col d-flex justify-content-center flex-row'
                let rlu = document.createElement('a')
                rlu.href = links['update'].replace('1',object['id'])
                let botonU = document.createElement('button')
                botonU.textContent = 'update '+ title;
                botonU.classList = 'btn btn-light'
                rlu.appendChild(botonU)
                
                let rld = document.createElement('a')
                rld.href = links['delete'].replace('1',object['id'])
                let botonD = document.createElement('button')
                botonD.textContent = 'delete '+title;
                botonD.classList = 'btn btn-light'
                rld.appendChild(botonD)
                
                let rls = document.createElement('a')
                rls.href = links['show'].replace('1',object['id'])
                let botonS = document.createElement('button')
                botonS.textContent = 'show '+title;
                botonS.classList = 'btn btn-light '
                rls.appendChild(botonS)
    
                field.appendChild(rlu)
                field.appendChild(rld)
                field.appendChild(rls)
            }
            else{
                field = document.createElement('td')
            
                field.textContent = object[elemento]
            }
            colTable.appendChild(field)
        });
        tablaView.appendChild(colTable)
    })
}
