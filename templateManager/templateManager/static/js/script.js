
const images = document.querySelectorAll('img');
const popup = document.querySelector('.popup');
const popupImage = popup.querySelector('img');
const close = popup.querySelector('.close');
const bodyTag = document.getElementsByTagName("body")

// Open popup and display clicked image
function openPopup(imageSrc) {
  popupImage.src = imageSrc;
  popup.style.display = 'block';
}

// Close popup when clicking on close button or outside the popup
function closePopup() {
  popup.style.display = 'none';
}

images.forEach(image => {
  // Add click event listener to each image
  image.addEventListener('click', () => {
    openPopup(image.src);
  });
});

close.addEventListener('click', closePopup);
popup.addEventListener('click', closePopup);
popupImage.addEventListener('click', event => {
  event.stopPropagation();
});


