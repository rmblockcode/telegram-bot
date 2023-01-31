from flask import Flask
from flask import request
from flask import Response
import requests
import json
from pprint import pprint

app = Flask(__name__)

TOKEN = 'YOUR TOKEN'

def parse_message(message):
    pprint(message)
    chat_id = message['message']['chat']['id']
    text = message['message']['text']
    return chat_id, text

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    return response

def send_poll(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPoll'
    payload = {
        'chat_id': chat_id,
        'question': 'Cual es tu lenguaje de programacio favorito',
        'options': json.dumps(['Python', 'Java', 'C', 'C++']),
        'is_anonymous': False,
        'type': 'quiz',
        'correct_option_id': 0
    }

    response = requests.post(url, json=payload)
    return response

def send_inlineurl(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "Cual enlace te gustaría visitar?",
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "YT channel", "url": "https://www.youtube.com/@rmblockcode"},
                    {"text": "Instagram", "url": "https://www.instagram.com/rmblockcode"}
                ]
            ]
        }
    }
 
    response = requests.post(url, json=payload)
 
    return response

def send_image(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': "https://imgs.search.brave.com/hzL_sxK7wUBl9UV41_m-8wFPxAbiT0czbk9us0hOULc/rs:fit:751:225:1/g:ce/aHR0cHM6Ly90c2U0/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5Y/OUxfUGtZTklFUGVB/U2RmQUVBN1dBSGFF/ciZwaWQ9QXBp",
        'caption': "This is a sample image"
    }
 
    response = requests.post(url, json=payload)
    return response

def send_audio(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendAudio'
 
    payload = {
        'chat_id': chat_id,
        "audio": "ARCHIVO.mp3",
 
    }
 
    response = requests.post(url, json=payload)
 
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.get_json()
        
        chat_id, text = parse_message(message)

        if text == 'hola':
            send_message(chat_id, 'Hola comunidad')
        elif text == 'encuesta':
            send_poll(chat_id)
        elif text == 'url':
            send_inlineurl(chat_id)
        elif text == 'imagen':
            send_image(chat_id)
        elif text == 'audio':
            send_image(chat_id)
        else:
            send_message(chat_id, 'Hola desde webhook')

        return Response('OK!', status=200)

    return '<h1>Hola Comunidad</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=5002)