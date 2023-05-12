from gpiozero import Button
from signal import pause
import requests
import json
import os
from datetime import datetime, time

# define the pin that the reed switch is connected to
reed_switch = Button(17)
ifttt_key = os.environ['IFTTT_KEY']
# define your IFTTT webhook URL
ifttt_url = 'https://maker.ifttt.com/trigger/door_alert/with/key/' + ifttt_key

def read_time_window():
    with open('time_window.json', 'r') as f:
        time_window = json.load(f)
    start_time = time(time_window['start_hour'], time_window['start_minute'])
    end_time = time(time_window['end_hour'], time_window['end_minute'])
    return start_time, end_time

def door_opened():
    start_time, end_time = read_time_window()

    # check the current time
    current_time = datetime.now().time()

    # check if the current time is within the defined window
    if start_time <= current_time <= end_time:
        print('Door opened during defined time window!')
        # send HTTP request to IFTTT
        response = requests.post(ifttt_url)

        # print response status (200 is success)
        print('Response status: ', response.status_code)
    else:
        print('Door opened outside of defined time window. No action taken.')

def door_closed():
    print('Door closed!')

# define what happens when the switch opens and closes
reed_switch.when_pressed = door_opened
reed_switch.when_released = door_closed

# keep the program running
pause()
