#!/usr/bin/env python3
# use of the following repo: 
# https://github.com/acheong08/ChatGPT
from revChatGPT.V3 import Chatbot

def get_key():
    with open('apikey.txt') as f:
        key = f.readline()
    return key

def main():
    chatbot = Chatbot(  api_key= get_key())
    try: 
        while True:
            prompt = input('\nUser: \n')
            print('\nChatGPT:')
            print(chatbot.ask(f'{prompt}'))

    finally:
        print('bye')
        exit()

if __name__ == '__main__':
    main()