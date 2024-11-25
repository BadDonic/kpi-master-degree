import {mapPixelsToBarcode} from "./mapPixelsToBarcode.js";

const fileInput = document.getElementById('fileInput');
const canvas = document.getElementById('canvas');
const resultElement = document.getElementById('result');
const ctx = canvas.getContext('2d');

fileInput.addEventListener('change', (event) => {
  const file = event.target.files[0];

  if (file) {
    const reader = new FileReader();

    reader.onload = (e) => {
      const img = new Image();
      img.onload = () => {

        const imgWidth = img.naturalWidth;
        const imgHeight = img.naturalHeight;

        canvas.width = imgWidth;
        canvas.height = imgHeight;

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

        const imageData = ctx.getImageData(0, Math.floor(canvas.height / 2), canvas.width, 1);
        const pixels = imageData.data

        const barcode = mapPixelsToBarcode(pixels);
        resultElement.innerHTML = `Decoded value: ${barcode}`;
      };
      img.src = e.target.result;
    };

    reader.readAsDataURL(file);
  }
});
