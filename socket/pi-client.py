import socketio
import  predict

sio = socketio.Client()
pr = predict.Predictor()

@sio.on("connect")
def on_connect():
    print("I\'m Connected!")

@sio.on("message")
def on_message(data):
    print("I received a message: " + str(data))

@sio.on("disconnect")
def on_disconnect():
    print("I\'m Disonnected!")


if __name__ == "__main__":
    sio.connect("http://joshuayuan.me:8080")

    pr.start(sio)
    # sio.emit("pi:server", {"msg": "actually new message!"})
