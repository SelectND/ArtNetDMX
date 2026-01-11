import socket
import serial

def send_artnet(dmx_data):
    with serial.Serial('COM23', 115200) as ser:
        ser.write(dmx_data)

def process_artnet(uni=0):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(('127.0.0.1', 6454))
        print("ArtNet listener listening on port 6454...")
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                if (data[0:8] == b'Art-Net\x00'
                        and int.from_bytes(data[8:10], byteorder='little') == 0x5000
                        and int.from_bytes(data[14:16], byteorder='little') == uni
                ):
                    print(bytes([0xFF]) + data[18:18+63])
                    send_artnet(bytes([0xFF]) + data[18:18 + 63])


        except KeyboardInterrupt:
            print("Shutting down socket...")


process_artnet()
