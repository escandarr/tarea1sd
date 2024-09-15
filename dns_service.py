import subprocess

def dns_lookup(domain):
    result = subprocess.run(['dig', '+short', domain], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()

if __name__ == '__main__':
    domain = 'example.com'
    ip = dns_lookup(domain)
    print(f"IP address for {domain}: {ip}")
