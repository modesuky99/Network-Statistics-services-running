import psutil

print(f"{'PID':<10}{'Name':<25}{'Status':<25}{'Username':<15}")
print("-" * 70)

for proc in psutil.process_iter(['pid', 'name', 'status', 'username']):
    try:
        pid = proc.info.get('pid', 'N/A')
        name = proc.info.get('name', 'N/A') or 'N/A'
        status = proc.info.get('status', 'N/A') or 'N/A'
        username = proc.info.get('username', 'N/A') or 'N/A'
        
        print(f"{pid:<10}{name:<25}{status:<25}{username:<15}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

print("\n" + "-" * 70)
print("Network Statistics:")
print("-" * 70)

net = psutil.net_io_counters()  
print(f"Bytes Sent: {net.bytes_sent} bytes")
print(f"Bytes Received: {net.bytes_recv} bytes")
print(f"Packets Sent: {net.packets_sent}")
print(f"Packets Received: {net.packets_recv}")
