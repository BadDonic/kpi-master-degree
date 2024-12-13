import {START_CODE, STOP_CODE, digitEncodingMap} from "./encode2And5MatrixBarcode.js";


const codeToDigitsMap = Object.entries(digitEncodingMap).reduce((acc, [digit, code]) => {
  acc[code] = digit;
  return acc;
}, {})

export const mapPixelsToBarcode = (pixels) => {
  let colorCode = ''
  for (let i = 0; i < pixels.length; i += 4) {
    const r = pixels[i];
    const g = pixels[i + 1];
    const b = pixels[i + 2];
    const a = pixels[i + 3];

    if (r === 0 && g === 0 && b === 0) {
      colorCode += 'B';
    }

    if (r === 255 && g === 255 && b === 255) {
      colorCode += 'W';
    }

  }

  const trimmedMatches = getMatches(colorCode);

  if (!trimmedMatches) {
    return 'Invalid barcode';
  }

  const {wideLength, narrowLength, matches} = findLongestSequence(trimmedMatches);

  let barcode = '';

  for (let i = 0; i < matches.length; i++) {
    const match = matches[i];
    const isWide = match.length === wideLength;
    const isNarrow = match.length === narrowLength;
    const isSeparator = (i + 1) % 6 === 0;

    if (isSeparator) {
      if (isNarrow) {
        barcode += 'S';
      } else {
        return 'Invalid barcode';
      }
    } else {
      if (isWide) {
        barcode += 'W';
      } else if (isNarrow) {
        barcode += 'N';
      } else {
        return 'Invalid barcode';
      }
    }
  }


  const [start, ...value]= barcode.split('S')
  const stop = value.pop()

  if (start !== START_CODE || stop !== STOP_CODE) {
    return 'Invalid barcode';
  }

  return value.map(code => codeToDigitsMap[code]).join('');
}


function findLongestSequence(matches) {
  let longestSequence = matches.reduce((longest, current) => {
    return current.length > longest.length ? current : longest;
  }, matches[0]);

  let shortestSequence = matches.reduce((shortest, current) => {
    return current.length < shortest.length ? current : shortest;
  }, matches[0]);

  return {
    wideLength: longestSequence.length,
    narrowLength: shortestSequence.length,
    matches,
  };
}

function getMatches(code) {
  const matches = code.match(/(B+|W+)/g);


  if (matches?.[0]?.[0] === 'W') {
     matches.shift();
  }

  if (matches?.[matches.length - 1]?.[0] === 'W') {
    matches.pop();
  }
  return matches;
}
