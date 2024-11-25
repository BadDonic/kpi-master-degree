export const draw2of5Barcode = (barcode, size) => {
  const narrowWidth = 3 * size;
  const lineHeight = 100 * size;
  const wideLineWidth = narrowWidth * 3;
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext("2d");

  let xPosition = 0;

  const N_COUNT = barcode.match(/N/g).length;
  const W_COUNT = barcode.match(/W/g).length;
  const S_COUNT = barcode.match(/S/g).length;

  canvas.width = N_COUNT * narrowWidth + W_COUNT * wideLineWidth + S_COUNT * narrowWidth;
  canvas.height = lineHeight;

  ctx.fillStyle = 'white'; // Or any desired color
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  barcode.split('S').forEach(part => {
    part.split('').forEach((code, index) => {
      const isBlack = index % 2 === 0;
      const isWide = code === 'W';
      const lineWidth = isWide ? wideLineWidth : narrowWidth;


      if (isBlack) {
        ctx.fillStyle = "black";
        ctx.fillRect(xPosition, 0, lineWidth, lineHeight);
      }

      xPosition += lineWidth;
    });

    xPosition += narrowWidth;
  })

  return canvas;
}
