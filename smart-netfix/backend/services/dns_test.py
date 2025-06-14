# import socket

# def check_dns(domain='www.google.com'):
#     try:
#         socket.gethostbyname(domain)
#         return True
#     except socket.error:
#         return False


import socket

def check_dns():
    try:
        socket.gethostbyname("www.google.com")
        return True
    except socket.error:
        return False
