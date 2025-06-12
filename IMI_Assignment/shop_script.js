let listProductHTML = document.querySelector(".pro_container");
let listCartHTML = document.querySelector(".cart_container")
let iconCartSpan = document.querySelector(".cart_symbol")
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
                <a href="#" class="cart_symbol">🛒</a>
            `;
            listProductHTML.appendChild(newProduct);
        });
    }
}


window.addEventListener("DOMContentLoaded", () => {
    addDataToHTML();
});

console.log(listProductHTML)
listProductHTML.addEventListener("click", (event)=>{
    let positionClick = event.target;
    if (positionClick.classList.contains("cart_symbol")) {
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
    console.log(carts)
}

const addCartToHTML = () => {
    listCartHTML.innerHTML = '';
    if(carts.length > 0){
        carts.forEach(cart => {
            let newCart = document.createElement('div');
            newCart.classList.add()
            // Redo the cart page : "https://www.youtube.com/watch?v=gXWohFYrI0M" 
        })
    }
}