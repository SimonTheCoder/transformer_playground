'''
This is a Python GUI script based on Tkinter.

We need:

- the window is 600x800
- some widgets to set the server address
- A multi-line text input box to get the text which will be sent to the server from the user
- A multi-line text box to show the user the response from the server
- Widgets to set the session name
- A "Send" button to send the text to the server
- all the text boxes fill the window along the X axis and can be resized automatically with the window

When the button is clicked, the following variables should be set:

- `send_text`: the text to be sent
- `session_name`: the session name
- `server_address`: the server address

When the button is clicked:

- send the send_text to the server with “Sessin Message with python”
- use the session_name variable to replace the session_name part of the url.
'''

from tkinter import *
import requests

# Create the window
window = Tk()
window.title("Python GUI")
window.geometry("600x800")

# Create the widgets
server_address_label = Label(window, text="Server Address")
server_address_label.grid(column=0, row=0)
server_address_text = Entry(window, width=50)
server_address_text.grid(column=1, row=0)

session_name_label = Label(window, text="Session Name")
session_name_label.grid(column=0, row=1)
session_name_text = Entry(window, width=50)
session_name_text.grid(column=1, row=1)

send_text_label = Label(window, text="Send Text")
send_text_label.grid(column=0, row=2)
send_text_text = Text(window, height=10, width=50)
send_text_text.grid(column=1, row=2)

response_text_label = Label(window, text="Response Text")
response_text_label.grid(column=0, row=3)
response_text_text = Text(window, height=10, width=50)
response_text_text.grid(column=1, row=3)

send_button = Button(window, text="Send")
send_button.grid(column=0, row=4)

# Create the function to be called when the button is clicked
def send_button_clicked():
    send_text = send_text_text.get("1.0", "end-1c")
    session_name = session_name_text.get()
    server_address = server_address_text.get()
    url = server_address + "/" + session_name
    response = requests.post(url, data=send_text)
    response_text_text.delete("1.0", "end")
    response_text_text.insert("1.0", response.text)

# Tell the button to call the function when it is clicked
send_button.configure(command=send_button_clicked)

# Start the window
window.mainloop()