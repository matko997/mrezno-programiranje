import sys
import socket
import getopt

def print_usage():
    print("Usage: prog.py [-t|-u] [-x] [-h|-n] hostname servicename")
    sys.exit(1)

def get_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        print(f"prog: nodename nor servname provided, or not known")
        sys.exit(1)

def get_cname(hostname):
    try:
        cname = socket.gethostbyaddr(hostname)[0]
        return cname
    except socket.herror:
        return ""

def get_port_number(servicename, is_udp):
    try:
        port = socket.getservbyname(servicename, "udp" if is_udp else "tcp")
        return port
    except socket.error:
        print(f"prog: service '{servicename}' not found")
        sys.exit(1)

def main(argv):
    is_udp = False
    use_hex = False
    use_network_order = False

    try:
        opts, args = getopt.getopt(argv, "tuinxh")
    except getopt.GetoptError:
        print_usage()

    for opt, _ in opts:
        if opt == '-t':
            is_udp = False
        elif opt == '-u':
            is_udp = True
        elif opt == '-x':
            use_hex = True
        elif opt == '-n':
            use_network_order = True
        elif opt == '-h':
            use_network_order = False

    if len(args) != 2:
        print_usage()

    hostname = args[0]
    servicename = args[1]

    ip_address = get_ip_address(hostname)
    cname = get_cname(ip_address)
    port = get_port_number(servicename, is_udp)

    if use_hex:
        port_str = f"{port:04x}"
    else:
        port_str = str(port)

    if use_network_order:
        port_str = port_str[-2:] + port_str[:2]

    print(f"{ip_address} ({cname}) {port_str}")

if __name__ == "__main__":
    main(sys.argv[1:])
