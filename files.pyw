import time
import os
import zipfile
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

user_path = r"C:/Users/USERNAME"  # Replace USERNAME with your user.

class MyHandler(LoggingEventHandler):

    def dispatch(self):

        files = os.listdir(user_path+"/Downloads")

        for file in files:

            file_type = file[-5::]

            folder = "Downloads"

            if file_type.find(".mp3") != -1 or file_type.find(".wav") != -1:
                folder = "Music"

            elif file_type.find(".mp4") != -1 or file_type.find(".mov") != -1:
                folder = "Videos"

            elif file_type.find(".jpg") != -1 or file_type.find(".png") != -1 or file_type.find(".jpeg") != -1:
                folder = "Pictures"

            elif file_type.find(".txt") != -1 or file_type.find(".pdf") != -1 or file_type.find(".docx") != -1 or file_type.find(".pptx") != -1 or file_type.find(".xlsx") != -1:
                folder = "Documents"

            else:
                print(f"Won't move {file}...")
                continue

            os.rename(fr"{user_path}/Downloads/{file}", fr"{user_path}/{folder}/{file}")
            print(f"Moved {file} to {folder}...")


if __name__ == "__main__":
    observer = Observer()
    observer.schedule(
        event_handler = MyHandler,
        path          = user_path + "/Downloads",
        recursive     = False
    )
    observer.start()

    print("started...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
