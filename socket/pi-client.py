import socketio

sio = socketio.Client()

@sio.on("connect")
def on_connect():
    print("I\'m Connected!")
@sio.on("message")
def on_message(data):
    print("I received a message: " + str(data))
@sio.on("my message")
def on_message(data):
    print("I received a custom message: " + str(data))
@sio.on("disconnect")
def on_disconnect():
    print("I\'m Disonnected!")


