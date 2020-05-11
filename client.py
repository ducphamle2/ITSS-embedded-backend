#from ev3dev.ev3 import *
from time import sleep
import socket
import socketio

HOST = 'http://192.168.43.236'
#PORT = 5001;
#HOST = '27.67.6.236'
PORT = 8088

sio = socketio.Client()


@sio.event
def connect():
    print("hello")


if __name__ == "__main__":
    print(f'{HOST}:{PORT}')
    sio.connect(f'{HOST}:{PORT}')

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, PORT))
# s.listen()

# while True:
#     conn, addr = s.accept()
#     with conn:
#         print('Conntect by', addr)
#         while True:
#             data = conn.recv(1024)
#             #m = LargeMotor('outB')
#             # m.run_forever(speed_sp=900)
#             # sleep(30)
#             # m.stop()
#             # sleep(30)
