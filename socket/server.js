var express = require("express");
var app = express();
var server = require("http").Server(app);
var io = require("socket.io")(server);

server.listen(8080, () => {console.log("website connected at port 8080")});

app.use(express.static('web'));
app.get('/', function(req, res) {
    res.sendFile(__dirname + "/index.html");
});
app.get('/web-script.js', function(req, res) {
    res.sendFile(__dirname + "/web-script.js");
});
app.get('/jquery.js', function(req, res) {
    console.log("wut");
    res.sendFile(__dirname + "/lib/jquery.min.js");
});

io.on("connection", function(socket) {
    console.log("a client connected");
    socket.on("pi:server", (data) => {
        console.log("server received from pi: " + data.msg);
        io.emit("server:website", data);
    });
});
