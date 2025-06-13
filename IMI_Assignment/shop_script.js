let iconCart = document.querySelector(".icon-cart");
let closeCart = document.querySelector(".close");
let body = document.querySelector("body")
let listProductHTML = document.querySelector(".listProduct");
let listCartHTML = document.querySelector(".listCart");
let iconCartSpan = document.querySelector(".icon-cart span ");

let carts = [];

const listProducts = [
    {
        "id":1,
        "name": "Product 1",
        "price":100,
        "image":"./images/worker.jpg",
        "category":"Graphic Card",
        "product_page_path": "sproduct.html"
    },
    {
        "id":2,
        "name": "Product 2",
        "price":200,
        "image":"./images/super_duper_sales_image.webp",
        "category":"Graphic Card",
        "product_page_path": "sproduct.html"
    },
    {
        "id":3,
        "name": "Product 3",
        "price":300,
        "image":"./images/worker.jpg",
        "category":"Graphic Card",
        "product_page_path": "sproduct.html"
    },
    {
        "id":4,
        "name": "Product 4",
        "price":400,
        "image":"./images/super_duper_sales_image.webp",
        "category":"Graphic Card",
        "product_page_path": "sproduct.html"
    },

    {
        "id":5,
        "name": "Product 5",
        "price":500,
        "image":"./images/worker.jpg",
        "category":"Graphic Card",
        "product_page_path": "sproduct.html"
    },

    {
        "id":6,
        "name": "Product 6",
        "price":600,
        "image":"./images/super_duper_sales_image.webp",
        "category":"Graphic Card",
        "product_page_path": "sproduct.html"
    },

    {
        "id":7,
        "name": "Product 7",
        "price":700,
        "image":"./images/worker.jpg",
        "category":"Graphic Card",
        "product_page_path": "sproduct.html"
    },

    {
        "id":8,
        "name": "Product 1",
        "price":800,
        "image":"./images/super_duper_sales_image.webp",
        "category":"Graphic Card",
        "product_page_path": "sproduct.html"
    }
]

iconCart.addEventListener("click", () => {
    body.classList.toggle('showCart')
})

closeCart.addEventListener("click", () => {
    body.classList.toggle('showCart')
})

const addDataToHTML = () => {
    listProductHTML.innerHTML = "";
    if (listProducts.length > 0) {
        listProducts.forEach(product => {
            let newProduct = document.createElement("div");
            newProduct.classList.add("pro");
            newProduct.dataset.id = product.id;
            newProduct.innerHTML = `
                <img src="${product.image}" alt="${product.name}" onclick="window.location.href = '${product.product_page_path}'">
                <div class="des">
                    <span>${product.category}</span>
                    <h5>${product.name}</h5>
                    <h4>$${product.price}</h4>
                </div>
                <button class="add_to_cart_button">🛒</button>
            `;
            listProductHTML.appendChild(newProduct);
        });
    }
}


window.addEventListener("DOMContentLoaded", () => {
    addDataToHTML();
});


listProductHTML.addEventListener("click", (event)=>{
    let positionClick = event.target;
    if (positionClick.classList.contains("add_to_cart_button")) {
        let product_id = positionClick.parentElement.dataset.id;
        addToCart(product_id);
    }
})

const addToCart = (product_id) => {
    let positionThisProductInCart = carts.findIndex((value) => value.product_id == product_id);
    if(carts.length <= 0){
        carts = [{
            product_id:product_id,
            quantity:1
        }]
    }else if(positionThisProductInCart < 0){
        carts.push({
            product_id:product_id,
            quantity:1
        });
    }else{
        carts[positionThisProductInCart].quantity = carts[positionThisProductInCart].quantity + 1;
    }
    addCartToHTML();
    addCartToMemory();
}

const addCartToMemory = () => {
    localStorage.setItem('cart', JSON.stringify(carts));
}

const addCartToHTML = () => {
    listCartHTML.innerHTML = '';
    let totalQuantity = 0;
    if(carts.length > 0){
        carts.forEach(cart => {
            totalQuantity = totalQuantity + cart.quantity;
            let newCart = document.createElement('div');
            newCart.classList.add("item")
            newCart.dataset.id = cart.product_id;
            let positionProduct = listProducts.findIndex((value) => value.id == cart.product_id);
            let info = listProducts[positionProduct];
            newCart.innerHTML = `
                <div class="image">
                    <img src="${info.image}" alt="">
                </div>
                <div class="name">
                    ${info.name}
                </div>
                <div class="totalPrice">
                    ${info.price * cart.quantity}
                </div>
                <div class="quantity">
                    <span class="minus"><</span>
                    <span>${cart.quantity}</span>
                    <span class="plus">></span>
                </div>
            `;
            listCartHTML.appendChild(newCart)
            })
    }
    iconCartSpan.innerText = totalQuantity;
}

listCartHTML.addEventListener('click',(event) =>{
    let positionClick = event.target;
    if(positionClick.classList.contains('minus') || positionClick.classList.contains('plus')){
        let product_id = positionClick.parentElement.parentElement.dataset.id;
        let type = 'minus';
        if(positionClick.classList.contains('plus')){
            type = 'plus';
        }
        changeQuantity(product_id,type);
    }
})

const changeQuantity = (product_id,type) => {
    let positionItemInCart = carts.findIndex((value) => value.product_id == product_id)
    if(positionItemInCart >= 0){
        switch (type){
            case'plus':
                carts[positionItemInCart].quantity = carts[positionItemInCart].quantity + 1; 
                break;
            default:
                let valueChange = carts[positionItemInCart].quantity - 1;
                if (valueChange>0){
                    carts[positionItemInCart].quantity = valueChange;
                }else{
                    carts.splice(positionItemInCart, 1);
                }
                break;
        }
    } 
    addCartToMemory();
    addCartToHTML()
}

const initApp = () =>{
    if(localStorage.getItem('cart')){
        carts = JSON.parse(localStorage.getItem('cart'));
        addCartToHTML();
    }
}

initApp()