# code to read serial form arduino
# requires pySerial
import serial
import json
import sys
import csv
import xml.etree.ElementTree



def main():
    # Configure from xml
    config = xml.etree.ElementTree.parse("settings.xml").getroot()

    for atype in config.findall('reactivision_settings_path'):
        react_config = atype.text
        print react_config
    for atype in config.findall('serial_port'):
        serial_port = atype.text
        print serial_port
    for atype in config.findall('baud_rate'):
        baud_rate = atype.text
        print baud_rate
    for atype in config.findall('output_csv'):
        output_csv = atype.text
        print output_csv
    # react_config = sys.argv[1]
    # # react_config = "/Users/pere-upf/Documents/Reactable/Preferences/reactivision_settings.xml"

    e = xml.etree.ElementTree.parse(react_config).getroot()
    for atype in e.findall('brightness'):
        brightness_value = atype.text


    print "Brightness: " + brightness_value
    ser = serial.Serial(serial_port, baud_rate)

    # We expect to receive data from arduino
    while True:
        rawLine = ser.readline()
        #print(rawLine)
        try:
            tempData = json.loads(rawLine)
            print("Computed Lux (full spec): " + str(tempData["data"]["lux"]))
            break
        except:
            # do nothing, not a valid JSON
            #print "Shit of json"
            pass

    dataset_instance = [str(brightness_value), str(tempData["data"]["lux"])]

    with open(output_csv, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(dataset_instance)
        f.close()

if __name__ == "__main__":
    main()
