import itertools

def tupleToString(tup):
    stringCopy = ""

    for obj in tup:
        stringCopy += obj
    
    return stringCopy

class TrieNode(): 
    def __init__(self): 
          
        # Initialising one node for trie 
        self.children = {} 
        self.last = False
        self.hits = 0
  
class Trie(): 
    def __init__(self): 
          
        # Initialising the trie structure. 
        self.root = TrieNode() 
        self.word_list = [] 
        self.lastSuggestion = []
    
    def getData(self, filePath):
        fileObject = open(filePath, "r")
        fileObject.seek(0)
        data = []

        for index, line in enumerate(fileObject):
            line = line.strip()
            if line:
                data.append((str(line), index))
            
        return data
  
    def formTrie(self, filePath):
        keys = self.getData(filePath)

        for key, hits in keys: 
            self.insert(key, hits) # inserting one key to the trie. 
  
    def insert(self, key, hits): 
           
        node = self.root 
  
        for a in list(key): 
            if not node.children.get(a): 
                node.children[a] = TrieNode() 
  
            node = node.children[a] 
  
        node.last = True
        node.hits = hits

    def updateHits(self, word):
        node = self.root 
        found = True
  
        for a in list(word): 
            if not node.children.get(a): 
                found = False
                break
  
            node = node.children[a]

        node.hits -= 10 # Giving word a higher ranking
        self.lastSuggestion = [] #clearing suggestion list

    def search(self, key): 
        # Checking if word is present in trie
        node = self.root 
        found = True
  
        for a in list(key): 
            if not node.children.get(a): 
                found = False
                break
  
            node = node.children[a] 
  
        return node and node.last and found 
  
    def suggestionsRec(self, node, word): 
        # recursively looks for word and when reached the end of branch, adds word to list
        if node.last: 
            self.word_list.append((word, node.hits)) 
           
        for a,n in node.children.items(): 
            self.suggestionsRec(n, word + a) 
    

    def cartesianProduct(self, charArr):
        result = list(itertools.product(*charArr))
        return result

    def quickSuggest(self, word):
        # optimization to look for word in previous suggestion rather than full trie
        for (wordSuggestion, hits) in self.lastSuggestion:
            if wordSuggestion.startswith(word):                    
                self.word_list.append((wordSuggestion, hits))
        
        return

    def topResults(self, suggestions):
        
        #function to return top 8 values
        suggestions.sort(key=lambda tup: tup[1])
        results = []

        if(len(suggestions) > 8):
            for i in range(0,8):
                results.append(suggestions[i][0])
        else:
            for word, hits in suggestions:
                results.append(word)

        return results

    def predict(self, key):
        # Looks at last suggestion if word is >= than 3
        if(len(key) >= 3 and self.lastSuggestion != []):
            words = self.cartesianProduct(key)
            for option in words:
                word = tupleToString(option)
                self.quickSuggest(word) 
            
            top = self.topResults(self.word_list)
            self.lastSuggestion = self.word_list
            self.word_list = []

            return top

        # Traverses trie if word is less than 3 
        words = self.cartesianProduct(key)
        for option in words:
            word = tupleToString(option)

            node = self.root 
            not_found = False
            temp_word = '' 
    
            for a in list(word): 
                if not node.children.get(a): 
                    not_found = True
                    break
    
                temp_word += a 
                node = node.children[a] 
    
            if not_found: 
                continue
            elif node.last and not node.children: 
                continue
  
            self.suggestionsRec(node, temp_word) 
  
        
        top = self.topResults(self.word_list)
        self.lastSuggestion = self.word_list
        self.word_list = []

        return top
    




# creating trie object 
t = Trie() 

# Filling trie 
t.formTrie("./data/google-10000-english.txt") 
  

# #Getting a suggestion (returns empty array if no suggestions found)
# t.predict([['u', 'u', 'u'], ['u', 'u', 'u']])

# # Updating hits with selected word
# t.updateHits("help")





