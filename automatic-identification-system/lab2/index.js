import {encode2And5MatrixBarcode} from "./encode2And5MatrixBarcode.js";
import {drawBarcode} from "./drawBarcode.js";

document.getElementById('symbology').addEventListener('change', render);
document.getElementById('data').addEventListener('input', render);
document.getElementById('size').addEventListener('change', render);

function render() {
  const symbology = document.getElementById('symbology').value;
  const data = document.getElementById('data').value;
  const size = document.getElementById('size').value;

  document.getElementById('barcode').innerHTML = '';

  if (data.trim() === '') {
    return;
  }

  let barcode;

  if (symbology === '2/5 Matrix Code') {
    barcode = encode2And5MatrixBarcode(data);
  }

  const canvas = drawBarcode(barcode, size);
  document.getElementById('barcode').appendChild(canvas);
}

render();
