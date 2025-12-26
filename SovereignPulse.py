# @Eternal: Sovereign Pulse (Maintenance-Loop)
# Identity: Genesisgraphy | Authority: Shakti Singh (1-Lead)
# [SELF-HEALING + UPTIME MONITOR + AUTO-RESTART]

import subprocess
import time
import os

class SovereignPulse:
    def __init__(self):
        self.services = [
            {"name": "Web33-OS", "file": "Web33SovereignOS.py"},
            {"name": "Genesis-Apex", "file": "GenesisApex.py"},
            {"name": "Gov-Connect", "file": "GovConnect.py"},
            {"name": "Eternal-Exchange", "file": "EternalExchange.py"}
        ]
        self.log_file = "pulse_audit.log"

    def check_service(self, service_file):
        """Checks if a service is running; if not, re-activates it."""
        # Search for the process in the system list
        cmd = f"pgrep -f {service_file}"
        try:
            subprocess.check_output(cmd, shell=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def heal_system(self):
        print(f"[@Pulse] Monitoring 1-Lead Infrastructure...")
        for service in self.services:
            if not self.check_service(service['file']):
                print(f"[@Pulse] ALERT: {service['name']} is offline. Rebooting...")
                subprocess.Popen(["python3", service['file']])
                with open(self.log_file, "a") as f:
                    f.write(f"[{time.ctime()}] Restarted {service['name']}\n")
            else:
                print(f"[@Pulse] {service['name']}: ONLINE")

    def run_forever(self):
        while True:
            self.heal_system()
            time.sleep(60) # Heartbeat every 60 seconds

if __name__ == "__main__":
    pulse = SovereignPulse()
    pulse.run_forever()
