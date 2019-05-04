from mpu6050 import mpu6050
import time

sensor1 = mpu6050(0x69)
sensor2 = mpu6050(0x68)

accel1 = sensor1.get_accel_data();
accel2 = sensor2.get_accel_data();
row = [accel1["x"], accel1["y"], accel1["z"], accel2["x"], accel2["y"], accel2["z"]]
row_str = str(accel1["x"]) + " " +  str(accel1["y"]) + " "  + str(accel1["z"]) + " " + str(accel2["x"]) + " " + str(accel2["y"]) + " " + str(accel2["z"])
print(row_str)
