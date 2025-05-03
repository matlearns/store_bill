import time, subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    process = None

    def on_modified(self, event):
        if event.src_path.endswith("main.py"):
            print(f"🔄 Reloading: {event.src_path}")
            if self.process:
                self.process.kill()
            self.process = subprocess.Popen(["python", "main.py"])

observer = Observer()
event_handler = ReloadHandler()
observer.schedule(event_handler, ".", recursive=False)
observer.start()

try:
    # Start app at first run
    event_handler.process = subprocess.Popen(["python", "main.py"])
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    if event_handler.process:
        event_handler.process.kill()
observer.join()
