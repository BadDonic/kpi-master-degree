export const fetchBookByBarcode = async (barcode) => {
  const response = await fetch(`/_api/book/${barcode}`).catch(() => null);
  if (!response || !response.ok) {
    return null;
  }else {
    const book = await response.json();
    return book;
  }
}