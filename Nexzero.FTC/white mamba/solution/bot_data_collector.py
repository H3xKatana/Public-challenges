#!/usr/bin/env python3
import requests
import time

API_URL = 'https://api.telegram.org/bot'
TOKEN = ''# get the token and put it here 
CHANNEL_ID = '-1002569946357'
CHAT_ID = '-1002583318161'

def get_my_commands(bot_token, chat_id=None):
    url = f"{API_URL}{bot_token}/getMyCommands"
    params = {}
    if chat_id:
        params['chat_id'] = chat_id
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()

def get_updates(bot_token, offset=None, timeout=30):
    url = f"{API_URL}{bot_token}/getUpdates"
    params = {'timeout': timeout}
    if offset:
        params['offset'] = offset
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()

def get_bot_info(bot_token):
    url = f"{API_URL}{bot_token}/getMe"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def get_my_default_administrator_rights(bot_token, chat_id):
    url = f"{API_URL}{bot_token}/getMyDefaultAdministratorRights"
    params = {'chat_id': chat_id}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()

def forward_message(bot_token, chat_id, from_chat_id, message_id):
    url = f"{API_URL}{bot_token}/forwardMessage"
    params = {
        'chat_id': chat_id,
        'from_chat_id': from_chat_id,
        'message_id': message_id,
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()

if __name__ == "__main__":
    # Print bot info and commands
    print("Bot info:", get_bot_info(TOKEN))
    print("Registered commands:", get_my_commands(TOKEN, CHAT_ID))
    print("Default admin rights:", get_my_default_administrator_rights(TOKEN, CHAT_ID))

    # Forward first 20 messages from CHANNEL_ID to CHAT_ID
    for message_id in range(1, 20):
        try:
            response = forward_message(TOKEN, CHAT_ID, CHANNEL_ID, message_id)
            if response.get('ok'):
                result = response['result']
                if 'text' in result:
                    print(f"[+] message_id = {message_id} | text: {result['text']}")
                elif 'document' in result:
                    print(f"[+] message_id = {message_id} | file_id: \"{result['document']['file_id']}\"")
        except requests.exceptions.HTTPError as e:
            print(f"Failed to forward message {message_id}: {e}")
        time.sleep(0.1)
