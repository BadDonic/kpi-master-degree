export const digitEncodingMap = {
  '0': 'NNWWN',
  '1': 'WNNNW',
  '2': 'NWNNW',
  '3': 'WWNNN',
  '4': 'NNWNW',
  '5': 'WNWNN',
  '6': 'NWWNN',
  '7': 'NNNWW',
  '8': 'WNNWN',
  '9': 'NWNWN',
};

export const START_CODE = 'WNNNN'
export const STOP_CODE = 'WNNNN'

export const encode2And5MatrixBarcode = (data) => {
  if (!/^\d+$/.test(data)) {
    throw new Error("Data for a 2 of 5 Matrix barcode must be numeric.");
  }

  const encodedValue = data.split('').map(digit => digitEncodingMap[digit]).join('S')

  return `${START_CODE}S${encodedValue}S${STOP_CODE}`;
}
