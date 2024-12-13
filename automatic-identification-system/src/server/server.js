const express = require('express');
const path = require('path');
const db = require('better-sqlite3')(path.join(__dirname, './db/books.sqlite'))

const app = express();

app.set('view engine', 'ejs');

app.use(express.static(path.join(__dirname, '../pages')));
app.use(express.static(path.join(__dirname, '../barcode')));


app.get('/_api/book/:barcodeId', (req, res) => {
  const book = db.prepare(`SELECT * FROM books where barcodeId = ${req.params.barcodeId}`).get()
  if (!book) {
    res.status(404).send('Book not found')
  } else {
    res.json(book)
  }
})

app.get('/book/:id', (req, res) => {
  const book = db.prepare(`SELECT * FROM books where bookId = '${req.params.id}'`).get()
  res.render(path.join(__dirname, '../pages/book/index.ejs'), book)
})


const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});