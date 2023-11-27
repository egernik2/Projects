import time

class ProgressBar:
    def __init__(self, total):
        self.total = total
        self.progress = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print()

    def update(self):
        self.progress += 1
        percent = int(self.progress / self.total * 100)
        print(f"\rProgress: [{'=' * percent}{' ' * (100 - percent)}] {percent}%", end='')

if __name__ == '__main__':
    with ProgressBar(100) as p:
        for i in range(100):
            p.update()
            time.sleep(0.1)