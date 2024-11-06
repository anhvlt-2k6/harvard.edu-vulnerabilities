import subprocess, time, psutil, argparse

def kill_old_processes():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'nmap':
            process.kill()

parser = argparse.ArgumentParser(description="Run Nmap scans using a DNS list.")
parser.add_argument('file_path', nargs='?', default="port-scanning/list.txt", help="Path to the DNS list file")
parser.add_argument('save_path', nargs='?', default="port-scanning/results/single-thread", help="Scan results to be saved in path")
args = parser.parse_args()

with open(args.file_path, "r") as f:
    dns_list = [dns.strip() for dns in f if dns.strip()]

for dns in dns_list:
    kill_old_processes()
    process = subprocess.Popen(
        ["nmap", "-T4", "-A", "-v", "-Pn", dns, "-oX", f"{args.save_path}/{dns}_nmap_scan.xml"]
    )
    process.wait()
