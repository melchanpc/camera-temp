import Adafruit_DHT
import requests
import time
# Set sensor type : Options are DHT11,DHT22 or AM2302

# Reading the DHT11 is very sensitive to timings and occasionally
# the Pi might fail to get a valid reading. So check if readings are valid.

request = None

start_time = time.time()
duration = 0
sensor=Adafruit_DHT.AM2302
# Set GPIO sensor is connected to
gpio=18
i = 0
# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
while (duration < 15*60):
    
    #write API keys
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    print("writing to ThingSpeak...")
    RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=A919IY7SOCZWU1H8&field2='
    RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=A919IY7SOCZWU1H8&field3='
    RequestToThingspeak+=str(temperature) + "&field3=" + str(humidity)
    request = requests.get(RequestToThingspeak)
    
    
    end_time = time.time()
    duration = end_time-start_time
    i += 1
    print("duration:",duration)
    print("collected:", i, "data")
    if i >= 30:
        break
    time.sleep(17)
    
RequestToThingspeak = 'https://api.thingspeak.com/channels/1128022/fields/2.json?api_key=BB28JIPVQDMFJQI5'

request = requests.get(RequestToThingspeak).json()
#get_data = request['feeds']

field2 = request['feeds']
print(field2)
t=[]
sum_temp = 0

for x in field2:
    if x['field2'] is not None:
        t.append(x['field2'])
        
for temp in range(0,len(t)):
    sum_temp+=float(t[temp])
ave_temp = sum_temp/len(t)


RequestToThingspeak = 'https://api.thingspeak.com/channels/1128022/fields/3.json?api_key=BB28JIPVQDMFJQI5'

request = requests.get(RequestToThingspeak).json()
#get_data = request['feeds']

field3 = request['feeds']
print(field3)
t=[]
sum_humid = 0

for x in field3:
    if x['field3'] is not None:
        t.append(x['field3'])
for humid in range(0,len(t)):
    sum_humid+=float(t[humid])
ave_humid = sum_humid/len(t)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(ave_temp, ave_humid))
    r = requests.post(
                 "https://maker.ifttt.com/trigger/trigger/with/key/bjiw0jg3AvS3HFEo9Kv5PV",
                 json={"value1" : ave_temp})
    r = requests.post(
                 "https://maker.ifttt.com/trigger/trigger/with/key/bjiw0jg3AvS3HFEo9Kv5PV",
                 json={"value2" : ave_humid})
else:
    print('Failed to get reading. Try again!')



    
    
    

