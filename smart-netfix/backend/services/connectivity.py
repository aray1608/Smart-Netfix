# import requests

# def check_internet():
#     try:
#         requests.get("https://www.google.com", timeout=3)
#         return True
#     except requests.ConnectionError:
#         return False

import socket

def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False



