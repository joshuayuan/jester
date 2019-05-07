from mpu6050 import mpu6050
import numpy as np
from sklearn import svm
import pickle
import time


class Predictor:

    def __init__(self):

        self.sensor1 = mpu6050(0x69)
        self.sensor2 = mpu6050(0x68)

        self.svm_model = None

    def load_model(self):
        pickle_fname = raw_input("Pickle file: ")
        svm_model = pickle.load(open(pickle_fname, "rb"))
        print("Done loading pickle file into model.")
        return svm_model

    def get_measurement(self):
        """
            gets manually called.
            returns numpy row array 1x6
        """
        accel1 = self.sensor1.get_accel_data();
        accel2 = self.sensor2.get_accel_data();
        row_str = str(accel1["x"]) + " " +  str(accel1["y"]) + " " + str(accel1["z"]) + " " + str(accel2["x"]) + " " + str(accel2["y"]) + " " + str(accel2["z"])

        row_list = [accel1["x"], accel1["y"], accel1["z"], accel2["x"], accel2["y"], accel2["z"]]
        return np.asarray([row_list])

    def get_steady_measurement(self):
        """
            includes while loop with delay to stream measurements from both imu.
            can call get_measurement function, and handles standard deviation
            returns measurement only when steady
        """

        # load 30 measurements, equals 3 seconds.
        data = self.get_measurement()
        for i in range(30):
            data = np.vstack((data, self.get_measurement()))
            time.sleep(.05)

        stds = np.std(data, axis=0)
        while True:
            success = 1 # 0 is fail.
            for s in stds:
                if s > 3:
                    success = 0
                    break
            if success == 1:
                return self.get_measurement()

            data = np.vstack((data, self.get_measurement()))
            data = np.delete(data, (0), axis=0)

            time.sleep(.05)

    def predict(self, model, point):
        return model.predict(point)


    def start(self):

        #load model
        # model = self.load_model()
        model = pickle.load(open("pickle_elnaz_model.sav", "rb"))

        while True:
            measurement = self.get_measurement()
            prediction = self.predict(model, measurement)
            print(prediction)
            print("Waiting 1 seconds now.")
            time.sleep(1)

