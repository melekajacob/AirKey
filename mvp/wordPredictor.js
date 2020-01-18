// Javascript analog of word predictor (will use module.export to export function)

// Requiring dependencies
const AhoCorasick = require("aho-corasick-node");
var fs = require("fs");
var checkWord = require("check-word");
words = checkWord("en");

// Cartesian product helper function
function cartesianProduct(arr) {
  return arr.reduce(
    function(a, b) {
      return a
        .map(function(x) {
          return b.map(function(y) {
            return x.concat(y);
          });
        })
        .reduce(function(a, b) {
          return a.concat(b);
        }, []);
    },
    [[]]
  );
}

// Building aho corasick
function buildTrie(filePath) {
  arr = [];
  const builder = AhoCorasick.builder();

  var fs = require("fs");
  var array = fs
    .readFileSync(filePath)
    .toString()
    .split("\n");

  array.forEach(word => builder.add(word));

  const ac = builder.build();
  return ac;
}

function charArrToString(arr) {
  str = "";
  arr.forEach(chars => {
    str += chars.join("");
    str += " ";
  });
  return str;
}

function predict(wordInput, ac) {
  wordList = [];
  // Get all possible letter combinations
  possibleWords = cartesianProduct(wordInput);

  // Check if present in dictionary
  for (var i = 0; i < possibleWords.length; ++i) {
    possibleWord = possibleWords[i].join("");
    if (words.check(possibleWord)) {
      match = ac.match(possibleWord);

      if (match[0] != "") {
        wordList.push(possibleWord);
      }
    }
  }

  // return values in order of prevalence, returns empty array if nothing present
  return [...new Set(wordList)];
}

// Working on autocomplete
function autocomplete(partialWord) {}

module.exports = {
  buildTrie: buildTrie,
  wordPredictor: predict
};
