# reactable-autocalibration
ML experiments involving light sensors to calibrate Reactable Live/Experience software

## Description

This project requires:
* Arduino UNO or similar
* [Adafruit TSL2591 Light sensor](https://www.adafruit.com/product/1980)
* Python

## Software dependecies

### Python
Install using pip
* [PySerial](https://pypi.python.org/pypi/pyserial)
* [Numpy](https://pypi.python.org/pypi/numpy)
* [Scikit-learn](https://pypi.python.org/pypi/scikit-learn/0.19.0)
* [Matplotlib](https://pypi.python.org/pypi/matplotlib)

### Arduino
Install the following libraries using the Arduino IDE package manager

* Adafruit_TSL2591_Library
* Adafruit_Unified_Sensor
* ArduinoJson

## Hardware setup

* Follow Adafruit's tutorial [here](https://learn.adafruit.com/adafruit-tsl2591)

* Open Arduino IDE and upload **Brightness_logger.ino**
* Check the Arduino port in the IDE and copy it to the **settings.xml** file
<br>Note the port can change!

## Usage
### Configuration step
Open the **settings.xml** and change the data fields to match your computer paths, arduino port ,...
### Data Logging
Run **brightness_logger.py** to retrieve brightness value (adjusted manually in Reactable) and Light Sensor Data
### Visualize and Train SVM(regression) model
Run **svmExample.py**


## Contact
Mail me to **pr.calopa@gmail.com** for any questions ;)
