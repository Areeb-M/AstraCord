from core import *
from astra import *
import os


def main():
    try:
        with open('token.txt') as token_file:
            token = token_file.read()
    except IOError:
        print("Token missing! Please create file named token.txt\
         in the same directory as main.py with the discord token.")

    data_path = os.path.dirname(__file__) + '\\data'
    if not os.path.isdir(data_path):
        os.mkdir(data_path)

    astra_cord = Bot(data_path)
    astra_cord.run(token)


if __name__ == '__main__':
    main()
