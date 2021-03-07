import requests
import json

# Some reading to do here: https://lifehacker.com/how-can-i-start-and-shut-down-my-computer-automatically-5831504

# Wrong link above try: https://docs.pushbullet.com/

def pushbullet_message(title, body):
    msg = {
        "type": "note", 
        "title": title, 
        "body": body
    }
    TOKEN = 'o.3Mqby3o8MCisITwU7n4COlNxpM2O9W21'
    resp = requests.post('https://api.pushbullet.com/v2/pushes', 
                         data=json.dumps(msg),
                         headers={'Authorization': 'Bearer ' + TOKEN,
                                  'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Error',resp.status_code)
    else:
        print ('Message sent') 

if __name__ == "__main__":
    print("Sending Test notification")
    pushbullet_message("Test Title", "This is a test of a body /n how well does it handle complex \n text.")
