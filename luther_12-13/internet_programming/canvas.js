drawit = function(){
	canvas = document.getElementById('mycanvas')
	canvas.width = canvas.width //This is just a really fast way to clear the canvas
	ctx = canvas.getContext("2d")
	// ctx.fillStyle = "red"
	// ctx.fillRect(boxx,boxy,150,100)
	// ctx.beginPath();
	// ctx.moveTo(25,250);
	// ctx.bezierCurveTo(25,500,475,500,475,250);
	// ctx.moveTo(25,250);
	// ctx.bezierCurveTo(25,0,475,0,475,250);
	// ctx.stroke();
	drawClock(ctx);
}

function drawClock(ctx) {
	setTimeout('drawClock(ctx)',1000);
	canvas.width = canvas.width
	ctx.translate(250,250);
	ctx.fillRect(-5,-165,10,30)
	for (i = 0; i < 12; i++) {
		ctx.rotate(30*Math.PI/180);
		ctx.fillRect(-5,-165,10,30);
	}

	ctx.fillRect(-1,-155,2,20)
	for (i = 0; i < 60; i++) {
		ctx.rotate(6*Math.PI/180)
		ctx.fillRect(-1,-160,2,20)
	}
	

	drawHands(ctx);
}

function drawHands(ctx) {
	var date = new Date()

	ctx.save()
	ctx.fillStyle = "black"
	ctx.rotate(date.getMinutes()*6*Math.PI/180);
	ctx.fillRect(-3,3,6,-160)
	ctx.restore()

	var hourRotate = (date.getHours()%12) + (date.getMinutes()/60);
	ctx.save()
	ctx.rotate(hourRotate*30*Math.PI/180);
	ctx.fillRect(-4,4,8,-80)
	ctx.restore()

	ctx.save()
	ctx.fillStyle = "red"
	ctx.rotate(date.getSeconds()*6*Math.PI/180);
	ctx.fillRect(-2,2,4,-160)
	ctx.restore()
}

drawit();