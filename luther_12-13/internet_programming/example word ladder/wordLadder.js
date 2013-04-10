Stack = function(){
    this.Stack = new Array();
}
Stack.prototype.push = function(x){

        this.Stack.push(x);
    }
Stack.prototype.pop = function(){

        return this.Stack.pop();

    }
Stack.prototype.isEmpty = function(){

        return (this.Stack.length == 0);
    
    }
Stack.prototype.size = function(){
	return this.Stack.length;
}
Stack.prototype.aCopy = function(){
	return this.Stack.slice(0);
}
Stack.prototype.getCopy= function(item){
	this.Stack = item;
}

Queue = function(){

   this.Queue = new Array();
}
Queue.prototype.enqueue = function(x){

       this.Queue.push(x);

   }

Queue.prototype.dequeue = function(){

       item = this.Queue.shift();
	   return item;

   }
  
Queue.prototype.isEmpty = function(){

        return (this.Queue.length == 0);
    
    }
Queue.prototype.size = function(){
	return this.Queue.length;
}



Set = function(){
	
	this.Set = new Array();
}	
Set.prototype.contains= function(object){
		
		return (this.Set.indexOf(object)!=-1);
	}
	
Set.prototype.add = function(object){
		
		this.Set.push(object);
	}
	
function checkIt(){
	var lArray = new Array();
	lArray.three=3;
	lArray.four=4;
	lArray.five=5;
	var wordLength = document.getElementById("wordLength").options[document.getElementById("wordLength").selectedIndex].value;
	var startWord = document.getElementById("startWord").value;
	var endWord = document.getElementById("endWord").value;
	var table = document.getElementById('wordTable');
	if (wordLength =="three"){
		wordArray = threeLetterWords;
	}
	else if (wordLength =="four"){
		wordArray = fourLetterWords;
	}
	else{
		wordArray = fiveLetterWords;
	}
	for (i=table.rows.length-1; i>-1;i--){
		table.deleteRow(i);
	}
	if (startWord.length != lArray[wordLength] || endWord.length != lArray[wordLength]){
		alert("Your words are the incorrect length")
	}
	else if (wordArray.indexOf(endWord)==-1){
		alert("Your end word is not in the dictionary!")
		}
	else if (wordArray.indexOf(startWord)==-1){
		alert("Your start word is not in the dictionary!")
	}
	else{
		wordIt(wordArray);
	}
}

function wordIt(wordArray){
	var queue = new Queue();
	var usedList = new Set();
	var alphabet = "abcdefghijklmnopqrstuvwxyz";
	var found = false;
	
	var startWord = document.getElementById("startWord").value;
	var endWord = document.getElementById("endWord").value;
	var wordLength = document.getElementById("wordLength").options[document.getElementById("wordLength").selectedIndex].value;
	var mystack = new Stack();
	mystack.push(startWord);
	usedList.add(startWord);
	queue.enqueue(mystack);
		while (!queue.isEmpty() && found==false){
			var stack = queue.dequeue();
			var word = stack.pop();
			for (i=0; i<word.length;i++){
                for (var ch = 'a'.charCodeAt(0); ch <= 'z'.charCodeAt(0); ch++){
					var newWord= word.slice(0,i) + String.fromCharCode(ch) + word.slice(i+1);
				
					if (wordArray.indexOf(newWord)!=-1 && !usedList.contains(newWord)){
					
						if (newWord!=endWord){
							var aStack = new Stack();
							aStack.getCopy(stack.aCopy());
							aStack.push(word);
							aStack.push(newWord);
							queue.enqueue(aStack);
							usedList.add(newWord);
						}
						else{
							found = true
							stack.push(word);
							stack.push(newWord);
							tableIt(stack);
						}
					}
					
		    	}
	  		}
	if (queue.isEmpty() && found==false){
		alert("Ladder can not be made.");
	}
}
	
function tableIt(stack){
	var table = document.getElementById('wordTable');
	while (stack.size()>0){
		var rowNum=table.rows.length;
		var row = table.insertRow(rowNum);
		var cell = row.insertCell(0);
		var temp = stack.pop();
		cell.innerHTML = temp;
	}
}	
	
	
	
	
	
	
	
	
}
