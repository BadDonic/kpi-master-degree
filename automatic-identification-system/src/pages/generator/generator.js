import {encode2And5MatrixBarcode} from "../barcode/encode2And5MatrixBarcode.js";
import {draw2of5Barcode} from "../barcode/drawBarcode.js";

document.getElementById('symbology').addEventListener('change', render);
document.getElementById('data').addEventListener('input', render);
document.getElementById('size').addEventListener('change', render);

function render() {
  const symbology = document.getElementById('symbology').value;
  const data = document.getElementById('data').value;
  const size = document.getElementById('size').value;

  const barcodeElement = document.getElementById('barcode');
  const errorElement = document.getElementById('errorMessage');

  barcodeElement.innerHTML = '';
  errorElement.innerHTML = '';

  if (data.trim() === '') {
    return;
  }



  try {
    if (symbology === '2/5 Matrix Code') {
      const barcode = encode2And5MatrixBarcode(data);
      const canvas = draw2of5Barcode(barcode, size);
      barcodeElement.appendChild(canvas);
      barcodeElement.appendChild(createExportButton(canvas));
    }
  } catch (e) {
    errorElement.innerHTML = e.message;
    return;
  }
}

function createExportButton(canvas) {
  const exportButton = document.createElement('button');
  exportButton.id = 'exportButton';
  exportButton.innerHTML = 'Export';
  exportButton.addEventListener('click', () => {
    const dataUrl = canvas.toDataURL();
    const a = document.createElement('a');
    a.href = dataUrl;
    a.download = 'barcode.png';
    a.click();
  });

  return exportButton;
}

render();
