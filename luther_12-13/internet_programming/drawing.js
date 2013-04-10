var boxx = 50;
var boxy = 50;

drawit = function(){
	canvas = document.getElementById('mycanvas')
	canvas.width = canvas.width //This is just a really fast way to clear the canvas
	ctx = canvas.getContext("2d")
	ctx.fillStyle = "red"
	boxx += 2
	boxy += 2
	ctx.fillRect(boxx,boxy,150,100)

}

myMouse = function(evt) {
	console.log(evt)
	canvas = document.getELementById('mycanvas')
	ctx = canvas.getContext("2d")
	ctx.beginPath()
	ctx.arc(evt.offsetX,evt.offsetY,10,0,2*3.1415)
	ctx.stroke()
}

press = function(evt) {
	console.log(evt.keyCode)
	if (evt.keyCode == 27) {
	  canvas = document.getElementBy('mycanvas')
	}
}
