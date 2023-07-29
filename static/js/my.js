// get elements for popup

const popupbtn = document.querySelector('.popupbtn');

const popup = document.querySelector('.popup-wrapper');

const popupclose = document.querySelector('.popup-close');

// popup

popupbtn.addEventListener('click',() =>{

    popup.style.display = "block";

    console.log("opening modal");

});

popupclose.addEventListener('click', () => {

    popup.style.display = 'none';

});

popup.addEventListener('click', (e) => {

    if(e.target.className === 'popup-wrapper'){

      popup.style.display = 'none';

    }

});


// Get the button that opens the modal
var btn = document.querySelector('.popupbtn-acc');

// Get the modal
var modal = document.querySelector('#add-account-popup');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("popup-close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}




const expensePopupBtn = document.querySelector('.add-expense-acc');
const expensePopup = document.querySelector('#add-expense-popup');
const expensePopupClose = expensePopup.querySelector('.popup-close');

expensePopupBtn.addEventListener('click',() => {
    expensePopup.style.display = "block";
    console.log("opening expense modal");
});

expensePopupClose.addEventListener('click', () => {
    expensePopup.style.display = 'none';
});

expensePopup.addEventListener('click', (e) => {
    if(e.target.className === 'popup-wrapper'){
      expensePopup.style.display = 'none';
    }
});


const expenseCategoryPopupBtn = document.querySelector('.add-expense-category-button');
const expenseCategoryPopup = document.querySelector('#add-expense-category-popup');
const expenseCategoryPopupClose = expenseCategoryPopup.querySelector('.popup-close');

expenseCategoryPopupBtn.addEventListener('click',() => {
    expenseCategoryPopup.style.display = "block";
    console.log("opening expense category modal");
});

expenseCategoryPopupClose.addEventListener('click', () => {
    expenseCategoryPopup.style.display = 'none';
});

expenseCategoryPopup.addEventListener('click', (e) => {
    if(e.target.className === 'popup-wrapper'){
      expenseCategoryPopup.style.display = 'none';
    }
});


