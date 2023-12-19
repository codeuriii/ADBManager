import subprocess

class ADBManager:
    def execute_command(self, command):
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    def enable(self, option):
        command = f"adb shell svc {option} enable"
        self.execute_command(command)

    def disable(self, option):
        command = f"adb shell svc {option} disable"
        self.execute_command(command)

class Options:
    WIFI = "wifi"
    GPS = "gps"
    # Ajoutez d'autres options au besoin

if __name__ == "__main__":
    adb_manager = ADBManager()
    
