let app=require('express')();
let http = require('http').Server(app);
let io = require('socket.io')(http);
var fs = require('fs');


app.get('/' , (req,res) =>{
		res.sendFile(__dirname+'/index.html');
})

http.listen(3000,() => {
	console.log('Connected');
})

io.sockets.on('connection' ,function(socket){
		console.log('there is a connection');

		socket.on('disconnect',() =>{
			console.log('Disconnected');

		})
		socket.on('creat', function(room) {

			console.log(room);
        	var dataf = fs.readFileSync('file.txt').toString().split("---");
			var i=0;
			var oldchats="";
			var rmn;
			for(i=0;i<dataf.length;i++){
			var splitString = dataf[i].split(",");
				if(splitString[0] === room){
					oldchats=splitString[2];
					rmn=splitString[1];
					break;
				}
			}
			console.log(oldchats);
			socket.join(room);
			io.sockets.emit('creat',{oldchat:oldchats,rn:rmn})

    	})

		socket.on('chat-message',(data)=>{
		var dataf = fs.readFileSync('file.txt','utf8').toString().split("---");
		var i=0;
		for(i=0;i<dataf.length;i++){
			var splitString = dataf[i].split(",");
			if(splitString[0] === data.rm)
				break;
			}
		
		dataf.splice(i, 1,data.rm+","+splitString[1]+","+dataf[i].substr(data.rm.length+splitString[1].length+2,dataf[i].length)+data.message+"##"+data.user+"#5#");
		var text = dataf.join("---");
		fs.writeFileSync('file.txt', text,'utf8');
		
			socket.to(data.rm).emit('chat-message',(data))			
		})
		socket.on('typing',(data)=>{
			socket.to(data.rm).emit('typing',(data))
		})
		socket.on('stoptyping',(data)=>{
			socket.to(data.rm).emit('stoptyping',(false))
		})
		socket.on('joined',(data)=>{
			socket.to(data.rm).emit('joined',(data))
		})
		socket.on('left',(data)=>{
			socket.to(data.rm).emit('left',(data))
		})
})

