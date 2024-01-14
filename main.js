document.addEventListener('DOMContentLoaded', function() {
    let navbar = document.querySelector('.navbar');
    let searchForm = document.querySelector('.search-form');
    let cartItem = document.querySelector('.cart-items-container');

    document.getElementById('menu-btn').onclick = () => {
        navbar.classList.toggle('active');
        console.log('Menu button clicked');
        searchForm.classList.remove('active');
        cartItem.classList.remove('active');
    };

    document.getElementById('search-btn').onclick = () => {
        console.log('search button clicked');
        searchForm.classList.toggle('active');
        navbar.classList.remove('active');
        cartItem.classList.remove('active');
    };

    document.getElementById('cart-btn').onclick = () => {
        console.log('cart button clicked');
        cartItem.classList.toggle('active');
        navbar.classList.remove('active');
        searchForm.classList.remove('active');
    };

    window.onscroll = () => {
        navbar.classList.remove('active');
        searchForm.classList.remove('active');
        cartItem.classList.remove('active');
    };
});
