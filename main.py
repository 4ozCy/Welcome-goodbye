from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return '''<body style="margin: 0; padding: 0;">
    <iframe width="100%" height="100%" src="https://syntaxcoderz.vercel.app/" frameborder="0" allowfullscreen></iframe>
  </body>'''

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()

keep_alive()
print("Server Running Because of Zcy.")
import requests
import json

# Webhook URL for the channel where you want the welcome and goodbye messages to be sent
webhook_url = 'https://discord.com/api/webhooks/1222254361321672744/WB4bwmj8tCBgSnJQWsSr7oA-_UqvRsL8P1g8FvNrQo7n_7dBZ8Yc_wGtN0-OFgH9KSSG'

# Event handler for member join
async def on_member_join(member):
    # Craft the welcome message with embed
    embed = {
        'title': f'Welcome to the server, {member.display_name}!',
        'description': 'We are glad to have you here.',
        'color': 0x00ff00,  # Green color
        'thumbnail': {'url': member.avatar_url},
        'image': {'url': 'https://cdn.discordapp.com/attachments/1187377061959045181/1222274125695811674/standard_4.gif?ex=66159e7c&is=6603297c&hm=5cc349480f7ac7b49b5c013b34c4eeac3b305cb8f0f5e61b7d00ed7b78d259d1'}
    }

    # Send the welcome message with embed via webhook
    await send_webhook_message(embed=embed)

# Event handler for member leave
async def on_member_remove(member):
    # Craft the goodbye message with embed
    embed = {
        'title': f'Goodbye, {member.display_name}!',
        'description': 'We will miss you.',
        'color': 0xff0000,  # Red color
        'thumbnail': {'url': member.avatar_url},
        'image': {'url': 'https://cdn.discordapp.com/attachments/1187377061959045181/1222274099036946494/standard_5.gif?ex=66159e75&is=66032975&hm=dd7225fb71a525b6e8e53fff9ac355cebb17df5011697a1dc2e62ceff87dfc3d'}
    }

    # Send the goodbye message with embed via webhook
    await send_webhook_message(embed=embed)

# Function to send message with embed via webhook
async def send_webhook_message(embed=None):
    data = {'embeds': [embed]} if embed else None
    response = requests.post(webhook_url, json=data)
    if response.status_code != 200:
        print('Failed to send webhook message')

# Run the Discord client
