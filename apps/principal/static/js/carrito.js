console.log("hfifhawoi");

let btnCarrito = document.getElementById("btnCarrito");

btnCarrito.addEventListener('click',function(){
    arrayProducto = [
        {   
            sku:1,
            nombre:"Comida perro",
            precio:1500,
            cantidad:1
        },
        {   
            sku:2,
            nombre:"Comida gatos",
            precio:4500,
            cantidad:5
        },
        {   
            sku:3,
            nombre:"Comida tigre",
            precio:7500,
            cantidad:3
        },

    ]
    localStorage.setItem("carrito",JSON.stringify(arrayProducto));

    let storage = localStorage.getItem("carrito");

    let token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    console.log("1111111111111",token);


    fetch('/carrito',{
        method:'POST',
        headers:{
            'content-type':'aplication/json',
            'X-CSRFToken':token
        },
        body:storage
    })
})