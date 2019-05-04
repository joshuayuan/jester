from mpu6050 import mpu6050
import time

sensor1 = mpu6050(0x69)
sensor2 = mpu6050(0x68)

fname = raw_input("File name: ")
file = open(fname, "w")
counter = 0
print("Beginning in 5...")
time.sleep(1)
print("Beginning in 4...")
time.sleep(1)
print("Beginning in 3...")
time.sleep(1)
print("Beginning in 2...")
time.sleep(1)
print("Beginning in 1...")
time.sleep(1)
print("Starting.")
while True:
    try:
        accel1 = sensor1.get_accel_data();
        accel2 = sensor2.get_accel_data();
        row = [accel1["x"], accel1["y"], accel1["z"], accel2["x"], accel2["y"], accel2["z"]]
        row_str = str(accel1["x"]) + " " +  str(accel1["y"]) + " "  + str(accel1["z"]) + " " + str(accel2["x"]) + " " + str(accel2["y"]) + " " + str(accel2["z"])
        print(str(counter) + ": " + row_str)
        file.write(row_str + "\n")
    except IOError as e:
        print("Got error: " + str(e))
    time.sleep(.1);
    counter += 1
