var socket = io();
socket.on('connect', function(){console.log("connected")});
socket.on('server:website', function(data) {
    console.log(data);
});
socket.on('disconnect', function(){});
