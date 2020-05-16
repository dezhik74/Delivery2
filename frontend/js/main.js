'use strict'; 

const ROOT_ADDRESS = 'http://127.0.0.1:8000';
const API_ADDRESS = ROOT_ADDRESS + '/api/v1/';

const cartButton = document.querySelector("#cart-button");
const modal = document.querySelector(".modal");
const close = document.querySelector(".close");
const buttonAuth = document.querySelector('.button-auth');
const modalAuth = document.querySelector('.modal-auth');
const closeAuth = document.querySelector ('.close-auth');
const logInForm = document.querySelector('#logInForm');
const loginInput = document.querySelector('#login');
const userName = document.querySelector('.user-name');
const buttonOut = document.querySelector('.button-out');
const cardsRestaurants = document.querySelector('.cards-restaurants');
const containerPromo = document.querySelector ('.container-promo');
const restaurants = document.querySelector ('.restaurants');
const menu = document.querySelector ('.menu');
const logo = document.querySelector ('.logo');
const cardsMenu = document.querySelector ('.cards-menu');
const restaurantMenu = document.querySelector ('.restaurant-menu');
const cartModalBody = document.querySelector ('.cart-modal-body');
const modalPricetag = document.querySelector ('.modal-pricetag');
const buttonClearCart = document.querySelector ('.clear-cart') 

let cart = JSON.parse(localStorage.getItem('gloDeliveryCart'));
if (cart === null) cart = [];

let login = localStorage.getItem('gloDelivery');

const getData = async function (url) {
  const responce = await fetch (url);
  if (!responce.ok) {
    throw new Error(`Ошибка по адресу ${url}, статус ошибки ${responce.status}!`);
  }
  return await responce.json();
};

function toggleModal() {
  modal.classList.toggle("is-open");
}

function toggleModalAuth () {
  modalAuth.classList.toggle("is-open");
  if (!login) {
    document.querySelector('.auth-error').style.display = 'none';
  } 
}

function authorized () {

  function logOut() {
    login = null;
    buttonAuth.style.display = '';
    userName.style.display = '';
    buttonOut.style.display = '';
    cartButton.style.display = '';
    buttonOut.removeEventListener('click', logOut);
    localStorage.removeItem('gloDelivery');
    localStorage.removeItem('gloDeliveryCart');
    checkAuth();
  }
  console.log('Авторизован');
  
  userName.textContent = login;
  buttonAuth.style.display = 'none';
  userName.style.display = 'inline';
  buttonOut.style.display = 'flex';
  cartButton.style.display = 'flex';
  buttonOut.addEventListener('click', logOut);
}

function notAuthorized () {

  function logIn (event) {
    event.preventDefault();
    if (loginInput.value) {
      login = loginInput.value;
      localStorage.setItem('gloDelivery', login);
      toggleModalAuth();
      buttonAuth.removeEventListener('click', toggleModalAuth);
      closeAuth.removeEventListener('click', toggleModalAuth);
      logInForm.removeEventListener('submit', logIn);
      logInForm.reset();
      checkAuth ();
    } else {
        document.querySelector('.auth-error').style.display = 'block';
    }
  }

  console.log("не авторизован");
  buttonAuth.addEventListener('click', toggleModalAuth);
  closeAuth.addEventListener('click', toggleModalAuth);
  logInForm.addEventListener('submit', logIn);
}

function checkAuth () {
  if (login) {
    authorized ();
  } else {
    notAuthorized();
  }
}

function createCardRestaurant ({ 
                                  image, 
                                  category:kitchen, 
                                  name, 
                                  price_level:price, 
                                  rating:stars, 
                                  delivery_time:timeOfDelivery, 
                                  id }) {
  const card = `
  <a class="card card-restaurant" id="${id}"
    data-name="${name}" data-rating="${stars}" data-price="${price}" data-kitchen="${kitchen}">
    <img src="${image}" alt="image" class="card-image"/>
    <div class="card-text">
      <div class="card-heading">
        <h3 class="card-title">${name}</h3>
        <span class="card-tag tag">${timeOfDelivery} мин</span>
      </div>
      <div class="card-info">
        <div class="rating">
          ${stars}
        </div>
        <div class="price">От ${price} ₽</div>
        <div class="category">${kitchen}</div>
      </div>
    </div>
  </a>
  `;


  cardsRestaurants.insertAdjacentHTML('beforeend', card);

}

function createRestaurantMenu (dataset) {

  const restMenu = `
    <h2 class="section-title restaurant-title">${dataset.name}</h2>
    <div class="card-info">
      <div class="rating">
        ${dataset.rating}
      </div>
      <div class="price">От ${dataset.price} ₽</div>
      <div class="category">${dataset.kitchen}</div>
    </div>
  `;
  restaurantMenu.textContent="";
  restaurantMenu.insertAdjacentHTML ('beforeend', restMenu);

}

function createCardGood ({ id, name, ingredients:description, price, image }) {

  const card = document.createElement('div');
  card.className = 'card';
  card.insertAdjacentHTML('beforeend', `
    <img src="${image}" alt="image" class="card-image"/>
    <div class="card-text">
      <div class="card-heading">
        <h3 class="card-title card-title-reg">${name}</h3>
      </div>
      <div class="card-info">
        <div class="ingredients">
          ${description}
        </div>
      </div>
      <div class="card-buttons">
        <button class="button button-primary button-add-cart" id=${id}>
          <span class="button-card-text">В корзину</span>
          <span class="button-cart-svg"></span>
        </button>
        <strong class="card-price card-price-bold">${price} ₽</strong>
      </div>
    </div>
  `);
  cardsMenu.insertAdjacentElement ('beforeend', card);
}

function openGoods (event) {
  
  const target = event.target
  const restaurant = target.closest('.card-restaurant');

  if (!login) {
    toggleModalAuth ();
    return;
  }
  
  if (restaurant) {
    cardsMenu.textContent = '';
    containerPromo.classList.add('hide');
    restaurants.classList.add('hide');
    menu.classList.remove('hide');
    createRestaurantMenu(restaurant.dataset);
    getData(`${API_ADDRESS + restaurant.id}/`).then(function (data) {
      data.dishes.forEach(createCardGood);
    })
  }

}

function addToCart (event) {
  const target = event.target;
  const buttonAddToCard = target.closest('.button-add-cart');
  if (buttonAddToCard) {
    const card = target.closest ('.card');
    const title = card.querySelector ('.card-title-reg').textContent;
    const cost = card.querySelector ('.card-price').textContent;
    const id = buttonAddToCard.id;

    const food = cart.find (function (item){
      return item.id === id;
    })
    if (food) {
      food.count += 1;
    } else {
      cart.push({
        id,
        title,
        cost,
        count: 1
      });
    }
    localStorage.setItem('gloDeliveryCart', JSON.stringify (cart));

  }
}


function renderCart () {
  cartModalBody.textContent = ''; 
  cart.forEach(function ({ id, title, cost, count }) {
    const itemCart = `
      <div class="food-row">
        <span class="food-name">${title}</span>
        <strong class="food-price">${cost}</strong>
        <div class="food-counter">
          <button class="counter-button counter-minus" data-id="${id}">-</button>
          <span class="counter">${count}</span>
          <button class="counter-button counter-plus" data-id="${id}">+</button>
        </div>
      </div>
    `;
    cartModalBody.insertAdjacentHTML('beforeend', itemCart);
  });
  const totalPrice = cart.reduce (function (result, item){
    return result + parseFloat(item.cost) * item.count;
  }, 0);
  modalPricetag.textContent = totalPrice + " ₽";
  localStorage.setItem('gloDeliveryCart', JSON.stringify (cart));
}

function changeCount (event) {
  const target = event.target;

  if (target.classList.contains('counter-button')) {
    const food = cart.find(function (item){
      return item.id === target.dataset.id;
    });
    if (target.classList.contains('counter-minus')) {
      food.count--;
      if (food.count === 0) {
        cart.splice(cart.indexOf(food), 1);
      }
    };

    if (target.classList.contains('counter-plus')) food.count++;
    renderCart();
  }
}

function init () {

  getData(`${API_ADDRESS}restaurants/`).then(function (data) {
    data.forEach(createCardRestaurant);
    
  })
  
  cartButton.addEventListener("click", function (){
    renderCart ();   
    toggleModal();
  });
  
  close.addEventListener("click", toggleModal);

  cardsRestaurants.addEventListener ('click', openGoods);

  cardsMenu.addEventListener('click', addToCart);

  cartModalBody.addEventListener('click', changeCount);

  buttonClearCart.addEventListener ('click', function () {
    cart.length = 0;
    renderCart();
  })
  
  Array.from(document.querySelectorAll('.logo')).map(function (item) {
    item.addEventListener ('click', function () {
      containerPromo.classList.remove('hide');
      restaurants.classList.remove('hide');
      menu.classList.add('hide');
    })
  })
  
  checkAuth ();
  
  new Swiper ('.swiper-container', {
    loop: true,
    sliderPerView: 1,
  });
  

}

init ();