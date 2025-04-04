import socket

def scan_ports(target, ports):
    print(f"\nScanning ports on {target}...\n")
    
    for port in range(ports[0], ports[1] + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"✅ Port {port} is OPEN")
            else:
                print(f"❌ Port {port} is CLOSED")
            s.close()
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    target = input("Enter target (IP/Domain): ")
    scan_ports(target, (20, 100))
