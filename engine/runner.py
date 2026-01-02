# engine/runner.py
import time
import random

class Runner:
    def __init__(self, platform, classifier):
        self.platform = platform
        self.classifier = classifier

    def run(self, minutes=30):
        watch_time = random.gauss(minutes * 60, minutes * 15)
        elapsed = 0

        self.platform.setup()

        while elapsed < watch_time:
            delay = max(1.5, random.gauss(4, 1))
            time.sleep(delay)
            elapsed += delay

            text = self.platform.extract_text()
            score = self.classifier.score(text)

            if random.randint(1, int(2 + 100 / score)) == 1:
                self.platform.like()

            self.platform.scroll()

        self.platform.close()
