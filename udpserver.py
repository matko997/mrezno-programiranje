import socket
import sys
import getopt

def handle_client(client_data):
    # Funkcija za obradu podataka primljenih od klijenta
    num_characters = len(client_data)  # Broj znakova u podacima
    num_a = client_data.count('a')  # Broj pojavljivanja slova 'a' u podacima
    return (num_characters, num_a)  # Vraća tuple sa brojem znakova i brojem slova 'a'

def udp_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', port))  # Veže socket na odabrani port

    print('Poslužitelj je pokrenut na portu', port)

    while True:
        data, client_address = server_socket.recvfrom(255)  # Prima podatke od klijenta
        client_data = data.decode('utf-8').rstrip('\n')  # Dekodira primljene podatke iz bajtova u string

        result = handle_client(client_data)  # Poziva funkciju za obradu podataka
        result_bytes = bytes(result)  # Pretvara rezultat u bajtove
        server_socket.sendto(result_bytes, client_address)  # Šalje rezultat klijentu
        break

    server_socket.close()  # Zatvara socket poslužitelja

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "p:")
    except getopt.GetoptError:
        print('Upotreba: udpserver.py [-p port]')
        sys.exit(1)

    port = 1234  # Zadani port

    for opt, arg in opts:
        if opt == '-p':
            port = int(arg)

    udp_server(port)  # Pokreće poslužitelj na odabranom portu

if __name__ == '__main__':
    main(sys.argv[1:])
