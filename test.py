import tkinter as tk
import requests

# Initialize the window
window = tk.Tk()
window.title('ChatGPT API')
window.geometry('600x800')

# Set server address
server_ip_label = tk.Label(window, text='Server IP: ')
server_ip_label.grid(column=0, row=0)
server_ip_input = tk.Entry(window)
server_ip_input.grid(column=1, row=0, columnspan=3, sticky="ew")

# Set session name
session_name_label = tk.Label(window, text='Session Name: ')
session_name_label.grid(column=0, row=1)
session_name_input = tk.Entry(window)
session_name_input.grid(column=1, row=1, columnspan=3, sticky="ew")

# Text Input
input_label = tk.Label(window, text='Input: ')
input_label.grid(column=0, row=2)
input_text = tk.Text(window, width=50, height=20)
input_text.grid(column=1, row=2, columnspan=3, sticky="ew")

# Response
response_label = tk.Label(window, text='Response: ')
response_label.grid(column=0, row=3)
response_text = tk.Text(window, width=50, height=20)
response_text.grid(column=1, row=3, columnspan=3, sticky="ew")

# Send button
send_button = tk.Button(window, text='Send', command=lambda: send_request(server_ip_input.get(), session_name_input.get(), input_text.get('1.0', 'end-1c')))
send_button.grid(column=1, row=4, columnspan=3, sticky="ew")

# Send request
def send_request(server_ip, session_name, input_text):
    url = "http://" + server_ip + "/message/" + session_name
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    data = {
        "message": input_text
    }
    response = requests.post(url, headers=headers, json=data)
    response_text.delete('1.0', tk.END)
    response_text.insert('1.0', response.text)

window.mainloop()

