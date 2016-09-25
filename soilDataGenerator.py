import serial
import os
import time
import datetime
import sys
import pdb

''' 
listens to arduino and reads the serial data
prints the serial data to a csv file
'''


def getSerialObject(port):
    try:
        arduino = serial.Serial(port, 9600, timeout=1)
        return arduino
    except(serial.SerialException):
        print("Arduino device cannot be found at port {}\n".format(port))
        time.sleep(10)

def getData(arduino):
    # the last bit gets rid of new-line chars/empty data
    data = arduino.readline()[:-2]
    return data

#not good i think
def checkIfWateredRecently(data):
    if data == "watered\n" or data == "watered":
        # reset timer
        global start
        start = datetime.datetime.now()

def printSerialToFile(data, file):
    # open and close repeatedly, in order to get an updated file to upload to
    # server
    f = open(file, 'a')

    # if data exists
    if data:
        # print(data.decode('utf-8')) #actually prints the data
        print("{:%Y-%m-%d %H:%M:%S}  {}".format(datetime.datetime.now(), data.decode('utf-8')))
        print("{:%Y-%m-%d %H:%M:%S}  {}".format(datetime.datetime.now(), data.decode('utf-8')),
            file=f)  # from bytes to unicode, prints to file
    f.close()


def sendToArduino():
    arduino.write(b'5')  # must convert unicode to byte
    b = mystring.encode('utf-8')


def main():
    arduino = getSerialObject('/dev/cu.usbmodemFD121')
    startTime = datetime.datetime.now()

    try:
        while True:
            data = getData(arduino)
            printSerialToFile(data, 'data/soilMoisture.csv')

            # check if its been 1 day since last watering
            # if startTime < datetime.datetime.now() - datetime.timedelta(days=1):
            #     sendToArduino()

    except(KeyboardInterrupt):
        sys.exit()


if __name__ == "__main__":
    main()
