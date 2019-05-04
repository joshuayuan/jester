On the Pi:

1. clone this repo
2. cd jester_pi
3. python stream_data.py
- type in your file name to save data to
4. record data for however many data points you want (maybe several hundred at the least. Keep your arm as still as possible (think of the acceleration vectors in x y and z)
5. ctrl + c to exit the program and repeat as much as you want
6. Now upload your files to the google colab
7. run through the program and train the svm. 
6. Now back here, run python get_data_point.py
9. Type this into the colab model.predict([...]) and see if it predicts the correct gesture!
