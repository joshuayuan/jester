from mpu6050 import mpu6050
import numpy as np
from sklearn import svm
import pickle


sensor1 = mpu6050(0x69)
sensor2 = mpu6050(0x68)

def get_measurement():
    """
        returns numpy row array 1x6
    """
    accel1 = sensor1.get_accel_data();
    accel2 = sensor2.get_accel_data();
    row_str = str(accel1["x"]) + " " +  str(accel1["y"]) + " " + str(accel1["z"]) + " " + str(accel2["x"]) + " " + str(accel2["y"]) + " " + str(accel2["z"])

    row_list = [accel1["x"], accel1["y"], accel1["z"], accel2["x"], accel2["y"], accel2["z"]]
    return np.asarray([row_list])


def main():

    #load model
    pickle_fname = "pickle_svm_model.sav"
    svm_model = pickle.load(open(pickle_fname, "rb"))

    while True:
        keyword = raw_input("Press enter to get prediction.")
        if keyword == "":
            measurement = get_measurement()
            prediction = svm_model.predict(measurement)
            print("From " + str(measurement) + " we predict " + str(prediction))


