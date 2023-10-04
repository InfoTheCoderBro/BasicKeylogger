# BasicKeylogger
This Python script utilizes the pynput library to create a simple keylogger that records and logs key presses in real-time. 
Here's a description of the script:

Keyboard Input Recorder Script

This Python script is designed to capture and record keyboard inputs in real-time using the pynput library. It provides a basic framework for logging key presses into a text file named "demo.txt." Here's how the script works:

Importing Libraries: The script begins by importing the necessary modules from the pynput.keyboard package, specifically Key and Listener. These modules are used to monitor keyboard events.

Initializing Variables: A list k is created to store the captured keys.

on_press Function: This function is called whenever a key is pressed. It appends the pressed key to the k list and then calls the write_1 function to write the pressed key to the "demo.txt" file. It also prints the pressed key to the console for real-time monitoring.

write_1 Function: This function takes a list var as input and writes its elements (representing key presses) to the "demo.txt" file. It removes any single quotes around each key representation and separates them by spaces.

on_release Function: This function is triggered when a key is released. It checks if the released key is the "esc" key (Key.esc). If it is, the function returns False, which stops the keyboard listener and exits the script.

Listener Setup: The script sets up a listener (l) using the Listener class provided by pynput. It specifies the on_press and on_release functions to be called when keyboard events occur.

l.join(): This line starts the listener and keeps it running until the "esc" key is pressed, as specified in the on_release function.

This script essentially creates a basic keylogger that records keyboard inputs into a text file. It's important to note that the use of keyloggers for unauthorized purposes or without consent is illegal and unethical. This script is intended for educational or legitimate use cases, such as monitoring keyboard inputs for debugging or research purposes, and should be used responsibly and within the bounds of the law and ethical guidelines.




