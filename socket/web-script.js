var socket = io();
socket.on('connect', function(){console.log("connected")});
socket.on('server:website', function(data) {
    // console.log(data);
    var code = data.code;
    var name = data.name;
    $("#gesture").text(name.substring(0, name.length - 4));

    $("img").hide();
    $("#image" + code).show();
});
socket.on('disconnect', function(){});
