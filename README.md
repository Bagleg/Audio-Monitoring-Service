This is a simple app that is meant to ensure that a PC user isn't too loud while playing games or chatting.

To run, ensure that:

    1. You have python installed
    2. You have matplotlib installed
    3. You have playsound (version 1.2.2) installed
    4. You have win10toast installed
    5. You have pyaudio (and portaudio see https://stackoverflow.com/questions/33513522/when-installing-pyaudio-pip-cannot-find-portaudio-h-in-usr-local-include for more info) installed
    

The decibel tracking solution was provided by lys on stack overflow https://stackoverflow.com/questions/70502339/how-would-i-find-the-current-decibel-level-and-set-it-as-a-variable

Run the benchmark first to see where your audio levels reach their highest. To do this run

    python3 benchmark.py <test_duration_seconds>

Find a number that feels right (no statistical analysis is done currently)

Once you find the number, run:
    
    python3 monitor.py <magic_number>

This will keep the program running in the background and you will recieve pings when you exceed your limit to the windows system tray.

You can implement this solution to run on start up. To do this, you are going to need to adapt the code a little. You are either going to want to change the threshold variable to your magic number so you don't need to enter it via command line or find some other way to include it in a lauching script. Once you have that figured out, write a bat file like the one below:

    @echo off
    cd /d "<PATH TO MONITOR DIRECTORY>"
    "<PATH TO PYTHON>" "<PATH TO MONITOR.PY>"
    pause

You can then add the script as a basic task to your taskschd.msc (To get here, press win + R and search taskschd.msc)
