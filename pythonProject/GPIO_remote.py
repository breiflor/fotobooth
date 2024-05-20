#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import threading


class GPIO_Remote:

    def __init__(self, cbk, PORT=26, pollinfrequency=.1, NC=False) -> None:
        self.port = PORT
        self.polling_freq = pollinfrequency
        self.cbk = cbk
        self.running = True
        self.NC = NC  # switch is normally closed
        self.triggered = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.port, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.poll_thr = threading.Thread(target=self.poll_for_update)
        self.poll_thr.start()

    def poll_for_update(self):
        while self.running:
            pressed = bool(GPIO.input(self.port))
            if pressed is self.NC and not self.triggered:
                self.cbk()
                self.triggered = True
            elif pressed is not self.NC and self.triggered:
                self.triggered = False
            time.sleep(self.polling_freq)

    def __del__(self):
        self.running = False
        self.poll_thr.join(0)

    def stop(self):
        self.running = False
        self.poll_thr.join(0)


def test():
    print("button triggered")


if __name__ == "__main__":
    remote = GPIO_Remote(test)
    time.sleep(30)
    remote.stop()