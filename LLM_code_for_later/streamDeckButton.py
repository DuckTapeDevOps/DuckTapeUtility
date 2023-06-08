# Chatsonic AI Reponse:
# '''
# To create a button on your Stream Deck that will clip the last X seconds of your Twitch stream, you'll need to use the Twitch API. 
# Here's some sample Python code that will create a button on your Stream Deck and start and stop video recording when pressed:
# '''


import requests

# Define the Twitch API endpoint
twitch_api_endpoint = "https://api.twitch.tv/helix"

# Define your Twitch API credentials
client_id = "your_client_id"
access_token = "your_access_token"

# Define the number of seconds to capture
seconds_to_capture = 30

# Define the start and stop recording URLs
start_recording_url = f"{twitch_api_endpoint}/streams/markers"
stop_recording_url = f"{twitch_api_endpoint}/streams"

# Define the headers for the Twitch API requests
headers = {
    "Client-ID": client_id,
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Define the button commands
def start_recording():
    response = requests.post(start_recording_url, headers=headers, json={"user_id": "your_user_id", "description": "Clip created!"})
    return response.json()

def stop_recording():
    response = requests.post(stop_recording_url, headers=headers, json={"type": "archive"})
    return response.json()

# Define the Stream Deck button actions
def stream_deck_pressed(action):
    if action == "start":
        start_recording()
    elif action == "stop":
        stop_recording()

# Call the Stream Deck API and define the button properties
def set_stream_deck_button():
    # Define the properties of the button
    button_properties = {
        "name": "Clip",
        "icon": "icon.png",
        "coordinates": {"column": 0, "row": 0},
        "state": {"key": "start", "title": "Start Recording"},
        "on_pressed": stream_deck_pressed
    }
    # Call the Stream Deck API to set the button properties
    requests.post("http://localhost:9980/action", json=button_properties)

# Call the function to set the Stream Deck button
set_stream_deck_button()