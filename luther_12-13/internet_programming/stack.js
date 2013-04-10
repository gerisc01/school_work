//Stack class
function Stack() {
    this.stack = new Array();
    this.push  = push; 
    this.pop   = pop;
    this.print = show;
    this.size = size;
    this.clone = clone;
}

function push(data) {
    this.stack.push(data);
}

function pop() {
    return this.stack.pop();
}

function show() {
    return this.stack;
}

function size() {
    return this.stack.length;
}

function clone() {
    var newStack = new Stack();
    newStack.stack = this.stack.slice(0);
    return newStack;
}


//Queue class (reusing some stack functions)
function Queue() {
    this.stack = new Array();
    this.enqueue = push;
    this.dequeue = dequeue;
    this.print = show;
    this.size = size;
}

function dequeue() {
    return this.stack.shift()
}



//The set that will be used to contain used words
function Set() {
    this.set = new Array();
    this.add = add;
    this.contains = contains;
    this.print = print;
}

function add(data) {
    this.set.push(data);
}

function contains(item) {
    var index = this.set.indexOf(item)
    if (index == -1) {
        return false
    } else {
        return true
    }
}

function print() {
    return this.set;
}

function prettyPrint(array) {
    var str = "";
    while (array.length != 0) {
        str = str + array.pop() + "<br><br>"
    }
    return str
}



function checkWord(word, length) {
    //Checking if the word is in the dictionary
    if (length == 3) {
        if (threeLetterWords.indexOf(word) == -1)
            return false
        else
            return true
    }
    else if (length == 4) {
        if (fourLetterWords.indexOf(word) == -1)
            return false
        else
            return true
    }
    else if (length == 5) {
        if (fiveLetterWords.indexOf(word) == -1)
            return false
        else
            return true
    }
    else { //Just making sure we don't get anything but 3,4,5 letter words
        return false
    }
}



function createList(start, end, length) {
    if (checkWord(start, length) == false) {
        alert("Bad starting word")
        return false;
    }
    if (checkWord(end, length) == false) {
        alert("Bad ending word")
        return false;
    }

    var found = false;
    var set = new Set();
    var startStack = new Stack();
    var queue = new Queue();
    set.add(start);
    startStack.push(start);
    queue.enqueue(startStack);
    
    //choose word array
    if (length == 3) {
        wordArray = threeLetterWords;
    }
    if (length == 4) {
        wordArray = fourLetterWords;
    }
    if (length == 5) {
        wordArray = fiveLetterWords;
    }

    while (queue.size() != 0 && found==false){
            var stack = queue.dequeue();
            var word = stack.pop();
            relWords = findWords(word, length, stack, queue)

            var loopLen = relWords.length;
            for (i = 0; i < loopLen; i++) {
                    var newWord = relWords[i];
                    if (wordArray.indexOf(newWord)!=-1 && !set.contains(newWord)){
                        if (newWord!=end){
                            var newStack = stack.clone()
                            newStack.push(word);
                            newStack.push(newWord);
                            queue.enqueue(newStack);
                            set.add(newWord);
                        }
                        else{
                            found = true
                            stack.push(word);
                            stack.push(newWord);
                            document.getElementById('myDiv').innerHTML = prettyPrint(stack.print())
                        }
                    }
                    
                }
            }
    if (queue.size() == 0 && found==false){
        alert("Ladder can not be made.");
    }
}



function findWords(word, length, stack, queue) {
    var currentStack = stack;
    var stackQueue = queue;
    var possibleWords = new Array();
    for (i = 0; i < length; i++) {
        for (j = 0; j < alphabet.length; j++) {
            if (word[i] != alphabet[j]) {
                var newWord = word.substr(0,i) + alphabet[j] + word.substr(i+1,word.length)
                possibleWords.push(newWord);
            }
        }
    }

    var l = possibleWords.length;
    var correctWords = new Array();
    for (i = 0; i < l; i++) {
        var tmp = possibleWords.pop();
        if (checkWord(tmp,length) != false) {
            correctWords.push(tmp);
        }   
    }
    return correctWords
}

function clearList() {
    document.getElementById('myDiv').innerHTML = " ";
}

function startWordLadder() {
    var start = document.getElementById("startWord").value;
    var end = document.getElementById("endWord").value;
    var length = document.getElementById("word_length").options[document.getElementById("word_length").selectedIndex].value;
    createList(start,end,length)
}