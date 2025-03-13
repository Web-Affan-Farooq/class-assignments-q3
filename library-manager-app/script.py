from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time

class Watcher(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.run_script()

    def run_script(self):
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen(["python", self.script])

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"Detected change in {event.src_path}, restarting script...")
            self.run_script()

if __name__ == "__main__":
    script_name = "app.py"
    event_handler = Watcher(script_name)
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()