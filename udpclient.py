import socket
import sys
import getopt

def udp_client(server_ip, server_port, data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5)  # Postavlja vremensko ograničenje za primanje podataka (5 sekundi)

    try:
        client_socket.sendto(data.encode('utf-8'), (server_ip, server_port))  # Šalje podatke poslužitelju
        response, _ = client_socket.recvfrom(2)  # Prima odgovor od poslužitelja (2 bajta)
        num_characters, num_a = response  # Raspakirava primljeni odgovor u broj znakova i broj slova 'a'

        print(f'{num_characters} znakova')  # Ispisuje broj primljenih znakova
        print(f'{num_a} slova a')  # Ispisuje broj pojavljivanja slova 'a'
    except socket.timeout:
        print('Isteklo je vremensko ograničenje. Poslužitelj ne odgovara.')
        sys.exit(1)
    finally:
        client_socket.close()  # Zatvara socket klijenta

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "p:")
    except getopt.GetoptError:
        print('Upotreba: udpklijent.py [-p port] server_IP')
        sys.exit(1)

    server_ip = ''
    server_port = 1234  # Zadani port
    data = ''

    for opt, arg in opts:
        if opt == '-p':
            server_port = int(arg)

    if len(args) > 0:
        server_ip = args[0]
    else:
        print('Upotreba: udpklijent.py [-p port] server_IP')
        sys.exit(1)

    data = input('Unesite redak podataka: ')  # Unos podataka s tipkovnice

    udp_client(server_ip, server_port, data)  # Pokreće klijenta i šalje podatke poslužitelju

if __name__ == '__main__':
    main(sys.argv[1:])
