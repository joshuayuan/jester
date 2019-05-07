from mpu6050 import mpu6050
import numpy as np
from sklearn import svm
import pickle
import time


sensor1 = mpu6050(0x69)
sensor2 = mpu6050(0x68)

svm_model = None

def load_model():
    pickle_fname = raw_input("Pickle file: ")
    svm_model = pickle.load(open(pickle_fname, "rb"))
    print("Done loading pickle file into model.")
    return svm_model

def get_measurement():
    """
        gets manually called.
        returns numpy row array 1x6
    """
    accel1 = sensor1.get_accel_data();
    accel2 = sensor2.get_accel_data();
    row_str = str(accel1["x"]) + " " +  str(accel1["y"]) + " " + str(accel1["z"]) + " " + str(accel2["x"]) + " " + str(accel2["y"]) + " " + str(accel2["z"])

    row_list = [accel1["x"], accel1["y"], accel1["z"], accel2["x"], accel2["y"], accel2["z"]]
    return np.asarray([row_list])

def get_steady_measurement():
    """
        includes while loop with delay to stream measurements from both imu.
        can call get_measurement function, and handles standard deviation
        returns measurement only when steady
    """

    # load 30 measurements, equals 3 seconds.
    data = get_measurement()
    for i in range(30):
        data = np.vstack((data, get_measurement()))
        time.sleep(.1)

    stds = np.std(data, axis=0)
    while True:
        success = 1 # 0 is fail.
        for s in stds:
            if s > 1:
                success = 0
                break
        if success == 1:
            return get_measurement()

        data = np.vstack((data, get_measurement()))
        data = np.delete(data, (0), axis=0)

        time.sleep(.1)

def predict(model, point):
    return model.predict(point)


def main():

    #load model
    model = load_model()

    while True:
        prediction = predict(model, get_steady_measurement())
        print(prediction)
        print("Waiting 3 seconds now.")
        time.sleep(3)

if __name__ == "__main__":
    main()
