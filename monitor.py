import pyaudio
import time
from math import log10
import audioop  
import sys

# Set base parameters
p = pyaudio.PyAudio()
WIDTH = 2
RATE = int(p.get_default_input_device_info()['defaultSampleRate'])
DEVICE = p.get_default_input_device_info()['index']
rms = 1
print(p.get_default_input_device_info())

# Calculate RMS
def callback(in_data, frame_count, time_info, status):
    global rms
    rms = audioop.rms(in_data, WIDTH) / 32767
    return in_data, pyaudio.paContinue


# Start stream
stream = p.open(format=p.get_format_from_width(WIDTH),
                input_device_index=DEVICE,
                channels=1,
                rate=RATE,
                input=True,
                output=False,
                stream_callback=callback)

stream.start_stream()

strikes = 0
threshold = sys.argv[1]

# Program loop
while stream.is_active(): 
    db = 20 * log10(rms)
    print(f"RMS: {rms} DB: {db}") 
    if db > float(threshold) and int(strikes) == 3:
        print("Too Loud!")
        strikes = 0
    elif db > float(threshold):
        strikes += 1
    # refresh every 0.3 seconds 
    time.sleep(0.3)

# Clean up
stream.stop_stream()
stream.close()

p.terminate()