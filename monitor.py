import pyaudio
import time
from math import log10
import audioop  
import sys
from win10toast import ToastNotifier
from playsound import playsound

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

# Set strikes to -1 to account for the first strike that occurs on launch
strikes = -1
# Grab the upper limit from command line
threshold = sys.argv[1]

# Set up toast-- begin loop
toaster = ToastNotifier()
while stream.is_active(): 
    db = 20 * log10(rms)
    if db > float(threshold) and int(strikes) == 3:
        playsound('sound.mp3')
        toaster.show_toast("You are being a bit loud", "Try to keep it down a little", duration=10)
        strikes = 0
    elif db > float(threshold):
        strikes += 1
        print("Strike number: ", strikes)
    # refresh every 0.3 seconds 
    time.sleep(0.3)

# Clean up
stream.stop_stream()
stream.close()
p.terminate()
