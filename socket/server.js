var express = require("express");
var app = express();
var server = require("http").Server(app);
var io = require("socket.io")(server);

server.listen(8080, () => {console.log("website connected at port 8080")});

app.use(express.static('web'));
express.static.mime.define({'text/css': ['css']});
app.get('/', function(req, res) {
    res.sendFile(__dirname + "/index.html");
});
app.get('/web-script.js', function(req, res) {
    res.sendFile(__dirname + "/web-script.js");
});
app.get('/jquery.js', function(req, res) {
    res.sendFile(__dirname + "/lib/jquery.min.js");
});
app.get('/normalize.css', function(req, res) {
    res.sendFile(__dirname + "/normalize.css");
});
app.get('/skeleton.css', function(req, res) {
    res.sendFile(__dirname + "/skeleton.css");
});
app.get('/custom.css', function(req, res) {
    res.sendFile(__dirname + "/custom.css");
});

var old_code = -1;
io.on("connection", function(socket) {
    console.log("a client connected");
    socket.on("pi:server", (data) => {
        if (data.code != old_code) {
            console.log("server received from pi: " + data.code);
            io.emit("server:website", data);
            old_code = data.code;
        }
    });
    socket.on("disconnect", () => {
        console.log("client disconnected");
        old_code = -1;
    });
});
