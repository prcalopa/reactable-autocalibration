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
* PySerial
* Numpy
* Scikit-learn
* Matplotlib

### Arduino
Install the following libraries using the Arduino IDE package manager

* Adafruit_TSL2591_Library
* Adafruit_Unified_Sensor
* ArduinoJson

## Hardware setup

Follow Adafruit's tutorial [here](https://learn.adafruit.com/adafruit-tsl2591)

## Usage
### Configuration step
Open the **settings.xml** and change the data fields to match your computer paths, arduino port ,...
### Data Logging
Run **brightness_logger.py** to retrieve brightness value (adjusted manually in Reactable) and Light Sensor Data
### Visualize and Train SVM(regression) model
Run **svmExample.py**
