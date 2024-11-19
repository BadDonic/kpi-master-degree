import {news} from './documents.js'
import {search} from './search.js'


const query = 'New Hope'

const docIndexes = search(query, news)

if (docIndexes.length === 0) {
  console.log(`Query '${query}' is not found in any news`)
} else {
  console.log(`Query '${query}' is found in news: ${docIndexes.join(',')}`)
}
