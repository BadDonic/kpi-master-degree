import WinkTokenizer from 'wink-tokenizer'
import {lemmatizer} from 'lemmatizer'
import {removeStopwords} from 'stopword'


const preprocess = (text) => {
  const tokenizer = new WinkTokenizer()
  const tokens = tokenizer.tokenize(text)
  const words = tokens
    .filter(token => token.tag === 'word')
    .map(token => token.value)
    .map(word => word.toLowerCase())
  const stopWordsRemoved = removeStopwords(words)
  const lemmatized = stopWordsRemoved.map(lemmatizer)
  return lemmatized
}

const buildInvertedIndex = (documents) => {
  return documents.reduce((invertedIndex, doc, index) => {
    doc.forEach(token => {
      if (invertedIndex[token]) {
        invertedIndex[token].add(index)
      } else {
        invertedIndex[token] = new Set([index])
      }
    })
    return invertedIndex
  }, {})
}

export const search = (text, documents) => {
  const preprocessedText = preprocess(text)
  const preprocessedDocuments = documents.map(preprocess)

  const invertedIndex = buildInvertedIndex(preprocessedDocuments)

  const allDocumentIndexes = documents.map((doc, index) => index)

  return preprocessedText.reduce((resultedIndexes, token) => {
    if (invertedIndex[token] && resultedIndexes.length !== 0) {
      return resultedIndexes.filter(index => invertedIndex[token].has(index))
    }

    return []
  }, allDocumentIndexes)
}
