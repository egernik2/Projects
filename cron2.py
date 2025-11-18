import time
import threading
from datetime import datetime, timedelta

class Task:
    def __init__(self, name, interval, action):
        self.name = name
        self.interval = interval  # Interval in seconds
        self.action = action
        self.next_run = datetime.now() + timedelta(seconds=interval)

    def run(self):
        self.action()
        self.next_run = datetime.now() + timedelta(seconds=self.interval)

class CronScheduler:
    def __init__(self):
        self.tasks = []
        self.lock = threading.Lock()
        self.running = False

    def add_task(self, task):
        with self.lock:
            self.tasks.append(task)

    def start(self):
        self.running = True
        thread = threading.Thread(target=self._run)
        thread.start()

    def stop(self):
        self.running = False

    def _run(self):
        while self.running:
            with self.lock:
                current_time = datetime.now()
                for task in self.tasks:
                    if current_time >= task.next_run:
                        task.run()
            time.sleep(1)

# Example usage
def example_action():
    print(f"Task executed at {datetime.now()}")

if __name__ == "__main__":
    scheduler = CronScheduler()

    # Add a task that runs every 5 seconds
    task = Task(name="ExampleTask", interval=5, action=example_action)
    scheduler.add_task(task)

    # Start the scheduler
    scheduler.start()

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        scheduler.stop()