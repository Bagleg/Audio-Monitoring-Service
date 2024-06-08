This is a simple app that is meant to ensure that a PC user isn't too loud while playing games or chatting.

To run, ensure that:

    1. You have python installed
    2. You have matplotlib and pyaudio (and portaudio see https://stackoverflow.com/questions/33513522/when-installing-pyaudio-pip-cannot-find-portaudio-h-in-usr-local-include for more info) installed 

The decibel tracking solution was provided by lys on stack overflow https://stackoverflow.com/questions/70502339/how-would-i-find-the-current-decibel-level-and-set-it-as-a-variable

Run the benchmark first to see where your audio levels reach their highest. To do this run

    python3 benchmark.py <test_duration_seconds>

Find a number that feels right (no statistical analysis is done currently)

Once you find the number, run:
    
    python3 monitor.py <magic_number>

This will keep the program running in the background and you will recieve pings when you exceed your limit to the windows system tray.
