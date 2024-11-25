export const drawBarcode = (barcode, size) => {
  const lineWidth = 5 * size;
  const lineHeight = 100 * size;
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext("2d");

  canvas.width = barcode.length * lineWidth;
  canvas.height = lineHeight;

  let xPosition = 0;

  for (let bit of barcode) {
    if (bit === "1") {
      ctx.fillStyle = "black";
      ctx.fillRect(xPosition, 0, lineWidth, lineHeight);
    }

    xPosition += lineWidth;
  }

  return canvas;
}
